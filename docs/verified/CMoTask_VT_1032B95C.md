# CMoTask_VT_1032B95C

### `0x10063130` CMoTask_VT_1032B95C::vf011

- **Verified C++** (`tree/src/CMoTask_VT_1032B95C.cpp`): `int CMoTask_VT_1032B95C::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x10056940 (tail_purges.json); entry ECX read: `0x10063130 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10063140` CMoTask_VT_1032B95C::vf012

- **Verified C++** (`tree/src/CMoTask_VT_1032B95C.cpp`): `int CMoTask_VT_1032B95C::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x1005F2C0 (tail_purges.json); entry ECX read: `0x10063140 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
