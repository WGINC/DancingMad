# sqgxShape

### `0x1028AA70` sqgxShapeIndexBufferBegin

- **Verified C++** (`tree/src/sqgxShape.cpp`): `XI_API int * __cdecl sqgxShapeIndexBufferBegin(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 71 returned normally, 42 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 71, town PASS 71, town2 PASS 71, combat PASS 71, zonetoinn PASS 71
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `_malloc_0`
- **Indirect calls:** 3, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Lazily creates a 3072-entry dynamic 16-bit index buffer (or malloc in software mode), sets it as indices and locks it with DISCARD, resetting the write count.

### `0x1028AB50` fn_1028AB50

- **Verified C++** (`tree/src/sqgxShape.cpp`): `XI_API int __cdecl fn_1028AB50(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 29 returned normally, 11 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 29, town PASS 29, town2 PASS 29, combat PASS 29, zonetoinn PASS 29
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10311C2C` ×4
- **Reads constants** (.rdata): 1
- **Indirect calls:** 13, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1028AFE0` sqgxShapeBegin

- **Verified C++** (`tree/src/sqgxShape.cpp`): `XI_API int * __cdecl sqgxShapeBegin(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 89 returned normally, 155 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 89, town PASS 89, town2 PASS 89, combat PASS 89, zonetoinn PASS 89
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxTextureUpdate`, `nullsub_31`, `sqgxColorUpdate`, `sqgxMatrixUpdate`, `j_sqgxVertexShaderSelect`, `sub_1028A770` ×5, `sub_1028A790` ×4, `sub_1028BB10` ×4, `sub_1028BB70` ×4, `sub_10297320`, `sub_1029BD50`, `sub_1029BF50`, `sub_1029C480`, `sub_1029C610`, `sub_1029C950` ×2, `sub_10311C2C` ×4
- **Reads constants** (.rdata): 1
- **Indirect calls:** 35, of which 12 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
