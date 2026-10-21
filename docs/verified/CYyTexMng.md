# CYyTexMng

### `0x1003AA40` CYyTexMng::GetRuntimeClass

- **Verified C++** (`tree/src/CYyTexMng.cpp`): `char ** __cdecl CYyTexMng::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyTexMng_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1003AA50` fn_1003AA50

- **Verified C++** (`tree/src/CYyTexMng.cpp`): `XI_API undefined4 __thiscall fn_1003AA50(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003AA50 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1003AA70` CYyTexMng::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyTexMng.cpp`): `_DWORD * CYyTexMng::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003AA71 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CYyTexMng_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1003AC80` CYyTexMng::FindByName

- **Verified C++** (`tree/src/CYyTexMng.cpp`): `undefined8 __thiscall CYyTexMng::FindByName(void * self, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 68 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003AAB0`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Walks the texture manager's linked list and returns the first texture (not flagged 8) whose 16-byte name at +12 equals a2.

### `0x1003AF10` CYyTexMng::FindByNameInResource

- **Verified C++** (`tree/src/CYyTexMng.cpp`): `int __thiscall CYyTexMng::FindByNameInResource(void * self, char * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 79 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1003AF11 mov dword ptr [esp], ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003AAB0`, `CMoResource::FindInScope` ×2
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Walks a resource chain (type 32 lookups) to find the resource whose 16-byte name matches a2, then returns the texture in the manager list owned by that resource.
