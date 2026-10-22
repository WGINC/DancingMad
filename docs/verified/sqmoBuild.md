# sqmoBuild

### `0x102851C0` fn_102851C0

- **Verified C++** (`tree/src/sqmoBuild.cpp`): `XI_API int __cdecl fn_102851C0(undefined4 * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40` ×4, `sqDebugPrintf`, `fn_1028A0F0` ×6, `fn_10293F80`, `fn_102944E0`
- **Run by a frame** (frame_set.json): static

### `0x102852E0` fn_102852E0

- **Verified C++** (`tree/src/sqmoBuild.cpp`): `XI_API int __cdecl fn_102852E0(undefined4 * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40` ×3, `sqDebugPrintf`, `fn_1028A0F0` ×6, `fn_102957B0`
- **Run by a frame** (frame_set.json): static
