# sqrdTexture

### `0x10298B30` fn_10298B30

- **Verified C++** (`tree/src/sqrdTexture.cpp`): `XI_API undefined4 * __cdecl fn_10298B30(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `fn_10298B90`
- **Run by a frame** (frame_set.json): static

### `0x10298B90` fn_10298B90

- **Verified C++** (`tree/src/sqrdTexture.cpp`): `XI_API void __cdecl fn_10298B90(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
