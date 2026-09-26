# FFXiMain.dll — Master Findings

Consolidated from three source documents (`FFXiMain_Rendering_Object_System.md`,
`FFXiMain_Skeleton_Skinning_System.md`, `FFXiMain_Dancer_Middleware_Discovery.md`). This is a
current-state reference only — no session history, no correction narrative. Everything below is
the present understanding, synthesized into one structure organized by subsystem rather than by
when it was found.

**Confirmed classes: 136 | Confirmed functions: 1,468** (100 unique-accessor / 34 shared-accessor
/ 2 no-accessor). Reproducible via `scan_class_descriptors.py FFXiMain_uncomped.dll` — re-run
directly and checked against this exact figure, not left as an inherited, unverified number. An
earlier version of this line read 1,487; that number didn't reproduce when checked, and the
scanner's own imm32 thunk-recognition support (added later in this project) is the most likely
explanation for a real, legitimate shift in how many function addresses resolve, though the
earlier figure's exact origin wasn't traced further. This is a structural floor (what the scanner
can verify), not a measure of how deeply each class is understood.

## Contents

1. [Provenance: two naming systems describing the same engine](#1-provenance-two-naming-systems-describing-the-same-engine)
2. [Confirmed class hierarchy (FFXI wrapper layer, 136 classes)](#2-confirmed-class-hierarchy-ffxi-wrapper-layer-136-classes)
3. [Core math layer: `CMoProcessor`](#3-core-math-layer-cmoprocessor)
4. [Rendering-pipeline core classes](#4-rendering-pipeline-core-classes)
5. [The `CMoElem` effect-element family](#5-the-cmoelem-effect-element-family)
6. [Vertex skinning — complete, confirmed pipeline](#6-vertex-skinning--complete-confirmed-pipeline)
7. [Animation blending (`CYyMotionQue` family / `sqMotion`)](#7-animation-blending-cyymotionque-family--sqmotion)
8. [The `dancer` middleware — complete module census](#8-the-dancer-middleware--complete-module-census)
9. [Real-time lighting: `g_lightTable`](#9-real-time-lighting-g_lighttable)
10. [FFXI game bootstrap ↔ `dancer` seam: the `St*` layer](#10-ffxi-game-bootstrap--dancer-seam-the-st-layer)
11. [Confirmed performance-relevant findings, consolidated](#11-confirmed-performance-relevant-findings-consolidated)
12. [Tooling reference](#12-tooling-reference)
12b. [The PC `CXi*Actor` family's real vtable structure, corrected](#12b-the-pc-cxiactor-familys-real-vtable-structure-corrected)
12c. [The PC `CXi*Actor` family, fully swept: confirmed matches, self-authored names, and honest gaps](#12c-the-pc-cxiactor-family-fully-swept-confirmed-matches-self-authored-names-and-honest-gaps)
13. [Open questions](#13-open-questions)
14. Not part of this project's scope
15. Survey backlog results
16. First real dynamic-analysis session
17. `sub_10034620` — bone rotation/translation reader (corrected)
18. The PC graphics pipeline, end to end
14. [Not part of this project's scope (confirmed real, but excluded)](#14-not-part-of-this-projects-scope-confirmed-real-but-excluded)
15. [Survey backlog results](#15-survey-backlog-results)

---

## 1. Provenance: two naming systems describing the same engine

This binary contains two independent, non-overlapping naming layers:

1. **FFXI's own wrapper classes** (`CMo*`, `CYy*`, `CXi*`, plus a handful of unprefixed classes)
   — recovered structurally from `class_descriptor_t` nodes in `.rdata`/`.data`. No debug symbols
   exist for any of it; behavior is confirmed from real disassembly, but class *names* here are
   real (read from the binary), while *method* names are working labels assigned by this
   investigation.
2. **A separate, real middleware library called `dancer`** — developed at `C:\dev\dancer\` and
   integrated into the build tree at `D:\build0001\FFXi_Win\Main\dancer\`. Confirmed via literal,
   unstripped debug source paths, `__FILE__`/`__LINE__`-tagged error strings, and embedded
   code-generation templates — not inferred from shape. 16 modules, 86 source files (confirmed
   exhaustive via a `total_pages: 1` broad path search).

**These are the same engine described twice.** Every structural inference the first layer had to
make was independently confirmed, by name, once the `dancer` strings were found — the keyframe
format, the bone-weight-group shape, the joint hierarchy, the light/directional distinction, all
matched exactly. FFXI's `CMo*`/`CYy*`/`CXi*` classes are the game's own wrapper around `dancer`'s
lower-level API, not a separate implementation.

A third naming layer exists only as a historical artifact: the PS2 beta binary (`maxomi9`) used a
`Kz`/`Ym`-prefixed convention (`KzObject`, `YmElem`, `KzOSM`, etc.) with **zero** string matches
in this retail binary — the whole subsystem was renamed between the PS2 beta and this PC build.
The `Ym*Elem`→`CMo*` and `KzObject`→`CYyObject` correspondences are confirmed via direct
name/hierarchy correspondence; the specific `KzOSM`/`KzMOD`/`KzSKD`→`CYyOsmTask`/`CYyModel`-family/
`CYySkl` three-way mapping is inference from shape, not independently verified.

A fourth, real but non-runtime source tree: `C:\dev\dancer\tools\mdlview\src\` — an internal
model/scene preview tool (confirmed via `"MDLVIEW Light File"`/`"MDLVIEW Camera File"` export
strings), not part of the shipped game's runtime path.

**Mangled C++ names in the IDA database are not a source of truth.** `FFXiMain.dll` is
stripped, yet the database carries mangled names such as `??YConvexDecomposition@@...`. Their
functions carry IDA's `FUNC_LUMINA` flag (`0x10000`): the names were supplied by Hex-Rays'
Lumina server, which matches function bytes against other people's databases. On this binary
the matches are overwhelmingly false positives on tiny, generic bodies — the same database
attributes Microsoft Concurrency Runtime (a Visual Studio 2010 component), PopCap's SexyApp
framework, DXUT and 58 copies of `codecvt_base::do_always_noconv` to this 2002-era engine, and
names `CXiSkeletonActor`'s field accessors after `SchedulerProxy`/`SchedulerBase` methods. The
"ConvexDecomposition" operators are the engine's own `float3` add/subtract/scale helpers
(`0x10026F20` is the same function this document calls `Vec3_AddInPlace`). `D3DXQuaternionDot`
and `CD3DXCodecDXT` are more plausible (D3D8-era games often statically linked D3DX) but come
from the same source and are unverified. Check provenance before using any such name — the
`name_provenance` tool (§12) does this.

**A sixth source: the PS2 build's own debug data.** `SCUS_972.66` (the Dec-2003 PS2 disc
executable, Metrowerks CodeWarrior for MIPS) carries a 12,227-entry function symbol table *and* a
14.8 MB DWARF version 1 `.debug` section — 321,865 entries describing 2,758 distinct named types
with every member's name, type and offset, plus inheritance. The parser written for it was
validated against the independent `XiEvents` project: every PS2 field name that project published
for `REQSTACK` and `XiEvent` (including its `Priorty` typo) appears at the right place. `dancer`
exists on PS2 as well, as a separately loaded module (`Dancer.bin`, relocations in
`.relDancer.bin`, functions at `0x6A0000`+), with 1,936 named `sq*` functions and 51 `sq*` types.
The PC's `CYy*` classes have no PS2 namesakes; the PS2 uses `Kz*`/`Ym*` names for that layer.

**The retail-install `FFXiMain.dll` is packed; the copy this project disassembles from is not.**
Direct inspection of a fresh copy from the game install (PE section table) shows `.text` with
`SizeOfRawData = 0` and zero entropy — no code bytes exist on disk for that section at all — while
a section named `POL1` carries entropy ≈7.5 (consistent with compressed or encrypted data) and the
entry point (`0x10BE4A50`) sits just before `.reloc`, outside every named section: the shape of a
custom packer/protector stub that decompresses the real `.text` into memory at load time, runs it,
and only the unpacked, in-memory image is what any disassembly-based analysis in this project has
ever actually read (referred to elsewhere as `FFXiMain_uncomped.dll`). Confirms this is why a
class-descriptor scan (data-only, reads `.rdata`/`.data`, unaffected by code packing) still finds
the same 136 classes against the raw retail file, while any scan that reads `.text` bytes directly
finds almost nothing there — not a regression in those tools, but the raw file genuinely lacking
the code on disk. Anyone pointing a tool at the retail file directly needs an unpacked/dumped copy
first, not the file as installed.

**An eighth source: an independent, separately-maintained C++ reconstruction of this same binary**
(four repos; the main one alone has 1,827 headers and 1,014 `.cpp` files, cross-referenced against
the same retail image via its own automated extraction tool). Not taken on faith: its most
consequential specific claim (§6's true vtable size) was independently re-derived from scratch
against the live IDB before being accepted, and several of its detailed sub-claims (exact
constructor addresses for five classes, one address correction) were spot-checked the same way and
matched exactly — genuinely careful, cross-verifiable work, not just plausible-sounding text. It is
not infallible either: one of its own claims was checked and found wrong by the identical
systematic error (a `-0xD0` banner offset) it had already caught and fixed in other classes,
confirming that a source's overall credibility never substitutes for checking its individual,
falsifiable claims. Where this document cites it directly, that citation means the specific claim
was independently re-verified, not merely copied.

---

## 2. Confirmed class hierarchy (FFXI wrapper layer, 136 classes)

**Independently cross-validated by external, unrelated community reverse-engineering.** Ashita's
own public SDK header (`plugins/sdk/ffxi/entity.h`, AshitaXI/Ashita-v4beta) — built entirely for
addon development, with no connection to this project — independently names `CYyObject` as "the
base ... VTable pointer" for its entity structure's first field, and types its `ActorPointer`
field as `CXiSkeletonActor*`. Two completely separate reverse-engineering efforts, using
completely different techniques (static class-descriptor scanning here vs. addon-developer memory
mapping there), arriving at the identical class names for the same proprietary binary — real,
independent confirmation, not a coincidence. The same SDK's `entity_t` structure (684 bytes) is
confirmed to be a *different, smaller* object than the actor itself — it merely holds a pointer
to it (`ActorPointer`) — so it doesn't have the depth to resolve this project's own offset-level
open questions about the actor object's internals; addon developers don't need that depth, and
the public SDK doesn't expose it. One additional, genuine corroboration: `entity_t`'s
`Attachments[12]` field is documented as holding secondary `CXiSkeletonActor*` pointers "used
with things such as GEO Indi's" (Geomancer's area-effect spells) — independently supporting this
project's own confirmed `CMoGeneratorClone` finding (§5) that attached-effect clones are
predominantly linked to `CXiSkeletonActor` territory, from a completely different angle.

```
CYyObject (4B — vtable pointer only)
├── CAcc, CAcc2, CApp, CDx, CEnv, CShader, XiCapture, CXiOpening, CXiMovie
├── CMoAttachments, CMoCamera, CMoCelestial, CMoDX, CMoDxStatusMng, CMoGeneratorClone,
│   CMoOT, CMoOcclusionMng, CMoPathObject, CMoProcessor, CMoResourceMng, CMoSpline
├── CMoResource
│   ├── CMoRabRes, CMoSphRes, CYySepRes
├── CMoTask
│   ├── ActorTechLoadPollingTask, CAtelIdleTask, CMoActorColorDriveTask,
│   │   CMoActorRotationDriveTask, CMoCameraTask, CMoLockColorDriveTask,
│   │   CMoLockLookAtDriveTask, CMoPathDriveActorTask, CMoSchedularTask,
│   │   CTsZoneMap, CXiActorDraw, CXiActorNameDraw, CXiSkeletonActorRes, CYyAfterImage,
│   │   CYyMusicLoadTask, CYyOs2VtxBuffer, XiActorTimerTask
│   ├── CMoOtTask
│   │   └── CMoElem
│   │       ├── CMoD3aElem → CMoD3aLightmapElem, CMoVuAnmElem
│   │       ├── CMoD3mSpecularElem, CMoDisintegrateProgElem, CMoDistModelElem,
│   │       │   CMoDistMorphElem, CMoDistRingElem, CMoLfdElem, CMoNullProgElem,
│   │       │   CMoPointLightProgElem, CMoSkeletonElem, CMoVuLineProgElem, CYySoundElem
│   │       └── CMoDist → CMoVuDist
│   └── CXiActor
│       ├── CXiAtelActor
│       │   └── CXiControlActor
│       │       ├── CXiCollisionActor
│       │       │   └── CXiSkeletonActor
│       │       │       ├── CXiDancerActor → CXiGeomActor, CXiMannequinActor, CXiSklFurnitureActor
│       │       │       └── XiSkeletonActor2 → XiChocoboActor2
│       │       ├── XiDoorActor
│       │       └── XiModelActor → XiFurnitureActor
│       │   └── XiLiftActor
│       └── CXiDollActor
├── CMoTaskMng
├── CXiTimer → CXiTimerHigh, CXiTimerLow
├── CYyCamMng2, CYyIcon
├── CYyMcb
│   ├── CYyDataMcb → CYyLowerObject → CYyLowerMemory; CYyUpperObject → CYyUpperMemory
│   ├── CYyElemMcb → CYyElemObject → CYyElemMemory; CYyWorkObject → CYyWorkMemory
│   ├── CYyExMcb → CYyExObject → CYyExMemory
│   ├── CYyLoadMcb → CYyLoadObject → CYyLoadMemory
│   └── CYyMenuMcb → CYyMenuObject → CYyMenuMemory
├── CYyModel, CYyModelBase, CYyModelDt, CYyMotionQueList
├── CYyNode → CYyResfList
├── CYyOsmTask → CYyOsmTaskXform
├── CYyQue → CYyBlendQue → CYyMoveBlendQue; CYyMotionQue
├── CYySkl
├── CYyTexBase → CYyTex; CYyTexMng
├── CYyVb, CYyVbMng
├── XiPng, XiZone
└── YkAlbum, YkBitmap, YkDiary, YkFurniture, YkJpeg, YkJpgBit, YkMyroom, YkSoldier, YkZip,
    YmCombineWeather
```

`PTR` and `attachdata` are known false positives (isolated root entries with no accessor or
vtable link).

**The actor hierarchy matches the PS2 debug data.** PS2 declares `XiActor` (`0xA0` bytes, base
`YmElemCore`) → `XiAtelActor` (`0xB0`) → `XiControlActor` (`0x180`) → `XiCollisionActor`
(`0x1E0`) → `XiSkeletonActor` (`0x450`), and `XiDollActor` separately — the same chain as the PC's
`CXi*` classes. The PC objects are larger (`CXiSkeletonActor` accessors reach past `+0xA00`), so
PS2 offsets do not transfer directly, but member *names and order* do once anchored (§6).

**Actor-family constructors, traced by vtable stores.** Three batched sweeps (variant accessors
→ the vtables holding them → the code storing each vtable) cover the actor hierarchy:

- **Most `_variant` accessors are unused.** Of 23 actor-family variants, only 8 are referenced
  anywhere in the image; the other 15 are unreferenced duplicate copies. Each of the 8 is slot 0 of
  exactly one vtable: `CXiActor` `0x1032CFE0`, `CXiAtelActor` `0x1032E3C8`, `CXiControlActor`
  `0x1032DFC8`, `CXiCollisionActor` `0x1032DB40`, `CXiDancerActor` `0x1032F4F0`, `XiModelActor`
  `0x10330AA0`, `CXiSkeletonActor` `0x10330F40`, `XiSkeletonActor2` `0x103313E8`.
- **`CXiSkeletonActor` has four confirmed constructors plus one probable.**
  - `XiSkeletonActor2`'s wrapper constructors (1–4 arguments, four of them in code IDA had never
    analyzed, now created) each call exactly one `CXiSkeletonActor` constructor and then store
    their own vtable. That confirms `CXiSkeletonActor_Constructor_1Arg`…`_4Arg` from call sites.
  - A fifth, `CXiSkeletonActor_Constructor_Factory`, is called only by `sub_1008F740` (8 calls, an
    apparent actor factory) and is a constructor by pattern.
  - `XiSkeletonActor2`'s destructor and scalar deleting destructor are identified the same way.
- `CXiControlActor_Constructor` stores `CXiAtelActor`'s vtable, then its own: the base constructor
  is inlined.
- Storing functions not yet classified as constructor or destructor: `CXiActor` (`sub_10081CF0`,
  `sub_10082B40`), `CXiCollisionActor` (`sub_100A4C20`), `CXiControlActor` (`sub_100A8CA0`),
  `CXiDancerActor` (`sub_100AB6C0`, `sub_100AB700`, `sub_100AB810`), `XiModelActor`
  (`sub_100C4160`, `sub_100C41B0`, `sub_100C41F0`), `XiSkeletonActor2` (`sub_100D7240`). Store
  position is only a hint: exception-handling prologues make early stores ambiguous.

### Confirmed multiple-inheritance patterns (three distinct, easy to conflate)

1. **A real base class with its own descriptor and normal accessor** (e.g. `CMoResourceMng`,
   embedded in at least one `CMoTask` compound vtable).
2. **A forwarding-only mixin with no independent identity** — every slot tail-calls back into
   the primary object's own vtable (10 confirmed instances, labeled `<mixin-of-ClassName@ADDR>`
   by the scanner).
3. **Coincidental neighbors in `.rdata`** with no actual object-layout relationship — a
   linker-placement accident. At least one confirmed case exists; address adjacency alone is
   never sufficient evidence of a real relationship.

**Large secondary-base offsets (imm32 thunks).** `this`-adjusting thunks with offsets of 128 or
more are encoded as `sub ecx, imm32` (`81 E9 …`) instead of the imm8 form the scanner checks. A
wildcard byte search finds exactly **four** in the whole binary, at `0x100AC2F0`–`0x100AC320`,
all `sub ecx, 0xC4 ; jmp …` into methods at `0x100ABCA0`, `0x100ABE80`, `0x100AC070` and
`0x100AC0B0`. They sit in a secondary vtable at `0x1032F91C`, directly after the class record for
**`CXiDollActor`** (name, size `0x440`, parent). So `CXiDollActor` embeds one secondary base at
`+0xC4` and overrides four of its methods. Adding the imm32 encoding to the scanner would add this
one mixin annotation and no new classes.

### Other confirmed structural conventions

- **Vtable slot 6 = destructor**, confirmed across every class checked (standard
  scalar-deleting-destructor shell: call the real destructor, conditionally call a shared
  `delete` helper if the flags argument's low bit is set). One confirmed exception:
  `CMoProcessor`'s slot 6 does not follow this convention (see §3).
- **`CMoTask`'s own size is exactly 0x34 (52 bytes)** — offset `0x34` in any `CMoTask`-derived
  class is simply "where `CMoTask`'s own fields end"; what actually lives there varies per class.
- **Size-tag technique**: constructors sometimes write `sizeof(class)` into an instance field,
  useful for disambiguating otherwise-identical shared-accessor vtables. Not universal — several
  siblings' constructors write no tag, or a tag matching zero or multiple known classes.
- **Shared-accessor ambiguity is a real compiler artifact, not a scanner bug**: when sibling
  subclasses never override `GetRuntimeClass`, the compiler emits identical code for all of
  them — the vtable-to-subclass mapping is genuinely lost information, recoverable only via a
  constructor trace (find what stores that exact vtable address).
- **Positive-offset `trivial` thunks** (`lea eax,[ecx+N]; ret` for small offsets `4, 8, 0x10,
  0x14, 0x34, 0x44`) are a family of "return a pointer to my Nth embedded member" accessors,
  most plausibly used by the large `XiActor`-family classes to expose internal sub-components
  through their huge vtables.

---

## 3. Core math layer: `CMoProcessor`

The engine's central CPU vector/matrix math utility — **not** a rendering-backend tier (an
earlier working hypothesis, superseded by direct evidence below).

- **51-slot interface (45 own methods)**, built via a hardware-capability-tiered factory selected
  once at startup: a "full" tier saturated with **AMD 3DNow! SIMD** instructions (`femms`,
  `pfmul`, `pfacc`), and two portable x87 FPU tiers computing identical scalar math to the 3DNow!
  version (differing mainly in allocated size — 2720 vs. 2992 bytes — not logic). A fourth,
  minimal 6-slot stub with no destructor override is the "capability too low, do nothing" null
  object. The real split is **CPU-capability tier, not GPU/shader tier.**
- Reached via a global pointer, `g_pProcessor` (`0x1047CF7C`), written from exactly one factory
  function. All 4 distinct compiled vtables resolve to the same class via their slot-0 accessor.
  Known limitation: `classify_confidence()` reports this class as `unique` (one accessor
  *address*) despite 4 genuinely distinct compiled vtables — the linker folded several identical
  tiny accessor stubs across real subclasses.
- **Confirmed primitives**: `Vec3_Add` (slot 42), `Vec3_Mul` (slot 43), `Vec3_MulAdd`/lerp-shaped
  (slot 44), `Vec3_Length` = `sqrt(x²+y²+z²)` (3DNow! at slot 37, FPU at slot 39, confirmed
  matched pair), `Mat4x4_Multiply` (`0x10070210`, slot 0x24, real 4×4 multiply confirmed via two
  independent call sites), `Mat4x4_Transpose` (slot 47, full 4×4 transpose), `Mat4x4_SafeTranspose`
  (`0x1006F0A0`, aliasing-safe wrapper copying to scratch buffers `this+0xAA0`/`this+0xAE0` before
  calling the real transpose when in/out pointers match), `Mat4x4_FromEulerAngles` (`0x1006FA40`,
  builds a rotation matrix from pitch/yaw/roll via cached sin/cos pairs).
- **Four independent rotation-matrix storage slots** (`this+0x810`/`+0x850`/`+0x890`/`+0x8d0`),
  confirmed built from Euler angles via a real usage site (not just a reset). Both hardware tiers
  build genuine identity matrices at construction (a near-miss reading one tier's buffer as
  all-zero was a pre-initialization artifact, not a real tier difference).
- **A third internal matrix region** (`this+0xAA0`) is a scratch/staging buffer for
  `Mat4x4_SafeTranspose`'s aliasing-safe wrapper — directly connects to and completes
  `Mat4x4_Multiply`, which reads from this exact offset.
- **Internal ring-buffer pool** (slot 28 = `Pool_AllocSlot`, `0x1004E3F0` = `Pool_FreeSlot`,
  `0x1006CE40` = `Pool_InitSlots`): a genuine **LIFO stack/arena allocator**, not a monotonic
  counter — allocate reads-then-increments a counter into a 32-slot array, free
  decrements-then-stores. 258 references across the binary; confirmed via a clean, complete
  allocate→use→free example in `CMoDistMorphElem`. Never overflows as long as calls are properly
  nested. The identical counter/array pattern (`[global+0xa90]` indexing `[global+0xa10]`) recurs
  in `CMoCameraTask`'s update code — a genuine, reusable engine idiom, not a one-off.
- **Many slots are pure forwarding thunks** to other slots in the same vtable (8, 10, 38, 40, 45,
  46) — internal aliases, several "different" operations reaching the same implementation two
  ways.
- Slot 6 does **not** follow the standard destructor convention here (no scalar-deleting-destructor
  shell; real, non-trivial control flow with multiple branches, not fully characterized).

**Race-condition candidate**: `CMoProcessor_ScratchMatrixOp`'s counter increment/decrement and
array read/write are plain, unsynchronized `mov`/`inc`/`dec`. Reachability from more than one
thread concurrently is not confirmed either way — flagged as a genuine open question given this
codebase is confirmed not naively single-threaded overall (`sqmoChannelBuildSQO` uses a real
mutex).

---

### Construction, tiers and the scratch-matrix pool (confirmed from the factory and constructor)

`CreateProcessorInstance` (`0x1006CB50`) builds exactly one processor and stores it in
**`g_pProcessor` (`0x1047CF7C`, 347 references)**, choosing one of three tiers:

| Tier | Condition | Allocation | Final vtable | Extra init |
|---|---|---|---|---|
| 1 | `byte_1047CF78` set (the 3DNow! tier) | `0xBB0` | `CMoProcessor_vtbl_ambiguous1` | constructs 4×64-byte matrices at `+0x810`; `sub_1006EF70` |
| 2 | `g_processorCapabilityFlag` set | `0xBB0` | `CMoProcessor_vtbl_ambiguous0` | `sub_100700E0` |
| 3 | neither (plain FPU) | **`0xAA0`** | `CMoProcessor_vtbl_ambiguous2` | none |

All three run `CMoProcessor_InitRotationMatrices`, which defines the shared layout:

| Offset | Field | Evidence |
|---|---|---|
| `+0x000` | vtable | per tier, above |
| `+0x004` | `ScratchMatrices[32]` (4×4 floats each, to `+0x804`) | the free list's initial pointers target `this + 4 + 64·i` |
| `+0x810` | `RotationMatrix[4]` | four identity matrices copied in |
| `+0xA10` | `ScratchMatrixFreeList[32]` (pointers) | filled with the 32 slot addresses |
| `+0xA90` | `ScratchMatrixStackTop` | zeroed; `ScratchMatrixOp` acquires `list[top++]` and releases with `list[--top] = m` |
| `+0xAA0` | `TransposeScratch` | **not present in tier 3**, whose allocation ends at `0xAA0` |
| `+0xAE0` | `TransposeScratchTemp` | tiers 1–2 only |

The pool counter and list are the plain, unsynchronized `inc`/`dec` pair flagged as a race
candidate in §11. `sub_1006E970` (a projected-bounds helper) uses the same acquire/release
pattern. The IDB's `CMoProcessor` struct is `0xBB0` bytes (tiers 1–2) with `g_pProcessor` typed
as `CMoProcessor *`; for tier 3, fields from `+0xAA0` on do not exist.

## 4. Rendering-pipeline core classes

| Class | Confirmed content |
|---|---|
| `CMoCamera` | 11-slot vtable. Get/set pair (`this+0x14`, slots 1/4) for a linked external object. `0x1003CB30`: copies two fixed 16-byte blocks (`this+0x20`/`+0x34`, plausibly position/direction), decodes a packed-count header (`(field>>7)&0x7FFFF`, minus 2) and copies that many 16-byte waypoint records into a growing buffer at `this+0x70` — a camera path/keyframe list, not a single static position. `0x10071980`: lazy-init singleton accessor returning a fixed global (`0x109F81C0`). Destructor releases `this+0x30` via the shared `ReleaseSubObjectIfPresent` helper. |
| `CDx` | 7-slot (destructor-only) shape. Destructor releases two handle-like values (`+0x1EC`/`+0x1F0`, checked against `0`/`-1` sentinels) via a virtual call through an interface at `this+0xC`, then calls `CAcc_Destructor` on its four `CAcc` members (`+428`, `+444`, `+460`, `+476`). **Constructor confirmed** (`sub_10008F90`): builds three `CAcc`s as an array at `+428/+444/+460` and a fourth at `+476`, plus members at `+400` (`sub_1000D040`) and `+500` (`sub_10017030`); stores its two constructor arguments at `+8`/`+0xC`; and initializes six floats at `+0x174`–`+0x188` to `128.0f` (`0x43000000`) and `+0x18C` to `0x80808080` — the PS2 "`0x80` = 1.0" convention again (see §6, actor opacity). `DetectDeviceCapabilities` (`0x100091B0`) is `CDx`'s other own method: queries that same interface for shader-model support, checking exact real DirectX constants — `0xFFFE0101`=`D3DVS_VERSION(1,1)`, `0xFFFF0101`=`D3DPS_VERSION(1,1)`, `0xFFFF0104`=`D3DPS_VERSION(1,4)` — and texture-stage count (defaults to 8, switches to 16 only if capability bit `0x10000` is set). **Also confirmed to load the game's custom animated mouse cursors from disk** in this same function: reads the current directory, walks a filename-suffix table (`aMousenorAni`), and loads each via `LoadCursorFromFileA`/`LoadCursorA` — `CDx` is not purely a device-capability class, it also owns cursor asset loading. Its only caller (`sub_10001520`) passes the global `dword_1045666C` as `this` — **`dword_1045666C` is confirmed to be (or provide) the one `CDx` instance**, the same global used pervasively as the renderer/device object throughout the draw-dispatch code discussed in the ongoing dynamic-capture work on this binary. |
| `CMoDX` | 7-slot shape. Destructor loops over exactly **8 fixed slots**, releasing each via a shared interface if flagged — independently confirmed by `DetectDeviceCapabilities`'s own default-to-8 logic. Reads as the fixed-function texture-stage state block. |
| `CYyTexMng` | 7-slot shape. Destructor releases one owned sub-object. Minimal. |
| `CYyVbMng` | 7-slot shape. Destructor walks and tears down a **global** linked list of vertex-buffer objects (head pointer `0x1047B978`), then clears the head — a global vertex-buffer registry independent of any single instance. |
| `CMoCelestial` | Genuinely trivial destructor — resets the vtable pointer only, no owned resources. |
| `CMoOcclusionMng` | Releases one sub-object (`+0x18`), then tail-jumps into the exact same address confirmed as `CAcc`'s destructor — identical-code linker folding (both derive from `CYyObject` and have handle-shaped fields at the same relative offsets), not an actual class relationship. |
| `CYyCamMng2` | Minimal, delegates to shared base cleanup. |
| `CEnv` | Minimal shell, not pursued further. |
| `CAcc` / `CAcc2` | `CAcc` (`sizeof 0x10`) is a **render-target bundle**, confirmed at its two known fill sites: `+4` is an `IDirect3DTexture8*` colour target (`0x1000A6E0`, real D3D8 `CreateTexture`, `D3DUSAGE_RENDERTARGET`, tried in format order A8R8G8B8/A1R5G5B5/X8R8G8B8/X1R5G5B5/back-buffer); `+0xC` is an `IDirect3DSurface8*` depth-stencil surface (`0x1000AD70`, `CreateDepthStencilSurface`); `+8` is confirmed always null at both sites (the out-parameter is written elsewhere and never copied in). Consumer `CDx_0x10009EA0` binds both via `SetRenderTarget`/`SetViewport` and pushes onto a per-`CDx` render-target stack. Fill sites: `sub_10044270` (a 256×256 cubemap), `sub_100755A0` (a scene-stream context sized to the stream). `CAcc2` is larger (`sizeof 0x1C` = vptr + 6 dwords, not 4) and its destructor issues six releases, so it wraps six COM pointers, not three. Constructor `sub_1000CFB0` only sets the vtable (`0x10329A3C`) and zeroes `CAcc`'s three pointers. **An earlier identification of `CAcc` as a DirectInput device wrapper is withdrawn:** the game's actual DirectInput devices are created inside a different object (next row). Not yet found: any write to the `CAcc`s embedded directly in `CDx` (`+0x190`/`+0x1AC`/`+0x1BC`/`+0x1CC`/`+0x1DC`) or in `CMoOcclusionMng` (`+8`) — a byte scan of their surrounding code finds only the constructor/destructor, no fill site, so either they're genuinely unfilled or filled through a computed pointer an offset scan can't catch. |
| DirectInput devices (inside `dword_10455C20`) | `sub_10001BB0` allocates the `0xDC4`-byte application-state object `dword_10455C20` (§10); `sub_100058F0` calls `DirectInput8Create(hinst, 0x800, IID_IDirectInput8, this+132, NULL)`. Three device setup functions follow, each identified from its own GUID and format bytes: `sub_10007E20` = **system keyboard** (`GUID_SysKeyboard`, `{6F1D2B61-…}`; data format size 256, the `c_dfDIKeyboard` signature); `sub_10007EF0` = **system mouse** (`GUID_SysMouse`, `{6F1D2B60-…}`, stored immediately after the keyboard GUID); `sub_100083D0` = **joystick with force feedback** (`EnumDevices` class 4 = game controllers, `DIPROP_RANGE` −127..127 on 8 axes, POV enumeration, `CreateEffect` with `GUID_ConstantForce` `{13541C20-8E33-11D0-…}`). Each device runs `CreateDevice` (vtable +12), `SetProperty(DIPROP_BUFFERSIZE, 320)` (+24), `SetDataFormat` (+44), `SetCooperativeLevel` (+52), `Acquire` (+28). The fourth sibling call, `sub_10008020`, is Japanese IME detection (`GetKeyboardLayout`/`ImmGetDescriptionA` against a table of Microsoft IME and ATOK names), not a device. The joystick's effect is what `sqOpcode` rumble drives (§10). |

### Draw-list management: `CXiActorDraw` / `CXiActorNameDraw`

- **`CXiActorNameDraw`**'s own method: gated behind a check of the global known here as `g_currentRenderPass` (`0x10456A28`) against `0x60`. That global has 295 references across the binary and is initialized with a fixed structure address during window creation (`sub_100157E0`); it is one central application-state value, so "render pass" describes only this one use and should be read as a provisional label, sets up
  a precisely-verified alpha-cutout billboard-text render state — `D3DRS_ZWRITEENABLE=1`,
  `D3DRS_FOGENABLE=0`, `D3DRS_ALPHATESTENABLE=1`, `D3DRS_ALPHAFUNC=5`
  (`D3DCMP_GREATEREQUAL`), `D3DRS_ALPHAREF=0`, `D3DRS_ALPHABLENDENABLE=1`, `D3DRS_SRCBLEND=5`
  (`D3DBLEND_SRCALPHA`), `D3DRS_DESTBLEND=6` (`D3DBLEND_INVSRCALPHA`) — every state ID and value
  checked against the real D3D8 enum (this is a Direct3D 8 client throughout — device calls use
  D3D8 vtable positions; the values happen to match D3D9's too, but the API is D3D8). Exactly the
  configuration for a character's floating name tag.
- **`CXiActorDraw`**'s own method delegates into `0x10082D70`: allocates a 60-byte record (the
  same stride confirmed in the skinning pipeline), reads a global (`0x1047D578`) heading a linked
  list of drawable actors (walked via `+0x54`), and compares a float field (`+0x8C`, plausibly
  view-space depth) between adjacent list nodes — maintaining a **depth-sorted draw list** for
  correct back-to-front transparency ordering. Conditionally calls a per-actor virtual method
  (vtable offset `0x288`) and sets dirty-flag bytes (`+0xB0`/`+0xB2`).
- `sqmdSort.c` (the `dancer` module) is a plausible real source for this depth-sort — inferred
  from module/behavior match, weaker than the string-confirmed connections elsewhere in this
  document.

---

## 5. The `CMoElem` effect-element family

All are `CMoTask`→`CMoOtTask`→`CMoElem` descendants. A shared "does this respond to message type
N" check recurs across siblings (confirmed at types 4, 6, 7, 9, 11, 13 — a coherent numeric
message-dispatch scheme, not fully enumerated).

| Class | Confirmed behavior |
|---|---|
| `CMoD3aLightmapElem` | Get/set pair for `+0x194` (lightmap texture reference). Frame function: reads a signed 16-bit frame count from the linked resource (`+0x32`), clamps the object's frame counter (`+0x170`), walks a variable-length record array (`resource+0x48`, each record `(byte_at_offset+2)×144+4` bytes) to the active frame, submits it to `CMoProcessor` — a real animated/multi-frame lightmap format. |
| `CMoD3mSpecularElem` | Message-type-7 check. Cached specular power/intensity getter (gated on flag `+0x179`). Bitfield setter on render-state flags (`+0x10c`). Computes an array index from a 16-bit resource field ×3 (RGB stride) and calls through `CMoProcessor`'s vtable, confirming `CMoProcessor` is shared infrastructure, not narrow to any one effect type. Own vtable `0x1032AD20`, constructor `0x10040F50` — confirmed against the product reconstruction's own dedicated source file. **Correction:** an earlier pass here wrongly attributed vtable `0x1032AC90`/destructor `0x1003FB10` to this class on a coincidental size match (both independently stamp `448` at `+0x176`); `0x1032AC90` is a separate, unnamed `CMoElem`-derived class (see the unnamed-siblings row below) that this class has no relationship to. |
| `CMoPointLightProgElem` | Computes `this+0x188` and passes it to a virtual call on `g_pProcessor` — registering light data with a central manager. Falloff/radius math over `this+0x54/0x58/0x5c` (position or color triple), gated behind a cached-flag byte. Message-type-11 check. |
| `CMoDisintegrateProgElem` | Thin: standard destructor shell + shared cleanup (`0x10044970`) + sub-object teardown (`+0x194`) + message-type-13 check + a deliberate no-op override. |
| `CMoVuLineProgElem` | Same thin shape as above, message-type-9 check. |
| `CMoDistModelElem` | `BuildDistortedMesh`: early-exits via a time comparison against the recurring constant `0x103295D8`. Reads a 16-bit count from the linked resource (`+0x36`), computes a buffer size `count × 3 × 36` bytes (triangles × 3 vertices × 36-byte vertex — position+normal+something), allocates, copies the source geometry via `rep movsd/movsb`. Two `CMoProcessor` pool-slot allocations (one carrying a float pair from `+0x194`), submitted through both `g_pResourceMng` and `CMoProcessor` vtable slot `0x24` (`Mat4x4_Multiply`) — a real, working geometry-distortion effect operating on an actual duplicated mesh copy, not a shader trick. |
| `CMoDistMorphElem` | `UpdateMorphBlend`: lazily computes/caches a morph-target handle (`+0x1bc`), validates morph blend data, allocates a `CMoProcessor` pool slot, stages a float pair, registers a second slot with `g_pResourceMng`, submits both via `CMoProcessor` slot `0x24` (same 3-argument shape as `CMoDistModelElem` — a generic "submit a parameter block" entry point shared across distortion types), calls the morph-apply function (`0x1003F440`), invalidates the cached handle (scoped to one call, not persistent), copies a 5-dword current→previous double-buffer, then **explicitly frees both pool slots** — a complete, balanced allocate→use→free cycle. **Genuinely derives from an unnamed `CMoElem`-family base** (vtable `0x1032AC90`, see below): its destructor is empty on its own account and legitimately chains to that base's destructor (`0x1003FB10`) before `CMoElem`'s shared cleanup — real C++ inheritance, not a copy-paste bug (confirmed against the product reconstruction's own source, which documents exactly this chain). |
| `CMoDistRingElem` | `AllocRingGeometry`: reads two signed byte fields (`+0x1b4` ring-segment count, `+0x1b5` ring count), computes segment count as `2n+2` (standard n-segment ring vertex count), scales by ring count, calls an allocator — a configurable concentric-ring distortion effect (shockwave/magic-circle geometry). |
| `CMoLfdElem` | Multiplies two fields (`+0x134`/`+0x138`, plausibly rate/scale) into `0x1047BC0C` — a confirmed cross-effect-type shared scratch global (multiple unrelated classes read/write it). |
| `CMoVuAnmElem` | On first run (flag `+0x1dc`), reads and scales a byte field from linked resource data (`resource+5`, ×3) — consistent with parsing VU ("Vector Unit," PS2-era) animation data. |
| `CMoNullProgElem` | Exactly three own (non-shared) slots: accessor, destructor (`0x100531B0`), and slot 11 (`0x100531A0`, a trivial `this+0x138=1.0f` setter). No other content exists. |
| `CYySoundElem` | Genuine audio-playback timing logic — elapsed-time-vs-threshold check, message-type-14 check, an "is active" validity check. Shares the `CMoElem` base because that base handles any attached effect (audio included), not because it does rendering work. |
| `CMoD3aElem` | The shared intermediate parent of `CMoD3aLightmapElem`/`CMoVuAnmElem`. Shared-accessor (3 compiled variants) — any specific vtable would carry subclass-attribution ambiguity; its two children already cover the concrete behavior at this level. |
| 5 unnamed `CMoElem`-derived siblings | All 5 report `GetRuntimeClass` as plain `CMoElem` (no distinct descriptor of their own — confirmed against the product reconstruction's `ClassExtract` tool, which independently proves no getter is ever shared between two *different* descriptors here), so they can't get real names from static analysis alone. But each is a genuine, distinct, real class with its own constructor/destructor and at least one distinguishing method, all confirmed against the product reconstruction's source (which names them by placeholder, `CXi<hash>_VT_<address>`, pending real names) and cross-checked instruction-by-instruction against the retail binary. None resets its vtable to "another of the five" — an earlier claim here conflated a genuine base-class chain (`0x1032AC90` is the real base of at least `CMoDistMorphElem`, not a sibling) with sibling-to-sibling sharing. Per-class: |

| Vtable | Ctor | Dtor | Distinguishing method(s) | Notes |
|---|---|---|---|---|
| `0x1032AC90` | `0x1003FB70` | `0x1003FB10` | `IsKind` (true only for kind 15, `0x1003FB40`); `RebuildBlendWeights`/`ReleaseBlendWeights` (`0x1003FBB0`/`0x1003FC30`) manage a cached blend-weight buffer at `+0x1BC` | Real base class of `CMoDistMorphElem` (constructs `CMoElem` first, then itself). Product source's own header notes it once carried the plain name `CMoElem` before this was caught and corrected. |
| `0x1032AD80` | `0x10052F00` | plain `0x10041110` (tail-jumps straight to `CMoElem`'s shared cleanup — no fields of its own); deleting-dtor `0x10041130` | `IsKind0` (true only for kind 0, `0x10041120`, shared verbatim with `0x1032B3B8`); `SubmitVertices` (`0x10040E20`) | The product source's own `ConstructAt`/destructor banners for this class are wrong by exactly `−0xD0` (`0x10052E30`/`0x10041040` both disassemble to garbage); addresses above are independently verified against the retail binary, not taken from the banners. |
| `0x1032ADE8` | `0x10041F40` (writes `424` at `+0x176`) | not yet isolated (still in the unsplit "generated" monolith; only `ConstructAt` has been pulled out so far, as `CXiSub_10041E70`) | — | Least far along in the product reconstruction — no distinguishing method identified yet beyond its constructor. |
| `0x1032B3B8` | `0x10052E90` (writes `412` at `+0x176`) | `0x10052E00` | `IsKind0` (shared with `0x1032AD80`, same address); `RebuildBlendWeights`/`SubmitVertices` (`0x10040E70`/`0x10040FB0`); `SetField198`/`GetField198` (`0x10052EB0`/`0x10052EC0`, a plain field at `+0x198`) | Same `−0xD0` banner error as `0x1032AD80` (`0x10052DC0` is garbage; real ctor is `0x10052E90`). |
| `0x1032B478` | `0x10052F80` (writes `438` at `+0x176`) | `0x10052FB0` | `IsKind` (true only for kind 2, `0x10052FA0`); `FadeRemaining` (`0x10045D00` — a genuine fade-timer check against the shared `0x103295D8` constant); `RebuildBlendWeights` (`0x100565A0` — a substantial ring/circular-burst vertex generator that calls `IDirect3DDevice8::SetRenderState` directly) | The most behaviorally distinct of the five — looks like a real "ring burst" particle effect, not a thin variant. |

All five construct through `CMoElem`'s own constructor (`0x10044890`) before their own, confirming all five really are `CMoElem` descendants despite reporting `CMoElem`'s own descriptor. |

### `CMoGeneratorClone`

**The class-descriptor tree shows `CMoGeneratorClone : CYyObject` directly, but its own
constructors install `CMoResource` and an intermediate class first** — a real disagreement between
the descriptor chain and what the constructors actually do, confirmed independently. Either way, a
`CMoGeneratorClone` instance is laid out on a `CMoResource` base, which is why the lobby-thread
race path (§13) can reach it through a generic resource-node destructor call.

A general-purpose "create and link an attached generator clone" utility. Confirmed 9 call sites
across one construction function: **5 of 9** sit inside `CXiSkeletonActor`'s territory (the
dominant use case — confirmed directly: creates a clone, links it to the caller via a
large-offset field `caller+0x764`, configures spawn radius/rate float parameters — genuine
character-actor-attached effect usage), 3 of 9 near `CMoSchedularTask`/`CMoTask` (generic
task-scheduling usage), 1 of 9 in general effect-element territory. **Not weather-exclusive** —
by call-site count this is used far more for character-attached effects than weather, though the
class's own setup logic genuinely does check weather-related string tags as one classification
path it supports.

- `InitCloneFromSource` (`0x10047C30`): zeroes a 0x50-byte block, copies two 4-float blocks
  (`+0`→`+0x20`, `+0x10`→`+0x34`), decodes a packed count (`(field>>7)&0x7FFFF`, minus 6, ×16 —
  the same packed-count-plus-array serialization convention `CMoCamera`'s `SetPathData` uses,
  there with minus 2 instead of minus 6) and copies that many bytes into `dest+0xC0`.
- `FixupClonedPointers` (`0x10047CE0`): pointer-delta fixup, defaults six float fields
  (`+0x78`–`+0x8C`) to `1.0`, then a classification block comparing a stored tag against `"weat"`/
  `"dryw"`/`"dust"` and zone/area codes (`"0b10"`, `"0b11"`, `"0b12"`, `"0b21"`, `"0b22"`,
  `"0b31"`, `"0b32"`, `"pb41"`), plus numeric ID comparisons from a hash/lookup call (not
  decoded — may correspond to non-weather categories given the confirmed call-site spread).
  Matches accumulate into flag bytes `+0xDE`/`+0xDF`.

### Shared cross-class infrastructure

| Address | Name | Role |
|---|---|---|
| `0x1047CF7C` | `g_pProcessor` | Active `CMoProcessor` instance |
| `0x1047BFA8` | `g_pResourceMng` | Active `CMoResourceMng`-family manager |
| `0x1047D128` | (resource manager global) | Shared by `CYyModelDt` and `CYyMotionQue` |
| `0x1003B5C0` | `ReleaseSubObjectIfPresent` | Null-check + conditional destructor call; reused by `CMoCamera`, `CMoNullProgElem`, and multiple anonymous classes |
| `0x10045D40` (+siblings) | `RegisterWithProcessor` | Hands a value to `g_pProcessor` |
| `0x1065C4CC` | `g_zoneLoggingActive` | Gates `CTsZoneMap`'s periodic log; cleared on ring-buffer cycle completion |
| `0x103295D8` | (timer constant) | Recurring float used across multiple unrelated timer/distance comparisons |
| `0x1047BC0C` | (scratch value) | Shared transient slot written/read across multiple unrelated effect-update functions |
| `0x10177800` | `LogZoneMetrics` | Periodic (~1s) telemetry: reads 4 scaled floats from a 4096-entry ring buffer, formats via printf-style helper, flushes at a 150-byte cap or full ring cycle (which also clears `g_zoneLoggingActive`) |

---

## 6. Vertex skinning — complete, confirmed pipeline

### Classes involved

- **`CYySkl`** — minimal (7-slot, destructor-only). Owns two raw buffers (`+8`, `+0x14`, freed
  via a shared generic deallocation wrapper — `sub_10028700`, used engine-wide by 35 unrelated
  callers including the real C++ `type_info` destructor — not `free` directly). **Confirmed
  embedded by value, not by reference, inside `CYyModelBase` at that class's own `+8`** — traced
  directly via both `CYyModelBase`'s real constructor (`sub_10029D30`, which constructs `CYySkl`
  at `this+8`) and its real destructor (`sub_10029DD0`, which destructs it at the same offset).
  `CYyModelBase` and `CYyModelDt` are **siblings**, both deriving directly from `CYyObject`
  (`CYyModelBase` is not `CYyModelDt`'s parent, an earlier misreading of §2's own tree) — so this
  confirms a model's skeleton lives embedded inside `CYyModelBase` specifically, not that it's
  reachable through `CYyModelDt`'s own inheritance chain. How a `CYyModelDt` and its sibling
  `CYyModelBase` combine into one rendered model is not traced here. **The
  buffers' contents are now resolved.** A real setter exists (`CYyModelBase::Init`,
  `0x100342A0`, called from the constructor `0x10029E50`), contradicting the earlier "constructor
  only zeroes them, no setter" finding: `+4` is a skeleton resource handle resolved through the
  resource manager; `+8` is a raw heap block of `(nBones+1)·64` bytes; `+0xC` is a 16-byte-aligned
  array of `nBones` identity-initialized 4×4 bone matrices; `+0x10` is a flag byte; `+0x14` is a
  per-bone byte table (bit `0x80` = "bone used", set by the parent-chain walker). The PC skeleton
  *resource* format differs from PS2's `KzSkeleton` (which is why matching against it found
  nothing): a version byte and bone count at `+0x30`/`+0x32`, then 30-byte bone records from
  `+0x34` with the parent index at record offset 0. **Checked directly, narrowed further**: the
  pose composer itself (`0x100343C0`) reads only that one parent-index byte from each raw record —
  the actual per-bone TRS it composes comes from a separate, already-decoded 13-float
  (52-byte-stride) scratch array (`unk_1045F064`), populated by some other, not-yet-found
  function. **Found (§18.15):** `MotionQueue_UpdateAllChannels` (`0x1001A420`) fills it
  (`g_poseScratch`, `0x1045F030`) from the actor's motion layers each update. The remaining 29 raw bytes' packing is therefore not resolved by this function; it's
  one step further removed than expected. Real consumers: `IsReady` (`0x10034330`) caches
  `+0xC` into a global pose scratch buffer; the pose composer (`0x100343C0`) multiplies each
  bone's local TRS by its parent's matrix into `+0xC[i]`; `MarkReferencedBones` (`0x1002A0C0`)
  clears `+0x14` and passes it to each mesh piece's vtable slot 10. `CYyModelDt_MarkReferencedBones`
  itself still operates on `CYyModelDt`'s own resource pointer, a separate, adjacent finding.
- **`CXiSkeletonActorRes`** — an **asynchronous skeleton-resource load task** (72 bytes,
  derived from `CMoTask`). Created by `sub_100D4330`: if the actor is a special case (vtable slot
  193 returns true, or its linked sub-object at `+0x70` has flag `0x80` or `0x100`) the skeleton is
  loaded synchronously (`sub_100D2F60`); otherwise a task is allocated, constructed by
  `sub_100D7020(task, actor, callback = sub_100D2F40)` and stored at `actor+0xA08`. The actor
  **owns** the task: its destructor (`sub_100C5C00`) calls the task's scalar-deleting destructor
  (vtable slot 6) and clears `+0xA08`. The task's own destructor (`sub_100D7050`) clears
  `g_pActiveSkeletonActorRes` (`0x1048A3D8`) if it points at the task, and clears `actor+0xA08`.
  A state machine (`sub_100D70A0`) drives the load via the state field below.

  | Offset | Field | Evidence |
  |---|---|---|
  | `+0x00`–`+0x33` | `CMoTask` base | base constructor `sub_10074740`; `CMoTask` is exactly `0x34` bytes |
  | `+0x34` | linked actor | constructor argument; getter `CXiSkeletonActorRes_GetLinkedActor` |
  | `+0x38` | completion callback | constructor argument |
  | `+0x3C` | load state | zeroed in the constructor; read by the state machine |
  | `+0x40` | zeroed | not traced |
  | `+0x44` | resource identifier | written by `sub_100D4330` right after construction |

- **`CXiSkeletonActor`** (`0x10330F40`) and **`XiSkeletonActor2`** (`0x103313E8`) each have their
  **own 264-slot vtable** — not one shared 153-slot table. Verified directly: reading past slot 153
  with `stop_at_non_code=false` finds real, valid function pointers all the way to slot 264, where a
  genuine non-code word (a float constant, `0x4096CBE4`) finally appears; pushing the read to 1024
  slots confirms 264 is the true end, not a query-limit artifact. The two tables differ only in
  slots 0, 6 and 237–241. The earlier "153, all decoded" claim came from never trying a larger
  `count` in the original read — a real gap in that pass, not a hard boundary. Skinning does not
  live here (no `CMoProcessor` use); this is actor state and behavior. Class-level slot counts,
  from constructor vtable-store order (`CXiSkeletonActor_Constructor_1Arg`..`_4Arg`, §2): `CYyObject`
  6 → `CMoTask` 11 → `CXiActor` 227 → `CXiAtelActor` 254 → `CXiControlActor` 255 →
  `CXiCollisionActor` 256 → `CXiSkeletonActor` 264 — so every slot from 41 through 226 is inherited
  from `CXiActor` itself, not a `CXiSkeletonActor` addition, and the PS2 comparison for that whole
  range is against `XiActor`'s general interface, not `XiSkeletonActor`-specific methods. Of slots
  153–263: 6 are field accessors with exact offsets (see below), 1 is the imm32 `this`-adjust thunk
  into the embedded `CYyModel` (`+0x674`, slot 172 — a fifth imm32 thunk family beyond the four
  `CXiDollActor` ones in §2), and the rest are real logic, not yet individually decoded. Notable
  details for slots 0–152:
  - Accessor families: bitflags at `+0x734` (set bits, clear bits, clear all, bits 0–3), `+0x8AC`
    (set/clear/test bit 0; bit 1 read by slot 85), `+0x840` bit 6; paired byte get/set at
    `+0x8A5`–`+0x8A9`, `+0x5E0`, `+0x79C`; dword pairs at `+0x660`, `+0x668`, `+0x66C`, `+0x730`,
    `+0x5E4`, `+0x174`, `+0xA8`; floats at `+0x170`, `+0x178`, `+0x94`, `+0x98`; one indexed
    array accessor (slot 141: `this + 0x180 + index × 0x68`, a table of 104-byte records).
  - Slot 3 reads bit 0 at offset `−0x8` — an inherited method reached through a secondary base.
  - Slots 53–87 reach through the linked sub-object at `+0x70` (state flags at its `+239`,
    `+300`, `+316`; a name lookup falling back to an inline buffer at `+0xB8`).
  - Slot 8 (`sub_100C63D0`, 7.7 KB) is the per-frame update: angle smoothing with ±π
    wrap-around, facing toward a target (`atan2`), eight bounding-box corners transformed by the
    device's view and projection matrices and compared against a camera value (consistent with
    visibility culling; not confirmed as such), and the opacity fade (`+0x59C`, see below).
  - Slot 113 (`sub_100D4560`) uses per-body-part float lookup tables feeding a scaled sum —
    plausibly hit location or damage modifiers; not traced.
  - One slot forwards to vtable offset `1012` on a linked object, so the actor interface extends
    well beyond this table.
  - **Init/reset** (`sub_100C5D60`) sets the opacity at `+0x59C` to 0, `+0x660` to `0x80808080`,
    `+0x668`/`+0x66C` to 128 (all PS2 "`0x80` = 1.0" values), writes the animation-name table
    `"idl?wlk?run?btl?"` at `+0x7C8`, and assigns the actor to the least-loaded of four buckets in
    each of two global counters (`dword_1048A358`, `dword_1048A368`; decremented by the
    destructor). **Confirmed staggering:** `sub_100CBDE0` compares each bucket index (`+0x9F0`,
    `+0x9FC`) with a counter modulo 4 (read from `dword_104568FC+0x34`, consistent with a frame
    counter) and runs the corresponding block of per-actor work only on a match — so that work
    runs for each actor once every four frames, with actors spread evenly over the four phases.
  **Method names from the PS2 vtable.** PS2 `__vt__15XiSkeletonActor` (131 words; two header words,
  so PS2 word *n* is method *n−2*) aligns with the PC table through slot 40. Each pairing is
  supported by field semantics (getter/setter order, argument count, and the init values above):

  | PC slot | PS2 method | PC behavior |
  |---|---|---|
  | 8 | `OnMove` | the per-frame update (`sub_100C63D0`) |
  | 9–10 | `OnDraw` | empty — the PC draws actors elsewhere |
  | 11 / 12 | `GetColor` / `SetColor` | `+0x660` (init `0x80808080`) |
  | 13 / 14 | `SetMultiTexAlpha` / `GetMultiTexAlpha` | `+0x668` (init 128) |
  | 15 / 16 | `SetSahdowAlpha` / `GetShadowAlpha` | `+0x66C` (init 128) |
  | 17 | *(PC addition)* | byte at `+0x663` |
  | 18 | `KillAllGenerater` | releases the two generator sub-objects (`sub_100D6370`) |
  | 19 / 20 / 21 | `EnableEffect` / `DisableEffect` / `DisableEffectAll` | OR / AND-NOT / clear `+0x734` |
  | 22 | `SetUVOffset(f, f)` | two-value store |
  | 23 / 24 / 25 / 26 | `SetDistAmount` / `SetEmapColor` / `SetEmapTexture` / `SetSeparateValue` | `+0x744` / `+0x74C` / `+0x750` / `+0x748` |
  | 27 / 28 / 29 | `IsEnvmap` / `IsDistortion` / `IsMasking` | bits 0 / 1 / 2 of `+0x734` (bit 3, slot 30, is a PC addition) |
  | 31 / 32 | `SetEmapAlphaMode` / `GetEmapAlphaMode` | `+0x730` |
  | **33–37** | **`StartDisintegration`, `EndDisintegration`, `DisintegrateByBBX`, `DisintegrateByBSP`, `DisintegrateAll`** | **five empty `ret` stubs** |
  | 38 / 39 / 40 | `GetWidthScale` / `GetHeightScale` / `GetDepthScale` | real functions |

  The PS2 field layout agrees: `color`, `alpha`, `mtex_alpha`, `shadow_alpha` are consecutive at
  PS2 `+0x2C8`–`+0x2D4`, matching PC `+0x660`–`+0x66C` in order and spacing. Past slot 40 the PC
  table contains methods the PS2 one lacks, so the alignment stops; shape-matched but unconfirmed:
  PC 104–110 ≈ `Get/SetMoveSpeed` (`+0x98`), `Get/SetMoveSpeedBase` (`+0x94`),
  `Get/SetWalkSpeed` (`+0x9C`).

  **Slots 41–152, aligned by field rather than by order.** The PC reorders and inserts methods
  from slot 41 on, so slot order alone is unreliable. Instead, the PS2 accessors were decoded
  (unoptimized MIPS: `this` is spilled to the stack and reloaded before each access) to the field
  each one reads or writes, and those fields were named from the PS2 debug data. Each class level
  sits at its own constant shift on PC, established from several independent fields:

  | Class level | PS2 → PC shift | Fields confirming it | PC slots named |
  |---|---|---|---|
  | `XiActor` | `+0x28` | `run_speed`, `run_speed_base`, `walk_speed`, `subactor_status` | 104–109, 139–140 |
  | `XiControlActor` | `+0x20` | `ground_normal`, `ground_height`, `ground_material`, `water_height` | 129–138, 141 |
  | `XiCollisionActor` | `+0x420` | `IsTouch`, `current_area_id` | 96–98, 101–103 |

  Details:
  - These accessors belong to the *base* classes (per the PS2 mangled names, e.g.
    `GetMoveSpeed__7XiActor`) and are shared by every actor class's vtable, so they are named
    `CXiActor_…`, `CXiControlActor_…`, `CXiCollisionActor_…`. Two carried Lumina false matches
    (`?GetNumBorrowedCores@SchedulerProxy…`, `?Id@SchedulerBase…`).
  - **Corrected:** slots 137–138 (`IsChocobo` pair) and 141 are `XiControlActor` overrides, not
    `XiActor` accessors as first placed by position — confirmed by class-level constructor tracing,
    not just field shape. Slot 96 is `XiCollisionActor`, not unassigned. Slot 108 (`GetWalkSpeed`)
    is placed by position; its PC body is not a plain load. `IsOnLift` reads `+0x5E2` where the
    shift predicts `+0x5E1` — **explained in §18.16:** the shift holds; PC keeps `is_on_lift`'s role
    at `+0x5E2` and adds a new input byte at `+0x5E1`.
  - **PS2 bug:** `XiActor::GetWalkSpeed` reads `run_speed` (`+0x70`), not `walk_speed`; the setter
    writes the correct field.
  - **The effect-parameter block is at PC `+0x72C`.** PS2 keeps `ef_param` at `+0x2E0`;
    subtracting its sub-offsets from the PC fields gives the same base three times (UV offset
    `+0x10`→`+0x73C`, emap color `+0x20`→`+0x74C`, emap texture `+0x24`→`+0x750`). The effect flags
    (`+0x734`) and emap alpha mode (`+0x730`) are fields of that block.
  - PS2's standalone `Get/SetUOffset`, `Get/SetVOffset`, `GetEmapColor` and `GetEmapTexture` have
    no PC slots; the PC merged the UV setter (`SetUVOffset`, slot 22) and dropped the getters.
  - The PC-only fields (`+0x8A5`–`+0x8A9`, `+0x840`, `+0x8AC`, `+0x9F8`, `+0xA04`) lie beyond the
    PS2 object's size and have no PS2 names.

  **The PC actor disintegration API is stubbed out.** On PS2 the five `void` disintegration methods
  are real code (116–380 bytes; `DisintegrateAll` is a 16-byte forwarder) and two getters return the
  captured triangle and vertex lists. On PC the five `void` methods are bare `ret` and the two getters
  are gone. This goes beyond the earlier finding that opcode `0x74` lands in an inert handler: even
  correctly routed, the effect would call methods that do nothing. A fix has to implement
  `StartDisintegration`…`DisintegrateAll` (and the capture they rely on), not only re-route the
  opcode.
- **`CYyModel`/`CYyModelBase`** — minimal, destructor-only. The real mesh-data class is
  **`CYyModelDt`** ("Data"), with 6 own methods — the entry point into the mesh-update pipeline
  and vertex skinning. Its own vtable is confirmed directly (`CYyModelDt_vtbl_ambiguous0`, at
  `0x1032A430`, verified via a real constructor, `sub_10025010`, that stores this exact address)
  — slot 7 is `CYyModelDt_PrepareRenderStateEntry` (`0x10025030`), slot 8 is
  `CYyModelDt_PrepareRenderStateSimpleEntry` (`0x10025060`), a "simple" variant of the same
  dispatch confirmed directly, sitting adjacent exactly as expected. `PrepareRenderState`
  (`0x100224D0`) passes its own third parameter (`a3`) straight through, unmodified, as
  `SkinVertices`' own third argument — so `a3`'s real identity is the same question either way.
  `a3` itself has a confirmed structural profile even without a class name: `+48` (bit `0x10`
  gates skinning entirely), `+52` (bit `0x1` gates a 3×-vs-6× scaling branch), `+72` (the
  overlay-decision block consumed by `sub_10033800`/`sub_10033A70`), `+168` (a 16-entry indexed
  lookup). **Tracing this further hits a genuine static-analysis wall**: `PrepareRenderStateEntry`
  has zero direct callers in IDA's analysis — it's reached only through a virtual dispatch
  (confirmed to be slot 7 of the vtable above), and a virtual call's target address is
  runtime-computed, not encoded in the call site's own bytes — no byte or address search can find
  it the way a direct call can. Resolving `a3`'s concrete class would need either an exhaustive
  scan of every function that could plausibly hold a `CYyModelDt*` and dispatch through slot 7, or
  a live capture of the actual pointer value.
- **`CMoSkeletonElem`** — the `CMoElem` sibling whose update method is the confirmed per-bone
  hierarchy-propagation step.

### Bone-hierarchy propagation (`CMoSkeletonElem::UpdateBoneTransform`, `0x10047590`)

1. Normalizes a bone's local Euler rotation (`this+0x61C/+0x620/+0x624`) against fixed range
   constants (wraparound).
2. Registers with `CMoProcessor` (`RegisterWithProcessor`).
3. Copies the local transform matrix (`this+0xA0`→`this+0x194`, 16 dwords).
4. Combines it with a parent matrix via `CMoProcessor`'s `Mat4x4_Multiply` (confirmed directly,
   not inferred): allocates two pool slots, stages both matrices, calls vtable+0x24. The combined
   world-space matrix is stored back to `this+0x194` **and** published into the linked actor's
   per-bone matrix array (`actor+0x5F8`) — this is how a finished bone matrix reaches the actor.
   **`actor+0x59C` is the actor's opacity.** The value stored is `HIBYTE(bone+62) × 1/128`: a
   byte where `0x80` means exactly `1.0` — the PlayStation 2 GS alpha convention. Its consumer is
   `CXiSkeletonActor`'s per-frame update (vtable slot 8, `sub_100C63D0`), which fades it in by
   `frameDelta/32` (clamped to 1.0), fades it out by `frameDelta/16` (clamped to 0), sets the
   actor's hidden flags (`+0xB0 = 1`, `+0xB2 |= 1`) when it reaches 0, and takes the fully-opaque
   render path only when `(+0x59C) × (+0x664) ≥ 1.0`. PS2 debug data names one of the two factors: `+0x664` is `XiSkeletonActor::alpha` (it sits between `color` and `mtex_alpha`, below), and `+0x59C` is a second opacity factor whose PS2 name is unknown. (An earlier suggestion that it is `XiControlActor::alpha_base` is withdrawn: the field-verified `+0x20` shift for `XiControlActor` puts `alpha_base` at PC `+0x190`, which the per-frame fade never touches, and PS2's `OnMove` does not access `alpha_base` at all.) The actor's init routine sets it to 0, so actors
   start invisible and fade in. Both pool
   slots are explicitly freed before return.

### The weighted vertex transform (`SkinVertices`, `0x10023290` / `SkinVerticesSimple`, `0x100231F0`)

1. **Per-vertex bone influences are `(bone_index, weight)` byte pairs**, read from an array sized
   by `this+0x5C`.
2. **Weights are quantized to 7 bits (0–127)** and used as an index into a **precomputed 128-entry
   × 64-byte table** (`g_boneWeightMatrixTable`, `0x1045EC20`) — `weight × BoneMatrix` computed
   once per distinct quantized weight rather than per vertex (a classic PS2-era optimization).
3. **Core transform** (`ApplyWeightedBoneMatrix`, `0x100235C0`): applies the looked-up 3×4
   affine matrix (rotation/scale block + translation) to a local vertex position: `M·v+t`.
4. **Contributions from multiple bones are summed** via `Vec3_AddInPlace` (`0x10026F20`), called
   twice per bone (position and normal accumulators, 12 bytes apart) — `position = Σᵢ weightᵢ ·
   (Mᵢ · local_positionᵢ + tᵢ)`.
5. **A third bone-influence group** (`this+0x5A`, distinct from the two counts at `+0x42`/`+0x5C`)
   is gated by a caller-supplied flag: if clear, the full weighted pipeline runs, then a blend
   step scales two parallel copies of a source vector by `0.75 − this+0x78` and flat `0.75`
   respectively (`this+0x78`, defaulted to `1.0` elsewhere — plausibly a blend-progress value),
   feeding this third group through the same `ApplyWeightedBoneMatrix` machinery. If the flag is
   set, blend/weight processing is skipped entirely. **The source vector is confirmed precisely**:
   both scaled copies read directly from `SkinVertices`' own third parameter at float offset 13
   (byte offset 52) — i.e. `a3[13..15]`. **Resolved statically**: the dispatch site is visible
   despite going through a virtual call — a full call-chain trace (`0x1002B6E0` — `0x1002C360` —
   `0x1002A3B0` — vtable slot 7 `0x10025030` — `PrepareRenderState`) shows the parameter is the
   model's own **owning `CYyModel*`** (not the mesh piece, not the actor directly). `CYyModel`'s
   constructor (`0x1002B4B0`) zeroes flags at `+0x30`, sets `+0x40 = 2.0f`, and builds the overlay
   block at `+0x48`; byte offset 52 (`+0x34`) is a translation vector applied when a flag at
   `+0xB8` is set. `CXiSkeletonActor` embeds its own `CYyModel` at `+0x674` (the target of the
   slot-172 imm32 adjustor, §6 above), so for actors this parameter is `&actor->model`. The
   premise that this dispatch site is the *only* path to `PrepareRenderState` is not itself
   proven — a rel32 scan finds exactly one direct caller at each link in the chain, which is
   strong but not exhaustive.
6. **The solver's vector math is the engine's own.** `SkinVertices` and
   `SkinVerticesFinish_SecondaryMotionSolver` use small `float3` in-place add, subtract and scale
   helpers (`0x10026F20`, `0x100270A0`, `0x100272B0`; add has 29 callers across skinning and
   actor code). IDA shows them under `ConvexDecomposition::operator…` names, but those names are
   Lumina matches on 33-byte bodies, not symbols from the binary (§1).

Both the flag-set and flag-clear paths converge on a common finishing function.

### The finishing function (`SkinVerticesFinish_SecondaryMotionSolver`, `0x10023700`) — a jiggle-physics solver with a camera-bias term, not a skinning-finish step

**The camera-relative section is now fully resolved, and every original guess for it (LOD
selection, billboard facing, distance fade) was wrong.** It's not a separate purpose at all — it
computes a "camera bias" term that feeds directly into the same accumulator the distance-
constraint solver below builds. Precisely: reads ~~the current-camera global~~ **the `XiZone` environment object** (`0x1065CB04`, formerly mislabeled `g_pCurrentCamera` — **corrected in §18.17**:
confirmed fields at `+292/+296/+300` for position and `+308` for a per-frame scale factor, newly
characterized directly), computes the delta between a vertex position and the camera
position, falls back to a direct subtraction if that delta is nearly zero (a degenerate-case
guard against a NaN/zero-length direction), scales it by the camera's `+308` field × `0.1`, and
adds it into the vertex's own physics accumulator — gated by a caller-supplied flag (`a2+380`)
that can disable the whole term. This is a small, continuous pull toward the camera applied to
secondary-motion elements (hair, cloth, accessories) — a real, known technique for preventing
jiggle-physics geometry from clipping backward through the character model or vanishing at
extreme viewing angles, confirmed by reading the function in full rather than inferred from its
mechanics alone.

**The dominant remaining work is an iterative distance-constraint relaxation solver**, reading
exactly like simple cloth/hair/accessory jiggle physics, not a "skinning finish" step:

1. Allocates a scratch buffer sized from two 16-bit fields (`+0x64`/`+0x66`, plausibly vertex/
   index counts).
2. Runs **exactly 4 fixed iterations**. Each iteration processes index pairs from a packed array
   (16-bit values, high bit as a per-entry flag), looks up two 3-float positions at the confirmed
   60-byte stride, computes distance between them, compares against a threshold
   (`0x1032A1A8` — the same constant confirmed as `CYyMotionQue`'s own threshold), and applies a
   scaled correction `(distance−target)×factor/distance` when significant. A second pass uses
   different per-instance factors (`+0x68`/`+0x6C`) and different flag-bit gating.
3. After all 4 iterations, calls a "commit" function (`SkinVerticesFinish_Commit`, `0x10023BD0`)
   and frees the scratch buffer.

Fixed iteration counts are a standard way to bound solver cost per frame. `SkinVerticesFinish_Commit`
itself is fully resolved (below).

### `SkinVerticesFinish_Commit` — a two-phase proximity-matching and constraint-application system

Not a simple "finish" step — a genuine spatial-matching system layered on top of the jiggle
solver, confirmed via its two real sub-functions:

- **`0x10023FF0`**: a bounds-checked array lookup — if an index is within a count field
  (`this+128`), returns that index into an array (`this+124`); otherwise falls back to the
  array's first element.
- **`0x1002B390`**: reads a candidate attachment record from a variable-length resource array
  (via a multi-level indexed-lookup chain — `sub_10035290`→`sub_10035270`→`sub_10035250`, the
  last of which reads its own record's header to determine a **variable stride**, `13×header+2`
  elements, the same "packed header, then N sub-records" convention already confirmed elsewhere
  in this engine), extracts a 3-float offset vector from that record, looks up a 64-byte-stride
  bone matrix (`this_a1+20`, indexed by a value from the same record) from
  `g_boneWeightMatrixTable`'s own table shape, and applies it via `sub_10028230` — confirmed to
  be **the exact same `M·v+t` transform shape already confirmed as `ApplyWeightedBoneMatrix`**.
  `sub_10028230` itself has **22 distinct callers** spanning completely unrelated parts of the
  binary — a generic, widely-shared "transform a point by a 3×4 matrix" primitive, not specific
  to skinning or this solver.

**The full two-phase structure, confirmed by reading `SkinVerticesFinish_Commit` to completion**:

- **Phase 1 — proximity matching.** For each candidate attachment record (loaded via the
  resource's variable-length data), computes the record's world-space position via
  `0x1002B390`'s confirmed matrix transform, computes the delta against the actual vertex
  position (read from the confirmed 60-byte-stride vertex array), and checks whether the
  distance² is within a per-record threshold (`radius²×1.5`, where the radius comes from the same
  record). Matches are marked eligible in a lookup table (`dword_10456E38`).
- **Phase 2 — constraint application.** For each vertex, re-walks the same attachment records;
  for every pair marked eligible in phase 1 *and* passing a separate flag check
  (`(HIBYTE(*record) & 0x80) == 0`), calls the actual constraint-application function
  (`sub_10024020`) **twice per match, with swapped argument order** — consistent with a symmetric
  two-point distance constraint applied in both directions.

Plausible real-world role: matching mesh attachment points (hair, a cape edge, jewelry, a loose
weapon) to nearby jiggle-solved vertices and applying the actual secondary-motion constraint
between them — inference from shape, not confirmed by name.

### Real cross-confirmation from the `dancer` middleware

Four independent confirmations of the same structure, from four different angles:

1. **File format** — `sqinSkinBuildBinary` (`0x1029ABD0`): rejects anything but version `2`,
   reads `clusterCount`/`idMax`, then per-cluster a bone-ID array and matching weight array
   (both dynamically allocated), resolves a bone/node reference, calls `sqinCluster_Create()`
   directly, landing fields on `sqinCluster_Dump`'s confirmed offsets.
2. **Runtime storage** — `sqVtx`'s confirmed 12-slot vertex-attribute taxonomy includes
   `DeformationWeights` and two `DeformationMatrix` slots — the real, named fields holding the
   bone-weight data `SkinVertices` was reverse-engineered to consume.
3. **Runtime object** — `sqinCluster` (found via its manual C-style vtable's `Dump` function):
   real confirmed fields `shape` (a 60-byte sub-object, matching `SkinVertices`'s vertex-record
   stride exactly), `trsMat`/`nTrsMat` (Translate/Rotate/Scale matrices), and `jointNode` (the
   specific bone this cluster is weighted to).
4. **Consumption** — `SkinVertices` itself, confirmed by hand from the opposite direction.

**A real discrepancy, resolved**: a skin cluster's bone reference resolves via
`sqskSkeleton_GetNodeByIndex` into the skeleton's **node array** (offset 32, 248-byte stride),
not directly into its **joint array** (offset 36, 156-byte stride) — both arrays are confirmed
real and distinct on the same skeleton object. A node is plausibly a joint plus hierarchy/
parent-child linkage (consistent with the larger size), though that specific composition isn't
confirmed.

### `sqskJoint` / `sqskSkeleton` real field layout

- **`sqskJoint`** (156-byte stride, confirmed by `sqskSkeleton`'s own iteration): `Translation`
  (+92), `Rotation` (+104), `Scaling` (+120) — a proper TRS decomposition — plus `fppa` (+132/
  136/140, three ints, meaning undetermined), `radius` (+148, plausibly capsule-collision),
  `influence` (+152, plausibly soft-skinning weight), and a combined `matrix` (+28).
- **`sqskSkeleton`**: `type` (+0), `root node` (+28), `node array` (+32), `joint array` (+36),
  `numBones` (+40).
- **`sqhiNode`** (`sqHierarchy` module, confirmed via its own `"sqhiNode <%x>"` string, not
  `sqSkeleton`'s own as might be assumed from the name): a genuine left-child/right-sibling tree
  (`parent`/`leftChild`/`sibling` pointers, `type`, `modelIndex`, a `dirty` flag, an embedded
  `matrix`, a separate `xform` pointer). Includes **`doBlur`, a per-node motion-blur toggle** —
  motion blur can be switched on for individual scene objects, not just globally.

**What a "node" is relative to a "joint" — fully resolved.** `sqhiNode`'s own complete field
dump (confirmed above) contains no joint reference or pointer of any kind — a genuine, definitive
negative result, not an unexplored gap. `sqskSkeleton_Dump` resolves the relationship directly
instead: the skeleton exposes a `root node` (a single pointer, traversed via `sqhiNode`'s own
parent/leftChild/sibling tree) *and* a separate `node array` field, while the joint array is
walked as a simple flat array indexed `0..numBones-1` — the same `numBones` count the node
hierarchy implicitly shares. **A joint is the TRS pose data for one bone** (a flat, simple array
entry). **A node is that same bone's hierarchy/transform wrapper** — tree links, a computed world
matrix, dirty flag, motion-blur toggle — reachable either as a tree (for traversal) or as a flat
array (for O(1) index lookup, exactly what `sqskSkeleton_GetNodeByIndex` uses). `node[i]` and
`joint[i]` are parallel, index-aligned views of the same i-th bone, not one containing the other.

---

## 7. Animation blending (`CYyMotionQue` family / `sqMotion`)

### FFXI wrapper classes

- **`CYyMotionQue`**: clean get/set property pairs for playback state (`+0x30` read-only, `+0x34`
  get/set resource pointer, `+0x28` write-only playback speed, `+0x3C` read-only via out-param,
  `+0x2C<0` as an "is stopped/invalid" query). Frame-advancement (`0x1001A8E0`): resolves a
  motion resource via the shared manager global `0x1047D128` (the same manager confirmed for
  `CYyModelDt` — a real link between the animation-queue and mesh-data systems), reads a signed
  16-bit frame count, clamps current time (`+0x38`) against it using the same NaN-safe comparison
  pattern and recurring `0x103295D8` constant used throughout this codebase's timer/distance
  code. Motion-transition function (`0x1001AB60`): defaults blend weight to `1.0` under specific
  conditions, resolves the motion resource, calls into the real motion-start function with it as
  `this`.
- **`CYyMoveBlendQue`**: one own method (`0x1001B400`), a 3-case mode dispatch on `this+0x28`.
- **The real motion-start function** (`0x10019A50`): substantially richer than a simple starter —
  a genuine motion-compatibility/queueing policy. Iterates a queue array; for each slot reads a
  byte from a global lookup table (`0x1045F028` — **corrected §18.15: a pointer to a per-*bone* mask
  table, `g_pBoneMotionMask`**), checks a "locked" bit
  (`&0x40`) and a 6-bit category (`&0x3F`, compared against 0/1) to decide between an
  immediate-override path (`0x10019EE0`) or a queue-if-allowed path (`0x10019B30`, sets a bit
  back into the same global table if it returns true) — "can this new motion interrupt/queue
  behind the current one."
- **`MotionQueue_UpdateAllChannels`** (`0x1001A420`): per-frame animation sampling — **7** motion
  slots (5 base layers + 2 weighted blend layers), not 12, gated per bone by `g_pBoneMotionMask`.
  Full breakdown in §18.15.
- **`CYyQue`/`CYyBlendQue`** — shared-accessor, ambiguous mapping, not individually pursued.
  `CYyMotionQueList`/`CYyAfterImage` — thin, destructor-only.

### `sqMotion` real type taxonomy

| Magic value | Type | Confirmed by |
|---|---|---|
| `0x50001` (327681) | FrameChannel | `sqmoFrameChannel_GetFramePtr`'s `"frame %d out of range %d"` bounds check |
| `0x50003` (327683) | KeyChannel | By elimination in `sqmoChannelMotion_Dispatch` |
| `0x50004` (327684) | Generic "channel motion" | `sqmoMixerMotion_Sample`'s `"is non-channel motion"` error |
| `0x50007` (327687) | MixerMotion | Dispatched from `sqmoMotion_Dispatch` |

- **`sqmoKeyChannel`**: `type` (+0), `entrySize` (+28), `timeSpan` (+32, float), `numKeys` (+40),
  `interpolation` enum (+36: `1`=Linear, `2`=Smooth, else None). Per-keyframe format: `(time
  float, entrySize data floats)` pairs. "Linear" is confirmed implemented by `Quat_NLerp`
  (`0x10033220`) and `Vec3_Lerp` (`0x100276A0`).
- **`sqmoFrameChannel`**: same `entrySize`/`timeSpan`/`interpolation` fields (shared across both
  channel types), stores fixed-rate `numFrames` samples rather than sparse time-keyed data.
  Additional fields: `dataType` (per-entry type tag) and `entryEnabled` (per-entry enable flag).
- **"Smooth" interpolation — confirmed data-format field, confirmed *not exercised* by any
  reachable code path** in this retail build. Checked both around `Quat_NLerp`/`Vec3_Lerp` and
  all 5 of `Quat_NLerp`'s actual callers (including `MotionQueue_UpdateAllChannels`) — neither
  branches on the interpolation-mode field. A genuine, tested negative result.
- **`sqmoMixerMotion`**: `sqmoMixerMotion_SetEntrySize` validates that an array of input motions
  share a compatible entry size and allocates the output buffer. `sqmoMixerMotion_Sample`
  validates each input's type tag and **recursively resolves nested motions** — a mixer's input
  can itself be another mixer (or any motion type). This is the confirmed motion-blending
  mechanism `CYyMoveBlendQue`/`CYyBlendQue` needed but lacked a concrete implementation for.
- **`sqmoChannel`/`sqmoChannelMotion`**: `sqmoChannelBuildSQO` explicitly rejects
  `sqmoStreamChannel`/`sqmoMayaChannel` types ("not supported") — those source files exist in the
  module but aren't reachable through this runtime code path, plausibly tool-side only.
  `sqmoMayaChannel.c`'s existence confirms animation content was authored in **Autodesk Maya**.

---

## 8. The `dancer` middleware — complete module census

**16 modules, 86 source files** (confirmed exhaustive via broad path-pattern search).

| Module | Prefix | Files | Role |
|---|---|---|---|
| `sqModel` | `sqmd` | 7 | Top-level model container (`sqmdModel`, `sqmdDMB`, IO/Snap/Sort/Script/Parser) |
| `sqMotion` | `sqmo` | 12 | Animation sampling, blending, mixing |
| `sqSkeleton` | `sqsk` | 3 | Joint/bone hierarchy |
| `sqSkin` | `sqin` | 5 | Vertex skinning — bone-weight clusters |
| `sqImage` | `sqim` | 5 | Texture loading — PS2 TM2 format, TIFF/SGI/PPM (plausibly tool-side) |
| `sqOpcode` | `sqop` | 3 | The `.fxt` trigger-file mechanism — time-keyed opcode tracks |
| `sqXform` | `sqxf` | 2 | Transform utilities |
| `sqRend` | `sqrd` | 4 | Light, Camera, Texture, Material |
| `sqBase` | `sq` | 12 | Math/utility primitives — Matrix3/4, Quat, Array, IO, Timer, Object, Error, Vtx, SQO, StructArray |
| `sqGrafix` | `sqgx` | 6 | DX8-era device/GPU submission — Context, Shader, Shape, Dlist, Aniso, Phong |
| `sqShader` | `sqsd` | 9 | Shader effects — Generic, Sampling, Aniso, Cartoon, Glow, AmbientMap, BRDF |
| `sqConstraint` | `sqco` | 1 | Generic data-flow connector (not physics/IK — see below) |
| `sqScene` | `sqsn` | 2 | Scene graph, shadows |
| `sqHierarchy` | `sqhi` | 1 | General node/hierarchy system |
| `sqShape` | `sqsh` | 13 | Base geometry — TriStrip, QuadMesh, DispList, Draw, Points, Curves, Index |
| `sqDeform` | `sqdf` | 1 | Mesh deformation — dirty-flag gated |

`sq` is almost certainly the middleware vendor/team's own prefix convention. The technique used
to find these (search for `__FILE__`-tagged debug strings) would miss a file with zero
error-reporting code, but given how pervasive that convention proved everywhere it was checked,
this census is very likely close to exhaustive, not just a floor.

### Performance-priority ranking (by confirmed/plausible per-frame or per-vertex execution, direct GPU state-change involvement, and call pervasiveness)

- **Tier 1 — confirmed hot path, substantially covered**: `sqSkin`, `sqSkeleton`, `sqMotion`.
- **Tier 2 — confirmed/near-certain hot path, direct GPU involvement**: `sqGrafix`, `sqShader`,
  `sqRend`, `sqShape`.
- **Tier 3 — likely frequent, lower/uncertain individual cost**: `sqScene`, `sqDeform`, `sqBase`
  (individually cheap but pervasively called), `sqHierarchy`, `sqXform`, `sqConstraint`.
- **Tier 4 — load-time or infrequent**: `sqModel`, `sqImage`. `sqOpcode` is event-triggered
  (infrequent in raw call volume) but its relevance is about VFX correctness, not performance.

### `sqBase` — the shared vertex/math foundation

- **`sqVtx`** — confirmed complete, real **12-slot vertex-attribute taxonomy**: `Points`,
  `Normals`, `UVs`, `Colors`, `UTangents`, `VTangents` (full tangent-space data, matches
  `sqShader`'s `bumptexture` parameter), `Parents` (bone/hierarchy parent index),
  `DeformationWeights`, two `DeformationMatrix` slots, and generic `User0`/`User1`. A vertex
  format is fully sparse — any subset of these 12 fields can be present per shape.
- Remaining `sqBase` files (`sqMatrix4`, `sqQuat`, `sqArray`, `sqTimer`, `sqObject`, `sqError`,
  `sqIO`, `sqStructArray`, `sqSQO`) are unopened; `sqQuat`'s operations are indirectly confirmed
  via `Quat_NLerp`.

### `sqGrafix` — the GPU-facing render context

- **`sqgxContext`** — the largest confirmed object in this entire project: **3,624 bytes**. Init
  (`sqgxContext_Init`, `0x10276260`) seeds a complete **16-texture-stage state cache**, every
  value initialized to `-1` (the classic "force the first real state-change to apply" sentinel) —
  this layer already implements proper render-state deduplication. Its dump function
  (`sqgxContext_Dump`, `0x102768E0`) reveals the complete GPU-facing render context by real
  name: full camera/projection/light matrices, **8 hardware lights** (the classic D3D8 limit),
  material properties including a `metal` parameter (= `sqrdMaterial`'s `metallic` boolean —
  simpler binary specular toggle, not true PBR), motion blur (`motionBlurSize`), glow
  (`glowData`/`glowDataExtra`), refraction (index, UV offset, texture ID), bump-mapping depth,
  shadow parameters (`shadowBlendFlag`, `shadowVolumeExtend`, `shadowW`), and the actual vertex/
  index/normal/UV/color GPU buffer handles. `BRDF` and `AmbientMap` are explicitly printed as
  `"not implemented"` — confirmed inert stubs in this shipped build, not active wasted work.
- **`sqgxContext_BatchIndices`** — a confirmed **index-buffer batching system**: accumulates
  indices from multiple shapes/draw calls into one shared buffer, capping batches at exactly
  **1,000 indices** before flushing, with correct degenerate-triangle-index insertion between
  strip segments, plus a redundancy check skipping re-setup when consecutive calls reuse the same
  index source. A real, already-implemented draw-call-batching optimization.
- **`sqgxContext_SelectShaderMode`** — a shared shader-permutation selector, confirmed called
  from at least 3 of the 5 shader bake functions with type-specific feature bitmasks
  (bump/environment/phong mapping, built from what the model actually has, with real
  `"Model is missing..."` diagnostic errors on a missing required feature).

### `sqShader` — a complete text-based shader script system

`sqsdShader_ParseScript` is a real script **parser** (confirmed reusable tokenizers,
`sqScript_ReadToken`/`sqScript_TokenEquals`) — shaders are authored as text scripts, not
compiled binary data, almost certainly sharing infrastructure with `sqModel`'s
`sqmdScript.c`/`sqParser.c`. Supports shader-inheritance (a script can reference an
already-defined shader as a template and override its parameters).

**All 5 shader types, confirmed parameters and application path:**

| Type | Parameters | Application |
|---|---|---|
| Generic | `color`/`ambient`/`diffuse`/`specular`/`shininess`/`transparency`/`metallic` + `colortexture`/`envtexture`/`bumptexture`/`phongtexture`/`refracttexture`/`phongmasktexture` + matching strengths + `decal`/`visible`/`cull`/`clamp`/`twoside`/`uselights`/`usevertexcolor`/`usealphatest`/`usealphamask`/`uvpersp`/`edgeaa` | Cached (magic tag `655369`, same convention as Glow/Aniso). References a real `"Spherigon"` curved-surface-normal technique. |
| Sampling | Base properties + a `phongtexture` sub-block with up to 16 `diffusecolors` (color ramp) | **No cache check** — always rebakes. This only affects model construction: every route into `sqsdSampling_BakeOntoShape` is the DMB builder (`sqmdDMBBuildShapes`) or a model-assembly script command (`skeleton_shape` and a sibling, registered in the command table at `0x103BC860`). No per-frame path exists. |
| Glow | `rgb`, `intensity`, `sharp`(`sharpness`), `cull` | Cached (tag `655369`). Bake creates a processed-shape wrapper combining base geometry with baked glow data. |
| Cartoon | Base properties + `outlinetexture` + `shadetexture` (cel-shading: outline pass + shade-ramp) | Confirmed **unimplemented stub** — fully defined in the script system but inert in this shipped build. |
| Aniso | Base properties + `anisotexture`, `mode`, `numdrawtris` | Cached (tag `655369`). |

**All shader types that cache do so via one unified convention** (magic tag `655369`), not five
separate implementations.

### `sqShape` — geometry and draw submission

- **`sqmdDMBBuildShapes`**: for each shape, looks up shader-type magic numbers (`0xF0001`–
  `0xF0005`) and calls the matching "bake this shader onto this shape" function — the real
  connection between `sqShape` and `sqShader`.
- **`sqshDraw_Submit`**: the real per-frame draw-submission function (confirmed via
  `"empty or missing vertex, can't draw"`), sets up device state, dispatches by primitive
  topology into a shared per-primitive submission call.
- **`sqshTriStripZSort`**: a per-triangle depth sort (confirmed via
  `"unknown phase in sqshTriStripZSort"`) — computes a view-space depth key per triangle
  (centroid · view direction, the painter's-algorithm formula) and runs a recursive range sort.
  Shadow volumes only work with `sqshTriStrip` shapes. **It is throttled:** its only caller,
  `sub_1029B250`, increments a counter at `+32` on each update and sorts only when it reaches a
  per-shape period stored at `+28`, then resets it. The eye position and view direction come from
  the combined matrix's translation terms and negated third column. What periods ship in real
  data is a data or dynamic question.
- **`sqshPoints`/`sqshCurves`**: both built on `sqVtx`. Points plausibly for particle/billboard
  VFX; curves for spline-based trail effects.
- **`sqshDispList`**: a real GPU display-list wrapper (pre-recorded render commands replayed with
  one call) — a legitimate period optimization alongside the state cache and index batching.
- **`sqshIndex_BuildSpatialGrid`**: a real 15×15×15 uniform spatial hash grid sized from a
  bounding box, almost certainly for efficient vertex welding when building an index buffer —
  avoiding an O(n²) all-pairs check.
- **`sqshStrip_GenerateFromTriangles`**: a genuinely sophisticated triangle-strip generator
  (confirmed via `"total nb triangles"`/`"nb meshes"`/`"averaged strip length"`/`"nb independent
  triangles"`) — builds a triangle-adjacency graph, greedily grows strips via a priority-bucket
  structure.
- **`sqshUtil_WeldVertices`**: real `dancer` code (source-file/line debug strings) using a naive
  O(n²) all-pairs comparison instead of the spatial grid above. **It is dead code in this build:**
  no direct callers in analyzed code, and a raw sweep of every segment (`find_code_refs_raw`)
  finds no `call`/`jmp rel32` and no absolute pointer to `0x102B4070` anywhere — including
  unanalyzed regions. The only remaining path would be an address computed at run time, for which
  there is no evidence. Its cost therefore does not matter.

### `sqRend` — light, camera, texture, material objects

- **`sqrdLight`**: `color` (RGB), `directional` (boolean) — confirmed via an embedded
  code-generation template (`static sqrdLight s_%s_light_%1d = {...}`) naming its real function
  pointers directly. Matches the `D3DLIGHT_POINT`/`D3DLIGHT_DIRECTIONAL` distinction already
  confirmed in FFXI's own `g_lightTable` (see §9) — very likely `sqrdLight` is the middleware's
  real light representation that `g_lightTable` wraps/converts from.
- **`sqrdMaterial`**: `color`, `ambient`, `diffuse`, `specular`, `shininess`, `metallic`
  (boolean), `transparency`.
- **`sqrdCamera`**: `field of view`, `near clipping plane`, `far clipping plane` — matches
  `sqgxContext_Dump`'s `fov`/`near`/`far` exactly.
- **`sqrdTexture`**: a simple `id` field for the runtime wrapper.
- **`sqmdDMBTextureSave`**: writes `sqrdTexture` structures then `sqimImage` pixel/CLUT data
  (2048-byte chunks) into `.dmb` format — tool-side, not runtime, but clarifies the file format.

### `sqScene` — the top-level organization

`sqsnScenePrint` reveals the real scene-graph structure: `numCameras`/`cameras[]`,
`numLights`/`lights[]`, a full shadow system (`shadowOn`/`shadowSize`/`numShadows`/`shadows[]`,
each a confirmed 48-byte record with a real `type` enum — `0`/`1`=Projected variants, `2`=
Volume, plus `blurSize`, stencil offset, and `shadow volume extend` — matching a field already
seen in `sqgxContext_Dump`), and `numLayers`/`layers[]` (each a 144-byte record: object pointer,
matrix, shader reference, lights) — ties cameras, lights, shadows, and renderable objects
together.

### `sqHierarchy` / `sqXform` / `sqConstraint`

- **`sqhiNode`** — see §6 (skeleton section).
- **`sqxfXformM`** — a simple static matrix transform, nothing else.
- **`sqxfXformTD`** — a **boom/orbit transform**, fully decoded from raw bytes of the
  compilation unit `sqxfXformTD.c` (`0x1026DD80`–`0x1026E290`), which IDA never analyzed:
  - Two constructors allocate the 124-byte (`0x7C`) object: `0x1026DEE0` (source line 28) and a
    copy/clone at `0x1026DFD0` (line 126). Init (`0x1026DF00`) writes type tag `0xC0003`
    (`SQXF_XFORMTD_TYPE`) and a manual vtable: `+0x08` Validate (`0x1026DF80`, a stub that prints
    "not implemented" and returns true), `+0x0C` Destroy (`0x1026DF90`), `+0x10` Print
    (`0x1026E040`), `+0x14` enabled flag (`0xFF`), **`+0x18` Update (`0x1026E1F0`)**. It then
    zeroes a position at `+0x5C`, sets an identity quaternion at `+0x68` and a scalar of `1.0` at
    `+0x78`. The same field order appears in the code-generation template that exports these
    objects.
  - **Update takes only `this` — no time argument.** It converts the quaternion to a 3×3 rotation
    and writes a 4×4 matrix at `+0x1C`–`+0x58` whose translation is
    `position + scalar × (rotation's third column)`, bottom row `0 0 0 1`: the object is placed
    `scalar` units along its own forward axis from a pivot. The "TD" is therefore not
    "time-driven"; "target/distance" matches the math, but the expansion is a reading, not a
    confirmed name. Animation comes from values written into position/quaternion each frame,
    which is the role of `sqcoConnector` below.
  - `Update` has no static callers because it is only reached through the `+0x18` function
    pointer. The unmapped address `0x10272286` that references the template string belongs to the
    MDLVIEW light-file **exporter**, not to `Update`.
- **`sqcoConnector`** — **not** a physics or IK constraint (despite the module name). Real fields:
  `active`, `source`, `destination`, `numCopyBytes`, `execFn` (custom function pointer),
  `userData`. A generic data-flow connector — plausibly the real wiring behind `sqmdModel`'s
  "Updaters" array, propagating a computed value (e.g. an animated `sqxfXformTD`'s matrix) into
  another object's field every frame, via raw byte copy or a custom function.

### `sqImage` — the TM2 texture pipeline and character-customization mechanism

A complete, confirmed mechanism, three functions read to completion:

1. **`sqimTM2LoadFile`** (`0x102A64D0`) — parses the real TM2 header, reads CLUT/palette data for
   indexed formats, allocates/reads pixel data, checks for an existing matching texture (by
   dimensions) before proceeding.
2. **`sqimTM2FindExisting`** (`0x102A6820`) — name-based texture cache/pool lookup (walks a
   linked list of buckets), comparing base filenames (extension stripped) and specifically
   checking for an **`"RT"` prefix** (literal ASCII bytes) — very likely "ReTexture."
3. **`sqimTM2Composite`** (`0x102A5D20`) — validates matching dimensions, then a per-pixel
   **masked overlay**: copies source pixels into the destination only where the destination pixel
   is currently `0` (transparent/empty).

**Put together**: loading a TM2 texture checks the name-based pool for a matching base name (the
`"RT"` convention); if found, new data is **composited onto the existing texture** (painting only
empty pixels) rather than replacing it. Very plausibly the real mechanism behind character
customization (dye colors, face paint) layered onto a shared base skin texture by name — the
mechanism's shape fits precisely, though no direct string ties it to that specific use case.

### `sqModel` — the top-level model container

**`sqmdModel`** is the real top-level model container. Confirmed arrays, each with a real name
and a "preallocated" capacity: `numTextures`, `numShaders`, `numUpdaters`, `numShapes`, `numAux`,
`numTags`, `numFiles`, `numSceneNdx` (layer+object pairs — placement within a scene layer/object
hierarchy). A `flags` field has three named bits: `Loaded`, `Linked`, `Visible`.

- `numShapes` confirms a model's Shapes array entries *are* `sqinShape` objects.
- `numUpdaters` confirms `sqmdDMBBuildUpdaters`/`sqmdDMBUpdaterEncode` populate this exact array.
- **Textures** and **Shaders** arrays: a model owns its own texture/shader lists directly, not
  just referencing a global pool.
- `sqmdModel_GetItemName` (`0x10279AB0`) looks up a display name via the `Tags` array, matching a
  `(category, index)` pair against parallel arrays — `Tags` is a name-tagging system linking
  human-readable names to any texture/shader/updater/shape/aux entry.
- `sqParser` is confirmed generic (text/number parsing, "parse a float from string, validate"),
  not graphics-specific.

### `sqinShape` — hardware-style 4-bone blend (a second skinning implementation)

- **`sqinShape_Blend4Bone`** (`0x102AEB40`): gathers one component at a time from four separate
  source streams (via `PackVec4`) into 4-vectors, transforms each through a shared matrix via
  `Mat4x4_TransformVec4` — classic hardware-style 4-bone-per-vertex skinning via matrix math,
  distinct from the weight-table-lookup implementation confirmed in `SkinVertices` (§6). A
  second, different implementation of the same underlying idea, not the same code path.
- **`sqinShape_Clear`** (`0x102AEC80`): frees two buffers (likely vertex/normal data) gated on a
  "built" flag bit.

---

### PS2 debug-data cross-check of the `dancer` layouts

- **Every `dancer` object starts with `sqObject`** { `type`, `id`, `validateFunc`, `destroyFunc`,
  `printFunc` } (`0x14` bytes); updatable objects continue with `active` (`+0x14`) and `updateFunc`
  (`+0x18`). This is the "manual C vtable" decoded by hand for `sqxfXformTD` (§8) — same offsets.
- **`sqskSkeleton`** (`0x30` bytes): `rootNode +0x1C`, `nodeArray +0x20`, `jointArray +0x24`,
  `numBones +0x28` — identical to the PC reconstruction — plus `hwm` at `+0x2C`.
- **`sqskJointStruct`** (`0xB0` bytes on PS2): `mat +0x20`, `translate +0x60`, `rotate +0x70`,
  `scale +0x80`, `fppa +0x90`, `fpp +0x9C`, `radius +0xA0`, `influence +0xA4`. Same order as the
  PC's 156-byte joint; the PS2 aligns vectors to 16 bytes, which accounts for the larger size.
- **`sqhiNodeStruct`** (`0x110`): the documented fields plus `blurMatrix +0x90` and
  `saveMatrix +0xD0`.
- **`sqcoConnector`** (`0x40`): `source`, `destination`, `numCopyBytes`, `execFn`, `userData`, plus
  `sourceID`, `destinationID`, `sourceOffset`, `destinationOffset`.
- **`sqmdModel`** (`0xAC`): each array (textures, shaders, updaters, shapes, aux, tags, files) is
  stored as pointer + per-entry flags + count + preallocated count; `shapes` also has `matrices`;
  `flags` is at `+0xA8`.
- **`sqgxContext`** is 2,336 bytes on PS2 against 3,624 on PC; the PC adds about 1.3 KB.

### PS2 skeleton and draw-info formats

- **`KzSKD`** (the skeleton file format): `nbelem`, a 3-float `scale`, an element-ID table,
  `jntEidNo`, `version_no` at `+0x1F`, then an array of 20-byte **`KzSkeleton`** joints — packed
  quaternion `qrot` (8 bytes), packed `trans` (6 bytes), `parent` index, `flip`, `flipaxis`.
  `KzGlobalSkeleton` is the 16-byte world-space variant. No class holds a `KzSKD` member; it is
  reached through casts of loaded data, and the functions taking `KzSKD*` include `GetParentNo`,
  `GetFlipNo`, `GetGlobalQRot`, `GetGlobalMatrix`, `Open`/`Close`.
- **`KzObjectDrawInfo`** (`0x54` bytes): `actor`, `ebuf`/`eref` (element buffers), five texture
  resources (`spec_res`, `env_res`, `self_env_res`, `summon_shadow_res`…), `inv_light`, lighting
  arrays, `cmax`/`cmin` bounds, `pack`, `cnt`, `alpha`, `ef_param`, `masking`, `mtex_alpha`. Taken
  by 22 drawing functions, including `Capture`, `MakeGroupPacket*` and `DisintegrateDraw`.
- **`KzCloth`** has its own 14-method family (`Open`, `Idle`, `UpdateVertex`, `CollisionProc`,
  `TransformVertex`, `CalcVertexNormal`, `Draw`…).

## 9. Real-time lighting: `g_lightTable`

A 26-entry global table (`0x104572B8`–`0x10457458`, 104 bytes per entry) — **confirmed to be
real D3D lighting, not a generic render command.**

- **`D3DLight_ValidateAndSet`** (dispatch function): validates each entry against the real D3D8
  `D3DLIGHTTYPE` enum precisely — tag `1` (`D3DLIGHT_POINT`) requires non-negative Range/Falloff
  fields, tag `3` (`D3DLIGHT_DIRECTIONAL`) requires a non-zero Direction vector — rejecting with
  the real `D3DERR_INVALIDCALL` HRESULT (`0x8876086C`, verified precisely) on failure.
- **`Light_ApplyTimeOfDayTint`**: gated behind `g_timeOfDayTintEnabled`, skips already-bright
  lights (any RGB channel ≥ 0.8) and otherwise scales a light's diffuse color by a fetched
  time-of-day/zone ambient factor before the light is set on the real device (vtable offset
  `0xB0`, `SetLight`-equivalent). This is the confirmed mechanism behind lights dimming/tinting
  by time of day or zone.
- Each entry's first dword is a tag; dwords 1–3 (`+4/+8/+0xC`) are a 3-float group (scaled color
  or vector) scaled by a per-instance factor (`ebx+0x12`). Confirmed tags `1`/`3` validate small
  field sets against the recurring `0x103295D8` constant as an "is this field set" sentinel
  (distinct role from its timer/distance use elsewhere).

`sqrdLight` (§8) is very likely the middleware's own light representation underlying this table.

**A real caveat, confirmed directly**: `g_timeOfDayTintEnabled` is not exclusively
lighting-related despite its name — it's also read, as a plain generic boolean, inside the
DirectInput device-setup code (§4/§10) to pick between two `SetCooperativeLevel` flag
combinations, entirely unrelated to lighting or time-of-day. Worth remembering before assuming
every reference to this global is part of the lighting system.

---

## 10. FFXI game bootstrap ↔ `dancer` seam: the `St*` layer

The `St*` family (`StAvatar`, `StChannel`, `StModel`, `StTrigger`) sits at
`D:\build0001\FFXi_Win\Main\dancer\*.cpp` (~`0x1024D000`–`0x10253200`, ~25 KB) — a higher-level
layer on top of the `sq*` middleware modules, plausibly FFXI's own game-side orchestration
wrapper rather than part of `dancer` proper.

**Confirmed real entry point**: `GameSystems_InitializeAll` (`0x10163640`, a massive
startup-construction function) builds `g_pStAvatarCoordinator` (`0x10668FAC`) — a manually
constructed 18-slot C-style vtable object. `StAvatarCoordinator_StateHandler` (`0x10237710`,
slot 6 of that vtable — confirmed by address arithmetic: `(0x10335BE0−0x10335BC8)/4=6`) is a real
9-state state machine whose state-9 case drives avatar teardown. This is the real seam between
FFXI's own bootstrap and the `dancer` middleware.

### Confirmed lifecycle pattern (shared by `StModel`, `StChannel`, `StTrigger`)

All three follow the same "load my own file format from the shared 11MB pool" shape:

- **Alloc from pool**: poll the pool with one wait-and-retry (`Sleep(2)` once, then give up).
  `StChannel` loads `.chn` files, `StTrigger` loads `.fxt` files, `StModel` loads `.dmp`/`.dmb`.
- **Assign buffer**: frees if already loaded or given invalid size, otherwise assigns the buffer
  and marks "owns data."
- **Resolve**: `StChannelItemResolve` calls `sqmoChannelBuildSQO` under mutex protection (a real,
  confirmed mutex-protected call), auto-upgrading an old format-version tag on success.
  `StTriggerItemResolve` calls straight into `g_pMeshResourceMng` — the same shared
  resource-manager global confirmed for `CYyModelDt`/`CYyMotionQue` — direct proof the `St*`/
  `dancer` layer integrates with the same resource system as the rest of the engine.
- **Clear**: `StChannelItemClear`/`StModelItemClear` dispatch cleanup based on how the item was
  built.

### `StAvatar` → `CYyMusicLoadTask` connection

`StAvatar`'s teardown method (`sub_1024D2C0`) is called, several levels up, from a chain whose
callees include a function confirmed to construct a `CYyMusicLoadTask` with volume/fade
parameters (127, 127, 30) before swapping it in for the previous active one, and three sibling
music-volume functions (`SetMusicTrackVolume_A`/`_B`/`_C`) resolved via `g_pMeshResourceMng` and
a real resource ID (`61`). Real, concrete evidence that character/avatar teardown is tied to a
music-track transition, plausible for scene/cutscene boundaries.

### `sqOpcode` — the real `.fxt` VFX-trigger mechanism

Confirmed literally via the error string `"Trigger file not found"`. A genuine 3-level
event-sequencing hierarchy:

- **`sqopSystem`**: `flags`, `trackNdx`, `trackCount`, `trackTotal`, `tracks[]` (16-byte entries).
- **`sqopTrack`**: `opcodeNdx` (playback position), `opcodeCount`, `opcodeTotal`, `opcodes[]`
  (12-byte entries).
- **`sqopOpcode`**: a minimal, generic structure — a type tag plus two raw parameters. No
  per-type fields; an opcode's meaning lives entirely in the dispatcher.

**Load chain, confirmed end to end**: `StTrigger_RegisterCallbacks` explicitly registers
`StTriggerItemResolve` + `StTrigger_BuildFromFXT` as a resolve/build pair in FFXI's generic
resource-callback system. `StTrigger_BuildFromFXT` calls `sqopSystemBuild` then
`sqopSystemActivate` (resets every track's playback position to start).

**Dispatch** (`StTrigger_ProcessOpcodesUpToTime`) is **time-keyed**: each call processes every
opcode whose time has passed since the last call, in one "catch-up" pass.

- **Type 0**: resolves a named/numbered resource via the same resource ID (`61`) and resolve call
  confirmed for the music-volume functions, and on success calls the identical function used
  there — strongly suggests a sound effect/music cue trigger by numbered ID. On a name mismatch,
  falls through to a call carrying several float parameters shaped like spatial/distance/falloff
  values, plausibly a positioned 3D sound trigger.
- **Types 1 and 2**: write into a large global object (`dword_10455C20`, 45 cross-references
  spanning nearly the entire `.text` section). This object is allocated/freed at the `CApp`
  (top-level application) level alongside three sibling subsystems — a broad, generic
  application-settings/state singleton with many unrelated purposes sharing one allocation, not a
  dedicated camera/effects structure. One of its nearby fields (`byte_10455C34`, +20 bytes)
  controls gamepad input configuration ("PADSIN"/"PADEXSIN"), unrelated to effects. Its
  construction is confirmed: a `0xDC4`-byte (3,524-byte) allocation, with `this+132` holding the
  real `IDirectInput8` interface pointer, created during application startup
  (`sub_10001520` → `sub_10001BB0` → `sub_100058F0`; see §4's DirectInput devices row). The same
  startup function also runs `CDx`'s capability check, which is why the two were once conflated.

  **Types 1 and 2 are confirmed, end to end, to be a controller rumble/force-feedback trigger
  system.** `StTrigger_ProcessOpcodesUpToTime` accumulates into `+3508` (type 1 adds its raw
  opcode parameter directly; type 2 adds a saturating 0-or-1 capped at 127) and sets a `+3516`
  dirty flag on any contribution. The confirmed consumer, `sub_10007AE0`, reads and resets both
  fields (plus a second, related accumulator at `+3504`) on a regular cadence, computes a scaled
  magnitude (capped at 256, scaled by `10000/256` — the real DirectInput force-feedback magnitude
  range), and calls `IDirectInputEffect::SetParameters` (vtable offset 24, the genuine COM
  position) directly on a `GUID_ConstantForce` effect object — confirmed byte-for-byte
  (`{13541C20-8E33-11D0-9AD0-00A0C9A06E35}`) — created earlier by `sub_100083D0`'s joystick
  device setup (see §4). Two more real fields, found in the same function: `+3512` is a cooldown
  timer (reset to 5 ticks after every trigger, decremented via a `GetTickCount`-style call), and
  `+3520` caches the last-sent magnitude to skip a redundant `SetParameters` call when nothing's
  changed — the same "diff before sending" discipline already confirmed elsewhere in this
  engine's rendering code.

  A genuine bonus found in the same function: IDA's own decompiler typed its parameter as
  `XINPUT_VIBRATION`, revealing a **parallel XInput (Xbox-controller) fallback path** sharing the
  identical accumulator fields, gated by separate flags (`+3225`/`+3226`) and calling a different
  function (`sub_10008ED0`, almost certainly wrapping `XInputSetState`) — the game supports
  rumble through whichever API the connected controller actually uses.

**A complete accounting of every possible opcode type is now confirmed directly, not just
inferred from what's handled.** `sqopOpcodeGet` (the type-extraction function every opcode-type
check ultimately depends on) has **exactly one caller anywhere in this binary**:
`StTrigger_ProcessOpcodesUpToTime` itself. There is no other consumer of opcode-type data to
check. Since that function exhaustively handles only types 0, 1, and 2, this is the complete
dispatch mechanism — a type value outside that set can exist in a `.fxt` file's raw data (the
type field is an unconstrained integer), but the runtime has no handling for it at all; it falls
through and is silently skipped with zero effect, not a missing feature elsewhere.

---

## 11. Confirmed performance-relevant findings, consolidated

**Real, already-implemented optimizations** (the engine is not naively unoptimized):

- `sqgxContext`'s 16-stage texture-state cache, seeded to `-1` (§8).
- `sqgxContext_BatchIndices`'s 1,000-index draw-call batching with degenerate-triangle bridging
  and redundant-setup avoidance (§8).
- The shader-baking cache shared by Generic/Glow/Aniso (magic tag `655369`) (§8).
- `sqshDispList`'s GPU display-list wrapper (§8).
- `sqshIndex_BuildSpatialGrid`'s 15×15×15 spatial hash for efficient vertex welding (§8).
- `CMoProcessor`'s weight-premultiplied bone-matrix table (128 entries), avoiding per-vertex
  weight multiplication (§6).
- `sqimTM2Composite`'s masked-overlay compositing (avoids regenerating a base texture per
  customization) (§8).

**Open performance leads:**

- `sqshTriStripZSort`'s per-shape throttle: the depth sort runs once every N updates, with N
  stored per shape (§8).
- **Per-actor work is already staggered 4:1** (§6): two blocks in `sub_100CBDE0` run for each
  actor only when a counter modulo 4 equals the actor's bucket, and new actors go to the
  least-loaded bucket. Profiling per-actor cost should account for this four-frame cycle.

**Checked and ruled out as performance concerns:**

- `sqshUtil_WeldVertices` (naive O(n²)) — dead code; nothing references it (§8).
- `sqShader`'s Sampling type (no bake cache) — reachable only during model construction (§8).
- `sqshTriStripZSort` — throttled, not unconditional per frame (§8). Actual periods in shipped data
  remain a data/dynamic question.

**Threads and the race-condition candidates:**

The client runs many threads — audio, TCP/socket handlers, the message loop, at least one timer
callback, plus whatever Direct3D/DirectInput/DirectSound start internally — confirmed by a real
import-table check (`CreateThread`/`ExitThread`/`TerminateThread`/`ResumeThread` are genuine
KERNEL32 imports, called from 14 distinct sites in `.text`, most passing a real, distinct function
address as the thread entry point, not a null or dynamically-computed one). Two of those threads
were traced in enough depth to settle whether they actually race the main thread over shared
resource-tree state — one does, one doesn't, and a third path (the general async file I/O worker)
turned out to be the one that matters most:

- **The file I/O worker thread is where the real, concurrent race lives.** Triggered by the
  Trigger-file loader (`0x10252F10`, called from the sound/trigger code at `0x1024D480`), which
  queues two async `READEX` requests. The completion callback (`0x10253030`) runs **on the file
  worker thread**, and does all of the following with no lock held against the main thread: builds
  a full resource tree via `MeshResourceMng_ResolveTree` (`0x10073430`, confirmed directly —
  masks a node-type field with `0x7F` early on, consistent with dispatching per node type across a
  ~1 KB stack frame) on the global resource manager at `0x1047D128`; dereferences the root, stamps
  its file ID at `+0x34`, and takes a reference via `0x10071E90` — confirmed by direct disassembly
  to be the exact increment counterpart to the release path below: it reads the same 16-bit count
  at node `+0x18`, increments it with a branchless XOR trick masked to `0x7FFF` (matching the
  count's confirmed 15-bit width), writes it back, then walks the same parent chain. The file
  worker also shares, unlocked, the resource manager's handle table, the engine-heap allocations
  the resource factory (`0x10071280`) makes, and — the sharpest edge — the evictor (`0x100740D0`),
  which that factory calls under memory pressure and which can free an unpinned tree from the
  worker thread while the main thread is still using it. A file-service lock exists but doesn't
  help: the callback holds it only around the file request itself, and the main-thread loaders
  (`0x10072FE0`, `0x100731C0`) build their own trees *after* releasing it — so a worker-side build
  and a main-thread build or eviction can genuinely overlap.
- **A second thread (`0x10245650`) touches the same tree, but by construction can't race main.**
  This is the lobby-to-world entry sequence — opens the `"lobyhelp"` menu, loads resources through
  `0x10245470` → `0x100731C0` → the same tree builder, takes/releases references, ends with a
  weather transition. Started suspended by mode handler `0x10013AD0` via a small thread pool
  (`0x100394E0`). Its interaction with main is not ordinary concurrency: byte flags in the thread
  object hand off control in lockstep — main sets a running flag and resumes the thread once per
  frame, then polls with `Sleep(1)`; the loader thread runs until it explicitly yields (clearing
  the flag, waiting for main to set it again) or finishes. Exactly one of the two runs at a time —
  a coroutine built out of a real OS thread plus polling, not a genuine race with main. It *does*
  still race the file I/O worker thread above, since nothing coordinates those two with each
  other.
- **Confirmed refcount pair:** `0x10071E90` (increment, above) and `0x10071EC0` (decrement —
  called directly five times by the loader thread and by 47 separate main-thread functions;
  releases by decrementing the same 15-bit count at `+0x18` and walking the parent chain at
  `+0x28`, plain read-modify-write, no lock, no atomic instruction). `0x10071050` → `0x10073B20`
  frees nodes whose count reaches zero, ending in a virtual destructor call (`0x100721F0`) whose
  target object type is not resolved statically.
- **Confirmed clean, by direct call-graph search:** the audio worker, music stream threads, both
  socket workers, the heartbeat, the gamepad thread, the timer callback, and 17 other async file
  callbacks have no *direct*-call path to the tree code.
- **Real limits on that last claim, stated plainly rather than glossed over:** this was a static
  call-graph check only. Of 476 functions that can reach the tree code, 210 are entered through
  vtables or callbacks that a direct-call search can't follow — so "no path" for anything reached
  only that way is unproven, not disproven. The audio thread's 14 table-dispatched command
  handlers specifically were not followed forward, so "no audio-thread path" means "none found via
  direct calls from the worker proc," not "definitively none." `CMoProcessor_ScratchMatrixOp`'s
  pool counter/array (plain `mov`/`inc`/`dec`, no lock) remains an open race candidate on the same
  basis — reachability from a second thread neither confirmed nor ruled out.
- **The concrete next step, not yet done:** a single breakpoint on `MeshResourceMng_ResolveTree`
  (`0x10073430`) logging the calling thread ID would settle the one thing static analysis can't —
  whether the file worker's build and a main-thread build/eviction ever actually land at the same
  moment — in one play session, rather than more static reading.
- The codebase is not naively single-threaded regardless: `sqmoChannelBuildSQO` uses a real mutex
  pair, confirmed independently of all of the above.

---

## 12. Tooling reference

`scan_class_descriptors.py` — regenerate via `python3 scan_class_descriptors.py
FFXiMain_uncomped.dll`.

- **`scan()`** — finds/validates `class_descriptor_t` nodes in `.rdata`/`.data` (recursive
  parent-chain validation, size cap 300,000 bytes, tuned empirically against known-real vs.
  known-garbage results).
- **`find_accessors()`** — finds every `mov eax, class_descriptor_addr; ret` stub in `.text` per
  confirmed class.
- **`find_vtables()`** — recovers vtable segments from `.rdata`, splitting compound/MI runs at
  recognized accessors and (via `classify_thunk()`) two confirmed MI-thunk shapes. A narrow,
  jump-target-verified merge re-joins the case where a `forwarding` thunk is itself a class's own
  forwarding accessor for an embedded mixin (10 confirmed instances, labeled
  `<mixin-of-ClassName@ADDR>`).
- **`classify_thunk()`** — classifies a function as `trivial` (`lea eax,[ecx+imm8]; ret`) or
  `forwarding` (`sub ecx, imm8; jmp rel32`), with signed offset. `trivial` with a **negative**
  offset is a reliable standalone secondary-base marker; `trivial` with a **positive** offset is
  the "Nth embedded member" accessor family (§2). Currently recognizes only the imm8 forwarding
  encoding (`83 E9 xx E9 ...`); the imm32 encoding (`81 E9 xx xx xx xx E9 ...`, offsets ≥128) is
  not yet checked for.
- **`classify_confidence()`** — tags every class `unique` (1 accessor address — trustworthy
  mapping, with the known `CMoProcessor`-style exception where identical stubs are shared across
  genuinely different compiled vtables), `shared` (>1 accessor — mapping is mechanically
  ambiguous, needs a constructor trace or size-tag read), or `no_accessor`.
- **`confirmed_counts()`** — the classes/functions ticker source. A reproducible floor, not a
  measure of understanding depth — a `shared`-accessor class's functions count the same as a
  `unique`-accessor one even though the concrete subclass-to-vtable mapping isn't known.
- `_ida_main_thread` (the IDA MCP bridge's tool-wrapping decorator) now correctly logs exception
  text via `log.log_exception(...)` before re-raising — previously silently swallowed every
  underlying Python traceback. `find_bytes`/`search_bytes` calls positionally
  (`find_bytes(pattern, ea, None, max_ea)`) rather than by keyword, working around a SWIG-binding
  limitation. `rename_symbol`/`batch_rename`/`comments` are confirmed working end to end against
  the live database (35+ real renames applied and cross-reference-verified as of the last
  session).
- **`types` tool fixes (IDAssistMCP 2.1.2–2.1.4).** Array members were silently created as scalars;
  `create_struct` could not replace an existing type; overwrite by delete-and-recreate changed the
  ordinal and left references dangling (fixed with `NTF_REPLACE`); `set_named_type` returns a
  `tinfo_code_t` where `TERR_OK == 0` (success is falsy — 2.1.3 misread this as an unreliable
  return value); and type changes did not invalidate Hex-Rays' cached pseudocode, so a decompile
  right after a change could predate it (fixed with `clear_cached_cfuncs()`). **Until 2.1.4 is
  installed, treat any decompile shortly after a type change as possibly stale.**
- **The symbol script now reproduces the IDB's types.** `tools/ffxi_symbols_ida.py` defines
  `CMoProcessor` and `CXiSkeletonActorRes` with IDA's own C parser (`idc.parse_decls`,
  `PT_REPLACE`) and types `g_pProcessor`, instead of listing struct fields to apply by hand.
- **IDAssistMCP 2.1.x extended tools.** Six tools added for gaps hit on this binary (package
  `IDAssistMCP-2.1.1.zip`):
  - `create_function` — define a function where auto-analysis never mapped one
    (`ida_funcs.add_func`, previously imported but never called by the package).
  - `disasm_range` — disassemble any bytes, inside a function or not, without modifying the
    database.
  - `name_provenance` — whether a name came from Lumina, FLIRT, the user or auto-naming, with a
    trust hint for tiny functions; `scan_all` lists every signature-named function.
  - `find_code_refs_raw` — raw `call`/`jmp rel32` and absolute-pointer sweep for one or more
    targets, including inside unanalyzed code, with a verdict per hit.
  - `read_vtable` — one-call vtable decode with each slot classified from its bytes.
  - `find_struct_offset_uses` — operand-level `[reg+offset]` search with read/write access.

  Live status in IDA: `read_vtable` works (used for the `CXiSkeletonActor` decode in §6);
  `find_code_refs_raw` works for pointer hits and proved `sqshUtil_WeldVertices` unreferenced.
  Version 2.1.0 had two bugs found only in real IDA — pointers inside instructions were labelled
  `data_pointer` (IDA's instruction tail bytes are not `is_code()`), and operand decoding failed
  at run time (the MCP layer hid the exception). 2.1.1 fixes the first, switches to the documented
  operand idiom for the second, and makes all six tools return the exception text instead of a bare
  error. Until 2.1.1 is installed, branch-reference sweeps and `find_struct_offset_uses` fail.
  Known limit: `read_vtable` cannot find the end of a vtable followed directly by another one.
- **Name provenance is mandatory before using a name as evidence.** Lumina supplied the mangled
  names in this database and they are mostly false matches on tiny functions (§1). A function's
  `FUNC_LUMINA` flag (`0x10000`) is the tell; `name_provenance` reports it.
- **Reading code IDA never analyzed.** A raw `read_memory` of a region followed by local
  disassembly (Capstone), or `disasm_range`, reads code without defining functions. This decoded
  `sqxfXformTD.c` completely (§8) without needing `create_function`.
- **Large tables in one pass.** Read a whole vtable or pointer table at once and classify it
  (`read_vtable`, or bulk read plus local decoding) rather than querying slots one at a time.
- **Self-describing structures found so far — worth sweeping for deliberately:**
  - Code-generation templates: only six exist (lights and cameras, one cluster at
    `0x103B1E44`–`0x103B2300`); their field lines give struct layouts in order.
  - Manual C vtables in `dancer` objects: type tag followed by Validate/Destroy/Print/Update
    function pointers at fixed offsets. Finding the Init function that writes them names every
    method of the type (this is how `sqxfXformTD::Update` was found).
  - Keyword→handler registries: tables of (name string, function) pairs, e.g. the model-script
    command table at `0x103BC860` (`allocate`, `skeleton`, `skeleton_shape`, `skin_shape`,
    `snap_skin2skin`, …). Each handler's purpose comes with its name.
  - Source-file path strings (`C:\dev\dancer\modules\…\*.c`): their cross-references
    enumerate every function in that compilation unit that allocates or asserts.
- **The PS2 `SCUS_972.66` debug sections are the strongest unused lever.** Earlier work used its
  25,672 *symbols*; its MIPS `.debug`/`.line` sections (DWARF v1) also carry **type layouts**. The
  community's `XiEvents` project took its PS2 field names from the same kind of data (PS2 beta
  disc DWARF). Parsing it would give struct members and offsets for classes whose PC layouts are
  still open (`CYySkl`/`KzSKD`, `KzObjectDrawInfo`, `CAcc`), and should be run per module before
  manual work.
- **External community resources.** `AshitaXI/Ashita-v4beta`'s SDK (`plugins/sdk/ffxi/entity.h`)
  and `atom0s/XiEvents` independently name `CYyObject` and `CXiSkeletonActor` (§2). `XiEvents`'
  `Event VM Structures.md` documents the event VM state (`xievent_t`, 0x268 bytes, at entity
  `+0xD4`; `reqstack_t`; `xieventex_t`, including entity fade fields `FadeFlag`/`NowAlpha`/
  `AlphaTime`) and the per-tick call chain `MainIdle → AtelIdle → XiAtelBuff::Idle →
  XiEvent::EventIdle → XiEvent::ExecProg`. `Event VM Functions.md` and `Event DAT Structures.md`
  are not yet reviewed.
- **PS2 debug-data tooling.** `ps2_dwarf_tools.zip` contains a DWARF 1 parser for
  `SCUS_972.66` (no standard library reads DWARF 1), a class indexer, and a JSON export of all 2,758
  named types with members, offsets, types and bases. Function symbols come straight from
  `.symtab`; vtables are `__vt__<len><Class>` data symbols whose first two words are a header.
- **Vtable alignment is the reliable PS2↔PC bridge.** Pairing a PS2 vtable (with symbol names) with
  the PC `read_vtable` output, and checking each pairing against field semantics, gives
  method-for-method correspondences.
- **The BinDiff results (`SCUS_972_vs_FFXiMain_unpacked.BinDiff`) are not usable for name
  transfer.** Overall similarity is 0.079. Against 24 PS2↔PC method pairs verified by vtable
  alignment, BinDiff got **0 right, 15 wrong, 9 unmatched**, with many wrong matches at the same
  0.40 similarity a right match would show. On C runtime functions its high-scoring matches are
  also wrong (`fabsf` ↔ `CreateFileA`, `scePrintf` ↔ `GetTickCount`); only identical-name matches
  (`htons`, `CreateThread`) are right. Cross-architecture (MIPS vs x86) structural matching is the
  likely cause. The `dancer` functions were not tested fairly: they live in `Dancer.bin`, outside
  the ELF's main section, and appear to be absent from the diff.

---

## 12b. The PC `CXi*Actor` family's real vtable structure, corrected

A prior pass this project reported all of `CXiControlActor`/`CXiCollisionActor`/`CXiSkeletonActor`
at a uniform 153 slots, via the class-descriptor scanner. That figure is wrong for at least the
first two, confirmed by direct inspection: real, valid code pointers continue for over 100 slots
past 153 in both. The scanner's heuristic appears to assume a shared, fixed length across this
family — an assumption already known to be false for `CXiSkeletonActor` specifically (independently
confirmed elsewhere in this document at 264 real slots), and it turns out to be wrong for the
others too.

**The authoritative lengths, cross-validated against two independent methods (constructor-vtable-
store tracing from earlier work, and direct boundary verification — a clean
garbage-data transition for the low end of the chain, an exact adjacent-symbol byte-gap for the
high end):**

| Class | Real length | Growth over parent |
|---|---|---|
| `CXiActor` | 227 | — (base) |
| `CXiAtelActor` | 254 | +27 |
| `CXiControlActor` | 255 | +1 |
| `CXiCollisionActor` | 256 | +1 |
| `CXiSkeletonActor` | 264 | +8 |

Naive byte-scanning for these boundaries is unreliable and produced wrong numbers on a first pass
(a runaway read that kept finding "valid-looking" pointers hundreds of slots past the real end,
simply because `.text` is large enough that many unrelated values fall in-range by chance) — the
trustworthy checks were a *clean* transition into obviously-non-code data (float bit patterns,
small integers) for `CXiCollisionActor`, and an *exact* byte-gap match to the next real symbol's
own address for `CXiControlActor`. Anyone continuing this should use one of those two methods, not
a plain in-range-address check.

**The load-bearing finding for everything already done in this project: layout is shared and
additive up the chain, confirmed directly, not assumed.**
- `CXiActor` and `CXiSkeletonActor` are identical at 96 of `CXiActor`'s 227 slots — meaning every
  slot this project has ever confirmed against `CXiSkeletonActor`'s table (§6 and this document's
  own `XiActor`-slot-naming work) is valid at the same index in `CXiActor`'s own standalone table
  too, not just in the combined one.
- `CXiAtelActor` matches `CXiActor` at 223 of 227 shared indices (only 4 real differences, three of
  them the expected per-class slots — destructor, and two others) — confirming PS2's own finding
  that `XiAtelActor` adds essentially nothing over `XiActor` (PS2's real `XiAtelActor` vtable is
  123 slots, identical to `XiActor`'s, with exactly two overrides: `OnMove` and `GetPos`).
- `CXiAtelActor`'s 27 new PC slots (indices 227–253) have **no PS2 `XiAtelActor` counterpart at
  all** — checked directly against PS2's real, complete 123-slot table, not inferred. These are
  PC-only additions, the same category as the already-confirmed 41–50 flag-pair block within
  `CXiSkeletonActor`'s own table, just at a different level of the hierarchy. Its one real
  override within the shared range (slot 111, `lea eax,[ecx+0xC4]; ret`) is `GetAtelPos` — the
  first link in the same cascading position-override chain later confirmed at `CXiControlActor`
  (`0xD4`) and `CXiCollisionActor` (`0x5C4`).
- **`CXiControlActor`'s and `CXiCollisionActor`'s single new slots each, both confirmed:**
  `CXiControlActor` slot 254 (`0x100AAF30`) = `SettingLookAtHeight` — an exact structural match to
  the real PS2 body, including an unusual, distinctive shared quirk (the result of a virtual call
  with literal argument `5` gets written to a *global*, not a member field, on both platforms).
  `CXiCollisionActor` slot 255 (`0x100A4CE0`) = `IsBlendNormal` — both platforms implement it as a
  genuine empty stub returning false unconditionally; confirmed as the correct match not by shape
  alone (which is weak in isolation for an empty stub) but because it's the *only* new slot either
  platform adds at this exact position in the hierarchy, leaving no ambiguous pool to confuse it
  with.
  **`CXiSkeletonActor`'s 8 genuinely new slots (256–263), mostly resolved, confidence
  differentiated honestly rather than flattened:**

  | PC slot | Field | PS2 method | Confidence |
  |---|---|---|---|
  | 260 | writes `+0x73C` | `SetUOffset` | High — clean pair with 261, matches PS2's adjacent-field pattern |
  | 261 | reads `+0x73C` | `GetUOffset` | High — same basis |
  | 262 | writes `+0x740` | `SetVOffset` | High — clean pair with 263, `+4` from the U pair, matching PS2 exactly |
  | 263 | reads `+0x740` | `GetVOffset` | High — same basis |
  | 259 | reads `+0x74C` | `GetEmapTexture` | High — `+0x74C` was independently established as `SetEmapTexture`'s field back in this project's earliest work (slots 0–40); this is a cross-check against prior work, not a fresh guess |
  | 258 | reads `+0x750` via out-pointer | `GetEmapColor` | Medium — plausible by proximity to the same established cluster, not independently confirmed the way the others are |
  | 257 | `xor al,al; ret` | none — PC-only | High confidence this is *not* any of the six PS2 targets (none are boolean stubs); genuine PC-only addition |
  | 256 | reads `+0x864` via out-pointer | none — PC-only (by elimination) | Lower confidence; field is distant from the rest of the cluster, no direct PS2 evidence either way |

  **`CXiSkeletonActor`'s 131 overrides within the shared 0–226 range: a large fraction were
  already resolved** — indices 8, 11–36 correspond exactly to the long-established
  color/effect/disintegration/scale cluster, and 41–50 is the separately-confirmed PC-only
  flag-pair block. That leaves 90 genuinely
  unexamined indices, of which the largest contiguous stretch (172–209, 38 slots) turned out to
  sit **entirely beyond PS2's own combined `XiSkeletonActor` table, which tops out at 131
  entries** — meaning those indices structurally cannot correspond to any `XiActor`-family PS2
  method by position at all; slot 172 specifically is already known from separate, earlier work
  to belong to a different class's adjustor thunk, not this family.

  **Same-index correspondence, tested directly rather than assumed, fails even in the "early"
  region:** checked PC indices 46–50 against the expected PS2 methods there
  (`GetGroundHeight`/`GetGroundNormal`/`ExecHitCheck`/`IsTouchDown`/`IsOnLift`) — those PC indices
  are confirmed to be the *already-known* PC-only flag-pair block instead, not these methods.
  `ExecHitCheck`/`IsTouchDown`/`IsOnLift` are empty only in `XiActor`'s *base* versions;
  **`XiCollisionActor` overrides all three with real field accessors, now matched (§18.16).** `GetGroundHeight`/`GetGroundNormal` were narrowed by whole-table shape search
  (excluding everything already confirmed) to 2 and 3 remaining unclaimed candidates
  respectively, sharing candidate pools with `GetWaterHeight`/`GetFocal`. A direct attempt to
  disambiguate further — searching for any function referencing two candidate field offsets
  together, which would reveal a real relationship between them — came back empty. Documented as
  narrowed, not guessed: `GetGroundHeight`/`GetWaterHeight` are one of {slot 129, slot 136} each;
  `GetGroundNormal`/`GetFocal` are two of {slot 132, slot 153, slot 246}, without a confirmed
  assignment.

  **`CXiAtelActor`'s 27 PC-only slots (227–253): self-authored names from observed behavior,
  since there is no PS2 counterpart to search for at all — marked as such throughout, not
  presented as confirmed PS2 identifiers.** Grouped by what was actually found in each body, not
  assumed:

  | PC slot | Address | Behavior | Author-assigned name |
  |---|---|---|---|
  | 227 | `0x10082920` | reads `+0xA4`, returns `value − 0x35` | `GetAtelTypeOffset53` |
  | 228 | `0x10082930` | param in `[0x35, 0x3C]` → bool | `IsAtelTypeInRange53to60` |
  | 229 | `0x10082960` | `+0xA4 == 0x52` → bool | `IsAtelType82` |
  | 230 | `0x10082950` | writes `+0xA4` | `SetAtelType` |
  | 231 | `0x10082980` | reads `+0xA4`, returns `value − 0x52` | `GetAtelTypeOffset82` |
  | 232 | `0x10082990` | param `== 0x52` → bool (validates a value, not the field) | `IsParamAtelType82` |
  | 233 | `0x100829c0` | `+0xA4 == 0x53` → bool | `IsAtelType83` |
  | 234 | `0x100829b0` | writes `+0xA4` — a second, separate setter for the same field as 230 | `SetAtelType2` |
  | 235 | `0x100829e0` | reads `+0xA4`, returns `value − 0x53` | `GetAtelTypeOffset83` |
  | 236 | `0x100829f0` | param `== 0x53` → bool | `IsParamAtelType83` |
  | 237 | `0x10082a10` | `xor eax,eax; ret` | `ReturnZero_0Arg` |
  | 238 | `0x10082a20` | `ret 4`, no body at all | `ReturnDefault_1Arg` |
  | 239 | `0x10082a30` | `xor al,al; ret` | `ReturnFalse_0Arg` |
  | 240 | `0x10082a40` | `ret 8`, no body | `ReturnDefault_2Arg` |
  | 241 | `0x10082a50` | `xor ax,ax; ret 4` | `ReturnZeroWord_1Arg` |
  | 242 | `0x10082a60` | returns fixed global `0x1047D640` | `GetSharedAtelDefaultA` |
  | 243 | `0x10082a70` | returns the *same* global as 242 | `GetSharedAtelDefaultA_Dup` |
  | 244 | `0x10082a80` | `xor al,al; ret 0xC` | `ReturnFalse_3Arg` |
  | 245 | `0x10082a90` | `xor al,al; ret 8` | `ReturnFalse_2Arg` |
  | 246 | `0x10082aa0` | returns a different fixed global `0x1047D4CC` | `GetSharedAtelDefaultB` |
  | 247 | `0x10082ab0` | `ret 4`, no body | `ReturnDefault_1Arg_B` |
  | 248 | `0x10082ac0` | `xor ax,ax; ret` | `ReturnZeroWord_0Arg` |
  | 249 | `0x10085b50` | real: allocates (`sub_10311BBB`, size `0x10`), then calls two more real functions to initialize the result | `ConstructAtelSubObject` |
  | 250 | `0x10085c90` | real: reads `+0x68`, walks a linked structure via `+0x2C` | `FindCasterLink` |
  | 251 | `0x10085cf0` | real: identical shape to 250, fields `+0x6C`/`+0x30` — same adjacent-offset pattern already confirmed for the `Unlink{Caster,Target}Attachments` pair | `FindTargetLink` |
  | 252 | `0x10082ae0` | `xor al,al; ret` | `ReturnFalse_0Arg_B` |
  | 253 | `0x10082ad0` | `ret 4`, no body | `ReturnDefault_1Arg_C` |

  Honesty check on what these names actually convey: the trivial `ReturnX` stubs (237–241, 244,
  245, 247, 248, 252, 253 — eleven of the twenty-seven) carry essentially no real semantic content
  beyond "does nothing, returns a fixed value of this type/arg-count" — the names label them for
  reference, they don't claim understanding of *why* they exist. The `AtelType` cluster (227–236)
  and the `FindCasterLink`/`FindTargetLink` pair (250/251) are the two places real, specific
  behavior was found and named accordingly. `249` (`ConstructAtelSubObject`) is real but its exact
  purpose is inferred from shape (allocate-then-initialize), not independently confirmed.

  **`CXiControlActor`'s 42 overrides within the shared range (vs. `CXiAtelActor`): self-authored
  names from behavior, same honesty standard.** This batch ruled out an earlier hypothesis rather
  than confirming it — slots 129/130, 133/134, 135/136 are three real, *working* Get/Set pairs on
  adjacent fields (`0x170`/`0x174`/`0x178`), which rules out `GetGroundHeight`/`GetWaterHeight` as
  the match here (PS2's `SetWaterHeight` is a confirmed empty stub, and `GetGroundHeight` has no
  setter in the vtable at all — neither fact fits three genuinely working pairs). That
  disambiguation from earlier remains unresolved; these are something else.

  | PC slot | Behavior | Author-assigned name |
  |---|---|---|
  | 111 | `lea eax,[ecx+0xD4]; ret` | `GetControlPos` — `CXiControlActor`'s own position override |
  | 112 | `lea eax,[ecx+0xE4]; ret`, 16 bytes after 111 (vec4 spacing) | `GetControlDir` |
  | 129 | reads `+0x170` | `GetPhysicsFieldA` |
  | 130 | writes `+0x170` | `SetPhysicsFieldA` |
  | 131 | compares a param float against a fixed threshold constant | `IsAboveThresholdA` |
  | 132 | `lea eax,[ecx+0x160]; ret` | ~~`GetFocal`~~ — **superseded, 2026-09-26 (§18.13):** this row's "fires every phase, including flat ground" reasoning doesn't actually distinguish GetFocal from GetGroundNormal (a ground-normal read needs the same per-frame recompute regardless of visible terrain). §18.11 reassigns this exact slot to `GetGroundNormal` on stronger evidence (the paired setter only stores when `\|y\| > 0.7`, a slope filter with no sensible reading as a scalar focal length). The real `GetFocal` is a separate method, still open — see §18.13. |
  | 133 | writes `+0x174` | `SetPhysicsFieldB` |
  | 134 | reads `+0x174` | `GetPhysicsFieldB` |
  | 135 | writes `+0x178` | `SetPhysicsFieldC` |
  | 136 | reads `+0x178` | `GetPhysicsFieldC` |
  | 137 | computes `ecx+0x388`, real setup call | `PrepareControlSubState` |
  | 138 | real, saves 3 registers, substantial | `ControlSubroutineA` (lowest-confidence name in this batch — shape only, no clear purpose identified) |
  | 141 | real: computes `ecx + index*104 + 0x180` — array indexing into 104-byte records | `GetIndexedControlRecord` |
  | 154 | reads a fixed global, allocates 256 bytes of stack, substantial | `ControlBufferSetup` |
  | 169 | reads `+0x68`, tests non-null — same field offset already seen in `FindCasterLink` (slot 250 of `CXiAtelActor`) | `CheckCasterLinkValid` (plausibly related to, not necessarily identical to, the `CXiAtelActor` function) |
  | 176–187 | each adds a different large, category-specific constant to an input value before jumping to a shared handler at `0x100A98D0` | `RemapResourceId_CategoryN` (N = position in the sequence, 1–8; the specific category each represents was not determined) |
  | 188 | real, matches 189's shape exactly | `ControlInitStepA` |
  | 189 | real, matches 188's shape exactly | `ControlInitStepB` |
  | 192 | calls a shared helper (`0x10081550`) with a fixed singleton address (`0x10487F58`) loaded first | `RegisterWithSubsystemA` |
  | 193 | same helper, different fixed singleton (`0x1047D600`) | `RegisterWithSubsystemB` |
  | 195 | validates a param, then reads `+0xFC` | `GetCheckedFlagsFC` |
  | 196 | plain read of the same `+0xFC` field, no validation | `GetFlagsFC` |

  Slots 204–209 in this same diff list are the same three byte Get/Set pairs (`+0xF9`/`+0xFA`/
  `+0xFB`) already encountered in `CXiSkeletonActor`'s own table — same addresses, confirming
  they're inherited down from `CXiControlActor`, not independently reimplemented.

  **`CXiCollisionActor`'s 9 overrides within the shared range (vs. `CXiControlActor`):** a much
  smaller, cleaner batch — three real Get/Set pairs, a lone getter, and a continuation of the same
  cascading position-override pattern already seen at this exact slot index for `CXiControlActor`
  (slot 111 was `0xD4` there, `0x5C4` here — each class in the chain keeps re-overriding its own
  position storage).

  | PC slot | Behavior | Author-assigned name |
  |---|---|---|
  | 96 | calls own slot 253 with `1` | `RequestHitCheck` (PC-only; real address `0x100A5620` — see §18.16) |
  | 97 | writes `+0x5E4` | `SetCurrentAreaId` (PS2 field `current_area_id`) |
  | 98 | reads `+0x5E4` | `GetCurrentAreaId` |
  | 101 | writes byte `+0x5E0` | `ExecHitCheck` (PS2 slot 46) |
  | 102 | reads byte `+0x5E0` | `IsTouchDown` (PS2 slot 47) |
  | 103 | reads byte `+0x5E2` | `IsOnLift` (PS2 slot 48) |
  | 111 | `lea eax,[ecx+0x5C4]; ret` | `GetPos` (PS2 slot 56) |
  | 252 | reads byte `+0x5EC` | `IsHitCheckPending` (PC-only) |
  | 253 | writes byte `+0x5EC` | `SetHitCheckPending` (PC-only) |

  *Updated in §18.16:* these were author-inferred placeholders; all nine are now matched or
  explained against the PS2 overrides and DWARF layout.

  **`CXiSkeletonActor`'s own overrides (vs. its immediate parent `CXiCollisionActor`): 97 diffs
  found, first batch of 14 named — honesty about confidence varies more in this batch than any
  previous one, since several are real, substantial functions whose exact purpose isn't
  determinable from shape alone.**

  | PC slot | Behavior | Author-assigned name | Confidence |
  |---|---|---|---|
  | 84 | doubles a param byte, XORs against `+0x8AC` | `CheckBitAgainstField8AC` | Medium |
  | 85 | reads `+0x8AC`, shifts right 1, masks bit 0 | `GetField8ACBit1` | Medium — plausibly related to 84 |
  | 99 | unconditionally writes `1` to byte `+0x9F8` | `ActivateFlag9F8` | High (behavior is unambiguous, purpose isn't) |
  | 100 | unconditionally writes `1` to byte `+0xA04` | `ActivateFlagA04` | Same basis as 99 |
  | 113 | real, substantial, `0x58`-byte frame | `SkeletonSubroutineA` | **Low** — placeholder label only, purpose not determined |
  | 114 | real, similar prologue shape to 113, smaller frame | `SkeletonSubroutineB` | **Low** — same caveat |
  | 115 | forwards two stack args onward | `ForwardTwoArgsHelper` | Medium |
  | 116 | real, saves `edi`/`esi`, takes a param via `esi` | `SkeletonSubroutineC` | **Low** |
  | 117 | calls `0x100C9300` | `CallHelperC9300A` | Medium |
  | 118 | same call target as 117, slightly different setup — likely a paired variant | `CallHelperC9300B` | Medium |
  | 121 | `jmp 0x100D12D0`, no other code — a pure tail-call forward | `ForwardToD12D0` | High (behavior is exact; the forwarded function's own purpose wasn't traced) |
  | 122 | real, substantial, `0x24`-byte frame, saves 3 registers | `SkeletonSubroutineD` | **Low** |
  | 127 | writes byte `+0x79C` | `SetField79C` | High |
  | 128 | reads byte `+0x79C`, pairs with 127 | `GetField79C` | High |

  The four `SkeletonSubroutine*` names are explicitly placeholders, not real understanding — they
  exist so these slots have a stable label to refer to, not because their purpose is known.

  **Second batch, the remaining 36 diffs from this same comparison — all now examined, naming
  applied with the same honesty split between clear and unclear:**

  | PC slot | Behavior | Author-assigned name | Confidence |
  |---|---|---|---|
  | 148 | doubled-XOR bit check against `+0x840` | `CheckBitAgainstField840` | Medium |
  | 149 | reads `+0x840`, extracts bit 6 | `GetField840Bit6` | Medium |
  | 150 | `or byte [ecx+0x8AC], 1` | `EnableFlag8AC` | High — clean, unambiguous set-bit |
  | 151 | `and byte [ecx+0x8AC], 0xFE` | `DisableFlag8AC` | High — clean, unambiguous clear-bit |
  | 152 | reads bit 0 of `+0x8AC` | `IsFlag8ACSet` | High — completes the triplet with 150/151 |
  | 158–162, 164, 166, 173, 174, 190, 191, 194 | real, substantial functions, no clear purpose from shape | `SkeletonSubroutineE`…`SkeletonSubroutineP` (13 placeholders, one per slot in ascending order) | **Low**, all — stable labels only |
  | 165 | sets up access to the embedded `CYyModel` at `+0x674` (the same field the confirmed adjustor thunk at slot 172 forwards into) | `PrepareModelSubObject` | Medium |
  | 175 | `ret 0x10`, no body at all | `EmptyStub4Arg` | High (an empty stub, matching the pattern seen throughout this project) |
  | 197 | validated getter (`param==1` check) for `+0x838` | `GetCheckedField838` | High |
  | 198 | plain getter, same field as 197 | `GetField838` | High |
  | 199 | `sete`-based boolean comparison on two params | `CompareParamsEqual_A` | Medium |
  | 200 | reads word `+0x83C` | `GetField83C` | High |
  | 201 | same shape as 199 | `CompareParamsEqual_B` | Medium |
  | 202 | array-indexed byte read (`[eax+ecx+0x83E]`) | `GetIndexedByte83E` | Medium |
  | 203 | reads word `+0x83E` | `GetField83E` | High |
  | 242 | calls a sub-function, branches on its result | `CheckModelSubState` | Low |
  | 243 | computes `+0x674` (the same `CYyModel` field as 165/172), calls another accessor | `GetModelSubObjectField` | Medium |
  | 244, 245, 254 | real, substantial, large frames, no clear purpose | `SkeletonSubroutineQ`/`R`/`S` | **Low** |
  | 246 | `lea eax,[ecx+0x878]; ret` | `GetGroundNormal` — resolved by real runtime data (§16): silent during an early flat-ground phase, activates specifically once a slope/water-adjacent scenario begins, and stays active through sustained non-flat terrain — the shape of a surface-normal check, not a constant per-frame value | High |
  | 247 | writes word `+0x670` | `SetField670` | High |
  | 248 | reads word `+0x670`, pairs with 247 | `GetField670` | High |
  | 255 | reads `+0x87A`, compares against the constant `2` | `IsState2At87A` | Medium |

  **This closes out all 97 diffs from the `CXiCollisionActor`-vs-`CXiSkeletonActor` comparison.**
  Roughly a third have real, specific names with genuine behavioral grounding; roughly a third are
  clean but purpose-generic (`GetFieldNNN`-style, accurate about *what* they do, silent on *why*);
  and the remaining third are explicit low-confidence placeholders for real, substantial functions
  whose purpose wasn't determinable from static shape alone.

---

## 12c. The PC `CXi*Actor` family, fully swept: confirmed matches, self-authored names, and honest gaps

Complete pairwise coverage of every adjacent-class boundary in the chain
(`CXiActor`→`CXiAtelActor`→`CXiControlActor`→`CXiCollisionActor`→`CXiSkeletonActor`), moved
here from §13 to keep the open-questions list itself readable. Confidence is marked per item
throughout — real PS2-confirmed matches, self-authored names with genuine behavioral grounding,
purpose-generic-but-accurate labels, and explicit low-confidence placeholders are four different
things and are never presented as the same level of certainty.

4. **The ~110 `CXiSkeletonActor` slots outside the already-named ones lack individual PS2 method
   names — closed by direct behavioral matching, not position.** Class
   ownership for every slot 41–226 was already settled (all inherited from `CXiActor`; §6). What
   changed: a naive positional-offset approach was tried and rejected — PC inserts real,
   PS2-less blocks at multiple points (e.g. slots 41–50, a run of boolean flag get/set pairs with
   no PS2 `XiActor` counterpart at all), and a bulk argument-count-distribution comparison across
   both sides (PS2's real 121-method vtable vs. a 176-slot PC candidate range) confirmed the same
   thing quantitatively: PC has roughly double the candidates PS2's ~84 remaining methods need,
   and PS2's four genuine 6-argument methods have zero PC candidates at 6 arguments anywhere in
   the sampled range — decisive evidence that count-matching alone can't distinguish real targets
   from PC-only insertions. Switched to direct behavioral verification instead. Confirmed so far,
   at two different but both real confidence levels:

   | PC address | Method | Basis |
   |---|---|---|
   | `0x10082F20` | `GetEnglishName` | Every branch verified against the real PS2 body (field check, boolean sub-call, static-buffer string-copy, null-field fallback — all four pieces match) |
   | `0x100832D0` | `AddRef` | Confirmed by elimination: matched by process of exclusion against all three other simple inc/dec-shaped PS2 candidates (`AddLock`/`SubLock` — ruled out, different indirect-through-`+0x3C` shape; `GetPosHandle`/`ReleasePosHandle` — ruled out, boolean set/clear, not arithmetic) |
   | `0x100832E0` | `SubRef` | Same elimination basis as `AddRef`; one open discrepancy: PC guards against underflow (checks non-zero before decrementing), PS2's real body doesn't — plausibly a PC-side hardening, not disqualifying, but not an exact match either |
   | `0x10083390` | `AddSchRef` | Exact shape match: both unconditional, no guard, matching field-touch pattern |
   | `0x100833A0` | `SubSchRef` | Exact shape match, same basis |
   | `0x100A4660` | `GetPos` | Shape + sequence match (trivial address-computation getter, immediately followed by `GetDir`'s equivalent shape) — not branch-verified beyond that single instruction, since there's only one instruction to verify |
   | (adjacent slot) | `GetDir` | Same basis as `GetPos` |

   **PC slots 104–112, confirmed as a nine-slot positional band, with a firm, checked boundary at
   both ends — the first proof that the slot-0–40 sweep technique still works here, just locally
   rather than as one long run.** All nine PS2 bodies read directly and checked in order:

   | PC slot | Field touched | PS2 method | Match basis |
   |---|---|---|---|
   | 104 | reads `+0x98` | `GetMoveSpeed` | reads PS2 `+112`, the same field `SetMoveSpeed` writes |
   | 105 | writes `+0x98` | `SetMoveSpeed` | writes the same field slot 104 reads — consistent pair |
   | 106 | reads `+0x94` | `GetMoveSpeedBase` | reads PS2 `+108`, a distinct field from `MoveSpeed`'s |
   | 107 | writes `+0x94` | `SetMoveSpeedBase` | writes the same field slot 106 reads — consistent pair |
   | 108 | reads `+0x98`, scales by a constant | `GetWalkSpeed` | PS2's real body doesn't store its own value at all — it reads `GetMoveSpeed`'s own field (`+112`) and multiplies by a constant; PC does exactly the same derived read off the same field, not a separate one |
   | 109 | writes `+0x9C` | `SetWalkSpeed` | writes a field distinct from what `GetWalkSpeed` reads (`+0x98`) — PS2 has this exact asymmetry too (`SetWalkSpeed` writes `+116`, `GetWalkSpeed` reads `+112` and never reads `+116` back) |
   | 110 | returns the literal constant `0x74657374` | `GetEquip` | PS2's real body is *also* just `lui`/`ori` loading that exact same literal and returning it — both platforms shipped an identical hardcoded "test" placeholder (the ASCII bytes literally spell `"test"`); two unrelated functions returning the same arbitrary 4-byte debug constant by coincidence is not a realistic possibility |
   | 111 | `lea eax, [ecx+0x5FC]` | `GetPos` | trivial address-computation getter, matches PS2's `addiu v0, a0, 640` shape and this exact sequence position |
   | 112 | `lea eax, [ecx+0x61C]` | `GetDir` | same basis, immediately following `GetPos` on both platforms |

   **The boundary is real and checked, not assumed:** slots 113–118 were read in full and compared
   against the next six PS2 methods (`GetElem`, `GetElemLocal`, `GetEidMatrix`, `GetMinElemPos`,
   `GetMaxElemPos`, `GetModel`) — none matched. PS2's `GetElem` is a bare stub returning 0;
   `GetMinElemPos`/`GetMaxElemPos` are a genuine base-class bug, both computing the identical
   `this+16` offset. PC 113–118 are substantial functions with real FPU math and adjustor-thunk
   patterns, calling code already confirmed elsewhere in this project (`sub_100279B0`, the
   identity-matrix initializer from the skinning work) — nothing like PS2's trivial stubs. The band
   ends cleanly at 112; 113 onward needs its own fresh investigation, not a continued sweep.

   **Beyond the confirmed band, real complexity that limits how much further this specific
   technique can go — documented honestly rather than forced past it:**

   - **A cluster of confirmed PS2-side empty stubs** (`SetWaterHeight`, `AddTarget`, `SubTarget`,
     `ClearTarget` — each just a stack adjust and `jr $ra`, no other instructions at all) is
     genuinely unresolvable to individual PC slots by behavior: an empty stub has no behavior to
     match against. Multiple different empty PS2 methods sharing the same argument count are
     indistinguishable from each other and from PC's own empty stubs. Not a search failure — a
     real information-theoretic floor. `GetWaterHeight` and `GetFocal`, the two real (non-stub)
     methods in the same batch, were narrowed by exhaustive whole-table shape search to 4 and 3
     remaining unclaimed candidates respectively (down from 264), but not resolved further —
     documented as narrowed, not guessed to a specific slot.
   - **Heavy overloading turns out to affect a meaningful fraction of what's left — checked
     directly, and it's worse than just "harder": a whole six-method sub-cluster is confirmed
     unresolvable by behavior, at the same information-theoretic floor as the empty target-
     management stubs above.** `SetAttack` has two distinct signatures, `UseMagic` has two,
     `ReplaceAttack` and `ReplaceMagic` one each — six vtable slots in total on `XiActor` alone.
     All six are empty (`addiu $sp,-N / addiu $sp,+N / jr $ra`, nothing else) — not just
     same-signature, but byte-for-byte identical bodies modulo frame size. There is no behavioral
     signal left to distinguish any of them, from each other or from any other empty stub in the
     vtable. Confirmed closed, not left as a gap.
   - **The immediately neighbouring cluster breaks the emptiness pattern, and is a real next
     target — just a bigger one than anything resolved so far.** `SetModel`, `SetAction`,
     `KillAction`, and `IsMovingAction` are genuine, substantial functions (128–240-byte stack
     frames, 5–8 saved registers, real branching and virtual dispatch — `IsMovingAction` calls
     through its *parameter's* own vtable, not `this`). `SetMotion` and `IsMovingTechnic` in the
     same neighbourhood are empty, matching the surrounding pattern. Not searched for on the PC
     side — each of the four real candidates would need the same full-body treatment
     `GetEnglishName` got, not a quick shape check, given their size and complexity.
   - **A third, larger empty-stub cluster confirmed by a full survey of every remaining band**
     (slots 46–50, 66–72, 80–82, 95–99, 100–101 — the entire rest of the PS2 `XiActor` table not
     already covered above): of 19 methods checked, 12 are empty or fixed-constant stubs
     (`ExecHitCheck`, `IsTouchDown`, `IsOnLift` — **base versions only; the `XiCollisionActor` overrides
     are real and matched in §18.16** — `Append`, `ViewVolumeClip` — a hardcoded `1`,
     `GetNamePos`, `OnDrawName`, `OnChangeEquip`, `OcclusionClip`, `AmIUserControlTarget`,
     `AmIControlActor`, `GetArrowPos`), unresolvable for the same reason as the clusters above.
     **`ViewVolumeClip`/`OcclusionClip` specifically were briefly given a PC "shape candidate"
     (`0x100A9230`) in an earlier round; that's retracted (§18.13) — a 716-byte real function
     cannot be a one-line constant stub, and it was never applied as a name.** (`GetNamePos`/
     `GetArrowPos` are the exception in this list: PC implemented real, distinguishable logic
     where PS2 only stubbed it, giving an actual behavioral signal to match against — see §18.11's
     slots 158/159. That's a different situation from `ViewVolumeClip`/`OcclusionClip`, where
     nothing distinguishes one trivial PS2 stub from another.) The
     remaining 7 are real: `GetGroundHeight` (reads `+20`, same shape family as `GetWaterHeight`),
     `GetGroundNormal` (`this+16`, same family as `GetFocal`), `ActorFindResource` (both
     overloads), `ActorGetResourceCount`, `GetModelFile` (reads the same `+140` field as the
     already-confirmed `GetModel`, but calls a distinct sub-function on it — genuinely different
     behaviour, not a duplicate), `IsReadComplete`, and the matched pair
     `UnlinkCasterAttachments`/`UnlinkTargetAttachments`. **All 7 are now matched on the PC side**
     (§18.11, §18.13) — `GetGroundHeight`/`GetGroundNormal`/`ActorFindResource`(×2)/
     `ActorGetResourceCount`/`GetModelFile`/`IsReadComplete`, and
     `UnlinkCasterAttachments`/`UnlinkTargetAttachments` (§18.13),
     which also corrected the two of these that had been misnamed `FindCasterLink`/
     `FindTargetLink`.
   - **A dedicated search for the `IsControlLock`/`IsMotionLock`/`IsDirectionLock`/`IsConstrain`/
     `IsFreeRun`/`IsWalkLock`/`IsParallelMove`/`IsChocobo`/`IsFishingRod` cluster (slots 102–122,
     18 methods forming 9 clean `Is­Xxx()`/`IsXxx(override)` pairs) came back empty across three
     independent attempts** — a loose shape search, a re-check of an already-ruled-out region, and
     a tight single-bit-mask search. All three genuinely searched the whole 264-slot table, not a
     sub-range. This is either a real absence (PC represents these flags in a form none of the
     three searches covered) or a genuine limit of what this method can find — documented as a
     checked negative, not a gap left by insufficient effort.

   **Session-wide tally, the full PS2 `XiActor` vtable (123 slots) now completely surveyed band by
   band, not just partially sampled:** roughly 55 slots confirmed matched to a specific PC address
   with real evidence (slots 0–36 from the original sweep, `GetEnglishName`, the `AddRef`/`SubRef`/
   `AddSchRef`/`SubSchRef`/`AddLock`-`SubLock` cluster, and the 51–59 speed/equip/pos/dir band).
   Separately, roughly 25–30 PS2 slots across every band checked are now **confirmed empty or
   fixed-constant stubs** — a real, permanent category, not unresolved work, since there is no
   behaviour left to search for once a body is confirmed empty (`ViewVolumeClip`/`OcclusionClip`
   among them — confirmed into this bucket in §18.13, retracting an earlier stray "shape
   candidate" for the former). **Of the remainder listed here** — `GetPosHandle`/`ReleasePosHandle`,
   the six `GetElem`-family methods,
   `GetWaterHeight`/`GetFocal`/`GetGroundHeight`/`GetGroundNormal`, `ActorFindResource`/
   `ActorGetResourceCount`/`GetModelFile`/`IsReadComplete`/the `Unlink*Attachments` pair,
   `SetModel`/`SetAction`/`KillAction`/`IsMovingAction`, and the 18-method `IsXxx` cluster — all
   but four are now matched (§18.11) or closed as a checked negative (§18.13). What's still
   genuinely open: the real `GetFocal` (narrowed to 2 candidate slots, neither confirmed),
   `KillAction`, `IsMovingAction` (a prior claim about its calling convention was itself wrong —
   see §18.13 — so this needs fresh static work from the corrected shape, not a re-run of the old
   search), and the 18-method `IsXxx` cluster (three independent searches already came back
   empty; treated as a real floor, not re-attempted without a new technique). `SetAction` now has
   a Medium-confidence candidate (§18.13).

   That `0x74657374`/`GetEquip` row is worth calling out on its own: a coincidence wouldn't
   reproduce a write-only field with no matching read either (the `SetWalkSpeed` row above), and
   here a coincidence *really* wouldn't reproduce an identical arbitrary debug constant across two
   independently-compiled platforms. Confirms the earlier
   lesson precisely — positional continuation from slot 40 broke almost immediately, but a fresh,
   locally-anchored short run (here, re-anchored off the already-confirmed `AddSchRef`/
   `SubSchRef` pair) can still sweep cleanly when PS2's own method ordering survived porting
   intact for that particular cluster. Worth checking any other PS2 method cluster the same way
   before defaulting to one-by-one search.

   **`AddLock`/`SubLock` — now fully resolved (see §18.11): PC slot 92 is `AddLock`, slot 93 is `SubLock`, and PC fixed PS2's bug.** The text below is the earlier, partial state, kept for the record.

   **`AddLock`/`SubLock`, resolved as far as static analysis can take it.** PS2's own two bodies
   are byte-identical (both genuinely `+1` — confirmed by re-checking the addresses directly
   against the symbol table before trusting it, since the finding looked enough like a copy-paste
   mistake to be worth a second check; it isn't one, both real addresses disassemble the same way).
   Searched for the distinctive shape (dereference a field on `this` to reach a different object,
   then increment a 16-bit field on *that* object) across the **entire** 264-slot PC vtable, not
   just the unnamed range: exactly one match, `0x100833B0` (slot 92). Since PS2's two
   implementations are behaviorally identical, there is no way to determine from behavior alone
   which of the two names this PC slot corresponds to — documented as both. What remains
   genuinely open, and is a real gap rather than an oversight: PS2 has two distinct vtable slots
   for this; PC's vtable appears to have only one matching this shape anywhere. Either the second
   was consolidated away during porting (a legitimate simplification, given the two PS2 bodies do
   the same thing anyway), or it survives in a form this shape-search doesn't catch. Not resolved
   further — genuinely needs either a different search shape or is a real, permanent
   1-to-2 asymmetry between the platforms.

---

## 13. Open questions

Each remaining question is tagged with what it needs next. **Static** = answerable from the
binaries with existing tools; **Dynamic** = a live capture or debugger session.

Most of this section was answered by an independent cross-check against a separate,
large-scale C++ reconstruction project of this binary (four repos, `ffximain-main` plus three
companions; its own `ClassExtract` tool does automated vtable/constructor/destructor extraction
directly from the retail image). Its central, most consequential claim (the true 264-slot
`CXiSkeletonActor`/`XiSkeletonActor2` vtable) was independently re-verified directly against the
live IDB before accepting it (§6). Several detailed sub-claims (the "5 unnamed siblings" table's
constructor addresses, the `Pool_FreeSlot` correction) were also independently re-checked and
matched exactly. Not everything in it is taken uncritically: one of its own claims (`CMoD3mSpecularElem`'s
constructor address) was checked and found wrong by the same `-0xD0` banner-offset error it had
already identified and fixed in three other classes — a reminder that even a careful, largely
correct source needs its specific, falsifiable claims checked, not just its overall credibility.

### Still open

1. **`CAcc`'s embedded instances — closed (§18.10).** Both fill sites are confirmed.
   `CMoOcclusionMng`'s `CAcc` is filled by `0x1006C220`. For `CDx`, **the original claim was right —
   an intervening "not confirmed" finding was wrong**, and was accepted without a re-check, which
   it should not have been. The check looked for accesses at the `CAcc`
   *base* offsets (`+0x1BC`/`+0x1DC`), but `CAcc`'s fields sit at base `+4`/`+8`/`+0xC`, so the real
   writes are at `0x1C0`/`0x1C4`/`0x1C8` and `0x1E0`/`0x1E4`/`0x1E8`, both inside `App_InitScene`
   (`0x10010D20`, re-decompiled directly). The two remaining `CAcc`s (`+0x1AC`, `+0x1CC`) were
   swept across every instruction of all 13,511 functions (`[reg+0x1B0/0x1B4/0x1B8/0x1D0/0x1D4/0x1D8]`
   writes and `lea [reg+0x1AC/0x1CC]`): the only `CDx`-based access is the constructor's. They are
   constructed and never filled.
2. **Whether the confirmed race candidates are ever actually hit concurrently, at runtime.**
   Sharpened here relative to §11: the loader thread (`0x10245650`) turned out to hand
   off with main via a polling coroutine pattern, not a genuine race — but the async **file I/O
   worker thread** is a real, unmediated race with both main and the loader thread over
   `MeshResourceMng_ResolveTree`'s tree (`0x10073430`) and the shared evictor (`0x100740D0`), full
   chain confirmed end to end: Trigger-file loader (`0x10252F10`) → completion callback
   (`0x10253030`, runs on the worker thread) → `ResolveTree` → reference-take (`0x10071E90`). The
   `CMoProcessor` scratch pool's reachability from a second thread remains unconfirmed either way.
   What's still unproven for all of it is actual runtime overlap — whether a real play session ever
   lands a worker-thread tree build or eviction at the same moment as a main-thread one. *Dynamic
   only*: a single breakpoint on `0x10073430` logging thread ID would settle it directly. **Partial
   update (§16):** a real logging session confirmed `ResolveTree` genuinely fires during normal
   play (1,406 hits, real `ecx` values captured) — but every hit that session logged the same
   single thread ID, so the race itself remains neither confirmed nor refuted; the capture window
   likely just didn't include a zone transition, which is still the specific moment worth
   targeting next.
3. **Z-sort periods in shipped data — answered negatively for the supplied DATs (§18.18).** None of the
   12 model DATs contains `dancer` shape data, and no `RES_TYPE` is a `dancer` model format. Original
   note follows. The encoding is fully known (period = a 4-bit field in
   `.dmb`-format updater data, `0` = never, `1` = every update; §8) — only the actual shipped
   values remain unconfirmed. **Correction (2026-09-26):** "`.dmb`" is the middleware's own
   internal format name (confirmed via the `sqmdDMBTextureSave` function name, §"sqRend"), not a
   standalone file extension FFXI ships. On disk this data lives inside FFXI's generically-named,
   numbered `.DAT` files under `ROM/`, the way all FFXI client assets do — there is no file
   picker by content type, so getting real values means the user supplying specific model DATs
   (any monster/NPC/player model DAT with animated geometry) for the tool-side `.dmb` chunk
   inside them to be parsed directly. *Data or Dynamic.*
4. **The ~110 `CXiSkeletonActor` slots outside the already-named ones — full pairwise sweep
   completed across the whole `CXiActor`→`CXiAtelActor`→`CXiControlActor`→
   `CXiCollisionActor`→`CXiSkeletonActor` chain, not just this one class in isolation. Moved to
   its own section (§12c) given the size of what that produced — confirmed PS2 matches, a large
   batch of self-authored names for genuinely PC-only content, and an honest accounting of what's
   still unresolved (a handful of narrowed-but-unpicked getter candidates, and roughly a dozen
   real functions whose purpose wasn't determinable from static shape alone). *Static* for the
   remaining unnamed placeholders; likely needs *Dynamic* analysis to go further, since multiple
   independent static techniques (shape search, field co-reference, caller-tracing) were tried
   and exhausted on the hardest remaining cases.
5. **Scanner re-run — done, confirmed unchanged.** Full imm32 support (ADD form, stack-`this` COM
   form) was implemented and actually re-run against the unpacked DLL: **136
   classes**, matching the pre-imm32 baseline exactly — the improved thunk recognition didn't
   change the top-level count. Closed.
6. **`CYySkl`'s per-bone record layout past the parent index — closed, but with a different
   answer than the question assumed.** There is no separate scratch-array-filling function to
   find: the pose composer at `0x100343C0` was already the whole answer, just not traced far
   enough. Confirmed directly — its real body is one continuous 100-instruction function (checked
   by disassembling from the confirmed start and verifying it reaches the previously-unexplained
   code on a clean instruction boundary, not a separate function starting nearby).

   **What that full body actually shows:** the 30-byte raw record's remaining 29 bytes are never
   read at all. The composer reads only byte 0 (the parent index, matching what was already
   known) from each 30-byte record, then advances by exactly 30 bytes (`add eax, 0x1E`, confirming
   the already-known stride) to the next record — nothing else in the record is ever touched. The
   real per-bone transform data comes from a wholly different array, 64-byte stride
   (`add edi, 0x40`), based at a separate global (`0x1045EC20`) — not from the 30-byte records at
   all. Each bone's scratch-array entry (`0x1045F064`, confirmed 52-byte stride via
   `add ebx, 0x34`) is built by four real helper calls per bone, all taking pointers into that
   64-byte array as their real data source:
   - `0x10027B30` and `0x10027CF0` — straightforward copies into specific scratch-entry offsets
     (`+0x1C`, `+0x10`).
   - `0x10032FA0` — thiscall convention (`ecx` = the scratch entry itself).
   - `0x10027D10` — the richest of the four, taking *both* the current bone's and its parent's
     64-byte-array entries. Disassembled directly and confirmed to be a real 4×4-matrix-shaped
     multiply-accumulate (a `0`–`4` loop of `fmul`/`faddp` pairs reading from both input
     pointers) — i.e., composing the current bone's transform relative to its parent, exactly the
     operation a pose composer needs.

   A real, separately-tracked mechanism sits before the main loop: a lookup table at
   `0x1045EC28` marks specific bone indices as "already handled" (written to `1`) via an
   override-list walk over a caller-supplied array, and the main per-bone loop skips the whole
   four-call composition step for any bone already marked — an explicit override/exception path
   for specific bones, layered on top of the normal parent-chain composition.

   **The 64-byte array's own filler, found and confirmed in a follow-up pass — closing the one
   piece left open above.** Of 38 raw references to the array's base address, most cluster inside
   the pose composer's own body (further reads, not fills); one stood apart, a small wrapper at
   `0x1002A394` that computes `array_base + index*64` (the confirmed stride) and tail-jumps into
   `0x10027AE0`. That target is the real initializer: it zeroes twelve of the sixteen dwords in the
   64-byte record, then scatters four dwords from a compact 16-byte source parameter into the
   remaining four slots (`+0`, `+0x14`, `+0x28`, `+0x3C`) — evenly spaced by 20 bytes, not a
   standard 16-byte matrix-row stride, so the exact structural meaning of that spacing (diagonal of
   some non-standard layout, or four independent scalar channels) wasn't determined here.
   What *is* confirmed: every bone's 64-byte entry starts as mostly-zeroed, with exactly four real
   values written in from outside — the compact source `0x10027AE0` reads from is the genuine
   origin of each bone's actual pose data, one level further back than anything traced before this
   pass.

   **What remains genuinely open, correctly re-scoped:** where the 64-byte array
   (`0x1045EC20`) itself gets filled — that's a real, separate function, not located here —
   and what the 29 unread bytes of each 30-byte raw record are actually *for*, since the pose
   composer confirmed doesn't use them at all; they may serve a different purpose entirely (setup,
   binding, or another system not yet identified) rather than being "the answer one level removed"
   as originally framed. **Update: the compact 16-byte source feeding the array's own initializer
   has since been decoded from real captured runtime data — see §16 — as a per-bone uniform scale
   value.** That closes the "what does the source actually contain" question.
   **Superseded (§17, §18.7):** the "29 unread bytes" finding was wrong — rotation and translation
   are read by `sub_10034620`, one stage before the composer; only byte `+0x01` is unexplained. The
   filler is `0x10027AE0` (a scale-matrix builder), called from `PerActor_FourBucketStaggeredUpdate`.

### Implication for the disintegrate fix

The PC's `CXiSkeletonActor` disintegration methods (vtable slots 33–37) are empty stubs (§6). A
working effect needs real implementations of those methods and of the triangle capture they drive
(PS2: `StartDisintegration` … `DisintegrateAll`, `GetDisintegratedTriList`,
`DisintegrateDraw(KzObjectDrawInfo&)`), not only a re-routed opcode. **Correction to an earlier
pass here:** the claim that four of the seven `XiSkeletonActor` disintegration functions are
trivial stubs on PS2 is wrong as stated — re-disassembled and confirmed directly.
`EndDisintegration__15XiSkeletonActorFv` (196 bytes) is real, substantial cleanup logic (checks
the `+0x8` effect-flag bit, calls `YmGenerater::SubRef`, frees the vertex list, calls
`DisintegratedInfo::DeleteList`), and both `GetDisintegratedTriList`/`GetDisintegrateVtxList` (76
bytes each) are real one-shot "take" accessors, not stubs — all independently disassembled and
matched against real PS2 symbol names. What *is* trivial is `XiActor`'s own base-class
declarations of these same seven names (16–20 bytes each, genuine no-ops/return-null defaults) —
`XiSkeletonActor` overrides all seven, and it's those overrides that matter for the actual effect.
The two symbol tables sitting side by side (`DisintegrateByBBX__7XiActorFPfPf` vs.
`DisintegrateByBBX__15XiSkeletonActorFPfPf`, etc.) made this an easy mix-up; `DisintegrateAll` is
the one case where both the base default *and* `XiSkeletonActor`'s own override are genuinely
empty (confirmed by disassembling both). Only `StartDisintegration`, `DisintegrateByBBX` and
`DisintegrateByBSP` contain real logic. **Confirmed by disassembling their actual PS2 bytes with a
purpose-built R5900 decoder** (standard MIPS disassemblers misdecode this CPU's `LQ`/`SQ` opcodes
as an unrelated standard-MIPS instruction — confirmed directly: capstone reads `sq $s0, 0($sp)` as
`ext $s0, $sp, 0, 1`, a plausible-looking wrong answer, not an error).
**The real per-frame consumer is now fully traced, end to end, overturning the original framing.**
There is no separate `YmGenerater::Step`-equivalent scanning the queue independently. Every link
below is confirmed by exhaustive `jal`-caller scanning of the whole PS2 image (not inferred from
naming), not by assumption:

1. `DisintegrateByBBX`/`DisintegrateByBSP` queue a `DisintegrationReq` via
   `DisintegratedInfo::AddReq`.
2. **Capture happens synchronously inside the actor's own draw call**, not on a separate schedule:
   `XiSkeletonActor::DisintegrateDraw` (`KzObjectDrawInfo&`) calls `KzObject::Capture` →
   `KzOSM::Capture` → `KzOSM::CaptureDisplayList`, which walks the display list and calls
   `KzOSM::Disintegrate` — confirmed to have **exactly two call sites in the whole binary, both
   inside `CaptureDisplayList`** — consuming the queued requests and producing a
   `DisintegratedTriList`.
3. **`KzOSM::Disintegrate` itself is now fully decoded** (1,228 bytes, 307 instructions, full
   opcode coverage including PS2's MMI byte-pack instructions and FPU compares — zero
   undecoded instructions). Real, checkable algorithm, not inferred from the name:
   - Walks the source mesh's vertices/normals/UVs three at a time (one triangle), buffering each
     triangle's data into local scratch space via `sceVu0CopyVector`.
   - `DisintegratedInfo::ReadFlag`/`SetFlag` give each source triangle a persistent "already
     decided" bit, keyed by a running triangle count — so a triangle already added (or already
     rejected) on an earlier call is never re-evaluated, even though `Disintegrate` itself can run
     across many calls as new `DisintegrationReq`s arrive.
   - For each **not-yet-decided** triangle, walks the request queue (`info->req[]`) and dispatches
     on each request's `type`: **BBX** transforms the triangle's 3 vertices through the caller-
     supplied matrix and tests each against the request's local-space min/max box on all 3 axes
     (paired `c.lt.s`/`c.le.s` FPU compares); **BSP** calls `KO_VectorLen` against each vertex and
     compares the result to the request's own threshold field. A triangle is accepted the instant
     **any one of its 3 vertices** satisfies **any one** queued request — first match wins, and the
     match state persists across the whole request-queue walk for that triangle (not reset per
     request).
   - Accepted triangles get written into the output `DisintegratedTriList` as: the triangle's
     centroid (`sceVu0AddVector` ×2 + `sceVu0ScaleVector` by 1/3), each vertex stored **relative to
     that centroid** (`sceVu0SubVector` ×3 — i.e. the list stores shape-around-centroid, not raw
     positions, which is exactly what a physics-driven "fly apart from the center" disintegration
     visual needs), the three source vertex indices, an optional texture-resource lookup
     (`GetTexRes`, skipped when the caller passes `-1`), and a packed colour/normal block built with
     PS2's `ppach`/`ppacb` MMI instructions (byte-packing SIMD ops — quantizing per-vertex
     colour/normal data down for storage, not decoded to the individual-channel level here).
   - A trailing mode parameter (one of the function's two true stack arguments) selects how the
     3-vertex accumulator behaves after each triangle: discard-and-restart (mode `3`), or a
     **rolling 2-vertex carryover** (mode `4` — shifts the last two buffered vertices down and
     only needs one new vertex next time), which is the standard trick for consuming a triangle
     *strip* rather than an independent triangle list. Any other mode value falls through without
     resetting the accumulator at all — a real code path, not obviously exercised by any confirmed
     caller.
4. **Rendering the result is a separate function again**: `YmDisgregaterProgElem::OnDraw` (a
   generic per-element draw, run through the normal `Ym`-element dispatch, not disintegration-
   specific) checks a captured-list flag at `+0x100`. If set, it fetches the element's reference
   matrix, colour and Z-offset and draws the real captured list via `KO_DrawVuTriParticle`. If not
   yet set, it looks up a fallback resource by a 4-character tag and type `14`, and draws *that*
   instead via a related particle-draw function (`ShapeAnm::DrawVuParticle`) — so an actor mid-
   disintegration with no captured data yet still shows a generic effect rather than nothing.
   `YmDisgregaterProgElem::OnMove` itself does no disintegration-specific work — confirmed by
   direct disassembly, it's an 8-instruction pure forward to `YmElem::VuOnMove`, the same generic
   per-frame VU update every `Ym` element gets.

The PC side has no equivalent of any of this — its five `void` disintegration methods are empty
stubs and its two list getters are gone (above), so a working PC fix needs to build this whole
four-stage pipeline (queue → synchronous per-triangle capture with box/plane testing inside the
actor's draw call → centroid-relative output record → separate draw-time render with a fallback
path), not just re-route the opcode into real bodies.

**`KzOSM::CaptureDisplayList` is now decoded (3,064 bytes, 766 instructions, full opcode
coverage — extended the R5900 decoder again for PS2's `LQC2`/`SQC2` VU0-register loads/stores,
`CVT.S.W`, `BREAK`, and the 64-bit `DSLL`/`DSRL`/`DSRA` shifts, none of which appeared in the
smaller functions decoded earlier).** It is not a simple display-list walk — its own `jal` targets
are real PS2 hardware calls: `sceGsSyncPath` (GS DMA sync), `KzKickSourceChannel`/`KzSetMFIFO`/
`KzFreeMFIFO` (DMA channel management), `MakeGifPacket` (builds a GS GIF-tag packet), plus the
skinning functions `CaptureLoadBlendMatrix`/`CaptureBlendVertex` (both `KzOSM` methods, tying
directly into this document's own §6 skinning pipeline). This is the real per-mesh
"skin the vertices, then submit them to the Graphics Synthesizer" function; disintegration is one
path through it, not its whole purpose.

`Disintegrate` is called from exactly two sites in this function, confirmed structurally
near-identical: same `this` (the `KzOSM` object — both are `KzOSM` methods, a same-object sibling
call, not a call through some other object), the same `info`/`triList`/`count`/`flagArray`
arguments, and the same two true stack arguments (a 3-bit mode field extracted from a 64-bit flags
value — matching the confirmed mode-`3`-vs-mode-`4` accumulator behaviour inside `Disintegrate`
itself — and a texture-lookup index). The **only** difference between the two call sites is which
of two adjacent 16-byte-stride slots supplies the `qwData` argument — consistent with processing
two vertices per iteration rather than any different disintegration behaviour between the two
calls.

**Why this doesn't unlock a complete PC port, and it's a structural reason, not a time-box:**
checked directly — PC's renamed `KzOSM` (`CYyOsmTaskXform`, confirmed via the RTTI descriptor
scan; PS2's `Kz*` prefix already known to become PC's `CYy*`) has a **9-slot vtable**. `Disintegrate`/
`Capture`/`CaptureDisplayList` are not virtual on PS2 either (they're plain `KzOSM` member
functions, never appearing in `__vt__5KzOSM`), so there is no vtable slot to search for a PC stub
the way the `CXiSkeletonActor` disintegration methods were found — finding PC equivalents, if they
exist at all, needs a structural pattern search through PC `.text` for similarly-shaped code, not
anything this project's vtable-based tooling can locate directly. More fundamentally: PS2's actual
submission mechanics here (`sceGsSyncPath`, `MakeGifPacket`, the MFIFO DMA calls) are calls into
the PS2 Graphics Synthesizer hardware, which has no Direct3D 8 analog to port to — this project has
already confirmed the PC client is D3D8 throughout (§4). Whatever PC actually does to submit a
mesh for rendering is necessarily different, native D3D8 code, sitting somewhere else entirely and
not yet located. `Disintegrate`'s own algorithm (the per-triangle selection and centroid-relative
output format) has no such dependency — it's ordinary CPU-side math and data-structure work — and
is the part actually reimplemented on the PC side (see below); the GS/DMA submission code around it
is not, and cannot be, ported as-is.

Not yet decoded: `KzObject::Capture`/`YmDisgregaterProgElem::OnDraw` (888 and 396 bytes) — "how it
gets called" rather than "what it does," lower priority for a PC reimplementation but needed for a
complete picture.

**Found in the reconstruction's own source, not invented: real PC replacements for two of the
three math dependencies `ProcessTriangle` needs.** Searched across all four related repos, not
just this one:

- **World matrix:** PC does not read a per-actor stored matrix through a method call at all (no
  `GetWorldMatrix`-named or plausibly-equivalent function exists anywhere in this repo, confirmed
  by a repo-wide grep). It reads the *current* object's world matrix out of a single global
  rendering-context singleton instead — `SqgxContext` (already documented, §4/§9), at the live
  address held in `dword_109696D8`, field `matObj` (confirmed offset `+0x1C8`, real struct in
  `include/core/SqgxContext.h`). Confirmed by real, existing code in this same repo
  (`core_generated_p17.cpp`) reading exactly this field for its own inverse-world-matrix need
  during lighting setup — not a guess, a second real consumer of the same field for a related
  purpose.
- **Matrix inverse:** `sub_1027EAB0` — a complete, real, already-reconstructed 4×4 inverse
  (determinant check, full cofactor expansion) in `src/core/sub_1027EAB0.cpp`, confirmed used for
  precisely this world-matrix-inversion purpose by that same lighting code.
- **Point-by-matrix transform:** no dedicated function exists under any name (checked
  `TransformCoord`, `Vec3Transform`, `TransformPoint`, `Vector3TransformFpu`, and a structural
  grep for the argument shape). What is real and confirmed is `Matrix4x4MultiplyFpu`'s own
  calling convention — read directly from its actual body, term by term, against a standard
  `(A×B)[0][0]` expansion: row-major storage, row-vector-on-the-left. Applying that same,
  confirmed convention to a single point is not a new invention, since the convention itself
  isn't a free choice once it's fixed by real, existing code — it's the only value the operation
  can produce.
- **Two-point distance** (PS2's `KO_VectorLen`, undecoded here): PC has a real, single-
  vector magnitude function with SHA256-tracked provenance to specific retail addresses across
  three backend variants (scalar/SSE/AMD-packed) — `TransformVectorLength`,
  `src/core/TransformVectorMath.cpp`. Composed with a plain subtraction to get a two-point
  distance, since that's what any such function has to do internally regardless of how PS2's own
  body was written.
- **Still genuinely unresolved:** what PC substitutes for `StartDisintegration`'s dropped
  `YmGeneraterRes*` parameter. No confirmed PC call site exists to observe (the function appears
  to have zero live callers in the shipped binary), and nothing structurally resembling a PC
  effect-generator resource type turned up in any of the four repos searched. This turns out not
  to block the selection algorithm itself, though: `DisintegratedInfo::gen` is read by nothing in
  `ProcessTriangle` — it's a pure resource-lifecycle field (`AddRef`/`SubRef`/`DeleteList`), so a
  PC port can legitimately leave it null and skip that bookkeeping without affecting whether
  triangles get selected correctly.
- **One caveat worth being direct about, not glossing over:** the derived PC offsets for the
  effect-flags/`disintegratedInfo` fields (`+0x734`/`+0x754`) are arithmetic from the confirmed
  `ef_param` base, not measured directly against real PC bytes — and a direct neighbour,
  `+0x750`, is already a *different*, independently confirmed field (`SetEmapTexture`). That
  doesn't necessarily mean a collision, but it means these two specific offsets sit in real,
  occupied territory and are the one part of this whole update that still needs checking against
  actual PC bytes before being trusted, the same discipline applied to everything else here.



- The unopened `sqBase` files, `sqmdModel`'s per-category accessors, and `XiEvents`'
  `Event VM Functions.md` / `Event DAT Structures.md` — see §15.

### Resolved

| Former question | Answer | Where |
|---|---|---|
| `CYySkl` record byte `+0x01` | `flip` (mirror bone index) by PS2 layout; PS2 uses it only for cloth; the PC pose pipeline never reads it | §17, §18.7 |
| `CDx`'s embedded `CAcc` fill sites | Filled in `App_InitScene` at `+0x1C0..+0x1C8` and `+0x1E0..+0x1E8`; `+0x1AC`/`+0x1CC` never filled. Last round's "not confirmed" was a base-vs-field offset mistake | §13 #1 |
| Texture upload path | `TexRes_LoadBm2` → `TexMgr_UploadPump` (≤20/frame in-game) → `TexObj_Create` (runtime DXT1/DXT3 per registry 0018/0019) → `TexObj_Upload` (staging + D3DX) | §18.9 |
| Post-processing | Exists: afterimage, flash, zoom-feedback, background→window upscale, UI composite, fade; a depth-gated distance blur is compiled in but dead | §18.10 |
| Particle rendering | No separate renderer or point sprites: `CMoElem` slot 18, `CMoOtTask` slot 11, the scheduler interpreter, and `dancer` | §18.11 |
| `AddLock`/`SubLock` one-slot asymmetry | PC slot 93 is `SubLock` (with a lock-count warning); PC fixed PS2's bug | §18.11 |
| `GetPosHandle`, `GetElem` family, `GetModel`/`GetModelFile`, `IsReadComplete`, `ActorFindResource` ×2, `ActorGetResourceCount` | Matched to PC slots 94–95, 113–124 | §18.11 |
| `CYySkl`'s `+8`/`+0x14` buffer contents | Skeleton resource handle, bone-matrix array, per-bone byte table; a real setter exists (`CYyModelBase::Init`) | §6 |
| `CYyModelDt_PrepareRenderState`'s third parameter | The model's own `CYyModel*`, via a fully-traced dispatch chain | §6 |
| `CAcc`'s `+4`/`+0xC` COM pointers | A render-target texture and a depth-stencil surface; `+8` confirmed always null at both fill sites | §4 |
| `CXiSkeletonActor` slots 41–226's class ownership | All inherited from `CXiActor` itself, not `CXiSkeletonActor` additions | §6 |
| The true `CXiSkeletonActor`/`XiSkeletonActor2` vtable size | 264 slots each, two separate tables, not one shared 153-slot table | §6 |
| Constructor tracing for the `shared`-accessor classes | Complete: 8 descriptors across 113 tables, every one with a proven installing site | §2 |
| `CMoProcessor` region `+0x000`–`+0xA94` | Vtable, 32-matrix scratch pool, free list, stack-top counter; three allocation tiers | §3 |
| imm32 thunk support in the scanner | Implemented for the four `CXiDollActor` thunks; a fifth family and twelve more remain (see Still open) | §13 #5 |
| Actor-family constructors | Vtables for 8 actor classes; `CXiSkeletonActor` constructors confirmed via `XiSkeletonActor2` wrappers | §2 |
| What gates the four-bucket balancers | Per-actor work in `sub_100CBDE0`, run when counter mod 4 = bucket | §6 |
| Names of `CXiSkeletonActor` slots 0–40 | From the PS2 vtable; includes the five stubbed disintegration methods | §6 |
| PC fields `+0x660`–`+0x66C`, `+0x730`–`+0x750` | `color`, `alpha`, `mtex_alpha`, `shadow_alpha`, effect flags and parameters | §6 |
| `KzObjectDrawInfo` as the PrepareRenderState parameter | Ruled out (size and layout) | §6 |
| PS2 `dancer` layouts vs. PC reconstructions | Match (`sqObject` header, `sqskSkeleton`, joint, node, connector) | §8 |
| Usability of the BinDiff results | Not usable for name transfer: 0/24 on verified pairs | §12 |
| `CXiSkeletonActorRes+0x34` setter | Async load-task constructor `sub_100D7020`, created in `sub_100D4330` | §6 |
| Use of `actor+0x59C` | Opacity, faded per frame in slot 8 (PS2 name unknown; not `alpha_base`) | §6 |
| `Pool_FreeSlot`'s real address | `0x1004E3F0`, not `0x1004E3F9` (a stale address 9 bytes into the same function) | §3 |
| `CAcc2`'s real pointer count | Six COM pointers (`sizeof 0x1C`), not four | §4 |
| Scanner imm32 support | Both remaining forms (ADD, stack-`this`) implemented and tested; full re-run pending | §13 #5 |
| `CYyModelBase`/`CYyModelDt` relationship | Siblings, both deriving from `CYyObject` — not parent/child | §6 |

## 14. Not part of this project's scope (confirmed real, but excluded)

- **Chocobo Racing subsystem** (`chocoborace_get_resultparam`/`_sectionparam`/`_chocoboparam`/
  `_raceparam`) — FFXI's real minigame, unrelated to rendering/animation.
- **`g_pStAvatarCoordinator`'s other 17 vtable slots** beyond the confirmed state-handler —
  broader game-bootstrap role, not graphics-pipeline.
- **`C:\dev\dancer\tools\mdlview\`** — a real internal preview tool (`mdlAdd`, `mdlRegister`,
  `mdlChannelAdd`, `mdlChannelLinkToCamera`, `chasmPreallocate`, `chasmNodeAdd`, `chasmLinkAdd`
  with `bodyBlend`/`headBlend`), confirmed tool-side only, not part of the shipped runtime path.
- **`_sqFree`** (`sub_102760F0`) — a confirmed, named custom allocator with debug-heap poisoning
  (double-free/use-after-free detection). Real and reusable as a lead for auditing memory
  lifetime elsewhere, but not itself a graphics-pipeline finding.

---

## 15. Survey backlog results

### `sqBase` on PC — file-to-function map

Twelve `sqBase` source files exist on PC (three more than previously listed: `sqUtil`, `sqMatrix3`,
`sqVtx`). One raw sweep for all twelve path strings locates the functions in each file that pass
a file/line pair (allocations and assertions), so each list is a lower bound for that file. The
files are laid out in link order across `0x10275000`–`0x102B4000`:

| File | Functions referencing it |
|---|---|
| `sqTimer.c` | `sub_10275090` |
| `sqQuat.c` | `sub_1027AFB0` |
| `sqMatrix4.c` | `sub_1027F0E0`, `sub_10280780`, one unmapped (`0x1027FBB5`) |
| `sqObject.c` | `sub_10285740`, `sub_10285780`, one unmapped |
| `sqError.c` | one unmapped (`0x1028591E`) |
| `sqUtil.c` | `sub_1028A360`, `sub_1028A5E0` (24 references; frequent allocator callers) |
| `sqIO.c` | `sub_10292130`, `sub_102921E0`, `sub_10292300`, `sub_10292400` |
| `sqMatrix3.c` | `sub_10296DC0`, one unmapped |
| `sqSQO.c` | `sub_1029CAE0`, `sub_1029CBE0`, `sub_1029CD40`, `sub_1029CE40` |
| `sqArray.c` | eight functions, `0x102A37E0`–`0x102A3D20` |
| `sqVtx.c` | nine functions, `0x102A9520`–`0x102A9FB0` |
| `sqStructArray.c` | five functions, `0x102B3990`–`0x102B3B80` |

The PS2 build has no standalone matrix, quaternion, I/O, error or struct-array functions (only
conversions such as `sqmoFloatsToQuat`), consistent with PS2 math going through the SDK's VU0
library. `sqArray` on PS2: `sqArrayAdd`, `Create`, `Destroy`, `Fini`, `Grow`; `sqObject`:
`sqObjectDestroy`, `Print`, `Validate`. On PS2, `sq` is Square's general library prefix: the build
also contains networking and PlayOnline families (`sqPlay`, `sqPolcon`, `sqMail`, `sqIrc`,
`sqAtok`, …).

### `sqmdModel` API (from PS2 symbols)

22 functions: `sqmdModelNew`, `Init`, `Fini`, `Destroy`, `Validate`, `Print`; loading —
`Read`, `ReadBinary`, `ReadMOD`, `ReadSQO`; visibility — `Show`, `Hide`, `ShowShadows`,
`HideShadows`; scene placement — `LinkToLayer`, `LinkShapeToLayer`, `SetLayerSort`,
`AddIllumLight`, `AddShadowLightInLayer`, `LookAt`; per frame — `Update`, `PathVariation`. The
struct layout is in §8.

### `XiEvents` event VM documentation

`Event VM Functions.md` gives byte signatures for the event VM (from a Feb-2022 client). Two
checked against this build match exactly once, at function starts: **`XiEvent::ExecProg` (the
opcode dispatcher) = `sub_100BC280`** and **`XiEvent::EventIdle` (per-tick scheduler) =
`sub_100BCD10`**. The document also covers `EventStartWait`, `InitEvent2`,
`XiAtelBuff::EventNew`, the `XiEvent` constructor/destructor/`XiEventInit`, byte-code readers
(`eventgetcode`/`eventgetcode2`), the work-variable accessors (`getworkofs`/`setworkofs` and the
string variants, including the `Work_Zone`, `Work_Zone_Memorize` and `Work_Zone_1700` global
arrays), `GetActorIndex`, `GetReqLevel`, `GetReqStatus`, `ReqSet`, and `lookatone`, each with a
signature for locating it. `Event DAT Structures.md` did not surface in search and was not read.

---

## 16. First real dynamic-analysis session — confirmed findings against the live client

An inline-hook logging DLL (built and unit-tested per the project's dynamic-analysis tooling) was
injected into a live, running game session and captured real runtime data across a substantial,
uninterrupted play session (96,000+ log lines, clean ending, no crash). This is the project's
first genuine dynamic confirmation of anything — everything below is real behavior, not inferred
from static bytes.

**Headline result: inline hooking does not trigger whatever crashed the game during the earlier
x64dbg software-breakpoint attempt.** All eight hooks installed and ran for the whole session with
no instability. This is real, standalone evidence that the client's crash-on-modification behavior
(whatever it is) is specific to the `0xCC` software-breakpoint byte, not a blanket reaction to any
code modification in these regions — narrowing, not closing, the open question from the earlier
race-condition/tamper-detection work.

**`CYySkl`'s compact 16-byte pose source, decoded — resolves the one piece question #6 left open.**
Every captured hit shows the same shape: three identical floats followed by a constant `1.0`,
drifting smoothly across a narrow band (0.92–1.05) between consecutive calls — e.g.
`(1.0,1.0,1.0,1.0)` → `(1.05,1.05,1.05,1.0)` → `(0.95,0.95,0.95,1.0)` → `(0.92,0.92,0.92,1.0)` →
`(0.97,0.97,0.97,1.0)`, decoded precisely from the raw bytes, not estimated. This is a **uniform scale value** `(s, s, s, 1)`. *Corrected in §18:* an earlier reading here called
it a smooth "breathing" drift on one bone. It isn't — the values form a small discrete, repeating
set (`0.92, 0.95, 0.97, 1.0, 1.05`), and both logged return addresses resolve to
`call 0x10027AE0` inside `PerActor_FourBucketStaggeredUpdate` (`0x100CBDE0`), i.e. one call per
actor/bone processed in the staggered update. Per-entity fixed scale factors fit the data; an
animation does not. `sourcePtr` was identical (`001AEA60`) across all 20 captured
hits, meaning this reads from one consistent scratch location, overwritten each call.

**The user confirmed three distinct zone transitions and multiple separate in/out-of-water trips
during this same session — the log's real, gap-aware structure (not first/last-line bounds, which
turned out to hide the true shape) confirms this cleanly:**

- **`Candidate_132`**: active from the first hit to the last, no gaps. 55,868 hits.
- **`Candidate_129`/`136`**: fire only together, tightly alternating, and — checked properly for
  gaps rather than just outer bounds — appear in **six separate windows** scattered through the
  session (e.g. lines 510–529, 3079–13108, 15073–15115, 16758–19423, 40835–40888,
  50498–50605), each one silent in between. Six independent entries into the same paired behavior
  is stronger evidence for a water-entry/exit signature than a single window would have been —
  this isn't one coincidental block, it's the same pattern repeating on its own six times,
  matching "in and out of water multiple times" directly.
- **`Candidate_246`**: many short bursts early (13 distinct windows in the first ~20,000 lines),
  then one continuous 74,000-line stretch from line 21818 to the session's end. Read together with
  the confirmed three-zone session, this fits one zone having sustained rough/hilly terrain
  throughout, versus earlier zone(s) with only occasional uneven patches — a rougher zone should
  produce exactly this sustained-vs-sporadic contrast.
- **`Candidate_153`**: zero hits, in any window, across the whole session.
- **`ResolveTree`**: 22 separate bursts spread across the *entire* session (line 25 to line 91280),
  not one localized cluster — consistent with real, repeated activity across all three zone
  visits, not a single load-then-idle event.

**A correction to the earlier read, worth stating plainly:** `ResolveTree`'s `ecx` staying at one
value (`28C316C0`) across all 1,406 hits does not mean no zone changes happened, as earlier framed
— it more likely means a single, persistent resource-manager object handles tree resolution across
every zone, not a fresh manager per zone. A constant `ecx` is fully compatible with three real
zone transitions; the earlier inference that it argued against them was wrong.

**With that correction, the race-condition negative result is more substantial than first
reported, not less.** Real zone activity is now confirmed (22 bursts across three transitions),
`ResolveTree` fired 1,406 times spread across that activity, and every single hit — no exceptions
— still shows the same thread ID (3528). That's no longer "one session happened not to catch it";
it's three real zone loads and over a thousand calls to the exact function this project's static
analysis found a confirmed, unmediated race in, with zero appearances of the second thread. The
most honest reading isn't "the race doesn't exist" — the full call chain to the async file-I/O
worker thread is still real and confirmed in the binary — but it now looks more likely that
*ordinary* zone travel doesn't route through that specific async path at all, and the race is
reserved for some narrower or rarer resource-load scenario (the Trigger-file loader mechanism
this project traced earlier may be triggered by something more specific than routine zoning, not
routine zoning itself). That's a real, if different, answer than "unconfirmed" — worth treating as
a meaningfully narrowed question, not a settled one.

---

## 17. `sub_10034620` — reads every bone's rotation and translation (corrected)

*This section originally claimed `sub_10034620` and the pose composer read two different arrays,
and that the parallel document's layout attribution was therefore wrong. That claim was itself
wrong and is retracted.* Both functions index the **same** shared skeleton, loaded from global
`0x1045EC24`: the composer's record pointer is `[0x1045EC24] + 0x52` with its loop starting at
bone 1, and `0x34 + 1×0x1E = 0x52`. The parallel document's layout is correct:

| Record offset (from `skeleton+0x34`, stride `0x1E`) | Contents | Read by |
|---|---|---|
| `+0x00` | parent bone index (byte) | composer `0x100343C0` |
| `+0x01` | `flip` (mirror-counterpart bone index) — by PS2 layout; unused by the PC pose pipeline | none of the 10 code sites that load the skeleton global (all read, §18.7) |
| `+0x02`–`+0x11` | rotation quaternion (4 floats) | `sub_10034620` |
| `+0x12`–`+0x1D` | translation (3 floats) | `sub_10034620` |

Bone count is the word at `skeleton+0x32`. `sub_10034620` loops over **all** bones (not only bone 0,
as first read), writing rotation and accumulated translation into the 52-byte scratch array
(`0x1045F030`, one entry per bone). Only the root bone additionally gets a fixed `3π/2`
(`0x4096CBE4` = 4.712389) rotational correction — an axis-convention fix at the skeleton root.

Consequently the earlier "29 of 30 record bytes are never read" finding (§13 #6) was also wrong:
the composer reads only the parent byte *itself*, but the rotation and translation are consumed one
stage earlier by `sub_10034620`. Byte `+0x01` is now accounted for too (§18.7): all 10 code sites that load the skeleton global were read and none touch it; PS2's `KzSkeleton` record has `parent` at `+0xE` and `flip` at `+0xF` (adjacent, exactly like PC `+0x00`/`+0x01`; `KzSKD::GetParentNo`/`GetFlipNo` read `skl[i]+0x2E`/`+0x2F`), and PS2's only consumer of `flip` is `KzCloth::SetupActiveFlg` (cloth simulation), not pose composition. PC dropped PS2's `flipaxis` byte (1+1+16+12 = 30). The full pipeline is in §18.

---

## 18. The PC graphics pipeline, end to end

Mapped from real disassembly, anchored on the one confirmed `d3d8.dll` import. Every
address below was read directly; interface methods were identified against the documented
`IDirect3D8`/`IDirect3DDevice8`/`IDirect3DTexture8` vtable layouts and cross-checked against real
call arguments (e.g. `SetRenderState(0x1C, 0)` = fog off, `(0x89, 0)` = lighting off,
`(0x0E, 1)` = Z-write on — all valid, sensible states).

**Method caveat, applies throughout:** the call graph used here follows *direct* calls only.
Virtual dispatch isn't followed, and actor drawing is virtual (`CMoTask` subclasses). "No device
calls reached" therefore means *none through direct calls within 7 levels*, not proof a function
never draws.

### 18.1 Device creation

| Step | Address | What it does |
|---|---|---|
| Holder object | `0x10002F20` | Allocates `0x478` bytes, constructs (`0x10003070`), stores in global `0x103D3CBC` |
| Bootstrap | `0x100031F0` | `Direct3DCreate8(220)` (DirectX 8.1) → holder`+4`; `GetAdapterModeCount` → `+0x40`; mode array (16 bytes each) → `+0x44`; keeps 640×480–2048×2048 in `X8R8G8B8`/`A8R8G8B8` |
| Capability probe | `0x10002130` | `CheckDeviceType`, `CheckDeviceFormat` (including DXT1/3/5) |
| Create | `0x100034B0` | `GetDeviceCaps`, fills `D3DPRESENT_PARAMETERS`, `CreateDevice` → device at holder`+8` |
| `CDx` | `0x100161B0` → `CDx_Constructor` `0x10008F90` | **Global `0x1045666C` = the `CDx` instance**; `IDirect3D8*` at `CDx+8`, device at `CDx+0xC` |
| `CDx` init | `0x100091B0` | Three `CheckDeviceFormat`, two multisample checks, loads `mousenor.ani` |
| `dancer` copy | `0x10251A80` | Copies both pointers into a separate context at `0x10669400` (device at `0x1066941C`) |

`CreateDevice` has two paths chosen by an argument: `BehaviorFlags = 0x40`
(hardware vertex processing) and `0x20` (software). The caller tries once with `0`, then `1`, a
first-attempt-then-fallback shape. **Which path wins at runtime is now logged directly by the
hooking DLL** (`GetCreationParameters` at startup) rather than inferred.

### 18.2 The frame

**`0x10011A00` is the per-frame render function** — the sole caller of `CDx::Present`
(`0x10009720`, which tail-jumps into `0x100035B0`: `Present(NULL,NULL,NULL,NULL)` retried up to
100 times, special-casing `D3DERR_DEVICELOST` `0x88760868`). Order: `TestCooperativeLevel`
(`0x10009710`) → `BeginScene` → ~180 calls → `EndScene` → `Present`.

It is a **state machine**, not a fixed pipeline: `[this+0x44]` drives an 18-case jump table
(`jmp [eax*4 + 0x10012EEC]`), and cases write the global scene-state record (18.4).

Passes identified by real evidence (strings, known globals, reached names, device calls):

| Call | Identified as | Evidence |
|---|---|---|
| `0x10009920` | Default render/texture-stage state | 345 instructions of `SetRenderState`/`SetTextureStageState` |
| `0x10009E20`, `0x1000A1D0`, `0x1000A800`, `0x1000A390` | Render-target, viewport, clear setup | Device calls reached |
| `0x10251500` / `0x102515F0` | World scene through `dancer` | Reaches `StAvatar_*`, `sqxfXformTD_Update`, camera, `dancer` device copy; only pass using `SetLight` |
| `0x1018B860` | Zone scene draw (**relabeled §18.17**) | Sits among `XiZone`'s methods and uses the `XiZone` singleton (the "camera" evidence was a mislabeled global); mesh manager, `CMoProcessor`; vertex shaders, stream sources |
| `0x10013AD0` → `0x10081A50` | Actor draw-list walk | Touches `g_pActorDrawListHead` |
| `0x1015FA00` | Menu / HUD | Strings `menu menuwind`, `menu holdtime`, zone name, `%d:%02d` clock |
| `0x10038520` | Font / text | String `font moji` |
| `0x101D0B00` | Copyright text | String `%c SQUARE ENIX` |
| `0x10003650` | Debug overlay | References `Debug.cpp` |

### 18.3 The submission layer (`CDx`)

`CDx`'s own vtable (`0x103299F0`) is a 6-slot base; its real API is **50 non-virtual methods**,
enumerated from every call made with `ecx` loaded from the `CDx` global. Highest fan-in:

| Method | Address | Callers |
|---|---|---|
| `DrawPrimitiveUP` | `0x1000CD00` | 57 |
| `SetTransform` | `0x1000BD50` | 51 |
| `SetLight` | `0x1000BF30` | 34 |
| `GetTransform` (from cache) | `0x1000BDB0` | 25 |
| Push render target | `0x10009E20` | 21 |
| `DrawIndexedPrimitive` | `0x1000CC00` | 20 |
| `SetTexture` | `0x1000A1D0` | 19 |
| `CreateTexture` | `0x1000A6E0` | 15 |
| `DrawPrimitive` | `0x1000CB20` | 10 |
| `SetViewport` | `0x10009DC0` | 7 |
| `BeginScene` / `EndScene` | `0x10009730` / `0x10009740` | 2 / 16 |
| End-clear-begin | `0x100096B0` | 3 |

`CDx` **shadows every transform it sets**: world `+0x93C`, view `+0x97C`, projection `+0x9BC`.
`CDx+0x158` is the depth of a **render-target stack** of 24-byte entries at `+0x98`
(`0x10009E00` returns the top); `0x10009F20` pushes a texture's surface 0 as the target.

**Performance-relevant:** geometry is overwhelmingly submitted with `DrawPrimitiveUP` — 50 calling
functions engine-wide (including the effect system, e.g. `CMoDistRingElem_AllocRingGeometry`),
versus 8 for `DrawPrimitive` (including `CYyModelDt_PrepareRenderState`) and 5 for
`DrawIndexedPrimitive`. Vertices are copied from CPU memory on every such call, consistent with
CPU-side skinning. The `dancer` layer bypasses `CDx` and draws on its own device copy.

### 18.4 Global scene state (correction to `g_currentRenderPass`)

`0x10456A28` is a **pointer** to a state record (initialized once, at startup in `0x100157E0`,
to the static record `0x10456984`), and the ID is that record's first field — the prior label
skipped a level. Nine IDs occur:

| ID | Set by | Checked by |
|---|---|---|
| `0x40` | `0x10245650` (the lobby/loader thread) | 7 functions, including the frame |
| `0x60` | `0x100142B0`, `0x1009EE60` | 33 functions, including gameplay code |
| `0x70` | frame, `0x10010D20`, `0x1008B100`, `0x1009EE60` | 2 |
| `0x90` | `0x10014AD0` | frame |
| `0xA0` | frame | — |
| `0xB0` / `0xC0` | `0x10017690` / `0x10017700` | — |
| `0xD0` / `0xE0` | `0x1024CAE0` | — |

Since the loader thread sets `0x40` and gameplay code checks `0x60`, this reads as a **global
scene/app state**, not a per-draw pass. It is also **shared state written from a second thread**,
worth adding to the §11 threading picture.

### 18.5 Camera, view, and projection

`D3DTS_WORLD` is set in 27 functions, `D3DTS_VIEW` in 13, `D3DTS_PROJECTION` in 4. The main
apply is `0x10015510`, which builds view through `0x10021900` (a 128-instruction camera
controller using `atan2` and smoothing-style constants), sets it, then builds projection.

The camera object is global **`0x104568FC`**: projection matrix at `+0x154`, near/far at
`+0x2DC`/`+0x2E0`, aspect inputs at `+0x2E8`/`+0x2F0`. The projection builder `0x10015480` calls
a statically-linked five-argument routine at `0x102D83C6` with exactly
`D3DXMatrixPerspectiveFovLH`'s signature (and it halves the FOV by `0.5` before the tangent).
**D3DX is linked in, not imported.** Field of view is computed as **`2·atan(192 / [+0x2F4])`** —
a focal-length-style camera with `192` as a reference half-height. (`+0x2F4` is unrelated to the
actor method `GetFocal`, which turned out to be a per-actor address getter, `this+0x34` — §18.14.)

### 18.6 Textures

All texture creation goes through `CDx::CreateTexture` (`0x1000A6E0`, 10 calling functions, format
passed as a variable). DXT1/DXT3/DXT5 support is **probed against the real GPU** at startup
(`0x10002130`, `0x100091B0`); the D3DX library code at `0x102DC56D` also handles DXT. The upload
path is traced in §18.9.

### 18.7 Bone pose pipeline (completes §13 #6)

All **10** code sites that load the shared-skeleton global `0x1045EC24` are now read (previously 5):
`Skel_BindShared` (`0x10034330`, sets the global, bone count at `+0x32`, the 64-byte matrix table,
and masks the per-bone flag bytes with `0x80`), `CXiSkeletonActor_PoseCompose` (`0x100343C0`, 3
sites), `Skel_LoadBoneRotTrans` (`0x10034620`), `Skel_LoadBindPoseToScratch` (`0x10034760`, copies
record bytes `+0x02..+0x1D` of every bone into the 52-byte scratch — reset to bind pose),
`Skel_ComposeMode` (`0x100347D0`: mode 0 full compose from the root with an override list, mode 1
only bones not yet marked, mode 2 rebuild from scratch rows), `Skel_ComposeFromBone`
(`0x10034B80`, bones N..end) and `Skel_OffsetAllTranslations` (`0x10035170`). None reads record
byte `+0x01` (see §17 — it is `flip`). The composers' override argument is a 4-byte
`{src0, src1, dst0, dst1}` list: bone `dst` gets a straight copy of bone `src`'s matrix
(`Mat4_Copy`, `0x100279F0`) and is marked handled.


1. **`sub_10034620`** — every bone: record quaternion + translation → 52-byte scratch
   (`0x1045F030`); root bone gets the `3π/2` correction.
2. **`PerActor_FourBucketStaggeredUpdate`** (`0x100CBDE0`) → **`0x10027AE0`** — writes a
   **scale matrix** into the bone's 64-byte entry: it zeroes the entry and sets float indices 0, 5,
   10, 15 (byte offsets `0`/`0x14`/`0x28`/`0x3C`) — **the diagonal of a 4×4 matrix**. That is the
   explanation for the previously-unexplained `0x14` spacing. Runtime values: `(s,s,s,1)`,
   `s ∈ {0.92, 0.95, 0.97, 1.0, 1.05}`.
3. **Composer** (`0x100343C0`, bones 1+) — per bone: scale (`0x10027B30`), rotation from scratch
   quaternion (`0x10032FA0`), translation (`0x10027CF0`), then multiply by the parent's matrix
   (`0x10027D10`). A table at `0x1045EC28` marks bones already handled, skipping them.

*(§18.8's original content was a stale status snapshot, since fully superseded by the sections
below and by §13 — removed rather than left to mislead a reader. Not renumbered to avoid touching
every cross-reference to §18.9 onward throughout this document.)*

### 18.9 Texture upload path (closes the §18.6 gap)

`CDx::CreateTexture` (`0x1000A6E0`) turns out to be render-target-only — all 19 call sites make
render targets. Asset textures take a separate path, entirely through the statically linked D3DX:

| Step | Address | What it does |
|---|---|---|
| Loader | `TexRes_LoadBm2` `0x1001D800` | Resource-vtable slot (table near `0x1032C8CC`). Checks the "Bm2" version nibble (`"Bm2 Version Error(%d)"`), dedupes by 16-byte name (`TexMgr_FindByName` `0x1003AEA0`, refcount), builds a 72-byte texture object (`TexObj_Constructor` `0x10039920`) and enqueues it (`TexMgr_Enqueue` `0x1003AB80`, state 1) — or uploads immediately if the manager's immediate flag (`+0x10`) is set. A sibling loader is `0x1001DF60`. |
| Pump | `TexMgr_UploadPump` `0x1003ABB0` | Called every frame from `Frame_Render` right after `BeginScene` (via `0x1003AB70`). State 1 → create + upload; state 2 → release + re-upload (device loss). **In-game (scene state `0x60`) it stops after 20 uploads per frame.** |
| Create | `TexObj_Create` `0x10039A80` | Picks the final format. Uncompressed art becomes **DXT1 (16-bit sources) or DXT3 (32-bit sources)** when the object's compression class (`flags>>4 & 0xF`) is allowed by `g_cfgTextureCompression` (registry 0018), or for class 10 (maps) by `g_cfgMapCompression` (registry 0019); class 9 never compresses. Otherwise `A1R5G5B5`/`A8R8G8B8`. Cube maps via `D3DXCreateCubeTexture`. Mips forced to 1 below 32 px; non-power-of-two sizes are read back afterwards (`GetDesc`) and the padded size written into the object. |
| Upload | `TexObj_Upload` `0x10039E50` | CPU conversion into a staging `D3DXCreateTexture` surface via `LockRect`/`UnlockRect`: rows **flipped vertically** (source is bottom-up), 4/8-bit expanded through the CLUT, 24→32 gets alpha `0x80`, 32-bit alpha copied raw (PS2 range kept), 16-bit maps alpha bit `0x80` → A1. Then `D3DXLoadSurfaceFromSurface` into level 0 (`FILTER_NONE` — this is where the DXT encode happens) and each further mip from the previous one (`FILTER_BOX`). Precompressed DXT data (format bit 7 set; FOURCC table `0x10351C94` = `DXT1`..`DXT5`) skips staging: `D3DXLoadSurfaceFromMemory` straight into level 0. |

Texture object layout (72 bytes): `+0x08` source resource (reference dropped after upload), `+0x1C`
CLUT, `+0x20` pixels (precompressed: `+4` pitch, `+8` blocks), `+0x24`/`+0x26` width/height,
`+0x28` source bpp, `+0x29` destination format code, `+0x2A` mip count, `+0x2C` flags (bits 0–2
cube face / ≥6 all faces, bit 3 special 32-bit converter `0x1001E0A0`, bits 4–7 compression class),
`+0x38` next, `+0x3C` state, `+0x40` `IDirect3DTexture8*`, `+0x44` `IDirect3DCubeTexture8*`.
Manager: `g_pTextureMng` (`0x1047B970`).

Other texture producers: the stereo-mode masks `CDx_CreateRampTexture1x16` (`0x1000C850`) and
`CDx_CreateRampTextures1024x2` (`0x1000C900`) — their only caller is `CDx_CreateStereoResources`
(§18.14); the font glyph cache (`FontGlyphCache_Construct`
`0x1025CAF0`: one 1024×1024 `A4R4G4B4` atlas split into glyph tiles; `FontGlyphCache_UploadDirtyTiles`
`0x1025D270` writes only the alpha nibble of dirty tiles).

**Performance relevance:** every uncompressed texture costs a staging-texture copy, a CPU DXT encode
and CPU box-filtered mips at load time, rate-limited to 20 per frame in-game. That is a credible
source of zone-in texture pop-in and hitching, and a concrete optimisation target (cache or
precompress the converted textures).

### 18.10 Render targets, post-processing, and the end of the frame

Post-processing **exists**. All render targets are created in `App_InitScene` (`0x10010D20`):

| Target | Where | Size / condition |
|---|---|---|
| Scene A | `CDx+0x194` texture, `+0x1A4` depth (`CAcc2` at `+0x190`) | **Background resolution** — registry 0003/0004 (`g_cfgBackgroundResX/Y`, default 512×512) |
| Scene B | `CDx+0x198` / `+0x1A8` | Same size; only when **stereoscopic 3D** mode is on (§18.14; registry 0030 → `g_cfgStereoMode` → `CEnv+0x18`, re-read every frame by `CEnv_UpdateDualTargetMode` `0x1000D630`; a 0..3 counter at `CEnv+0x1C` cycles while on) |
| UI | `CAcc` at `+0x1DC` (`+0x1E0`/`+0x1E8`) | **Menu resolution** — registry 0037/0038 (`g_cfgMenuResX/Y`); only when it differs from the window size |
| 256×256 | `CAcc` at `+0x1BC` (`+0x1C0`/`+0x1C8`) | Only when `g_depthBlurEnabled_Dead` (`0x10456AD8`) ≠ 0 — see below |
| Half-res feedback | `g_feedbackTexHalfRes` (`0x10456938`, one per scene target) | Half the scene size |
| Afterimage | `g_afterimageTex` (`0x10456910`, one per scene target) | Created on demand by the scheduler opcode interpreter; owned by an afterimage task (`g_pAfterimageTask`, dtor `0x10060010`, per-frame `AfterimageTask_OnMove` `0x1005FFD0` sets `g_afterimageStrength` = remaining/total) |

`Frame_Render` (`0x10011A00`) in order:

1. `TestCooperativeLevel` → `BeginScene` → default state → **texture upload pump** (§18.9).
2. Push + clear scene B (stereo mode only — the right eye), then push + clear scene A (clear colour `app+0x308`).
3. App state machine; the world path draws `0x1018B130`, `0x1018C2B0`, the `dancer` world
   (`0x10251500`), the main mesh pass (`0x1018B860`), **the `CMoTaskMng` draw** (`0x10074C30` —
   actors and effects), `dancer` end (`0x102515F0`) and `0x10036230`.
4. Debug overlay (`0x10003650`).
5. **Depth-gated distance blur** (`Post_DepthBlurComposite` `0x1000AAB0` → `CDx_DrawScreenQuadAtDepth`
   `0x1000A3B0`): scene A is downsampled into the 256×256 target, then drawn back as a screen quad at
   the projected depth of a camera parameter with Z-test on and Z-write off, so only pixels beyond
   that depth get the blurred copy. **Unreachable in the shipping client:** its gate
   `g_depthBlurEnabled_Dead` defaults to 0 (`Config_SetDefaults` `0x100178B0`), is not in the
   registry table, and no other code or data holds its address. The effect is compiled in and dead.
6. **Afterimage** (`Post_Afterimage` `0x10012F40`): the first frame copies the scene; later frames
   alpha-blend the previous copy over the scene (alpha = strength × 255, colour `0x808080`) and
   re-copy.
7. **Flash and zoom-feedback** (`Post_FlashAndZoomFeedback` `0x100132B0`): an additive full-screen
   flash (colour `app+0x324`, alpha 2×`app+0x327`), and a zoom-feedback trail that blends the previous
   half-res accumulation over the scene (tint `app+0x32C`, alpha 2×`app+0x32F`, UV zoom `app+0x330`,
   `MODULATE2X`) and then copies the scene back into it.
8. Brightness/fade colour from `0x10350174` (`0x80` = neutral) into `app+0x338`; copyright text
   (`0x101D0B00`).
9. **Final composite** (`CDx_CompositeSceneToBackBuffer` `0x1000C0B0`): scene A drawn over the window
   viewport with linear filtering and `MODULATE2X` — **this is where the background resolution is
   upscaled to the window**. In stereo mode, A and B (left and right eye) are first packed side by side (left half / right
   half) into the target at `CDx+0x824`, then drawn with alpha test (ref 96/127).
10. UI: if the UI target exists, it is pushed, the scene is copied in, and the menu, map, chat and
    status passes draw into it (`0x101BCE30`, `0x10005A40`, `0x10123E90`, `0x100088F0`, `0x101579C0`,
    `0x101AB820`, `0x101AE3E0`, `0x101A2E80`, `0x101C46A0`, `0x101AB770`, `0x10154860`, the
    `0x1015FA00` menu family, `0x1025E0E0`/`F0`, `0x101D5680`, `0x10018850`, `0x101248A0`); then
    `0x1000ABE0` composites it to the back buffer.
11. **Global fade quad** (`CDx_DrawFadeQuad` `0x1000A820`, colour `app+0x31C`): alpha ≤ `0x80` darkens
    (fade to black), > `0x80` adds (fade to white).
12. 2D layer on a 640×512 virtual canvas (`0x1021D4C0`), `0x101D0C70`, fonts (`0x100384B0`,
    `0x10038520`); `CDx_DrawStereoOddFrameOverlay` (`0x1000BB90`) draws only on odd values of the
    `CEnv+0x1C` counter (stereo mode) — see §18.14.
13. `EndScene` → `Present`.
14. **Frame limiter:** spins `Sleep(1)`/`Sleep(0)` until the frame has taken `app+0x30` sixtieths of a
    second (the constructor sets 2 — **the 30 fps cap**); a 4-frame moving average clamped to 20; and a
    wall-clock drift correction against `GetLocalTime` that retunes the timer after sustained drift
    over 1.5 s.

### 18.11 Effect and particle rendering, and the full draw-call census

**73 functions issue draw calls** (70 in game code; the other three are D3DX). There is **no separate
particle renderer**: no point-sprite render state (154–161) is set by a literal anywhere in game code,
and effect geometry is built on the CPU and submitted four ways:

- **`CMoElem` family** — each element class's vtable slot 18 builds its vertices and calls
  `CDx::DrawPrimitiveUP` (e.g. `CMoDistRingElem` → `0x10043720`, `CMoElem_vtbl_ambiguous2` →
  `0x10041C20`). VU-animated and morph elements (`CMoVuAnmElem` and four siblings) share `0x10043F40`,
  which uses `CDx::DrawPrimitive`.
- **`CMoOtTask`** slot 11 → `0x100421A0` (`DrawPrimitiveUP`).
- **`CMoSchedularTask`** slot 8 → `0x10057E10` → **`CMoSchedularTask_Interpret`** (`0x10057FB0`), the
  23.6 KB scheduler opcode interpreter (jump table `0x1005DC1C`). It bypasses `CDx` and talks to the
  device directly (render/texture-stage state, vertex shader, `DP`/`DIP`/`DPUP` and about 40 other
  device slots), and it creates the afterimage textures. This is the PC side of the `.fxt` opcode
  machinery (§10).
- **`dancer`** on its own device copy: `sqgxContext_BatchIndices` → `0x1028AB50`, `0x1029B9D0`,
  `0x10280DE0`.

Other draw owners: models (`CYyModelDt_PrepareRenderState`; `0x1002DC10` via `CYyModelDt` slot 7),
actor shadow/decal (`0x10085060`, `DrawIndexedPrimitiveUP`, via `CXiActor`-family slot 194),
furniture/model actors (slot 162 → `0x101844C0`), `CXiMovie` (`0x10026AD0`), `XiPng` (`0x1025C900`),
text (`0x10038720`, `0x10038A80`, `0x10038E10`), UI (`0x1011x`, `0x1016x`–`0x1017x`), occlusion
(`0x1006C530`), scene stream (`0x10075280`, `0x10075C40`, `0x10076030`), and the world/terrain family
`0x10183xxx`–`0x10185xxx`.

**`CXiSkeletonActor` slots resolved** (PS2 `__vt__15XiSkeletonActor`, 131 slots, compared
against PS2's *overrides* rather than the `XiActor` base stubs the earlier sweep used; matched on
arity, callees, size order and field shift; MSVC puts overloads in reverse declaration order):

| PC slot | Address | Name | PS2 slot | Evidence | Confidence |
|---|---|---|---|---|---|
| 92 | `0x100833B0` | `AddLock` | 40 | increments word `[this+0x70]+0xF2` | High |
| 93 | `0x100833C0` | `SubLock` | 41 | decrements it; at 0 prints SJIS "XiActorのLock回数がおかしい" ("lock count is wrong"). PC fixed PS2's bug (PS2's `SubLock` also incremented), which resolves the one-slot-for-two asymmetry in §12c | High |
| 94 | `0x10081FB0` | `GetPosHandle` | 44 | PS2: if `[+0x5C]`==0 set 1, return 1. PC: same on bit 0 of `+0x88` | High |
| 95 | `0x10081FD0` | `ReleasePosHandle` | 45 | clears it, returns 0 | High |
| 113 | `0x100D4560` | `GetElem` | 60 | `ret 8`; position and size order | Medium-high |
| 114 | `0x100D4800` | `GetElemLocal` | 61 | `ret 8` | Medium-high |
| 115 | `0x100D49B0` | `GetEidMatrix` | 62 | `ret 8`; forwards to the model sub-object at `+0x674` | Medium |
| 116–118 | `0x100D49D0`, `0x100C9310`, `0x100C92D0` | PC-only matrix/element variants | — | 117/118 convert an index via `0x100C9300` and call slots 114/115 | Author-inferred |
| 119 | `0x10082200` | `GetModel` | 65 | handle at `+0xB4` = PS2 `+0x8C` + the `0x28` `XiActor` shift; `IsReadComplete` calls this slot as the model | High |
| 120 | `0x10082210` | `GetModelFile` | 69 | byte-identical to 119; the finder trio uses it as its fallback resource file | Medium-high |
| 121 | `0x100A47E0` → `0x100D12D0` | `IsReadComplete` (+ `IsReadCompleteResList` inlined) | 70 | every resource handle, the model and slot 256 must be resident | High |
| 122 | `0x100CEB00` | `ActorFindResource(type, id, n)` | 67 | `ret 0x10`; `ResourceIter_FindFirst`/`FindNext` (`0x100742B0`/`0x100745C0`) | High |
| 123 | `0x100CE9B0` | `ActorFindResource(type, id)` | 66 | `ret 0xC`; FindFirst only | High |
| 124 | `0x100CEC90` | `ActorGetResourceCount` | 68 | counts FindFirst/FindNext hits | High |
| 158/159 | `0x100D04C0`/`0x100D06F0` | `GetNamePos`/`GetArrowPos` (order not settled) | 80/100 | EID → `GetElem` → + height offset `+0x8C0` → screen projection | Medium |
| 164 | `0x100CF210` | `SetModel` (candidate) | 83 | 1 arg, 1335 B, resource resolve + FindFirst/FindNext walks | Medium |

**Ground/water slot mapping.** The `XiControlActor` `+0x20` shift gives `+0x160` ground normal,
`+0x170` ground height, `+0x174` ground material, `+0x178` water height, so slot 132
`GetGroundNormal`, 131 `SetGroundNormal` (PC-only; stores the normal only when |y| > 0.7 — a
walkable-slope filter), 129/130 ground height, 133/134 ground material, 135/136 water height. Real
dynamic confirmation for these — correlated hit counts matching a water-depth test evaluated only
near water — is in §18.13.

### 18.12 Configuration and CPU capability

The registry is mapped by a 28-entry table at `0x103507E8` of `{global*, key, 0}`: 0000 `A98`,
0001 `A58`, 0002 `C08`, 0003 `A60`, 0004 `C04`, 0007 `A88`, 0011 `AC0`, 0017 `BF0`, 0018 `AD0`,
0019 `AB0`, 0020 `C00`, 0021 `BF8`, 0022 `BE4`, 0023 `AA4`, 0024 `BEC`, 0028 `A9C`, 0029 `A94`,
0030 `ABC`, 0031 `AD4`, 0032 `AB4`, 0033 `A64`, 0034 `A7C`, 0035 `BFC`, 0036 `AA0`, 0037 `AC8`,
0038 `A90`, 0039 `BF4`, 0040 `A74` (all `0x10456xxx`). Meanings confirmed from code: 0003/0004
background resolution, 0018 texture compression, 0019 map compression, 0030 stereoscopic 3D (§18.14),
0037/0038 menu resolution. The rest are unverified here.

`CEnv` (`g_pEnv`, `0x104566E8`; constructor `0x1000D380`) is a CPUID capability object:
`CEnv_DetectCpuFeatures` (`0x1000D400`) fills `+4` vendor (1 Intel, 2 AMD), `+8` MMX, `+9` SSE,
`+0xA` an SSE3-class flag, `+0xB` AMD extended features, `+0x10` logical CPU count; accessors
`0x1000D670`–`0x1000D6C0` feed `CMoProcessor`'s tier choice (§3). `+0x18` is the stereo-3D flag (§18.14).

### 18.13 Dynamic confirmation: device path, terrain queries, and skeleton-actor corrections

A live logging session (85,848 lines, `dynamic_analysis_hooks`, single continuous run) confirmed
several static findings directly and corrected three that had been wrong:

- **`CreateDevice` path — confirmed.** `CreationParameters hr=00000000 adapter=0 deviceType=1
  (1=HAL) behaviorFlags=00000040` = `D3DCREATE_HARDWARE_VERTEXPROCESSING`. Hardware vertex
  processing, confirmed directly rather than inferred.
- **`StartDisintegration` — zero hits across the entire log.** That absence doesn't rule the path
  out — there's no confirmation the player triggered an actual death/disintegration animation
  during this capture — it only narrows when a future capture needs to target it.
- **`GetGroundHeight`/`GetWaterHeight`/`GetGroundNormal` — confirmed by real correlated
  behavior, not just applied names holding.** `GetGroundNormal` fired in every 5,000-line window
  of the whole log (38,649 hits total) — genuinely continuous, matching a value recomputed every
  frame for character/terrain alignment. `GetWaterHeight`/`GetGroundHeight` were near-zero for
  the first ~35,000 lines (an inland/rough-terrain stretch), then ramped up together — in the
  windows right at that transition their counts matched exactly (623/623, 539/539, 495/495)
  before diverging in later windows as the player moved in and out of water repeatedly. This is
  exactly the water-depth-test signature the slot mapping above predicts, seen directly rather
  than assumed.
- **The race condition — still open.** Only one thread ID (`6360`) appeared anywhere in the
  entire 85K-line log, on `ResolveTree` and everywhere else; `Evictor` had zero hits (the
  eviction path itself never ran). The specific precondition — a second thread overlapping a
  genuinely fresh zone load — still hasn't been captured; needs a session that starts logging
  before the very first zone-in.

**`GetFocal` is not slot 132.** PC address `0x100A4590` (Candidate_132) fires in every phase of a
session, including flat, unremarkable terrain — but that doesn't actually discriminate between
hypotheses: a ground-normal read needs identical per-frame recomputation for character/foot
alignment regardless of whether the terrain looks rough to a human observer, so "fires every
frame, everywhere" is equally consistent with both a focal-length read and a ground-normal read.
What does discriminate is the paired setter, `SetGroundNormal` (slot 131, `0x100AA820`): it only
stores the incoming vector when `|y| > 0.7`. That's a walkable-slope filter — it has no sensible
reading as anything to do with a scalar camera focal length. `GetGroundNormal` stands, confirmed
on the setter, not on shape alone. The real PS2 `GetFocal` is a separate, still-real method (one
of the two non-stub members of its stub cluster, confirmed elsewhere in this document), narrowed
only to `{slot 153 @ 0x10082450, slot 246 @ 0x100D04B0}` since slot 132 is excluded. The log
doesn't resolve it further: slot 153 had zero hits in the entire 85K-line session, and slot 246
fired heavily for the first ~35,000 lines then dropped to near-silence — neither pattern reads as
"a value needed every frame," so `GetFocal` stays open, not guessed.

**`Unlink{Caster,Target}Attachments` — resolved, by re-reading a function this project had
already found but misread.** `CXiAtelActor` slots 250/251 (`0x10085C90`/`0x10085CF0`) were
previously named `FindCasterLink`/`FindTargetLink` on the basis that they read `this+0x68`/
`+0x6C` and walk a linked list via `+0x2C`/`+0x30` — true, but incomplete: a full disassembly
shows each function takes **one parameter** (the specific node to remove), searches the list for
it, **splices it out** (patching the previous node's link, or the list root if it was the head),
**zeroes the removed node's own link field**, and **calls a destructor/release helper on it**
(`0x1003b750` for the caster list, `0x1003b780` for the target list). A find doesn't mutate
state or call a destructor on its result — this is a mutating unlink with a specific target,
which is exactly what `UnlinkCasterAttachments`/`UnlinkTargetAttachments` are. High confidence.

**`ViewVolumeClip`/`OcclusionClip` are not stubs on PS2 — neither is permanently unresolvable.**
§13/§18 already established that on PS2 both of these are fixed-constant stubs (`ViewVolumeClip`
hardcodes a return of `1`), sitting in the same information-theoretic-floor cluster as
`ExecHitCheck`/`IsTouchDown`/`IsOnLift`/etc. — trivial, mutually indistinguishable bodies with no
behavioral signal to map any one of them to a specific PC candidate over any other. A PC "shape
candidate" for `ViewVolumeClip`, `0x100A9230`, doesn't fit: it's a real, 716-byte function, and a
function that size cannot be a one-line `return 1` stub. That candidate was never applied as a
name (checked directly in both the live IDB and the symbols script — it isn't there), so nothing
needs undoing. These two join the other confirmed-permanent stub clusters (§13/§18.11).

**`SetAction`/`KillAction`/`IsMovingAction` — one candidate found, one common assumption
corrected, two items still genuinely open.** PS2's real mangled names and signatures come
directly from `SCUS_972.66`'s symbol table: `SetAction(uint, XiActor*, CXiSchStatus*)` (3 args),
`KillAction(uint, XiActor*)` (2 args), `IsMovingAction(uint, XiActor*)` (2 args) — all on
`XiActor` itself (`XiSkeletonActor` overrides only `SetAction`). Disassembling
`IsMovingAction`'s real PS2 body directly (`0x00195A60`, R5900 MIPS) shows it does **not** call
through its `XiActor*` parameter's vtable, contrary to what its signature might suggest. Both of
its indirect calls go through **`this`'s own vtable** — one at slot `0x118/4=70`
(unidentified), and one at slot `0x108/4=66`, which is the already-confirmed
`ActorFindResource(type, id)`, called here with `type=7` — real, independent cross-validation of
that match, found as a side effect of tracing this one down. `KillAction` and `SetAction`'s real
bodies both call through `this`-vtable slot `0x34/4=13` as well.
  - On the PC side, arity (the `ret N` byte count used throughout this project) gives
    `0x100CFC10` (`ret 0xC`, 3 args) as the only real match candidate for `SetAction` — its body
    calls the identity-matrix-init/matrix-copy helpers from the skinning work and pokes CDx-family
    render-state fields, a plausible "reset pose, kick off the new action's visuals" shape.
    **Medium confidence** — arity-only, not branch-verified against the real PS2 body. Applied
    live as `CXiSkeletonActor_SetAction_Candidate`.
  - The other `ret 8` (2-arg) candidate large enough to be worth checking, `0x100CFF40` (1390
    bytes), was checked and **ruled out** for `KillAction`/`IsMovingAction`: its own indirect
    calls go through `eax`/`edx` at `+0x1C0`/`+0x1BC`/`+0x1C4`/`+0x1C8` — the same CDx
    CAcc-embedded-instance field range from the `App_InitScene` finding (§13), not through
    `this` at all. Wrong shape entirely; more likely a per-frame pose-compose-and-submit-to-device
    routine. Left with its default name in IDA, with a comment recording the negative finding, so
    this ruled-out lead doesn't get re-tried blind.
  - `KillAction` and `IsMovingAction` themselves remain **open** — no PC candidate found yet fits
    their corrected real shape.

**The 18-method `IsXxx` cluster (`IsControlLock`/`IsMotionLock`/etc.) — left closed as a checked
negative, not re-attempted.** Three independent static searches (a loose shape search, a
re-check of a ruled-out region, and a tight single-bit-mask search) already came back empty
across the whole 264-slot table. No further technique is available to try, and a repeat pass
over the same search space wouldn't add information; this stays documented as a genuine floor
rather than re-run for its own sake.

### 18.14 Phase 3 closeout: the rest of the actor interface, and registry 0030 = stereoscopic 3D

**Method change that made this work.** Every earlier `CXiSkeletonActor` round compared PC bodies
against *summaries* of PS2 bodies written in previous sessions. This round read each PS2 body
directly (R5900 disassembly of `SCUS_972.66`) and used two things the symbol table gives for free:
the **PS2 names of every callee** (so a PC function that calls "the thing at `0x10056C70`" can be
matched to a PS2 body that calls `YmScheduler::Execute`), and the **full 131-slot
`__vt__15XiSkeletonActor` order**. Several older summaries turned out to be wrong, which is why three
searches had "come back empty":

| Older claim | What the PS2 body actually is |
|---|---|
| `ViewVolumeClip` "a hardcoded `1`" | 672 B: `GetWorldMatrix`, `TransBBX`, `KO_ClipBBox`, `KO_OcclusionCulling`, 6 calls to `GetBoundingBox` |
| `OcclusionClip` an empty stub | 524 B: builds the skeleton world matrix, calls `KO_OcclusionCulling` |
| `AmIUserControlTarget`/`AmIControlActor` stubs | real: compare `this` against a global |
| `IsMovingAction` "calls through its parameter's vtable" | calls through **`this`** (`IsReadComplete`, `ActorFindResource(7,id)`) |
| `IsXxx` cluster = single-bit flags | lock **counters** (`IsControlLock`, `IsDirectionLock`), plain words/bytes, an indexed halfword array (`IsConstrain`), and — for `IsChocobo(STATUS)`/`IsFishingRod(STATUS)` — **setters** of `SUBACTOR_STATUS` |

**The action cluster (PS2 85/86/87 → PC 166/167/168), High.** Matched by callee sequence against the
PS2 bodies, whose callees resolve by name:

| PC | Name | Real PS2 callee sequence reproduced |
|---|---|---|
| `0x100CEE40` (166) | `CXiSkeletonActor::SetAction(uint, XiActor*, CXiSchStatus*)` | `ReverseFindRes(7,id,-1)` → `YmScheduler::Execute`; else `YmResourceFile::FindResourceUnder(7,id)` → `Execute`; else `~CXiSchStatus` |
| `0x10084CC0` (167) | `CXiActor::KillAction(uint, XiActor*)` | `IsKindOf(CXiSkeletonActor)` → `ReverseFindRes` / model resource file → `YmScheduler::Kill` |
| `0x10084D40` (168) | `CXiActor::IsMovingAction(uint, XiActor*)` | `IsReadComplete` (vslot 121) → model `+0xB4` residency → `ActorFindResource(7,id)` (vslot 123) → `IsKindOf` → `ReverseFindRes` → global fallback → `YmScheduler::IsMoving` |

Named helpers: `Scheduler_Execute`/`Kill`/`IsMoving` (`0x10056C70`/`0x10056EF0`/`0x10057010`; arities
`ret 0x10`/—/`ret 8` match PS2), `CXiSkeletonActor_ReverseFindRes` (`0x100CE480`),
`YmResourceFile_FindResourceUnder` (`0x100724C0`), `CYyObject_IsKindOf` (`0x1002C8F0`),
`CXiSchStatus_Destructor` (`0x1018C620`), `ResourceHandle_Deref`/`_IsResident`, `operator_delete`.
**Retraction:** an earlier `SetAction` candidate, `0x100CFC10` (slot 244), was wrong — renamed
`CXiSkeletonActor_Slot244_Unknown`. `0x100CFF40` (slot 245) stays unnamed, correctly ruled out.
Resource type `7` is the action/scheduler resource type in all three.

**Positional run, PS2 slots 75–99 → PC 153–193.** Anchored by the three empty `AddTarget(1)`/
`SubTarget(1)`/`ClearTarget(0)` stubs at PC 155–157 (arities `ret 4`/`ret 4`/`ret`) and the action
cluster at 166–168, with PC-only insertions identified by body:

| PC | Address | Name | Evidence | Conf. |
|---|---|---|---|---|
| 153 | `0x10082450` | `GetFocal` | PS2 `return this+0x10`; PC `lea eax,[ecx+0x34]; ret` (+0x24 shift, same as `SUBACTOR_STATUS` `+0x80→+0xA4`) | High |
| 154 | `0x100A9F40` | `SetTarget` | both `sprintf` a command string into a stack buffer | High |
| 155–157 | `0x10082470/80/90` | `AddTarget`/`SubTarget`/`ClearTarget` | empty on both; anchors | High |
| 158 | `0x100D04C0` | `GetNamePos` | `GetElem` → `CXiActor_NameCalc` (`0x100830C0`, = PS2 `XiActor::NameCalc`, 4 args both) | High |
| 159 | `0x100D06F0` | `GetArrowPos` (PS2 100) | `GetElem` → vslot 160; PS2 = `NameCalc` + `YmDB::Translate3Dto2D` | Med-High |
| 160 | `0x100D0740` | `ProjectToScreen` (PC-only) | the `Translate3Dto2D` analog, via `CDx_SetTransform` | Author |
| 161 | `0x100D0510` | `OnDrawName` | calls vslot 158 (`GetNamePos`) through its vtable, as PS2 does | High |
| 162 | `0x100CBD60` | `RunStaggeredUpdates` (PC-only) | two calls into `PerActor_FourBucketStaggeredUpdate` | Author |
| 163 | `0x100824F0` | `OnChangeEquip` | empty on both | High |
| 164 | `0x100CF210` | `SetModel` | upgraded from `_Candidate`: now inside the run | High |
| 165 | `0x100CD490` | `SetMotion` | `ret 8` = `(YmResource*, float)`; PS2 base is empty, PC implements it | Medium |
| 169 | `0x100A8D60` | `IsMovingTechnic` | walks the attachment list `+0x68` (= PS2 `+0x40`) as PS2 walks `+0x40` | High |
| 170/171 | `0x10084E70`/`0x10084FB0` | `AddTimerTask`/`FindTimerTask` (PC-only) | create / `IsKindOf`-search `XiActorTimerTask` | Author |
| 173 | `0x100CF030` | `SetAttack(CXiSchStatus*)` | calls `SetAction` through vslot 166, as PS2 calls it through vtbl+0x154 | High |
| 174 | `0x100CEE00` | `SetAttack(uint, XiActor*, …)` | same; PC signature is one stack arg shorter (`ret 0x10`) | High |
| 175 | `0x100CEDF0` | `ReplaceAttack` | empty on both, `ret 0x10` | Med-High |
| 176 | `0x100A9230` | `UseMagic(CXiSchStatus*)` | creates `ActorTechLoadPollingTask`, resolves technique resources | High |
| 177 | `0x100A9700` | `UseMagic(uint, XiActor*, …)` | `ret 0x14`; tail-calls the shared handler `0x100A98D0` that slots 178–187 also feed | Med-High |
| 191 | `0x100CCF50` | `OcclusionClip` | screen-rect occlusion query (`Occlusion_QueryScreenRect` `0x1006C280`) using camera viewport size | Med-High |
| 192/193 | `0x100A4620`/`0x100A4640` | `AmIUserControlTarget`/`AmIControlActor` | resolve a singleton's actor handle (`ActorHandle_Resolve` `0x10081550`, 0x900-entry actor table `0x10480AF0`) and compare with `this` | Med-High |
| 194 | `0x100D62C0` | `DrawResourceShadows` (PC-only) | per resident model resource → shadow/decal draw `0x10085060` | Author |
| 125/126 | `0x100822A0`/`0x10082290` | `Append` ×2 | empty 7-arg stubs; PS2 `Append` is empty | Medium |

MSVC's overload grouping shows up again: PS2 declares `SetAttack(5)`, `ReplaceAttack`, `UseMagic(5)`,
`ReplaceMagic`, `UseMagic(st)`, `SetAttack(st)`; PC has `SetAttack(st)`, `SetAttack`, `ReplaceAttack`,
`UseMagic(st)`, `UseMagic`. `ReplaceMagic` has no separate PC slot (likely folded into the
`0x100A98D0` handler family).

**`ViewVolumeClip` has no PC vtable body.** No slot in the 264-entry table has its shape (1 arg,
bounding-box frustum clip). The only culling code reachable from the actor is the screen-rect occlusion
query, called from `OcclusionClip` and from `PerActor_FourBucketStaggeredUpdate`. PC moved view-volume
culling out of this virtual; if a slot survives for it, it is one of the empty `ret 4` stubs 142/144/146,
which can't be told apart.

**The `IsXxx` cluster — all nine pairs placed.** PC widened the early `XiControlActor` fields by
+0x24 (the same shift as `SUBACTOR_STATUS`):

| PS2 | Body | PC get / set | Conf. |
|---|---|---|---|
| `IsControlLock` | counter `+0xD8`; `(c)` inc/dec | 196 / 195, counter `+0xFC` | High |
| `IsFreeRun` | byte `+0xD5` | 204 / 205, byte `+0xF9` | High |
| `IsWalkLock` | byte `+0xD6` | 206 / 207, byte `+0xFA` | High |
| `IsParallelMove` | byte `+0xD7` | 208 / 209, byte `+0xFB` | High |
| `IsDirectionLock` | counter `+0x3D0` | 198 / 197, counter `+0x838` | High |
| `IsConstrain` | `(c,i)`: halfword `[+0x3D8+2i] = (c==1)`; `()`: word | 200 / 199, bytes at `+0x83C` (`sete`, indexed) | High |
| `IsMotionLock` | word `+0x3D4`, plain store | 149 / 148, bit 6 of `+0x840` | Medium |
| `IsChocobo` | `()`: `SUBACTOR_STATUS` in 1..4; `(STATUS)` is a **setter** | 211 / 212, `+0xA4` in [1,4] | High |
| `IsFishingRod` | `()`: status ≥ 5; `(STATUS)` setter | 216 / 217, `+0xA4` in [5,0x24] (PC widened the enum) | Medium |

PC 201–203 (`+0x83E`) are a second, PC-only `IsConstrain`-shaped pair. PC 210–226 are the rest of an
expanded `SUBACTOR_STATUS` query family (ranges `0x11`, `0x25–0x34`, `0x35–0x3C`, `0x3D–0x51`, `0x54`),
the same field the `CXiAtelActor` "AtelType" slots 227–236 read (§12b; names left as-is — they are
PC-only range queries on `SUBACTOR_STATUS`). **Correction:** slots 137–140 had been named
`SetIsChocobo`/`IsChocobo`/`SetIsFishingRod`/`IsFishingRod` in an earlier pass; none of them touch
`SUBACTOR_STATUS`, so they are renamed neutrally (`Slot137_Set388`, `Slot138_Scan3F0`,
`SetFieldA8`/`GetFieldA8`).

Also re-read directly: PS2 `XiControlActor` ground/water fields are `+0x140` normal, `+0x150` ground
height, `+0x158` water height (the `+0x20` shift gives PC `+0x160`/`+0x170`/`+0x178`), confirming
§18.11's names from the source rather than from shape.

**Registry 0030 is stereoscopic 3D.**

- `CDx_CreateStereoResources` (`0x1000C6E0`, only when `CEnv+0x18`): the pack target `CDx+0x824`
  (A and B side by side), two 1024×2 two-row mask textures (`+0x814` rows magenta/green, `+0x81C`
  rows green/magenta, alpha 0x80), and a 1×16 texture at `+0x82C`.
- **Every `CDx` draw entry point** (`DrawPrimitive`, `DrawIndexedPrimitive`, `DrawPrimitiveUP`,
  `0x1000CDF0`) asks `CDx_GetStereoSecondEyeTarget` (`0x1000CA00`). When the per-draw flag
  `CDx+0x828` is set, stereo is on, and the current target is scene A or B, the draw is **issued
  twice**. The first pass uses `CDx+0x810 = 0` into the current target. The second uses
  `CDx+0x810 = 1` into scene B (`+0x198`, depth `+0x1A8`), after which the target is restored.
- Around each pass, `CDx_ApplyStereoEyeProjection` (`0x1000CF20`) sets the projection's `_41`
  (X translation) to **−0.006** for eye 0 and **+0.006** for eye 1 (`g_stereoEyeOffset`
  `0x1034FFA0`), multiplied into the saved projection at `CDx+0x9BC`. That's a depth-dependent
  horizontal parallax, i.e. a left/right eye pair. `CDx_RestoreProjection` (`0x1000CF90`) puts it
  back.
- `Frame_Render` sets `CDx+0x828` for the 3D world pass. Text (`0x10038A80`/`0x10038E10`), the
  occlusion query, and `0x1001D3B0` clear it, so 2D elements aren't doubled.
- The composite packs left (A) and right (B) side by side into `+0x824` (§18.10 step 9).
  `CDx_DrawStereoOddFrameOverlay` (`0x1000BB90`) stretches the 1×16 texture over a rect only on
  odd values of the 0..3 counter at `CEnv+0x1C`. That's an every-other-frame signal consistent
  with shutter-glasses sync.
- What's certain is that this is two-eye stereo rendering. The exact display format
  (side-by-side vs. row-interleaved via the two-row masks vs. frame-sequential) is Medium
  confidence without a toggle test. Cost when on: **the entire 3D world is drawn twice.**

### 18.15 Animation → pose: how motion data reaches the bones

This closes the gap §6 left open ("the 52-byte scratch array … populated by some other,
not-yet-found function") and connects §7 (motion queues and channels) to §18.7 (pose composition).

**The chain, per model** — `Model_AnimateAndPose` (`0x1002A140`), reached from
`PerActor_FourBucketStaggeredUpdate` through `0x1002C2D0`:

1. `Skel_BindShared` — binds the skeleton, points the matrix table at the actor, resets the per-bone
   mask to `&0x80`.
2. **`MotionQueue_UpdateAllChannels`** (`0x1001A420`) — fills `g_poseScratch` (`0x1045F030`, 52 bytes
   per bone: quaternion `+0`, translation `+0x10`, scale `+0x1C`; bone count `g_poseScratchBoneCount`
   `0x10462430`):
   - resets every bone to a default quaternion (`0x10456D2C`, built once), zero translation and
     unit scale (`0x1035109C` = 1,1,1);
   - asks the 5 **base** motion slots (`this+0x00`…`+0x50`, stride `0x14`) whether anything is
     playing (`CYyMotionQue_IsActive` `0x1001B340`) and returns early if nothing is;
   - samples each base slot **directly into `g_poseScratch`** (`CYyMotionQue_SampleInto`
     `0x1001B230`), slot 4 first and slot 0 last, so lower slots override higher ones on the bones
     they drive, marking touched bones with bit 6 in the per-bone mask;
   - samples the 2 **blend** slots (`+0x64`, `+0x78`) into `g_poseBlendScratch` (`0x1045B820`) and
     blends them in by the slot's weight, only on bones whose mask has bit 7 and a nonzero category:
     rotation by `Quat_NLerp` (`0x10033220`), translation and scale by `Vec3_Lerp` (`0x100276A0`).
     The call after `NLerp` (`0x10032A70`) is an empty `ret`, so blended quaternions are not
     renormalised.
3. The composers (`Skel_ComposeMode` etc., §18.7) turn `g_poseScratch` into bone matrices; with no
   motion, `Skel_LoadBoneRotTrans` fills the scratch from the bind pose instead.

`0x1045F028` is a **pointer to a per-bone byte table** (indexed in lockstep with the scratch), not a
per-motion-slot table as §7 had it; renamed `g_pBoneMotionMask`. Low 6 bits = channel category,
bit 6 = set by a base layer this update, bit 7 = bone accepts blend layers.
`MotionQueue_ApplyPolicy` (`0x10019A50`) reads the same bits when deciding whether a new motion
can interrupt or must queue.

Keyframe decoding itself is §7: key channels (sparse, time-keyed) and frame channels (fixed-rate),
linear interpolation only (the "Smooth" mode is a data field no code path reads), mixer motions
that nest.

**~~Open, dynamic only~~ — closed statically in §18.16:** visible actors animate every frame; the
1-in-4 bucket staggers only the occlusion re-test of off-screen actors.

### 18.16 Animation rate and the collision actor — closed

**Animation rate (closes §18.15's open note, statically — no hook needed).** Every path into motion
sampling was traced: `MotionQueue_UpdateAllChannels` ← `Model_AnimateAndPose` (`0x1002A140`) ←
`Model_AnimateEntry` (`0x1002C2D0`, calls it unconditionally apart from a null-model check) ← two
sites, both inside `PerActor_FourBucketStaggeredUpdate` (`0x100CBDE0`): a direct call at `0x100CC950`
and two calls through `0x1002B6E0`. There is no draw-time animation path elsewhere.

The gate in front of `0x100CC950`, decoded:

1. A virtual check (slot `0x304/4`) can skip the whole update.
2. **Full update** if any of: force flag `+0x9F8`, a local flag, a global at `[0x103D3CB8]+0x4C`, or
   `GetFrameCounter() % 4 == +0x9F0` (bucket A).
3. The full update runs **`Occlusion_QueryScreenRect`** (`0x1006C280`) on the actor's bound
   (`+0x8F0`–`+0x910`, radius `+0x900`, with the viewport width/height) and **caches the result in
   `+0x9F4`** (nonzero = culled). It also clears `+0x9F8`. Visible → animate; culled → skip.
4. **Off-bucket frames reuse the cached result:** `+0x9F4 == 0` → animate (that path reaches the call
   with no branch around it); nonzero → skip (`+0xA04` selects between two skip variants).

`CXiSkeletonActor_Init` sets `+0x9F4 = 1` (assume culled), `+0x9F8 = 1` (force a test on frame one),
`+0x9EC` = a global serial number (`0x1048A34C`), and `+0x9F0` = the least-loaded bucket.

**Result (qualified in §18.17 by the per-frame actor draw budget): visible actors animate every frame. The 1-in-4 bucket staggers only the occlusion re-test;
off-screen actors don't animate and are re-checked once every four frames.** For GPU-offload planning,
pose data changes every frame for everything on screen. Bucket B (`+0x9FC`) does not gate animation —
both outcomes of both of its compares reach the `0x1002B6E0` calls.

**The collision actor.** Resolved against the PS2 `XiCollisionActor` overrides and DWARF layout
rather than `XiActor`'s base versions — which is where earlier passes went wrong. PS2
`XiCollisionActor` overrides exactly: `GetRuntimeClass` (0), `OnMove` (3), `ExecHitCheck` (46),
`IsTouchDown` (47), `IsOnLift` (48), `GetPos` (56), the destructor (99), and adds `IsBlendNormal`.
The base versions of 46–48 really are empty; the overrides are not:

| PS2 body | Behavior |
|---|---|
| `ExecHitCheck` | `sb $zero, 448` — clears `IsTouch` |
| `IsTouchDown` | `lb $v0, 448` — returns `IsTouch` |
| `IsOnLift` | `lb $v0, 449` — returns `is_on_lift` |
| `GetPos` | returns `&pos` (`384`) |
| `IsBlendNormal` | returns 0 |

PC collision layout, from the constructor and `OnMove`: **every PS2 scalar field sits at exactly the
`+0x420` shift** — `IsTouch` `+0x5E0`, `is_on_lift` slot `+0x5E1`, `current_area_id` `+0x5E4`,
`hit_check_count` `+0x5E8`, `current_plight` `+0x5F0` — plus three **PC-only bytes** placed in PS2's
padding: `+0x5E2`, `+0x5EC`, `+0x5F4`. The 64-byte vector sub-block is arranged differently: PC's
working collision position is `+0x5C4` (`OnMove`'s `lea ebp,[esi+0x5C4]`), not the `+0x5A0` a uniform
shift predicts. Its internal order wasn't determined.

**The `IsOnLift` byte, explained.** PS2's `OnMove` *computes* `is_on_lift` (`sb $v0, 449` / `sb $zero,
449`) and never reads it. On PC, `OnMove` *reads* `+0x5E1` as an input (written only by the constructor
and `0x100CA730`) and *writes* the computed result to `+0x5E2`, which `IsOnLift` returns. PC split one
PS2 byte into an input and a result.

**Deferred hit check (PC-only).** `+0x5EC` is a request flag. Slot 96 (`RequestHitCheck`, called from
`0x100852D0` and `0x100AD1E0`) sets it via slot 253; `OnMove` reads it via slot 252, reruns the hit
test (`0x101814D0`) to recompute `IsTouch`, and clears it with slot 253(0).

**Naming, and the one judgment call.** Slots 101–103 sit inside the already-verified +55 PS2→PC run
(49→104, 56→111, 57→112), and each touches the same field in the same direction as its PS2 override,
so 101 = `ExecHitCheck`, 102 = `IsTouchDown`, 103 = `IsOnLift`, 111 = `GetPos`. PC's `ExecHitCheck`
takes a byte argument and writes it where PS2's writes 0, and has no virtual callers — the skeleton
code writes `IsTouch` directly from three functions. By *behavior*, slot 96 plays the "request a hit
check" role; it is named `RequestHitCheck` to keep the two distinct. 97/98 are PC-only accessors for
the real PS2 field `current_area_id` (10 and 12 virtual call sites).

**Corrections carried in:**
- `ExecHitCheck`/`IsTouchDown`/`IsOnLift` were listed as "permanently unresolvable stubs" (§12b,
  §12c). Only their `XiActor` base versions are stubs; the collision overrides are matched here.
- The symbol script had `CXiCollisionActor_InvokeSelfActivation` at `0x100D6670`. Slot 96 is
  `0x100A5620` in both the collision and skeleton vtables; `0x100D6670` is an unrelated function.
  The wrong entry was removed.
- §18.15's animation-rate question was framed as needing a hook; it didn't.

### 18.17 Actor draw budget, the zone environment, and weather — plus corrections

**1. `0x1002B6E0` is the actor's model draw, behind a per-frame draw budget (corrects §18.16).**
It is not a secondary pass. It resets render state, fetches the cached view/projection/world
transforms, sets fog modes, animates through `Model_AnimateEntry` (both of its internal branches do),
and draws. `PerActor_FourBucketStaggeredUpdate` reaches it through a budget gate:

- `CXiActorDraw_UpdateDrawList` resets the counter `0x1048A350` to 0 each frame and sets the limit
  `0x1048A354` from **`0x10193850(0x3C)`** — index `0x3C` of an in-game settings object
  (`0x106626CC`, read via `0x10195330`). That object is not the registry table of §18.12, so this
  is an in-game setting; which menu option it is was not determined.
- Each drawn actor increments the counter. **Under budget → draw. Over budget → draw only if**
  `[+0x768]` or `[+0x76C]` points to an actor whose `+0x6A4 == 4`, or the actor's own `+0x728 <= 1`;
  otherwise skip.
- `+0x768`/`+0x76C` are dereferenced as actor pointers. PS2 `XiSkeletonActor` has exactly two
  `XiActor*` fields in that region, `link_actor` and `eidlink_actor`; the constant `ef_param` shift
  does **not** hold here, so the exact pairing is unproven. `+0x6A4 == 4` is compared in this one
  place only in the whole binary; its meaning is not determinable from comparisons.

**Correction to §18.16:** an over-budget actor that fails these checks is neither drawn nor
animated. The accurate statement is: *visible actors within the draw budget (or linked to a
qualifying actor) animate every frame*.

**2. `0x1065CB04` is the `XiZone` singleton, not the camera.** `0x1018B130` allocates `0x1DC` bytes
(476 — exactly `XiZone`'s size), runs the `XiZone` constructor `0x1018B170` (installs vtable
`0x10336838`), and stores the result there; `XiZone`'s slot 1 (`0x1018B360`) destroys it and zeroes
the global on messages 2 and 5. The symbols script's `g_pCurrentCamera` ("inferred, not fully
confirmed") was wrong. Knock-on corrections:
- §18.2's `0x1018B860` "main 3D mesh render, camera" — the camera evidence was this global. It sits
  among `XiZone`'s methods and uses the `XiZone` object: it is the **zone scene draw**.
- The secondary-motion solver (§6, "camera bias") reads `XiZone+0x124/+0x128/+0x12C` and `+0x134`.
  Those are written by **`0x10187050`**, the environment-record applier (it also writes the fog
  color), and `+0x134` is additionally ramped by `0x10188A50` (steps of 0.0025 / 0.01, cap 1.2). So
  the "pull toward the camera" is a pull along a **zone-environment vector with an animated
  strength**. That fits wind acting on hair/cloth; the vector's meaning is inference, the writers
  are confirmed.

**3. The zone environment: how fog and ambient reach the screen.** The only data-driven fog/ambient
setters in the binary cluster in `0x1017B510`, `0x1017C9C0`, `0x1017DE20`, `0x10183DA0`. They read a
large renderer object (`this`, not `XiZone`): **ambient `+0x39250`, fog color `+0x39254`, fog end
`+0x39258`, fog start `+0x3925C`**. `0x1017B510` also sets fog table/vertex/range modes and is one
of only four functions that set `D3DTS_PROJECTION` — consistent with a sky/far-environment pass,
not yet decoded. It fills those fields by calling two `XiZone` methods with output pointers:

- `XiZone_GetAmbient` `0x1018B9E0` → `Env_ComputeAmbient` `0x10188E00`
- `XiZone_GetFog` `0x1018BA20` → **`Env_ComputeFog` `0x10189120`**

Both first look up a sub-area by ID (`0x101889C0`) and fall back to the zone. `Env_ComputeFog`:
- environment not loaded → white fog, end 400, start 0;
- loaded → defaults grey `0x808080`, end 400, start 300; with a record at `[this+0x18]`, color from
  the RGB-float vector at `+0x114` (×255), and end/start from **one of two record sets** chosen by a
  mode argument (`+0x1C/+0x20` or `+0x3C/+0x40`);
- each distance × `Env_FogDistanceFactor` `0x101892B0` = 1.0, or when loaded a threshold test
  (`0x10187020`) × a per-mode global scale (`0x10456AA8`/`0x10456AB8`, in the settings-globals block)
  × **`XiZone+0x1D4`** (set by the constructor and `0x1018B3A0`);
- clamp: end ≤ start → end = start + 1.

**4. Weather.** A real system, previously covered only in passing (an effect-clone classifier
recognizing `weat`/`dryw`/`dust` tags, §5; a lobby thread that ends with a weather transition, §11):
- **20 weather types**, table `0x10377B18` (8-byte stride, 4-char codes): `fine suny clod mist dryw
  heat rain squl dust sand wind stom snow bliz thdr bolt aura ligt fogd dark` — FFXI's 20 weather
  states in order (clear, sunshine, clouds, fog, hot spell, heat wave, rain, squall, dust storm, sand
  storm, wind, gales, snow, blizzards, thunder, thunderstorms, auroras, stellar glare, gloom,
  darkness). A packed copy and a `…1` variant set follow it.
- The lookup `0x1018BB40` (`&table[id*8]`) has no callers or stored pointers — dead as a function;
  callers inline the arithmetic.
- **Event-driven weather:** `0x100B84B0` is an event-VM opcode handler (called from
  `XiEvent_ExecProg`) that reads its operands via the event argument reader and loads a weather
  file — the `ERROR!:Weather file ga nee! [%d]` ("weather file missing") message is its own.
- Log formats `Weather[%s]Area[%s]` / `File[%s]Weather[%s]Area[%s]` and the class
  `YmCombineWeather` (vtable is only the generic 6-slot base; logic non-virtual) indicate
  **per-weather, per-area environment files** combined into the zone's environment.
- `XiZone` slots 6–8 run/kill/poll a scheduled resource (`Scheduler_Execute`/`_Kill`/`_IsMoving`) —
  the mechanism for zone-driven effect sequences.

**How weather reaches rendering, as far as confirmed:** through the zone environment records above
(fog color/distances, ambient, and the wind-like vector feeding hair/cloth), and through effect
generators tagged for weather (rain, snow, dust particles are drawn by the ordinary effect path,
§18.11). **Not yet traced:** which code selects the environment record by weather and by time of
day, and how weather transitions blend over time.

**5. Other rendering-adjacent areas the map glosses over** (found in this sweep; each is a real
gap, not a claim of absence):
- **Sky / sun / moon / clouds** — no mention anywhere in the documents. `0x1017B510`'s projection
  override plus fog/ambient setup is the strongest lead.
- **Time of day** — no mention. The environment applier `0x10187050` copies records; what picks
  the record by the in-game clock is not located.
- **Water surface rendering** — only the height accessors are documented; no surface/reflection pass.
- **Shadows** — `dancer`'s shadow-volume system is documented at the data level (§8), and actors
  carry a `shadow_alpha`; whether stencil shadow volumes actually render on PC, and how actor blob
  shadows are drawn, is not in the pipeline map.
- **The in-game settings object** (`0x106626CC`) — distinct from the registry table; its indices
  (e.g. `0x3C` = actor draw budget) are unmapped.

### 18.18 Phase 6 closeout: resource types, time of day, weather records, and the rest

**1. The resource (chunk) type map — authoritative.** Every FFXI DAT is a chain of 16-byte-headed
chunks (4-byte name; packed word: type = low 7 bits, size = bits 7–25 × 16). The engine's loader
(`ResourceFile_CreateByType`, a two-level switch at `0x100712D8`: byte table `0x10071914` → jump
table `0x1007189C`, cases 0–`0x5F`) builds one object per chunk. The type *names* come from the PS2
DWARF enum `YmResourceHeader::RES_TYPE`, read from the raw block the project's parser had dropped:

| # | Name | # | Name | # | Name | # | Name |
|---|---|---|---|---|---|---|---|
| 0 | Terminate | 25 | KeyFrame | 50 | Med | 75 | Bmd |
| 1 | Rmp | 26 | Bmp | 51 | Msh | 76 | Qif |
| 2 | Rmw | 27 | Bmp2 | 52 | Ysh | 77 | Qdt |
| 3 | Directory | 28 | Mzb | 53 | Mbp | 78 | Mif |
| 4 | Bin | 29 | Mmd | 54 | Rid | 79 | Mdt |
| 5 | Generater | 30 | Mep | 55 | Wd | 80 | Sif |
| 6 | Camera | 31 | D3m | 56 | Bgm | 81 | Sdt |
| 7 | Scheduler | 32 | D3s | 57 | Lfd | 82 | Acd |
| 8 | Mtx | 33 | D3a | 58 | Lfe | 83 | Acb |
| 9 | Tim | 34 | DistProg | 59 | Esh | 84 | Afb |
| 10 | TexInfo | 35 | VuLineProg | 60 | Sch | 85 | Aft |
| 11 | Vum | 36 | RingProg | 61 | Sep | 86 | Wwd |
| 12 | Om1 | 37 | D3b | 62 | Vtx | 87 | NullProg |
| 13 | FileInfo | 38 | Asn | 63 | Lwo | 88 | Spw |
| 14 | Anm | 39 | Mot | 64 | Rme | 89 | Fud |
| 15 | Rsd | 40 | Skl | 65 | Elt | 90 | DisgregaterProg |
| 16 | UnKnown | 41 | Sk2 | 66 | Rab | 91 | Smt |
| 17 | Osm | 42 | Os2 | 67 | Mtt | 92 | DamValueProg |
| 18 | Skd | 43 | Mo2 | 68 | Mtb | 93 | Bp |
| 19 | Mtd | 44 | Psw | 69 | Cib | 94 | Sef |
| 20 | Mld | 45 | Wsd | 70 | Tlt | 95 | Mhb |
| 21 | Mlt | 46 | Mmb | 71 | PointLightProg | 96 | Mht |
| 22 | Mws | 47 | **Weather** | 72 | Mgd | 97 | Max |
| 23 | Mod | 48 | Meb | 73 | Mgb | | |
| 24 | Tim2 | 49 | Msb | 74 | Sph | | |

Cross-checks: type 61 (`Sep`) is the only PC case whose class names itself (`CYySepRes`); the PC
switch covers exactly `0`–`0x5F`, matching `Max = 97`. Every supplied DAT parses to its exact last
byte. What the supplied DATs contain (types present, confirmed from content):

| Type | Content | Seen in |
|---|---|---|
| 32 `D3s` | Texture — `tim` header, name, dimensions, `3TXD` (DXT3, byte-reversed) | all 12 files |
| 31 `D3m` | Small effect meshes (8–16 vertices) tagged with effect names (`areise`, `yam_mod`) | Prishe, Shadowlord |
| 41 `Sk2` / 42 `Os2` / 43 `Mo2` | Skeleton / mesh / motion | all characters, monsters, mounts |
| 46 `Mmb` | Furniture model | both furnishings |
| 5 `Generater`, 7 `Scheduler`, 25 `KeyFrame`, 61 `Sep`, 62 `Vtx`, 69 `Cib`, 84 `Afb` | effect/scheduler/keyframe/sound-effect-program data | per file |

**Z-sort periods (§13 #3): negative result for these files.** No supplied DAT holds `dancer` shape
data, and no `RES_TYPE` is a `dancer` model format — `D3m` is effect geometry, not `dancer` shapes.
The shipped period values therefore can't come from model DATs; if `dancer` shapes ship at all, they
arrive by a path other than the `YmResource` loader.

**Mounts:** each mount DAT (Beetle, Moogle, Omega) is a standalone single-skeleton model, and the
"Ygnas riding Darrcuiln" DAT is **one** combined model with one skeleton, not two linked actors. The
draw-budget link fields (§18.17) therefore can't be read off DAT structure; they stay a runtime item.

**2. Weather records are time-keyed, and time of day is keyframe interpolation.** Type 47 `Weather`
resources are constructed by `WeatherRes_Construct` (`0x101893B0`) — the environment records that
`Env_ComputeFog`/`Env_ComputeAmbient` read (§18.17) *are* these weather resources.
- **Record selection:** `WeatherRes_FindAtOrBefore` (`0x10189E30`) and its sibling `0x1018A0F0` walk
  every loaded type-47 resource (`ResourceIter_FindFirst(…, 0x2F)`/`FindNext`) and pick by time.
- **Each record's key is its 4-character resource name read as `HHMM`.** `WeatherRes_GetTimeKey`
  (`0x10072180`) takes the name dword and computes `(c0·10 + c1) − 0x210` (`0x210` = `'0'·10+'0'`)
  per digit pair; `Time_FromHours` (`0x1018BF50`) scales hours (days × 24 + hour) into clock ticks.
- **"Now"** is `XiZone+0x1C8`, read by `Zone_GetClock` (`0x10189C60`), gated by a flag in the
  camera object. Times wrap on a fixed cycle: `Time_Normalize` (`0x1018BC40`) reduces by
  `0x6F3C9000` = 1,866,240,000 = 5⁴·9³·4096.
- **Blend:** `Env_BlendTimeOfDay` (`0x1018A340`, called from the zone update `0x1018ADE0`) computes
  `t = (now − previous key) / (next key − previous key)` (`fild; fidiv`, wrap-aware) and interpolates
  the two records via `0x10189490`. It runs a second selector pair (`0x1018A220`/`0x1018A260`)
  as well; that is most likely the weather-to-weather transition, not decoded further.

So: **an area's weather file supplies a set of `HHMM`-named records per weather; the zone
interpolates between the two that bracket the current game time**, and fog/ambient/wind (§18.17)
come out of the blend.

**3. Time-of-day light tint is registry key 0034.** `Light_ApplyTimeOfDayTint` (already named) is
gated by `g_timeOfDayTintEnabled` `0x10456A7C` — which is registry key **0034**'s global in §18.12's
table. One more registry key identified.

**4. The world environment render.** `0x1017B510` (1,438 instructions) is not just a sky pass: it
sets projection, lights (`CDx_SetLight`, `Light_ApplyTimeOfDayTint`), fog and ambient, and draws,
through sub-passes `0x1017C9C0`/`0x1017DE20` that apply their own fog. Renamed
`Zone_RenderEnvironment`. The sky is not a separately identifiable pass within it.

**5. Water.** There is **no `SetClipPlane` call on the device anywhere**, so there is no planar
reflection pass. Water surfaces are drawn as ordinary zone geometry; the only water-specific state
the engine keeps is the height/depth pair (§18.16).

**6. Shadows.** Stencil is enabled (`D3DRS_STENCILENABLE = 1`) in exactly four functions, all in the
`dancer` range (`0x1028F8C0`, `0x10297CC0`, `0x10297EC0`, `0x102A2530`); nothing in the FFXI layer
enables stencil. So `dancer`'s shadow-volume path is compiled and wired to the device on PC; whether
it runs in normal play is a runtime question. Actor shadows in the FFXI layer are alpha-blended
(`shadow_alpha`), not stencil.

**7. The in-game settings object** (`0x106626CC`, `Settings_GetValue`): about 60 distinct constant
indices are read (`3`, `0xF`–`0x19`, `0x32`–`0x35`, `0x3C`, `0x41`–`0x49`, `0x8B`–`0x98`,
`0x9C`–`0xCE`); `0xAB` alone at 25 sites, `0xAF` at 7. Only `0x3C` (actor draw budget) has a known
meaning. This is an index map, not a meaning map.

**A further logging session (377,805 lines, one thread ID throughout, 375,700+ terrain-candidate
hits) closed two of the four remaining runtime items and left two genuinely open:**

- **Weather-to-weather transition — confirmed real.** `WeatherSelA`/`WeatherSelB` (`0x1018A220`/
  `0x1018A260`) fired 16 and 13 times respectively during ordinary play. This is a real, distinct
  code path exercised in normal play, not dead code (§18.18); the internals of what it blends
  were not re-examined here.
- **`dancer` stencil shadows — confirmed not exercised in this log, a real negative result.**
  Zero hits across all four `StencilFnA`–`D` hooks despite a long, varied session. Stencil is still
  compiled in and wired to the device (§18.18); it simply didn't run here. One log isn't proof
  it never runs, but it's a genuine, substantial negative, not an untested guess.
- **Draw-budget gate — still open; this log never exercised it.** Zero `DrawBudgetGate` hits
  means the per-frame actor count never exceeded the budget, so the gate never fired at all — the
  meaning of `+0x6A4 == 4` and which link field is populated remain unanswered. This needs a
  scenario with enough on-screen actors to actually exceed the budget (a crowded event zone, many
  active pets/trusts), not just an ordinary logging session.
- **Race condition — still unconfirmed.** Every line in this log again shows the same single
  thread ID; still needs a session logging before the very first zone-in after a fresh client
  launch (§ Future box).

Device creation was independently reconfirmed the same way as before: `deviceType=1 (HAL)`,
`behaviorFlags=0x40 (HARDWARE_VP)` — matching Phase 1's original finding exactly.

**Genuinely remaining, runtime only:** the draw-budget gate's `+0x6A4` meaning and link-field
identity (needs a crowded-scenario session), and the file-I/O race condition (needs a
fresh-launch, pre-zone-in session).

