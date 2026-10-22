# sqopTrack

### `0x10289B40` fn_10289B40

- **Verified C++** (`tree/src/sqopTrack.cpp`): `XI_API void __cdecl fn_10289B40(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10289BA0` fn_10289BA0

- **Verified C++** (`tree/src/sqopTrack.cpp`): `XI_API void __cdecl fn_10289BA0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqFree`, `fn_10289B40`
- **Run by a frame** (frame_set.json): static

### `0x10289EF0` sqopTrackSetIndex

- **Verified C++** (`tree/src/sqopTrack.cpp`): `XI_API int __cdecl sqopTrackSetIndex(int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqopTrackSetIndex` (not stated)
- **DancingMad note:** Bounds-checked seek of a track's opcodeNdx.

### `0x10289F10` sqopTrackAdvance

- **Verified C++** (`tree/src/sqopTrack.cpp`): `XI_API undefined4 __cdecl sqopTrackAdvance(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `sqopTrackSetIndex`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqopTrackAdvance` (not stated)
- **DancingMad note:** Increments the track's opcodeNdx by one (via the bounds-checked sqopTrackSetIndex).
