# CYyModel

### `0x100298C0` CYyModel::GetRuntimeClass

- **Verified C++** (`tree/src/CYyModel.cpp`): `char ** __cdecl CYyModel::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModel_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1002B4B0` CYyModel::Constructor

- **Verified C++** (`tree/src/CYyModel.cpp`): `void __thiscall CYyModel::Constructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1002B4B1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1001D170`, `fn_10025260`, `fn_10025BF0`, `fn_10033710`, `fn_10038A20`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): CYyModel constructor: constructs members, sets the CYyModel vtable and zeroes/initialises fields.

### `0x1002B530` CYyModel::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyModel.cpp`): `int * CYyModel::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1002B531 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CYyModel::Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1002B550` CYyModel::Destructor

- **Verified C++** (`tree/src/CYyModel.cpp`): `void __thiscall CYyModel::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 77 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x100337C0 (tail_purges.json); entry ECX read: `0x1002B551 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_1001D1F0`, `ProjTex_Destructor`, `sub_10025C30`, `sub_10038A60`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): CYyModel destructor: sets vtable, deletes the owned object at +0x44 and destroys members in reverse order.

### `0x1002B5A0` CYyModel::GetField44Addr

- **Verified C++** (`tree/src/CYyModel.cpp`): `int __thiscall CYyModel::GetField44Addr(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1002B5A0 lea eax, [ecx + 0x44]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns the address of the field at this+0x44.

### `0x1002B6A0` CYyModel::CreateModelBase

- **Verified C++** (`tree/src/CYyModel.cpp`): `undefined4 __thiscall CYyModel::CreateModelBase(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1002B6A6 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10029D30`, `fn_1002B630`, `Mem_AllocDefault`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Allocates and constructs a 200-byte model-base object and attaches it to this model.
