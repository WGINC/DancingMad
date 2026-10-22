# sqshCurves

### `0x102ACF20` fn_102ACF20

- **Verified C++** (`tree/src/sqshCurves.cpp`): `XI_API undefined4 * __cdecl fn_102ACF20(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40`, `fn_102ACF40`
- **Run by a frame** (frame_set.json): static

### `0x102ACF40` fn_102ACF40

- **Verified C++** (`tree/src/sqshCurves.cpp`): `XI_API void __cdecl fn_102ACF40(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_1028D9A0`
- **Run by a frame** (frame_set.json): static

### `0x102AD990` fn_102AD990

- **Verified C++** (`tree/src/sqshCurves.cpp`): `XI_API void __cdecl fn_102AD990(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40`, `sqFree`, `fn_102A9EF0`, `fn_102A9F30`, `sub_102AD1D0`, `sub_102AD770`
- **Run by a frame** (frame_set.json): static
