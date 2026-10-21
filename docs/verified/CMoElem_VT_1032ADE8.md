# CMoElem_VT_1032ADE8

### `0x10041AF0` CMoElem_VT_1032ADE8::vf18

- **Verified C++** (`tree/src/CMoElem_VT_1032ADE8.cpp`): `void CMoElem_VT_1032ADE8::vf18()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 30 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 95, town PASS 95, town2 PASS 95, combat PASS 82, zonetoinn PASS 95
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10041AF5 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::GetRenderTargetTop` ×2, `sub_1003B700`, `Font_DrawProjectedText3D`, `sub_10044C40`, `CXiActor_NameCalc`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_scratchValue`, `g_pResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10041FE0` CMoElem_VT_1032ADE8::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoElem_VT_1032ADE8.cpp`): `int * CMoElem_VT_1032ADE8::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10041FE1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
