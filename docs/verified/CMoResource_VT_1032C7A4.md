# CMoResource_VT_1032C7A4

### `0x10038920` CMoResource_VT_1032C7A4::vf008

- **Verified C++** (`tree/src/CMoResource_VT_1032C7A4.cpp`): `void CMoResource_VT_1032C7A4::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071A10` CMoResource_VT_1032C7A4::vf009

- **Verified C++** (`tree/src/CMoResource_VT_1032C7A4.cpp`): `void CMoResource_VT_1032C7A4::vf009()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071B00` CMoResource_VT_1032C7A4::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoResource_VT_1032C7A4.cpp`): `unsigned int ** CMoResource_VT_1032C7A4::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10071B01 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoResource::Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
