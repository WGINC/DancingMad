# CMoLfdElem

### `0x10053030` fn_10053030

- **Verified C++** (`tree/src/CMoLfdElem.cpp`): `XI_API undefined8 __thiscall fn_10053030(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10053031 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoElem::Constructor`
- **Run by a frame** (frame_set.json): static

### `0x10053050` CMoLfdElem::vf012

- **Verified C++** (`tree/src/CMoLfdElem.cpp`): `BOOL CMoLfdElem::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10053060` CMoLfdElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoLfdElem.cpp`): `int * CMoLfdElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10053061 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoLfdElem_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100548B0` CMoLfdElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoLfdElem.cpp`): `char ** __cdecl CMoLfdElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoLfdElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor
