# sqsnScene

### `0x1028E1B0` fn_1028E1B0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028E1B0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 26 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqFree` ×9, `fn_10281A70`, `sub_10285740`
- **Reads globals:** `g_sceneFadeMaskRT`
- **Writes globals:** `g_sceneFadeMaskRT`
- **Run by a frame** (frame_set.json): static

### `0x1028E350` fn_1028E350

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028E350(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10298B90 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1028EBF0` fn_1028EBF0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028EBF0(int param_1, int param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028EC30` fn_1028EC30

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028EC30(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028EC50` fn_1028EC50

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028EC50(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028ECC0` fn_1028ECC0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028ECC0(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028ECE0` fn_1028ECE0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028ECE0(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028ED00` fn_1028ED00

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API int __cdecl fn_1028ED00(int param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 77 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275E90`
- **Run by a frame** (frame_set.json): static

### `0x1028ED50` fn_1028ED50

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API int __cdecl fn_1028ED50(int param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 67 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275E90` ×2
- **Run by a frame** (frame_set.json): static

### `0x1028EDE0` fn_1028EDE0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API int __cdecl fn_1028EDE0(int param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, int param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 15 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 5 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275E90` ×3, `fn_1028EFB0`
- **Run by a frame** (frame_set.json): static

### `0x1028EFB0` fn_1028EFB0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028EFB0(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1028F130` fn_1028F130

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API int __cdecl fn_1028F130(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 76 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275E90`
- **Run by a frame** (frame_set.json): static

### `0x1028F220` fn_1028F220

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028F220(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028F3C0` fn_1028F3C0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028F3C0(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 86 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275E90`
- **Run by a frame** (frame_set.json): static

### `0x1028F430` fn_1028F430

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API int __cdecl fn_1028F430(int param_1, uint32_t param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1028F4A0` fn_1028F4A0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028F4A0(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1028F4C0` fn_1028F4C0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028F4C0(undefined4 param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxMatrixShape`, `sub_102A1F20`
- **Run by a frame** (frame_set.json): static

### `0x1028F5F0` sqsnScene_1028F5F0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnScene_1028F5F0(int param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 98 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026E3D0`, `fn_10283260` ×4, `fn_10283300` ×3, `fn_10283DA0`, `fn_10283DE0`
- **Run by a frame** (frame_set.json): static

### `0x1028F6E0` fn_1028F6E0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028F6E0(int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 33 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026E3D0` ×2, `fn_10283260` ×4, `fn_10283300` ×4, `fn_10283DA0` ×2, `fn_10283DE0` ×2
- **Run by a frame** (frame_set.json): static

### `0x1028F8C0` sqsnSceneDraw

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnSceneDraw(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 64 returned normally, 267 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 64, town PASS 71, town2 PASS 72, combat PASS 71, zonetoinn PASS 72
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxSprite`, `sqgxTextureAdd` ×3, `sqgxTextureGetSize`, `sqgxTextureSet` ×2, `sqgxTextureDecal` ×2, `sqgxTextureClamp` ×2, `sqgxTextureStencilClear`, `sqgxTextureClear` ×4, `sqgxTextureDraw` ×7, `sqgxZTest` ×4, `sqgxBlendTrsp`, `sqgxBlendOff` ×2, `sqgxColor`, `sqgxMatrixCamera` ×2, `sqsnSceneLayerDraw` ×2, `sqsnSceneLayerDrawShadowed` ×2, `sqsnSceneLayerSnapShotComposite`, `fn_10290430` ×2, `sqsnSceneLayerSort`, `sqrdCamera_Apply` ×2
- **Reads constants** (.rdata): 4
- **Indirect calls:** 8, of which 8 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_sceneFadeMaskRT`, `g_pDancerDevice`, `g_pSqgxContext`, `g_sceneRT`, `g_sceneRT1`
- **Writes globals:** `g_sceneFadeMaskRT`, `g_sceneRT`, `g_sceneRT1`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws all scene layers: renders snapshot layers into ping-pong 1024x512 render targets and composites them, draws normal/shadowed layers with pre/post callbacks, and applies a stencil-masked fade when scene alpha < 1.

### `0x1028FDD0` sqsnSceneLayerDraw

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnSceneLayerDraw(int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 47 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxMatrixCamera`, `fn_1028F4C0` ×2, `fn_1028F6E0` ×2, `fn_1028FF80`, `sqrdCamera_Apply`, `fn_102A2130`
- **Run by a frame** (frame_set.json): static

### `0x1028FF80` fn_1028FF80

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_1028FF80(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10282350 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxSprite`, `sqgxTextureSet`, `sqgxTextureDecal`, `sqgxTextureDraw` ×2, `sqgxZTest`
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static

### `0x1028FFF0` sqsnSceneLayerDrawShadowed

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnSceneLayerDrawShadowed(int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 36 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxMatrixCamera` ×2, `fn_1028F4C0` ×2, `fn_1028F6E0` ×2, `fn_1028FF80`, `sqrdCamera_Apply` ×2, `fn_102A2130`, `fn_102A2160`, `fn_102A2190`, `sqsnPlanarShadowDraw`, `fn_102A2720`, `fn_102A2C00`
- **Run by a frame** (frame_set.json): static

### `0x102902C0` sqsnSceneLayerSnapShotComposite

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnSceneLayerSnapShotComposite(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_102813B0`
- **Run by a frame** (frame_set.json): static

### `0x10290430` fn_10290430

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_10290430(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10290440` sqsnSceneLayerSort

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnSceneLayerSort(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 20 trials, 7 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `M4fTransform`, `M4fTranspose`, `sqMatrix4_10280140`, `sqgxMatrixCamera`, `sqgxMatrixShape`, `fn_1028DBB0`
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static

### `0x10290610` fn_10290610

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_10290610(int param_1, int param_2, int param_3, int param_4, int param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 79 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 5 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80` ×5, `sqDebugPrintf` ×5, `fn_1028EFB0`
- **Run by a frame** (frame_set.json): static

### `0x102907C0` fn_102907C0

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_102907C0(int param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 92 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80` ×2, `sqDebugPrintf`
- **Run by a frame** (frame_set.json): static

### `0x10290840` fn_10290840

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl fn_10290840(int param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `sqDebugPrintf`
- **Run by a frame** (frame_set.json): static
