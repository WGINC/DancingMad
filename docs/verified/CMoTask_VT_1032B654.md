# CMoTask_VT_1032B654

### `0x10053350` CMoTask_VT_1032B654::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoTask_VT_1032B654.cpp`): `_DWORD * CMoTask_VT_1032B654::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10053351 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoTask_VT_1032B654_Destructor`
- **Run by a frame** (frame_set.json): stack

### `0x10054460` CMoTask_VT_1032B654::vf011

- **Verified C++** (`tree/src/CMoTask_VT_1032B654.cpp`): `int CMoTask_VT_1032B654::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100542E0 (tail_purges.json); entry ECX read: `0x10054460 sub ecx, 0x30` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10054470` CMoTask_VT_1032B654::vf012

- **Verified C++** (`tree/src/CMoTask_VT_1032B654.cpp`): `int CMoTask_VT_1032B654::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x10053840 (tail_purges.json); entry ECX read: `0x10054470 sub ecx, 0x30` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
