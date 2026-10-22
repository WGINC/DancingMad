# CMoResource_VT_1032C7FC

### `0x10019A30` CMoResource_VT_1032C7FC::vf004

- **Verified C++** (`tree/src/CMoResource_VT_1032C7FC.cpp`): `int CMoResource_VT_1032C7FC::vf004(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10019A30 mov ecx, dword ptr [ecx + 0x14]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10019A40` CMoResource_VT_1032C7FC::vf005

- **Verified C++** (`tree/src/CMoResource_VT_1032C7FC.cpp`): `void CMoResource_VT_1032C7FC::vf005(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071A00` CMoResource_VT_1032C7FC::vf009

- **Verified C++** (`tree/src/CMoResource_VT_1032C7FC.cpp`): `void CMoResource_VT_1032C7FC::vf009()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071AC0` CMoResource_VT_1032C7FC::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoResource_VT_1032C7FC.cpp`): `unsigned int ** CMoResource_VT_1032C7FC::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10071AC1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoResource::Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
