# CYyVb

### `0x1003B420` fn_1003B420

- **Verified C++** (`tree/src/CYyVb.cpp`): `XI_API undefined4 __thiscall fn_1003B420(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003B420 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1003B430` fn_1003B430

- **Verified C++** (`tree/src/CYyVb.cpp`): `XI_API void * __thiscall fn_1003B430(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003B431 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `fn_1003B4A0`
- **Run by a frame** (frame_set.json): stack

### `0x1003B450` CYyVb::Constructor

- **Verified C++** (`tree/src/CYyVb.cpp`): `void * __thiscall CYyVb::Constructor(void * self, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x1003B451 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003B4D0`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Stores CYyVb vtable, links it (sub_1003B4D0), and records size, FVF, usage, pool, in-use state 3 and the D3D VB pointer.

### `0x1003B4A0` fn_1003B4A0

- **Verified C++** (`tree/src/CYyVb.cpp`): `XI_API void __thiscall fn_1003B4A0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 80 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003B4A1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pVertexBufferListHead`
- **Run by a frame** (frame_set.json): stack
