# CMoD3aLightmapElem

### `0x1003EE60` CMoD3aLightmapElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoD3aLightmapElem.cpp`): `char ** __cdecl CMoD3aLightmapElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoD3aLightmapElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10052C30` fn_10052C30

- **Verified C++** (`tree/src/CMoD3aLightmapElem.cpp`): `XI_API undefined8 __thiscall fn_10052C30(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10052C31 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoElem::Constructor`
- **Run by a frame** (frame_set.json): static

### `0x10052C50` CMoD3aLightmapElem::set_field_194

- **Verified C++** (`tree/src/CMoD3aLightmapElem.cpp`): `int CMoD3aLightmapElem::set_field_194(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052C54 mov dword ptr [ecx + 0x194], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10052C60` CMoD3aLightmapElem::get_field_194

- **Verified C++** (`tree/src/CMoD3aLightmapElem.cpp`): `int CMoD3aLightmapElem::get_field_194()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10052C60 mov eax, dword ptr [ecx + 0x194]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10052C70` CMoD3aLightmapElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoD3aLightmapElem.cpp`): `int * CMoD3aLightmapElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052C71 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
