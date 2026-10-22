# sqmdSort

### `0x1029B100` fn_1029B100

- **Verified C++** (`tree/src/sqmdSort.cpp`): `XI_API undefined4 * __cdecl fn_1029B100(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `fn_1029B120`
- **Run by a frame** (frame_set.json): static

### `0x1029B120` fn_1029B120

- **Verified C++** (`tree/src/sqmdSort.cpp`): `XI_API void __cdecl fn_1029B120(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1029B310` fn_1029B310

- **Verified C++** (`tree/src/sqmdSort.cpp`): `XI_API void __cdecl fn_1029B310(int * param_1, int * param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 16 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80` ×2
- **Run by a frame** (frame_set.json): static
