# CYyCamMng2

### `0x1001E2F0` fn_1001E2F0

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `XI_API void __cdecl fn_1001E2F0(undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `0x10456DB0`
- **Writes globals:** `0x10456DB0`, `0x10456DB1`, `0x10456DB4`
- **Run by a frame** (frame_set.json): static

### `0x1001E470` CYyCamMng2::CreateGlobal

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `undefined4 __cdecl CYyCamMng2::CreateGlobal()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10015100`, `fn_1001E590`, `fn_1001E600`, `Mem_AllocDefault`
- **Reads globals:** `0x10456D6C`
- **Writes globals:** `0x10456D6C`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Allocates and constructs a 280-byte object, stores it in global dword_10456D6C, initialises it and returns the result of sub_10015100 on it.

### `0x1001E4B0` CYyCamMng2::CallGlobalVfunc1

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `void __cdecl CYyCamMng2::CallGlobalVfunc1()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x10456D6C`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): If the global object dword_10456D6C exists, calls its vtable slot 1 with &unk_10351224.

### `0x1001E4D0` fn_1001E4D0

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `XI_API long double __cdecl fn_1001E4D0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Calls directly:** `Camera_GetField50` ×2
- **Run by a frame** (frame_set.json): static

### `0x1001E4F0` fn_1001E4F0

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `XI_API void __thiscall fn_1001E4F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1001E4F3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10015290`, `fn_10026E50`, `Vec3_Copy` ×4
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static

### `0x1001E590` fn_1001E590

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `XI_API void __thiscall fn_1001E590(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1001E591 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1001E4F0`
- **Run by a frame** (frame_set.json): static

### `0x1001E600` fn_1001E600

- **Verified C++** (`tree/src/CYyCamMng2.cpp`): `XI_API void * __thiscall fn_1001E600(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1001E602 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1001E2F0`, `fn_1001E590`, `fn_10027990`
- **Writes globals:** `0x10456D70`, `0x10456D74`, `0x10456D78`, `0x10456D7C`, `0x10456D80`, `0x10456D84`, `0x10456D88`, `0x10456D8C`, `0x10456D90`, `0x10456D94`, `0x10456D98`, `0x10456D9C`, `0x10456DA0`, `0x10456DA4`, `0x10456DA8`
- **Run by a frame** (frame_set.json): static
