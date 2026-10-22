# YkFurniture

### `0x101CCE00` fn_101CCE00

- **Verified C++** (`tree/src/YkFurniture.cpp`): `XI_API int __cdecl fn_101CCE00(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x101CD900` fn_101CD900

- **Verified C++** (`tree/src/YkFurniture.cpp`): `XI_API void __thiscall fn_101CD900(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 146 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101CD901 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100AB320`, `fn_100AB550`, `fn_100C3E70`, `fn_101CD9D0` ×2, `fn_101CDA00` ×2, `fn_101CDA30` ×2
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
