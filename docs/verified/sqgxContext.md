# sqgxContext

### `0x10284B20` sqgxShader

- **Verified C++** (`tree/src/sqgxContext.cpp`): `XI_API int * __cdecl sqgxShader(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 46 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxTextureDecal` ×4, `sqgxTextureClamp` ×5, `nullsub_32`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Writes globals:** `g_sqgxShaderDirty`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqgxContext_SelectShaderMode` (confirmed) — differs from this repository's `sqgxShader`
- **DancingMad note:** Shared shader-mode/permutation selector, confirmed called from at least 3 of the 5 shader bake functions (Generic, Sampling, Aniso) with type-specific bitmask constants. Not traced to its own implementation.
