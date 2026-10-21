# sqVtx

### `0x102A9520` fn_102A9520

- **Verified C++** (`tree/src/sqVtx.cpp`): `XI_API undefined4 * __cdecl fn_102A9520(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40`, `fn_102A9550`
- **Run by a frame** (frame_set.json): static

### `0x102A9550` fn_102A9550

- **Verified C++** (`tree/src/sqVtx.cpp`): `XI_API void __cdecl fn_102A9550(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x102A9EF0` fn_102A9EF0

- **Verified C++** (`tree/src/sqVtx.cpp`): `XI_API void __cdecl fn_102A9EF0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 34 trials, 18 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_102A9980`
- **Run by a frame** (frame_set.json): static

### `0x102A9F30` fn_102A9F30

- **Verified C++** (`tree/src/sqVtx.cpp`): `XI_API void __cdecl fn_102A9F30(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 34 trials, 18 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_102A9980`
- **Run by a frame** (frame_set.json): static

### `0x102A9FB0` fn_102A9FB0

- **Verified C++** (`tree/src/sqVtx.cpp`): `XI_API void __cdecl fn_102A9FB0(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 30 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `sqFree`, `sub_10311C2C`
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static
