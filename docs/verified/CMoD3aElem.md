# CMoD3aElem

### `0x1003E6A0` CMoD3aElem::GetRuntimeClass_variant0

- **Verified C++** (`tree/src/CMoD3aElem.cpp`): `char ** __cdecl CMoD3aElem::GetRuntimeClass_variant0()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoD3aElem_GetRuntimeClass_variant0` (not stated)
- **DancingMad note:** SHARED accessor (x3) -- do not assume this specific stub identifies a specific subclass instance

### `0x1003EB30` CMoD3aElem::vf18

- **Verified C++** (`tree/src/CMoD3aElem.cpp`): `int * CMoD3aElem::vf18()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003EB30 mov eax, dword ptr [ecx + 0x104]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1003E910`
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): stack

### `0x1003EE50` CMoD3aElem::GetRuntimeClass_variant1

- **Verified C++** (`tree/src/CMoD3aElem.cpp`): `char ** __cdecl CMoD3aElem::GetRuntimeClass_variant1()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoD3aElem_GetRuntimeClass_variant1` (not stated)
- **DancingMad note:** SHARED accessor (x3) -- do not assume this specific stub identifies a specific subclass instance

### `0x1003EF00` CMoD3aElem::GetRuntimeClass_variant2

- **Verified C++** (`tree/src/CMoD3aElem.cpp`): `char ** __cdecl CMoD3aElem::GetRuntimeClass_variant2()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoD3aElem_GetRuntimeClass_variant2` (not stated)
- **DancingMad note:** SHARED accessor (x3) -- do not assume this specific stub identifies a specific subclass instance

### `0x10052CB0` CMoD3aElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoD3aElem.cpp`): `int * CMoD3aElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052CB1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): stack
