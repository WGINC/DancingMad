# CMoResource_VT_1032C588

### `0x10071C90` CMoResource_VT_1032C588::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoResource_VT_1032C588.cpp`): `unsigned int ** CMoResource_VT_1032C588::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10071C91 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoResource_Destructor`
- **Run by a frame** (frame_set.json): stack

### `0x100745E0` CMoResource_VT_1032C588::vf011

- **Verified C++** (`tree/src/CMoResource_VT_1032C588.cpp`): `int CMoResource_VT_1032C588::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x1003C880 (tail_purges.json); entry ECX read: `0x100745E0 sub ecx, 0x30` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100745F0` CMoResource_VT_1032C588::vf012

- **Verified C++** (`tree/src/CMoResource_VT_1032C588.cpp`): `int CMoResource_VT_1032C588::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x10071C60 (tail_purges.json); entry ECX read: `0x100745F0 sub ecx, 0x30` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10074610` CMoResource_VT_1032C588::vf008

- **Verified C++** (`tree/src/CMoResource_VT_1032C588.cpp`): `void CMoResource_VT_1032C588::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10074620` CMoResource_VT_1032C588::vf009

- **Verified C++** (`tree/src/CMoResource_VT_1032C588.cpp`): `__int16 CMoResource_VT_1032C588::vf009()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100721F0 (tail_purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
