# sqrdCamera

### `0x10291110` fn_10291110

- **Verified C++** (`tree/src/sqrdCamera.cpp`): `XI_API void __cdecl fn_10291110(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x102911E0` sqrdCamera_Apply

- **Verified C++** (`tree/src/sqrdCamera.cpp`): `XI_API void __cdecl sqrdCamera_Apply(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10283C10`
- **Run by a frame** (frame_set.json): static
