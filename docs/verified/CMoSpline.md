# CMoSpline

### `0x10063450` CMoSpline::GetRuntimeClass

- **Verified C++** (`tree/src/CMoSpline.cpp`): `char ** __cdecl CMoSpline::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoSpline_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10063460` fn_10063460

- **Verified C++** (`tree/src/CMoSpline.cpp`): `XI_API undefined4 __thiscall fn_10063460(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10063460 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10063480` CMoSpline::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoSpline.cpp`): `int * CMoSpline::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10063481 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CMoSpline::Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100634A0` CMoSpline::Destructor

- **Verified C++** (`tree/src/CMoSpline.cpp`): `void __thiscall CMoSpline::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10063550 (tail_purges.json); entry ECX read: `0x100634A0 mov dword ptr [ecx], 0x1032c088` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Destructor of CMoSpline: restores vtable and frees spline data.
