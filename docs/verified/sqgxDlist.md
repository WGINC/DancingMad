# sqgxDlist

### `0x1029B620` sqgxDlistEnd

- **Verified C++** (`tree/src/sqgxDlist.cpp`): `XI_API _DWORD * __cdecl sqgxDlistEnd(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 9 returned normally, 168 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned; gates: fuzz PASS 9, town PASS 9, town2 PASS 9, combat PASS 9, zonetoinn PASS 9
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqFree` ×2
- **Indirect calls:** 6, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static

### `0x1029B9D0` sqgxDlistDraw

- **Verified C++** (`tree/src/sqgxDlist.cpp`): `XI_API void __cdecl sqgxDlistDraw(IDirect3DVertexBuffer8 **a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 553 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1028A730`, `sqgxShapeBegin`
- **Indirect calls:** 9, of which 9 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
