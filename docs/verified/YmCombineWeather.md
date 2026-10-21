# YmCombineWeather

### `0x1018AAC0` fn_1018AAC0

- **Verified C++** (`tree/src/YmCombineWeather.cpp`): `XI_API void __thiscall fn_1018AAC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1018AAC0 mov ecx, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10072540`
- **Run by a frame** (frame_set.json): static

### `0x1018AB40` fn_1018AB40

- **Verified C++** (`tree/src/YmCombineWeather.cpp`): `XI_API void __thiscall fn_1018AB40(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1018AB40 mov ecx, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10072540`
- **Run by a frame** (frame_set.json): static

### `0x1018ABF0` fn_1018ABF0

- **Verified C++** (`tree/src/YmCombineWeather.cpp`): `XI_API void __thiscall fn_1018ABF0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1018ABF4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10056EB0`, `sub_100742A0`, `ResourceIter_FindFirst` ×3, `fn_10074310`, `ResourceIter_FindNext` ×6, `fn_101880C0`, `sub_1018ABB0` ×2, `fn_1018AD50`, `fn_1018AD60`, `fn_1018AD80`, `fn_1018ADA0`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): static
