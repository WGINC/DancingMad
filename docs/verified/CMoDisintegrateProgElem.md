# CMoDisintegrateProgElem

### `0x100426B0` CMoDisintegrateProgElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoDisintegrateProgElem.cpp`): `char ** __cdecl CMoDisintegrateProgElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDisintegrateProgElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x100426C0` CMoDisintegrateProgElem::vf018

- **Verified C++** (`tree/src/CMoDisintegrateProgElem.cpp`): `void CMoDisintegrateProgElem::vf018()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100530F0` fn_100530F0

- **Verified C++** (`tree/src/CMoDisintegrateProgElem.cpp`): `XI_API undefined8 __thiscall fn_100530F0(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100530F1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoElem::Constructor`
- **Run by a frame** (frame_set.json): static

### `0x10053130` CMoDisintegrateProgElem::vf012

- **Verified C++** (`tree/src/CMoDisintegrateProgElem.cpp`): `BOOL CMoDisintegrateProgElem::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10053140` CMoDisintegrateProgElem::vf008

- **Verified C++** (`tree/src/CMoDisintegrateProgElem.cpp`): `int CMoDisintegrateProgElem::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x10053140 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10053150` CMoDisintegrateProgElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoDisintegrateProgElem.cpp`): `int * CMoDisintegrateProgElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10053151 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`, `MoProgElem_FreeBuffer40`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
