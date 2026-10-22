# unit_101D2FF0

### `0x101D30B0` fn_101D30B0

- **Verified C++** (`tree/src/unit_101D2FF0.cpp`): `XI_API void __thiscall fn_101D30B0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 78 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D30B1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x101D30F0` fn_101D30F0

- **Verified C++** (`tree/src/unit_101D2FF0.cpp`): `XI_API undefined4 __thiscall fn_101D30F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D30F0 mov ax, word ptr [ecx + 0x7e6]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x101D31B0` fn_101D31B0

- **Verified C++** (`tree/src/unit_101D2FF0.cpp`): `XI_API void __thiscall fn_101D31B0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D31B0 mov eax, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `ResHandle_FreeIfUnreferenced`, `CMoResource::ReleaseChain`
- **Run by a frame** (frame_set.json): static

### `0x101D3DC0` fn_101D3DC0

- **Verified C++** (`tree/src/unit_101D2FF0.cpp`): `XI_API void __thiscall fn_101D3DC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D3DC4 mov word ptr [ecx + 0x7e6], 0` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `fn_101CD900`
- **Run by a frame** (frame_set.json): static

### `0x101D3FC0` fn_101D3FC0

- **Verified C++** (`tree/src/unit_101D2FF0.cpp`): `XI_API void __thiscall fn_101D3FC0(void * self_, int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 93 returned normally, 93 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x101D3FC2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Camera_GetFrameScale`, `sub_1011FB60`, `Gfx_ProjectWorldToScreen`, `sub_10311C2C`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x101D5680` fn_101D5680

- **Verified C++** (`tree/src/unit_101D2FF0.cpp`): `XI_API void __thiscall fn_101D5680(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D5680 movsx eax, word ptr [ecx + 0x1c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_101D30F0`, `fn_101D3FC0`
- **Run by a frame** (frame_set.json): static
