# Cross-check against the verified reconstruction

This document compares DancingMad's names and claims with the ffximain-gfx repository. That repository
reconstructs the graphics code of the same `FFXiMain.dll` as C++ and gates every function against the game's own
code. Each result says what was checked, against what, and what it shows. Where a check could not decide
something, it says so rather than picking a side.

The tools, both in ffximain-gfx:
- `pipeline/dm_crosscheck.py` reads this repository's symbol scripts with `ast` (they are never run) and
  checks every named address.
- `pipeline/dm_reference.py` writes `docs/verified/`: one entry per verified function.

## 1. The same binary

- 779 of the 785 function names in `tools/ffxi_symbols_ida.py` fall exactly on a function's first instruction
  in ffximain-gfx's unpacked image (sha256 `1b9b59ae…a3ad`, PE timestamp `0x6A995428`). The other 6 are in §2.
- All 503 data names fall outside every function.
- So `FFXiMain_uncomped.dll` here and that repository's unpacked DLL are the same build. Every address below
  compares like with like.

## 2. Symbol-script entries whose kind does not match the code

Each of these is passed to `apply_name` with `is_func=True`. Running the script names them as functions, and
IDA would split the function that holds them.

| Address | Name here | What the code shows |
|---|---|---|
| `0x10085E89` | `ActorInit_CallSite_GenericMoveTowardTarget` | An instruction inside 0x10085E40. Nothing calls, jumps to or refers to it. It names a call site, not a function. |
| `0x100D6464` | `CXiSkeletonActor_CreateGeneratorClone_CallSite` | The same: an instruction inside 0x100D63F0, never a target. |
| `0x10040F50` | `CMoD3mSpecularElem_Ctor` (marked confirmed) | Inside 0x10040E70 (0x10040E70–0x10040FAC). No call, jump, or dword anywhere in the image refers to it, so no code can enter a function there. The function that stores this class's vtable `0x1032AD20` and stamps 448 at `+0x176` is **0x10041020** (§6.3). |
| `0x10052E00` | `CXi471011C8_VT_1032B3B8_Dtor` | Inside 0x10052DF0 (0x10052DF0–0x10052E1B), with no reference to it. The destructor is likely the function at 0x10052DF0 that holds it; that is not checked here. |
| `0x1006CE40` | `Pool_InitSlots` (marked confirmed) | Reached only by `jmp` from three functions (0x1006CF89, 0x1006F089, 0x100701F9): a tail block they share. The name describes the code, but it is not a function anything calls. |
| `0x100035B0` | `D3DHolder_Present` | Reached only by the `jmp` at 0x10009726, the end of `CDx::Present`'s three-instruction stub at 0x10009720. It is the body of `CDx::Present`, not a separate function. |

## 3. Names that differ

Both sides' names are inferences except where marked. Neither is taken as right because the other differs.

| Address | Here | ffximain-gfx | What decides it |
|---|---|---|---|
| `0x10085060` | `DrawResourceShadows` (Author; §18 says `DrawIndexedPrimitiveUP`) | `CXiActor_SpawnResourceGenerators` | **The code.** Its 124 instructions make 10 calls: `ResourceIter_FindFirst`/`FindNext`, `0x10053A00`, a no-op, `CMoGeneratorClone_CreateInstance`, and one virtual call `[eax+0x124]`. None of them draws, and it makes no Direct3D call. It starts generator clones for flagged resources. FINDINGS §18 (line 2701) and GRAPHICS_PIPELINE §6.2 and §8 list it as a shadow/decal draw. |
| `0x1021D4C0` | "2D layer on a 640×512 virtual canvas" (GRAPHICS_PIPELINE §10) | `CXiMovie_DrawFrame` | **The code.** `Frame_Render` passes it a rectangle whose right and bottom are `0x280` and `0x200` (0x10012A3D, 0x10012A4F; its left is EAX = 0 from 0x10012A37), and ffximain-gfx's reading of the function (docs/NAMES.md) is that it draws the current movie frame. The UI's own virtual screen is 640×480: `MenuMng_Init` stores `0x280` at `+0x80` (0x1015D902) and `0x1E0` at `+0x82` (0x1015D949). The 640×512 is the movie rectangle, not the 2D canvas. |
| `0x1002DC10` | `CYyModelDt_PrepareRenderState(V2)` | `CYyModelDt_SkinAndDrawV2` | Both list it among the draw functions. ffximain-gfx's reading of the code (docs/NAMES.md, 1 Oct): it locks the vertex buffers, skins on the CPU and calls `DrawIndexedPrimitive` per material. |
| `0x1002C2D0` | `Model_AnimateEntry` | `CXiSkeletonActor_AnimateModels` | ffximain-gfx's reading (docs/NAMES.md): it loops over every model in the list and stops at the first failure, which is more than a single entry. The name is the only difference. |
| `0x10284B20` | `sqgxContext_SelectShaderMode` (confirmed) | `sqgxShader` (tree) | Not decided here. The tree's name comes from the export; check this one against the PS2 symbols. |
| `0x1017B510` | `Zone_RenderEnvironment` | `XiZone_Draw` | Same function, same role ("projection, lights, fog, draw"); only the name differs. |
| `0x10456A7C` | `g_timeOfDayTintEnabled` | `g_windowMode` | ffximain-gfx's reading of the code (docs/NAMES.md, with the functions named): 0 is exclusive fullscreen, 1 windowed, 2 popup, 3 popup at screen size. `App_CreateMainWindow` switches on it for the window style, and `App_WinMain` passes `== 0` as the fullscreen flag. In windowed modes `Env_ComputeAmbient` brightens dark ambient by the gamma value instead, which is why it looked like a tint switch. |
| `0x1048A350` / `0x1048A354` | `g_actorDrawCountThisFrame` / `g_actorDrawBudget` | `g_actorUpdateCounter` / `g_actorUpdateInterval` | **Open.** Both are medium-confidence readings of the same counter-and-limit pair in the staggered update. Whether the limit gates drawing or updating is not decided by either side's evidence. |

Six more functions are named only here, and only by inference. Nothing in ffximain-gfx's sources contradicts
them: `CXiCollisionActor_OnMove` 0x100A4ED0, `XiZone_GetInstance` 0x1018B130, `XiZone_FindSubArea` 0x101889C0,
`Env_ComputeFog` 0x10189120, `Env_FogDistanceFactor` 0x101892B0, and `Time_Normalize` 0x1018BC40.

## 4. Claims in GRAPHICS_PIPELINE.md and FINDINGS §18, checked

| Claim | Result | Evidence |
|---|---|---|
| `Frame_Render` is an 18-case state machine (table `0x10012EEC`) | **Agrees** | `cmp eax, 0x11; ja; jmp [eax*4 + 0x10012EEC]` at 0x10011CE0. |
| A 30 fps cap: `app+0x30` set to 2 | **Agrees for the game's code, but not what runs** | From ffximain-gfx docs/RENDERER.md §3: the only setter, 0x1008A0E0, is called with 2 (and with 4 in one state); the global 0x1035B5E8 starts at 2. In all four live memory dumps ffximain-gfx took, `[this+0x30]` is **1, which is 60 fps**: something outside the game's code wrote it. ffximain-gfx's speedfix reads it as 0 to remove the wait. |
| Wait loop: `Sleep(1)`/`Sleep(0)` spin | **Mostly agrees** | ffximain-gfx docs/RENDERER.md §3: the loop at 0x10012B12–0x10012B64 calls `Sleep(1)` and `pause` while the elapsed 1/60 s ticks are below `[this+0x30]`. |
| Caller counts of the `CDx` methods | **Count differs** | From the code: `DrawPrimitiveUP` 0x1000CD00 has 50 calling functions and 76 call sites (57 here); `SetTransform` 43 and 71 (51); `SetLight` 8 and 33 (34); `GetTransform` 19 and 34 (25); push render target 16 and 28 (21); `DrawIndexedPrimitive` 4 and 20 (20); `SetTexture` 12 and 21 (19); `CreateTexture` 10 and 19 (15); `DrawPrimitive` 8 and 13 (10). The numbers here match neither count, which suggests they are IDA cross-references of other kinds. |
| `DrawPrimitiveUP` is `0x1000CD00` | **Agrees** | The gate sees its calls as `(5, 2, ptr, 0x1C)`: `D3DPT_TRIANGLESTRIP`, 2 primitives, a vertex pointer, a stride of 28. |
| The `dancer` device copy: `0x1066941C` holds the device | **The copy agrees; the device is not established by a definitive source** | `Dancer_InitDevice` (0x10251A80) copies `[[0x103D3CBC]+4]` to 0x10669418 (0x10251AFA) and `[[0x103D3CBC]+8]` to 0x1066941C (0x10251B0B), at +0x18 and +0x1C of the block at 0x10669400. That block's first field gets `0xB00000 − 0x200000` (0x10251B03) and +8 gets the 0xB00010-byte allocation (0x10251AA5). Nothing statically proves `[0x103D3CBC]+8` is the device. ffximain-gfx's next `facts=1` session measures the 218 calls through it. |
| The packed retail file's entry point is outside every section | **Not checkable here** | In the unpacked image the address lies inside `POL1`. Section sizes differ between the packed and unpacked files, so this neither confirms nor refutes the claim about the retail file. |

The other claims in these two documents were not checked in this pass. They are not confirmed by omission.

## 5. Found by gating the code, not stated in DancingMad

- **`Frame_Render` returns a byte.** Its only caller (0x10001B74) tests `al`, and both paths then call
  `_controlfp` before EAX is read again.
- **`exit_0` (0x100182E0) returns.** 0x10018310 returns at once when the byte at 0x10350E38 is 0. At all four call
  sites in `Frame_Render`, the code then continues with `add esp, 4; jmp 0x100121C4`. IDA marks `exit_0` as never
  returning, and Hex-Rays drops those paths.
- **`_chkstk` (0x10312150) saves and reloads ECX** and leaves it as it was. That settles which registers 49 more
  functions read.
- **The measured timer calls in `Frame_Render`'s wait** (0x10012B28, 0x10012BCB, 0x10012BF5) pop 0 and go to
  `CXiTimerLow` methods 9 and 8 (vtable 0x1032A118).

## 6. FINDINGS §1–17: checks made so far

This pass reads FINDINGS §1–17 for claims the code can settle. It is not finished. A claim not listed here has
not been checked.

### 6.1 The `0x1032B3B8` row of the vtable table (line 420)

All results below are read from the image: the vtable's dwords and the instructions of the functions named.

| Claim | Result | Evidence |
|---|---|---|
| Constructor `0x10052E90`, writes 412 at `+0x176` | **Agrees** | It calls `0x10044890`, stores `0x1032B3B8` at `[this]` and `0x19C` (412) at `+0x176`, and returns `this`. Its one caller is the call at 0x10050FAC in 0x1004E8D0. |
| `0x10052DC0` is not a function | **Agrees** | It is inside 0x10052DA0, the constructor that stores vtable `0x1032B2F8` and `0x1E0` at `+0x176`. |
| Destructor `0x10052E00` | **Does not match the code** | 0x10052E00 is the `call 0x10044970` inside 0x10052DF0, and no call, jump or dword refers to it. 0x10052DF0 is slot 6 of `0x1032B2F8` (at 0x1032B310), the class 0x10052DA0 builds, not `0x1032B3B8`. Slot 6 of `0x1032B3B8` is **0x10052ED0**. It stores `0x1032AD80` at `[this]`, calls `0x10044970`, frees `this` when bit 0 of its argument is set, and returns with `ret 4`. The symbol script's `CXi471011C8_VT_1032B3B8_Dtor` (§2) carries the same address. |
| `IsKind0` shared with `0x1032AD80` | **Agrees** | 0x10041120 is slot 12 of both vtables. |
| `RebuildBlendWeights`/`SubmitVertices` `0x10040E70`/`0x10040FB0` | **Agrees on the addresses** | Slots 18 and 20 of `0x1032B3B8`. The symbol script names 0x10040F50, an address inside 0x10040E70 that nothing refers to, `CMoD3mSpecularElem_Ctor` (§2). |
| `SetField198`/`GetField198` `0x10052EB0`/`0x10052EC0` | **Agrees on the addresses** | Slots 14 and 15. |

Slot 6 is taken to be the deleting destructor because of its shape: it takes a flag, frees `this` when bit 0 is
set, and returns `this`. That 0x10052ED0 stores the `0x1032AD80` vtable before calling `0x10044970` is what the
code does. Why it does so, for example a base class, is not established here. In `0x1032AD80`, slot 6 is
0x10041130, the deleting destructor the same table names.

### 6.2 Names that differ within DancingMad

Each address below has two names in this repository. The code was not used to choose between them.

| Address | FINDINGS.md | Elsewhere here |
|---|---|---|
| `0x10034330` | `IsReady` (line 499) | `Skel_BindShared` (FINDINGS line 2568; `tools/ffxi_symbols_ida.py`) |
| `0x1000D630` | `CEnv_UpdateDualTargetMode` (line 2632) | `CEnv_UpdateStereoMode` (`tools/ffxi_symbols_ida.py`, which says it was renamed) |
| `0x10276260` | `sqgxContext_Init` (line 948) | `sqgxContext_Create` (`tools/ffxi_symbols_ida.py`) |

### 6.3 The rest of the §5 table, and `CMoD3mSpecularElem`'s constructor

Read the same way, from the vtables' dwords and the functions' instructions.

| Vtable | Claim | Result | Evidence |
|---|---|---|---|
| `0x1032AC90` | Ctor `0x1003FB70`; dtor `0x1003FB10`; `IsKind` `0x1003FB40`; `RebuildBlendWeights`/`ReleaseBlendWeights` `0x1003FBB0`/`0x1003FC30` | **Agrees** | The ctor calls `0x10044890`, stores the vtable and `0x1C0` (448) at `+0x176`. 0x1003FB10 is the plain destructor: it frees `+0x1BC` and tail-jumps to `0x10044970`. Slot 6 is the deleting destructor 0x1003FB50, which calls it. The methods are slots 12, 18 and 20. |
| `0x1032AD80` | Ctor `0x10052F00`; plain dtor `0x10041110`; deleting `0x10041130`; `IsKind0` `0x10041120`; `SubmitVertices` `0x10040E20` | **Agrees** | The ctor stores the vtable and nothing at `+0x176`. 0x10041110 stores the vtable and tail-jumps to `0x10044970`. 0x10041130 is slot 6. The methods are slots 12 and 20. |
| `0x1032ADE8` | Ctor `0x10041F40` writes 424 at `+0x176` | **Agrees** | It stores `0x1A8` (424) after the vtable and returns with `ret 4`. Slot 6 is 0x10041FE0; the table leaves the destructor open, and it was not read here. |
| `0x1032B478` | Ctor `0x10052F80` writes 438; dtor `0x10052FB0`; `IsKind` `0x10052FA0`; `FadeRemaining` `0x10045D00`; `RebuildBlendWeights` `0x100565A0` | **Agrees** | `0x1B6` (438) at `+0x176`. The dtor is slot 6. The methods are slots 12, 17 and 18. |
| `0x1032AD20` (`CMoD3mSpecularElem`, line 401) | Constructor `0x10040F50`, stamps 448 | **Does not match the code** | The only function that stores `0x1032AD20` at `[this]` is **0x10041020** (at 0x10041032). It calls `0x10044890` first and stores `0x1C0` (448) at `+0x176`. Its one caller is the call at 0x10050FF1 in 0x1004E8D0, the function that also calls `0x10052E90`. 0x10040F50 is inside 0x10040E70, which is slot 18 of `0x1032B3B8` (§6.1). Slot 6 of `0x1032AD20` is 0x100410F0. |

0x10052ED0 (slot 6 of `0x1032B3B8`) has the same instructions as 0x10041130 (slot 6 of `0x1032AD80`), and both
store `0x1032AD80`. They are two separate copies. The code shows this; it does not show the class relationship.

### 6.4 Functions cited 0x10 past their start (§11, lines 1338–1360)

Eight of the functions §11's file-I/O race paragraph names are cited at an address exactly 0x10 bytes past the
function's first instruction. Six of those addresses do not fall on an instruction boundary. No call, jump,
push or immediate anywhere in the image refers to any of the eight. The function each one falls in is
referred to:

| Cited | Role in §11 | Function holding it | Referred to by |
|---|---|---|---|
| `0x10252F10` | trigger-file loader | 0x10252F00 | the call at 0x1024D48C (inside 0x1024D470, which the text cites as `0x1024D480`) |
| `0x10253030` | completion callback | 0x10253020 | `push 0x10253020` at 0x10252F13, inside the loader 0x10252F00 |
| `0x10071280` | resource factory | 0x10071270 | 5 calls |
| `0x100740D0` | evictor | 0x100740C0 | the call at 0x100712CD, inside 0x10071270 |
| `0x10072FE0` | main-thread loader | 0x10072FD0 | 10 calls |
| `0x100731C0` | main-thread loader | 0x100731B0 | 23 calls |
| `0x10245470` | lobby-entry loader | 0x10245460 | 5 calls |
| `0x100394E0` | thread pool | 0x100394D0 | the call at 0x10245629 |

The other addresses in the same paragraph are function starts. These were 0x10073430, 0x10071E90, 0x10245650
and 0x10013AD0.

The calls in the table agree with the paragraph's structure, read with the corrected addresses:
- the loader is called from 0x1024D470's code and pushes the callback's address;
- the factory calls the evictor.

Whether the race the paragraph describes happens was not checked.

Also in §13: the "small wrapper at `0x1002A394`" (line 2041) is an instruction inside 0x1002A380, a 46-byte
function called once, from 0x1002C344.

### 6.5 §12b: the `CXi*Actor` vtable lengths

The bounds below come from the image. Each vtable's dwords are read from its start, and each one is checked
for whether it is a function's first instruction. The table ends where something else begins: the first
address after the start that code refers to. The vtable addresses are those each class's constructor stores.

| Class (vtable) | §12b | From the code | Where it ends |
|---|---|---|---|
| `CXiActor` (`0x1032CFE0`) | 227 | **254** | Slots 0–253 are all function starts. 0x1032D3D8, slot 254's position, holds `0x45800000`. Nine functions read it as a float with `fmul dword ptr [0x1032D3D8]`, the first at 0x1008306B. |
| `CXiAtelActor` (`0x1032E3C8`) | 254 | 254 (agrees) | 0x1032E7C0, slot 254's position, is stored as a vtable by 0x100A9416 and 0x100A9617. |
| `CXiControlActor` (`0x1032DFC8`) | 255 | 255 (agrees) | Slot 255 is 0. |
| `CXiCollisionActor` (`0x1032DB40`) | 256 | 256 (agrees) | 0x1032DF40 is referred to by code. |
| `CXiSkeletonActor` (`0x10330F40`) | 264 | 264 (agrees) | Slot 264 holds `0x4096CBE4`, which is not code, and 0x10331360 is referred to by code. |

So `CXiActor`'s own table has 254 slots, not 227. Slots 227–253 of `CXiActor` and `CXiAtelActor` are
identical; the first is 0x10082920 in both. §12b's "27 new PC slots" (227–253) are therefore already in
`CXiActor`, and `CXiAtelActor` adds none. Over 0–253, `CXiAtelActor` differs from `CXiActor` only at slots 0,
6, 8 and 111.

Over the first 227 slots, §12b's counts are reproduced exactly:
- `CXiActor` and `CXiSkeletonActor` share 96;
- `CXiActor` and `CXiAtelActor` share 223.

`CXiControlActor` slot 254 is 0x100AAF30, as §12b says. 0x100AAF30 is also slot 254 of `CXiCollisionActor`.
That table's own new slot is 255, 0x100A4CE0.

**On ffximain-gfx's side:** its `data/class_vtables.json` lists 283 slots for `CXiAtelActor`. That runs 29
slots past 0x1032E7C0, into the next vtable, so that file is wrong for this class.
