# sqinSkin

### `0x10299FE0` fn_10299FE0

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API undefined4 * __cdecl fn_10299FE0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `fn_1029A000`
- **Run by a frame** (frame_set.json): static

### `0x1029A000` fn_1029A000

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API void __cdecl fn_1029A000(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_102AEC50`
- **Run by a frame** (frame_set.json): static

### `0x1029A160` fn_1029A160

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API void __cdecl fn_1029A160(int param_1, int param_2, undefined4 * param_3, undefined4 * param_4, undefined4 param_5, uint32_t param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 17 trials, 8 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 6 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80` ×2, `fn_102AEE90`
- **Run by a frame** (frame_set.json): static

### `0x1029A230` fn_1029A230

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API void __cdecl fn_1029A230(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 69 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1029A330` fn_1029A330

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API undefined4 __cdecl fn_1029A330(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275E90`
- **Run by a frame** (frame_set.json): static

### `0x1029A450` fn_1029A450

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API void __cdecl fn_1029A450(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 52 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10274650`, `sub_10275090` ×12, `sub_10275D80` ×2, `sqFree` ×2, `fn_1027C9D0`, `M4fSet`, `sqMatrix4_1027F0E0` ×2, `sqMatrix4_10280140`, `fn_102AEE90`
- **Reads globals:** `0x109A2830`, `0x109A2834`, `0x109A2838`, `0x109A283C`, `0x109A2844`
- **Writes globals:** `0x109A2830`, `0x109A2834`, `0x109A2838`, `0x109A283C`, `0x109A2844`
- **Run by a frame** (frame_set.json): static

### `0x1029A6F0` fn_1029A6F0

- **Verified C++** (`tree/src/sqinSkin.cpp`): `XI_API void __cdecl fn_1029A6F0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
