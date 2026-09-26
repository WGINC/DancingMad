# FFXI PC Graphics Pipeline Map

**Binary:** `FFXiMain.dll` (unpacked; MD5 `f6dbabefc672dfc8586ac14486ff904d`), Direct3D 8.1, base
`0x10000000`. **Status:** complete as of 2026-09-26. Every address here is in `tools/ffxi_symbols_ida.py`
(1,251 names) and applied in the IDB. Section references (§) point to `FINDINGS.md`,
which holds the evidence; this document is the map.

Confidence is High unless marked. "Author" means a working name for PC-only code with no PS2
counterpart to check against.

---

## 1. The whole frame at a glance

```
STARTUP (once)
  Direct3DCreate8(220) ─ probe caps/DXT ─ CreateDevice (HW vertex processing, confirmed)
  CDx (0x1045666C) ─ dancer device copy ─ CEnv CPUID ─ CMoProcessor tier ─ registry config
  App_InitScene: render targets A [B] [UI] [256²] [feedback] [stereo pack]

EVERY FRAME  Frame_Render 0x10011A00          (30 fps cap)
  TestCooperativeLevel → BeginScene → default states
  ├─ TexMgr_UploadPump  (≤20 texture uploads/frame in-game, CPU DXT encode)
  ├─ push+clear scene B (stereo only) → push+clear scene A          ◄ render at "background res"
  ├─ state machine [this+0x44], 18 cases
  │    world:  0x1018B130 → 0x1018C2B0 → dancer world 0x10251500
  │            → main mesh pass 0x1018B860
  │            → CMoTaskMng draw 0x10074C30   (actors + effects, CPU-skinned, DrawPrimitiveUP)
  │            → dancer end 0x102515F0 → 0x10036230
  ├─ debug overlay
  ├─ [depth blur — compiled in, dead]
  ├─ afterimage → flash + zoom-feedback
  ├─ fade colour, copyright text
  ├─ COMPOSITE: scene A (+B side-by-side in stereo) → back buffer, upscaled, MODULATE2X
  ├─ UI target: menus/map/chat/status → composite
  ├─ global fade quad
  ├─ 2D layer (640×512 canvas), fonts, [stereo odd-frame overlay]
  EndScene → Present (100 retries, device-lost aware) → frame limiter
```

The map below follows that order.

---

## 2. Startup

### 2.1 Device creation (§18.1)

| Step | Address | What it does |
|---|---|---|
| Holder | `0x10002F20` | `0x478`-byte object → global `0x103D3CBC` |
| Bootstrap | `0x100031F0` | `Direct3DCreate8(220)`; enumerates modes 640×480–2048×2048 in X8R8G8B8/A8R8G8B8 |
| Capability probe | `0x10002130` | `CheckDeviceType`/`CheckDeviceFormat`, including DXT1/3/5 |
| Create | `0x100034B0` | `GetDeviceCaps`, present parameters, `CreateDevice`. Tries `BehaviorFlags 0x40` (hardware VP) then `0x20` (software). **Runtime: `0x40` wins** (session-2 log). |
| `CDx` | `CDx_Constructor` `0x10008F90` | The renderer object. Global **`0x1045666C`**. `IDirect3D8*` at `+8`, device at `+0xC`. |
| `CDx` init | `0x100091B0` | Format/multisample checks, VS 1.1 / PS 1.1 / PS 1.4 caps, texture-stage count, animated cursors |
| `dancer` copy | `0x10251A80` | Copies both pointers into the middleware context `0x10669400` (device `0x1066941C`) |

### 2.2 CPU capability and the math layer (§3, §18.12)

- `CEnv` (`g_pEnv` `0x104566E8`), `CEnv_DetectCpuFeatures` `0x1000D400`: vendor, MMX, SSE,
  SSE3-class, 3DNow!, logical CPU count.
- `CMoProcessor` (`g_pProcessor` `0x1047CF7C`, factory `0x1006CB50`): the engine's CPU vector/matrix
  library, **three tiers chosen by CPU** (3DNow!, x87 with extras, plain x87). Not a GPU tier. Owns a
  32-slot scratch-matrix pool with an unsynchronized stack pointer (§11).

### 2.3 Configuration (§18.12)

28-entry registry table `g_registryConfigTable` `0x103507E8` (`{global*, key, 0}`), defaults in
`Config_SetDefaults` `0x100178B0`. Keys that shape rendering:

| Key | Global | Effect |
|---|---|---|
| 0003/0004 | `g_cfgBackgroundResX/Y` | Scene render-target size (default 512×512); upscaled to the window at composite |
| 0037/0038 | `g_cfgMenuResX/Y` | UI render-target size; the UI target exists only if it differs from the window |
| 0018 | `g_cfgTextureCompression` | Allows runtime DXT encode of uncompressed art |
| 0019 | `g_cfgMapCompression` | Same, for map textures (class 10) |
| 0030 | `g_cfgStereoMode` | **Stereoscopic 3D** (§11 of this map) |

Not in the table and defaulting to 0: `g_depthBlurEnabled_Dead` `0x10456AD8` (§8.1).

### 2.4 Render targets (`App_InitScene` `0x10010D20`, §18.10)

A `CAcc` (16 bytes) is a render-target bundle: `+4` colour texture, `+0xC` depth surface.

| Target | Where | Size / condition |
|---|---|---|
| Scene A | `CDx+0x194` / depth `+0x1A4` | Background resolution |
| Scene B | `CDx+0x198` / `+0x1A8` | Same; **stereo mode only** (right eye) |
| UI | `CAcc` at `+0x1DC` | Menu resolution; only if ≠ window |
| 256×256 | `CAcc` at `+0x1BC` | Only if the dead depth-blur gate is set |
| Half-res feedback | `g_feedbackTexHalfRes` `0x10456938` | Half the scene size, per scene target |
| Afterimage | `g_afterimageTex` `0x10456910` | Created on demand by the effect interpreter |
| Stereo pack + masks | `CDx+0x824`, `+0x814`/`+0x81C`/`+0x82C` | Stereo only (`CDx_CreateStereoResources` `0x1000C6E0`) |

`CDx+0x1AC` and `+0x1CC` are never filled.

---

## 3. The frame loop (`Frame_Render` `0x10011A00`, §18.2, §18.10)

A **state machine**, not a fixed pipeline: `[this+0x44]` selects one of 18 cases (jump table
`0x10012EEC`). The world case is the one that matters for rendering. Global app state lives behind
`0x10456A28` → a record whose first field is the state ID (`0x40` set by the lobby/loader thread,
`0x60` = in-game, checked by 33 functions; §18.4).

In order:

1. `TestCooperativeLevel` (`0x10009710`) → `BeginScene` → `0x10009920` (345 instructions of default
   render / texture-stage state).
2. **Texture upload pump** (`TexMgr_UploadPump` `0x1003ABB0`) — §7.
3. Push + clear scene B (stereo only), then push + clear scene A (clear colour `app+0x308`).
4. World case: `0x1018B130`, `0x1018C2B0`, the `dancer` world `0x10251500` (the only frame pass
   reaching `SetLight` through direct calls), the main mesh pass `0x1018B860`, **the `CMoTaskMng` draw `0x10074C30`**
   (actors and effects — §6, §8), `dancer` end `0x102515F0`, `0x10036230`.
5. Debug overlay `0x10003650`.
6. Post-processing — §9.
7. Composite to the back buffer, then UI, fade, 2D — §9.
8. `EndScene` → `CDx::Present` `0x10009720` → `Present(NULL…)` retried up to 100 times,
   special-casing `D3DERR_DEVICELOST`.
9. **Frame limiter:** `Sleep(1)`/`Sleep(0)` spin until `app+0x30` sixtieths of a second have passed
   (set to 2 → **30 fps cap**), with a 4-frame moving average and wall-clock drift correction.

---

## 4. The submission layer: `CDx` (§18.3, §18.14)

Almost everything draws through `CDx`'s ~50 non-virtual methods. The exceptions are the `dancer`
middleware (own device copy) and the effect-script interpreter (talks to the device directly).

| Method | Address | Callers |
|---|---|---|
| `DrawPrimitiveUP` | `0x1000CD00` | 57 |
| `SetTransform` | `0x1000BD50` | 51 |
| `SetLight` | `0x1000BF30` | 34 |
| `GetTransform` (cached) | `0x1000BDB0` | 25 |
| Push render target | `0x10009E20` | 21 |
| `DrawIndexedPrimitive` | `0x1000CC00` | 20 |
| `SetTexture` | `0x1000A1D0` | 19 |
| `CreateTexture` (render targets only) | `0x1000A6E0` | 15 |
| `DrawPrimitive` | `0x1000CB20` | 10 |

- **Transform shadowing:** world `+0x93C`, view `+0x97C`, projection `+0x9BC`.
- **Render-target stack:** 24-byte entries at `CDx+0x98`, depth at `+0x158`.
- **Every draw entry point checks for stereo** (`CDx_GetStereoSecondEyeTarget` `0x1000CA00`) and may
  issue itself twice — §11.
- **Submission style:** `DrawPrimitiveUP` from 50 functions vs. 8 for `DrawPrimitive` and 5 for
  `DrawIndexedPrimitive`. Vertices are rebuilt on the CPU and copied every call. This is the single
  most important structural fact for performance work (§12).

---

## 5. Camera, view, projection (§18.5)

- Camera object global **`g_pCamera` `0x104568FC`**: projection matrix `+0x154`, near/far
  `+0x2DC`/`+0x2E0`, aspect inputs `+0x2E8`/`+0x2F0`, viewport width/height words `+0x18`/`+0x1A`
  (`Camera_GetViewportWidth/Height` `0x10015680`/`0x10015690`).
- Apply `0x10015510`: view from the camera controller `0x10021900` (atan2 + smoothing), then
  projection via `0x10015480` → statically linked `D3DXMatrixPerspectiveFovLH` (`0x102D83C6`).
- **FOV = 2·atan(192 / [camera+0x2F4])** — a focal-length camera with 192 as the reference
  half-height.
- `D3DTS_WORLD` is set in 27 functions, `VIEW` in 13, `PROJECTION` in 4 (plus the stereo eye
  offset, §11).

---

## 6. Actors: what the frame draws most

### 6.1 Draw list (§4)

`CXiActorDraw` (`0x10082D70`) keeps a **depth-sorted linked list** of drawable actors (head
`0x1047D578`, next `+0x54`, key `+0x8C`) for back-to-front transparency, and calls each actor's
vtable slot 162 (three call sites in `0x10082D70`) — the real per-actor draw hook on PC. `CXiActorNameDraw` draws name tags with an alpha-cutout
state block, only in app state `0x60`.

### 6.2 The actor's rendering interface (`CXiSkeletonActor` vtable, 264 slots; §12b, §12c, §18.11, §18.14)

The class chain is `CXiActor` → `CXiAtelActor` → `CXiControlActor` → `CXiCollisionActor` →
`CXiSkeletonActor`. Render-relevant slots:

| Slot | Name | Role in the pipeline |
|---|---|---|
| 8 | `OnMove` | Per-frame update (PS2's `OnDraw` has no PC body — drawing goes through slot 162) |
| 11–32 | colour, multi-texture alpha, shadow alpha, effects, UV offset, distortion, env-map | Per-actor material and effect state |
| 33–37 | the disintegration methods | **Empty stubs on PC** — the subject of the disintegrate fix |
| 38–40 | W/H/D scale | Per-actor scale |
| 113–115 | `GetElem` / `GetElemLocal` / `GetEidMatrix` | Bone/element positions for attachment points |
| 119 / 120 | `GetModel` / `GetModelFile` | Model handle `+0xB4` |
| 121 | `IsReadComplete` | All resources resident? Gates drawing and actions |
| 122–124 | `ActorFindResource` ×2 / `ActorGetResourceCount` | Resource lookup (type, id) |
| 129–136 | ground height / normal / material, water height | Terrain alignment; normal read every frame |
| 153 | `GetFocal` | `this+0x34` |
| 158 / 159 / 160 | `GetNamePos` / `GetArrowPos` / `ProjectToScreen` | World → screen for name tags and target arrows |
| 161 | `OnDrawName` | Name-tag draw |
| 162 | per-actor draw hook (`RunStaggeredUpdates` on skeleton actors) | Called by the draw list for every actor. Skeleton actors run the staggered pose/occlusion update here; furniture/model actors draw here (`0x101844C0`) |
| 164 / 165 | `SetModel` / `SetMotion` | Model and motion binding |
| 166–168 | `SetAction` / `KillAction` / `IsMovingAction` | Start/stop/query action scripts (resource type 7) via the scheduler |
| 173–177 | `SetAttack` ×2, `ReplaceAttack`, `UseMagic` ×2 | Combat actions → `SetAction` / technique loading |
| 191 | `OcclusionClip` | Screen-rect occlusion query; sets `+0xB0`/`+0xB2` on failure |
| 194 | `DrawResourceShadows` (Author) | Per-resource shadow/decal draw (`0x10085060`, `DrawIndexedPrimitiveUP`) |
| 195–209 | `IsControlLock`, `IsDirectionLock`, `IsConstrain`, `IsFreeRun`, `IsWalkLock`, `IsParallelMove` | Movement/animation lock state |
| 211–226 | `IsChocobo`, `IsFishingRod`, … | `SUBACTOR_STATUS` (`+0xA4`) mount/tool queries |

There is **no `ViewVolumeClip` body on PC** — PC moved view culling out of that virtual. The only
per-actor culling reachable is the occlusion query (`Occlusion_QueryScreenRect` `0x1006C280`),
from `OcclusionClip` and from the staggered update.

### 6.3 Per-actor cost is staggered 4:1 (§11)

`PerActor_FourBucketStaggeredUpdate` (`0x100CBDE0`) staggers per-actor work across four frames using
`GetFrameCounter() % 4` against the actor's bucket (`+0x9F0`/`+0x9FC`). New actors go to the
least-loaded bucket. It also writes each bone's uniform scale (§6.4).

**What bucket A actually staggers is the visibility test, not animation** (master §18.16; qualified by the actor draw budget, §18.17). On the
actor's bucket frame (or when forced), it runs `Occlusion_QueryScreenRect` on the actor's bound
(`+0x8F0`–`+0x910`) and caches the result in `+0x9F4` (nonzero = culled). On every other frame it
reuses that cached result. **Visible actors animate every frame; culled actors skip animation and
are re-tested once every four frames.** Bucket B (`+0x9FC`) gates a different block and does not
gate animation.

### 6.4 Animation (§7, §18.15)

Per model, `Model_AnimateAndPose` (`0x1002A140`) runs animation before pose composition. The
motion data itself is Maya-authored `sqMotion`: key channels (time-keyed) and frame channels
(fixed-rate), linear interpolation only, and mixer motions that can nest.

`MotionQueue_UpdateAllChannels` (`0x1001A420`) fills the per-bone pose scratch
`g_poseScratch` (`0x1045F030`, 52 bytes per bone: quaternion, translation, scale):

1. Reset every bone to default rotation, zero translation, unit scale.
2. **5 base layers** (`CYyMotionQue` slots, 20 bytes each) are sampled straight into the scratch,
   slot 4 first and slot 0 last, so lower slots override on the bones they drive.
3. **2 blend layers** are sampled into `g_poseBlendScratch` (`0x1045B820`) and mixed in by weight:
   `Quat_NLerp` for rotation (not renormalised), `Vec3_Lerp` for translation and scale.
4. A per-bone mask (`g_pBoneMotionMask` → byte per bone) decides which bones each layer may touch;
   the motion-start policy (`MotionQueue_ApplyPolicy` `0x10019A50`) uses the same bits to decide
   whether a new motion interrupts or queues.

Actions (§6.7) choose *which* motions are in those slots; this step turns them into a pose.

### 6.5 Skeleton pose (§6, §17, §18.7)

Per actor, all on the CPU, reading the scratch that animation just filled:

1. `Skel_BindShared` `0x10034330` — sets the shared-skeleton global `0x1045EC24`, bone count, the
   64-byte bone-matrix table; masks per-bone flags with `0x80`.
2. With no motion playing, `Skel_LoadBoneRotTrans` `0x10034620` / `Skel_LoadBindPoseToScratch`
   `0x10034760` fill the scratch from the bind pose instead (root gets a 3π/2 correction).
3. `Mat4_BuildScale` `0x10027AE0` (from the staggered update) — uniform bone scale `(s,s,s,1)`,
   observed `s ∈ {0.92, 0.95, 0.97, 1.0, 1.05}`.
4. Composer `CXiSkeletonActor_PoseCompose` `0x100343C0` / `Skel_ComposeMode` `0x100347D0` —
   scale × rotation × translation × parent, root first; an override list copies whole bone
   matrices (`Mat4_Copy` `0x100279F0`).

Bone record byte `+0x01` (PS2 `flip`) is unused by this path.

### 6.6 Skinning (§6)

**CPU skinning.** `SkinVertices` `0x10023290` / `SkinVerticesSimple` `0x100231F0` transform vertices
with a weight-premultiplied bone-matrix table (128 entries) in `CMoProcessor`.
`SkinVerticesFinish_SecondaryMotionSolver` `0x10023700` adds jiggle physics with a camera-bias
term, and `SkinVerticesFinish_Commit` applies proximity-matched constraints. The skinned vertices
are what `DrawPrimitiveUP` copies each frame. `dancer`'s `sqinShape` has a second, hardware-style
4-bone blend (§8).

### 6.7 Actions and effects on actors

`SetAction` → `CXiSkeletonActor_ReverseFindRes` / `YmResourceFile_FindResourceUnder` → the
scheduler (`Scheduler_Execute` `0x10056C70`, `_Kill` `0x10056EF0`, `_IsMoving` `0x10057010`). The
scheduler runs effect scripts (§8).

---

## 7. Textures (§18.6, §18.9)

Asset textures bypass `CDx::CreateTexture` (which only makes render targets) and go entirely
through the statically linked D3DX:

1. **Load** — `TexRes_LoadBm2` `0x1001D800`: checks the "Bm2" version, dedupes by 16-byte name
   (`TexMgr_FindByName` `0x1003AEA0`, refcounted), builds a 72-byte `TexObj` and queues it.
2. **Pump** — `TexMgr_UploadPump` `0x1003ABB0`, every frame after `BeginScene`: state 1 → create +
   upload, state 2 → re-upload after device loss. **In-game it stops after 20 uploads per frame.**
3. **Create** — `TexObj_Create` `0x10039A80` picks the format: uncompressed art becomes **DXT1
   (16-bit sources) or DXT3 (32-bit)** when the compression class is allowed by registry
   0018/0019; otherwise A1R5G5B5 / A8R8G8B8. Cube maps via `D3DXCreateCubeTexture`.
4. **Upload** — `TexObj_Upload` `0x10039E50`: CPU conversion into a staging texture (rows flipped
   bottom-up → top-down, CLUT expansion, PS2 alpha kept), then `D3DXLoadSurfaceFromSurface` into
   level 0 (**the DXT encode happens here, on the CPU**) and each mip box-filtered from the
   previous one. Precompressed DXT data goes straight in via `D3DXLoadSurfaceFromMemory`.

Manager `g_pTextureMng` `0x1047B970`. The font cache is one 1024×1024 A4R4G4B4 atlas
(`FontGlyphCache_Construct` `0x1025CAF0`) updated tile by tile.

---

## 8. Effects and particles (§5, §10, §18.11)

**There is no particle renderer and no point sprites.** No game code sets render states 154–161.
Effect geometry is built on the CPU and submitted four ways:

| Path | Where | Draw |
|---|---|---|
| `CMoElem` family | vtable slot 18 of each element class (e.g. `CMoDistRingElem` → `0x10043720`); VU/morph elements share `0x10043F40` | `DrawPrimitiveUP` / `DrawPrimitive` |
| `CMoOtTask` | slot 11 → `0x100421A0` | `DrawPrimitiveUP` |
| **Effect-script interpreter** | `CMoSchedularTask` slot 8 → `CMoSchedularTask_Interpret` `0x10057FB0` (23.6 KB, jump table `0x1005DC1C`) | **Direct to the device**: render/texture-stage state, vertex shader, DP/DIP/DPUP and ~40 other device calls; creates the afterimage textures |
| `dancer` | `sqgxContext_BatchIndices` → `0x1028AB50` / `0x1029B9D0` / `0x10280DE0` | Own device copy; 1,000-index batching |

The interpreter is the PC side of the `.fxt` opcode machinery (`StTrigger` loads `.fxt`, §10).
Attached effect clones (`CMoGeneratorClone`) hang off `CXiSkeletonActor` attachment lists (`+0x68`
caster, `+0x6C` target; unlinked by `UnlinkCaster/TargetAttachments` `0x10085C90`/`0x10085CF0`).

**Full draw census:** 73 functions issue draw calls (70 in game code). Besides the above: models
(`CYyModelDt_PrepareRenderState`, `0x1002DC10`), actor shadow/decal (`0x10085060`), furniture/model
actors (slot 162 → `0x101844C0`), `CXiMovie` (`0x10026AD0`), `XiPng` (`0x1025C900`), text
(`0x10038720`/`0x10038A80`/`0x10038E10`), UI (`0x1011x`, `0x1016x`–`0x1017x`), occlusion
(`0x1006C530`), scene stream (`0x10075280`/`0x10075C40`/`0x10076030`), world/terrain
`0x10183xxx`–`0x10185xxx`.

---

## 9. Lighting (§9)

`g_lightTable` (`0x104572B8`, 26 × 104-byte entries) holds real D3D8 lights (point and
directional, validated against `D3DLIGHTTYPE`). `Light_ApplyTimeOfDayTint` scales non-bright
lights by a time-of-day/zone factor before `SetLight`. Among the frame's passes, only the `dancer` world pass reaches `SetLight`
through direct calls (`CDx::SetLight` has 34 callers engine-wide). Fixed-function lighting.

---

## 10. Post-processing and the end of the frame (§18.10)

After the 3D passes, in order:

1. **Depth-gated distance blur** (`Post_DepthBlurComposite` `0x1000AAB0`) — **dead**: its gate
   `g_depthBlurEnabled_Dead` defaults to 0, is not in the registry table, and nothing else holds its
   address.
2. **Afterimage** (`Post_Afterimage` `0x10012F40`): blends the previous frame's copy over the scene,
   alpha = strength × 255, driven by an afterimage task (`AfterimageTask_OnMove` `0x1005FFD0`).
3. **Flash + zoom-feedback** (`Post_FlashAndZoomFeedback` `0x100132B0`): additive full-screen flash;
   a zoom trail blending the previous half-res accumulation (`MODULATE2X`), then re-copying.
4. Brightness/fade colour `0x10350174` (`0x80` = neutral); copyright text `0x101D0B00`.
5. **Composite** (`CDx_CompositeSceneToBackBuffer` `0x1000C0B0`): scene A drawn over the window
   viewport, linear filter, `MODULATE2X` — **the background-resolution → window upscale**. In
   stereo mode, A and B are packed side by side into `CDx+0x824` first, drawn with alpha test.
6. **UI:** if the UI target exists, push it, copy the scene in, draw menus / map / chat / status
   (`0x1015FA00` family and ~15 others), then composite (`0x1000ABE0`).
7. **Global fade quad** (`CDx_DrawFadeQuad` `0x1000A820`): alpha ≤ `0x80` darkens, > `0x80` whitens.
8. **2D layer** on a 640×512 virtual canvas (`0x1021D4C0`), fonts (`0x100384B0`, `0x10038520`), and in
   stereo mode the odd-frame overlay (§11).

---

## 11. Stereoscopic 3D mode (registry 0030; §18.14)

Off by default. When on (`g_cfgStereoMode` → `CEnv+0x18`, re-read every frame by
`CEnv_UpdateStereoMode` `0x1000D630`):

- **Every `CDx` draw is issued twice** while the per-draw flag `CDx+0x828` is set (the whole 3D world
  pass; text, occlusion queries and some UI clear it): once into scene A with eye index
  `CDx+0x810 = 0`, once into scene B with `= 1`.
- `CDx_ApplyStereoEyeProjection` `0x1000CF20` adds **∓0.006** (`g_stereoEyeOffset` `0x1034FFA0`) to
  the projection's X translation per eye — depth-dependent horizontal parallax.
  `CDx_RestoreProjection` `0x1000CF90` restores it.
- The composite packs left/right side by side. Two 1024×2 row masks (complementary magenta/green)
  and a 1×16 texture exist only for this mode. A 0..3 counter at `CEnv+0x1C` drives an overlay
  (`CDx_DrawStereoOddFrameOverlay` `0x1000BB90`) on odd frames only — consistent with a shutter
  sync signal.
- Certain: two-eye stereo rendering. Medium: the exact output format (side-by-side vs.
  row-interleaved vs. frame-sequential). **Cost when on: the entire 3D world twice.**

---

## 12. Where the time goes (performance summary for this project)

| Finding | Why it matters | § |
|---|---|---|
| CPU skinning + `DrawPrimitiveUP` everywhere | Vertices rebuilt and copied from CPU memory every draw; the main GPU-offload target | §6, §18.3 |
| Effects built on CPU, submitted UP; interpreter bypasses `CDx` | Effect-heavy scenes scale on CPU, and any render-state hook must also cover the interpreter's direct device calls | §18.11 |
| Runtime DXT encode + CPU mips, 20 uploads/frame | Credible cause of zone-in pop-in and hitching; cacheable | §18.9 |
| Background resolution default 512×512, upscaled | Scene resolution is a registry setting, not the window size | §18.10 |
| 30 fps cap by busy-wait `Sleep` loop | Frame pacing is set by `app+0x30`, not vsync | §18.10 |
| Per-actor work staggered 4:1 | Profiling must account for the four-frame cycle | §11 |
| Stereo mode doubles the world | Irrelevant unless 0030 is on | §18.14 |

Already optimized in the engine (§11): `sqgxContext`'s 16-stage texture-state cache, 1,000-index
batching, the shader-bake cache, display lists, the weight-premultiplied bone table.

---

## 13. Future box (parked; none of these changes the map)

- **Race condition** (`ResolveTree` `0x10073430` / `Evictor` `0x100740D0`): a live log has so far
  shown one thread across 85K lines and no `Evictor` hits. Needs a log started before the first
  zone-in after launch.
- **`StartDisintegration`**: zero hits so far. The DLL already repoints its 7 slots; needs a session
  with deaths / disintegration effects.
- ~~**Animation rate**~~ — **closed statically (master §18.16):** visible actors animate every frame;
  the 1-in-4 bucket only staggers the occlusion re-test for off-screen actors.

---

## 14. Key addresses

| Global | Address | | Function | Address |
|---|---|---|---|---|
| `CDx` instance | `0x1045666C` | | `Frame_Render` | `0x10011A00` |
| `g_pCamera` | `0x104568FC` | | `App_InitScene` | `0x10010D20` |
| `g_pEnv` | `0x104566E8` | | `CDx::Present` | `0x10009720` |
| `g_pProcessor` | `0x1047CF7C` | | `CMoTaskMng` draw | `0x10074C30` |
| `g_pTextureMng` | `0x1047B970` | | Main mesh pass | `0x1018B860` |
| App state record ptr | `0x10456A28` | | `dancer` world / end | `0x10251500` / `0x102515F0` |
| Actor draw list head | `0x1047D578` | | `TexMgr_UploadPump` | `0x1003ABB0` |
| Shared skeleton | `0x1045EC24` | | `CMoSchedularTask_Interpret` | `0x10057FB0` |
| `g_lightTable` | `0x104572B8` | | `CDx_CompositeSceneToBackBuffer` | `0x1000C0B0` |
| `g_registryConfigTable` | `0x103507E8` | | `PerActor_FourBucketStaggeredUpdate` | `0x100CBDE0` |
| `dancer` context | `0x10669400` | | `SkinVertices` | `0x10023290` |
| Pose scratch | `0x1045F030` | | `MotionQueue_UpdateAllChannels` | `0x1001A420` |
| Global actor table | `0x10480AF0` | | `CXiSkeletonActor_PoseCompose` | `0x100343C0` |

## Addendum — draw budget, zone environment, weather (master §18.17)

- **Actor draw budget:** per frame, `CXiActorDraw_UpdateDrawList` sets a limit from in-game setting
  index `0x3C`; `PerActor_FourBucketStaggeredUpdate` draws (and animates) over-budget actors only if
  they're linked to a qualifying actor. `0x1002B6E0` is the actor model draw.
- **`0x1065CB04` is the `XiZone` singleton**, not the camera; `0x1018B860` is the zone scene draw.
- **Fog and ambient** come from `XiZone` environment records (`Env_ComputeFog` `0x10189120`,
  `Env_ComputeAmbient` `0x10188E00`) into the renderer's `+0x39250`–`+0x3925C` block.
- **Weather:** 20 types (table `0x10377B18`), per-weather/per-area environment files, event opcode
  `0x100B84B0`, zone-scheduled effects. Selection by weather/time of day not yet traced.
- **Not yet mapped:** sky/sun/moon, time of day, water surface, PC shadow rendering, the in-game
  settings object.

## Addendum — time of day, resource types, environment (master §18.18)

- **Time of day:** weather records (type 47) are named `HHMM`; `Env_BlendTimeOfDay` (`0x1018A340`)
  interpolates the two bracketing the zone clock (`XiZone+0x1C8`). Registry 0034 = time-of-day tint.
- **World environment render:** `Zone_RenderEnvironment` (`0x1017B510`) — projection, lights, fog,
  draw. No separate sky pass; no clip-plane reflections; stencil shadows only in `dancer`.
- **Resource types:** all 97 names (PS2 `RES_TYPE`) matched to the PC loader switch at `0x100712D8`.

