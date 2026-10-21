# CYyTexBase

### `0x10039770` CYyTexBase::GetRuntimeClass_variant0

- **Verified C++** (`tree/src/CYyTexBase.cpp`): `char ** __cdecl CYyTexBase::GetRuntimeClass_variant0()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyTexBase_GetRuntimeClass_variant0` (not stated)
- **DancingMad note:** SHARED accessor (x2) -- do not assume this specific stub identifies a specific subclass instance

### `0x10039780` CYyTexBase::GetRuntimeClass_variant1

- **Verified C++** (`tree/src/CYyTexBase.cpp`): `char ** __cdecl CYyTexBase::GetRuntimeClass_variant1()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyTexBase_GetRuntimeClass_variant1` (not stated)
- **DancingMad note:** SHARED accessor (x2) -- do not assume this specific stub identifies a specific subclass instance

### `0x100398B0` CYyTexBase::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyTexBase.cpp`): `_DWORD * CYyTexBase::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100398B1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CYyTexBase_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
