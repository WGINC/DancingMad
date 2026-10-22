# sqmoUtil

### `0x1027D650` fn_1027D650

- **Verified C++** (`tree/src/sqmoUtil.cpp`): `XI_API void __cdecl fn_1027D650(int param_1, int param_2, int param_3, undefined1 * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 98 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqDebugPrintf` ×2
- **Run by a frame** (frame_set.json): static
