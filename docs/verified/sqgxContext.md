# sqgxContext

### `0x10276260` sqgxContext_Create

- **Verified C++** (`tree/src/sqgxContext.cpp`): `XI_API undefined4 __cdecl sqgxContext_Create(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `sqgxContext_Init`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqgxContext_Create` (confirmed)
- **DancingMad note:** Allocates 3624 bytes -- by far the largest confirmed object in this project. The central Direct3D device state-cache object.

### `0x10276290` sqgxContext_Init

- **Verified C++** (`tree/src/sqgxContext.cpp`): `XI_API void __cdecl sqgxContext_Init(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10274670`, `PackVec4` ×5, `fn_1027EB50`, `sub_1027EBD0` ×5
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqgxContext_Init` (not stated)
- **DancingMad note:** CAPSTONE FINDING for sqGrafix: seeds a complete 16-texture-stage state cache with every value at -1 (the classic 'force the first real state-change to apply' sentinel) -- confirms this subsystem already implements proper render-state deduplication, not naive per-call resubmission. Also seeds per-light state for 8 hardware lights and a 640x480 default viewport.

### `0x10284B20` sqgxShader

- **Verified C++** (`tree/src/sqgxContext.cpp`): `XI_API int * __cdecl sqgxShader(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 46 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxTextureDecal` ×4, `sqgxTextureClamp` ×5, `fn_10284EB0`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Writes globals:** `g_sqgxShaderDirty`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqgxContext_SelectShaderMode` (confirmed) — differs from this repository's `sqgxShader`
- **DancingMad note:** Shared shader-mode/permutation selector, confirmed called from at least 3 of the 5 shader bake functions (Generic, Sampling, Aniso) with type-specific bitmask constants. Not traced to its own implementation.
