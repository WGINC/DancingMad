# YkJpeg

### `0x101CF870` fn_101CF870

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API void __thiscall fn_101CF870(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 57 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101CF871 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_101CF820` ×4, `fn_101D09C0` ×4, `fn_101D09E0` ×8, `fn_101D0A20` ×4, `fn_101D0A40` ×4
- **Run by a frame** (frame_set.json): static

### `0x101CFDB0` fn_101CFDB0

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API void __stdcall fn_101CFDB0(int param_1, int param_2, int param_3, int param_4, int param_5, int param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 24` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x101CFE20` fn_101CFE20

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API int __stdcall fn_101CFE20(uint32_t param_1, int * param_2, int * param_3, int param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x101CFEB0` fn_101CFEB0

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API void __thiscall fn_101CFEB0(void * self_, int param_1, int param_2, int param_3, int param_4, int param_5, int * param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x101CFEC0 mov dword ptr [esp + 0xc], ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_101CFE20` ×2
- **Run by a frame** (frame_set.json): static

### `0x101CFF60` fn_101CFF60

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API void __stdcall fn_101CFF60(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x101D0210` fn_101D0210

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API void __thiscall fn_101D0210(void * self_, int * param_1, char * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x101D021A mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_101D0970` ×6
- **Run by a frame** (frame_set.json): static

### `0x101D0370` fn_101D0370

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API undefined4 __thiscall fn_101D0370(void * self_, uint32_t param_1, uint32_t param_2, int param_3, int param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 10 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x101D0378 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `Mem_AllocDefault`, `fn_101CF660`, `fn_101CF870`, `sub_101CFA00`, `fn_101CFDB0`, `fn_101CFEB0`, `fn_101CFF60` ×3, `sub_101D01B0` ×3, `fn_101D0210` ×3, `fn_101D05E0` ×2, `fn_101D0860`, `fn_101D0880`, `fn_101D08E0`, `fn_101D09E0` ×5, `fn_101D0A20` ×3, `fn_101D0A40`, `fn_101D0A60`, `Allocator_Generic`
- **Run by a frame** (frame_set.json): static

### `0x101D05E0` fn_101D05E0

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API undefined * __cdecl fn_101D05E0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_101C8D70`, `_sprintf`
- **Run by a frame** (frame_set.json): static

### `0x101D0600` fn_101D0600

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API int __thiscall fn_101D0600(void * self_, uint32_t param_1, uint32_t param_2, int param_3, int param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x101D060A mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_101D0370`, `fn_101D0880`
- **Run by a frame** (frame_set.json): static

### `0x101D08C0` fn_101D08C0

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API undefined4 __thiscall fn_101D08C0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D08C0 mov edx, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_101D0860`
- **Run by a frame** (frame_set.json): static

### `0x101D08D0` fn_101D08D0

- **Verified C++** (`tree/src/YkJpeg.cpp`): `XI_API void __thiscall fn_101D08D0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x101D0880 (tail_purges.json); entry ECX read: `0x101D08D0 mov dword ptr [ecx], 0x10337e80` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): static
