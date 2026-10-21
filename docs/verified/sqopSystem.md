# sqopSystem

### `0x102531B0` sqopSystemActivate

- **Verified C++** (`tree/src/sqopSystem.cpp`): `XI_API undefined4 __cdecl sqopSystemActivate(uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `sqopTrackSetIndex`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqopSystemActivate` (not stated)
- **DancingMad note:** Resets every track's playback position to the start (via sqopTrackSetIndex(0)) after a successful build.

### `0x10289620` fn_10289620

- **Verified C++** (`tree/src/sqopSystem.cpp`): `XI_API void __cdecl fn_10289620(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x102896A0` fn_102896A0

- **Verified C++** (`tree/src/sqopSystem.cpp`): `XI_API void __cdecl fn_102896A0(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 74 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqFree`, `fn_10289620`, `fn_10289BA0`
- **Run by a frame** (frame_set.json): static
