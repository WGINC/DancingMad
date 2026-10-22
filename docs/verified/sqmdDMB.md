# sqmdDMB

### `0x10288660` fn_10288660

- **Verified C++** (`tree/src/sqmdDMB.cpp`): `XI_API int __cdecl fn_10288660(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `0x109A278C`
- **Writes globals:** `0x109A278C`
- **Run by a frame** (frame_set.json): static

### `0x10288680` fn_10288680

- **Verified C++** (`tree/src/sqmdDMB.cpp`): `XI_API uint32_t __cdecl fn_10288680(uint32_t param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10288660`, `sub_10314D55`
- **Reads globals:** `0x109A2788`
- **Run by a frame** (frame_set.json): static

### `0x10288BB0` fn_10288BB0

- **Verified C++** (`tree/src/sqmdDMB.cpp`): `XI_API undefined4 __cdecl fn_10288BB0(int param_1, uint32_t param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 40 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10288660`, `fn_10288680`, `sub_10314D55`
- **Reads globals:** `0x109A2788`
- **Run by a frame** (frame_set.json): static

### `0x10288C20` fn_10288C20

- **Verified C++** (`tree/src/sqmdDMB.cpp`): `XI_API char * __cdecl fn_10288C20(int param_1, uint32_t param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 17 trials, 2 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10288660` ×5, `fn_10288680`, `sub_10314D55` ×5
- **Reads globals:** `0x109A2788`
- **Run by a frame** (frame_set.json): static

### `0x10288DC0` fn_10288DC0

- **Verified C++** (`tree/src/sqmdDMB.cpp`): `XI_API void __cdecl fn_10288DC0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 15 trials, 7 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x10288E00` fn_10288E00

- **Verified C++** (`tree/src/sqmdDMB.cpp`): `XI_API void __cdecl fn_10288E00(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 25 trials, 8 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
