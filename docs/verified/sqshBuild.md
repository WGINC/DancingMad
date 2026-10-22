# sqshBuild

### `0x10299D60` fn_10299D60

- **Verified C++** (`tree/src/sqshBuild.cpp`): `XI_API int __cdecl fn_10299D60(undefined4 * param_1, undefined4 * param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqDebugPrintf`, `fn_1028A0F0` ×5, `fn_102A9520`, `sub_102A9980`
- **Run by a frame** (frame_set.json): static
