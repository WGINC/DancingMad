# sqshDispList

### `0x102A2000` fn_102A2000

- **Verified C++** (`tree/src/sqshDispList.cpp`): `XI_API undefined4 * __cdecl fn_102A2000(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40`, `fn_102A2020`
- **Run by a frame** (frame_set.json): static

### `0x102A2020` fn_102A2020

- **Verified C++** (`tree/src/sqshDispList.cpp`): `XI_API void __cdecl fn_102A2020(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_1028D9A0`
- **Run by a frame** (frame_set.json): static
