# CYyModelDt_VT_1032A72C

### `0x1002A0A0` CYyModelDt_VT_1032A72C::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyModelDt_VT_1032A72C.cpp`): `_DWORD * CYyModelDt_VT_1032A72C::ScalarDeletingDtor(char a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1002A0A1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelDtBase_Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): stack
