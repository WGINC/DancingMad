# sqshTriStrip

### `0x102AA2D0` fn_102AA2D0

- **Verified C++** (`tree/src/sqshTriStrip.cpp`): `XI_API undefined4 * __cdecl fn_102AA2D0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40`, `fn_102AA2F0`
- **Run by a frame** (frame_set.json): static

### `0x102AA2F0` fn_102AA2F0

- **Verified C++** (`tree/src/sqshTriStrip.cpp`): `XI_API void __cdecl fn_102AA2F0(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_1028D9A0`
- **Run by a frame** (frame_set.json): static

### `0x102ABEB0` fn_102ABEB0

- **Verified C++** (`tree/src/sqshTriStrip.cpp`): `XI_API undefined4 __cdecl fn_102ABEB0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `0x109AAAC0`
- **Run by a frame** (frame_set.json): static

### `0x102ABEC0` fn_102ABEC0

- **Verified C++** (`tree/src/sqshTriStrip.cpp`): `XI_API void __cdecl fn_102ABEC0(int param_1, undefined * param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 22 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x109AAAC0`
- **Writes globals:** `0x109AAAC0`
- **Run by a frame** (frame_set.json): static
