# CMoResource_VT_1032C778

### `0x10071A20` CMoResource_VT_1032C778::vf008

- **Verified C++** (`tree/src/CMoResource_VT_1032C778.cpp`): `char CMoResource_VT_1032C778::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10071A20 add ecx, 0x30` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `nullsub_13`, `nullsub_90`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071A30` CMoResource_VT_1032C778::vf009

- **Verified C++** (`tree/src/CMoResource_VT_1032C778.cpp`): `char CMoResource_VT_1032C778::vf009()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10071A30 add ecx, 0x30` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
