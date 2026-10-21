# CYyModelDt_VT_1032A430

### `0x10025090` CYyModelDt_VT_1032A430::vf011

- **Verified C++** (`tree/src/CYyModelDt_VT_1032A430.cpp`): `int CYyModelDt_VT_1032A430::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100250A0` CYyModelDt_VT_1032A430::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyModelDt_VT_1032A430.cpp`): `int * CYyModelDt_VT_1032A430::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100250A1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelDt_Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100252D0` CYyModelDt_VT_1032A430::ScalarDeletingDtor_2

- **Verified C++** (`tree/src/CYyModelDt_VT_1032A430.cpp`): `int CYyModelDt_VT_1032A430::ScalarDeletingDtor_2(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100252D1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `ProjTex_Destructor`, `operator_delete`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
