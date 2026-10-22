# unit_1029BCD0

### `0x1029BCD0` fn_1029BCD0

- **Verified C++** (`tree/src/unit_1029BCD0.cpp`): `XI_API void __cdecl fn_1029BCD0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 50 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static

### `0x1029BD40` fn_1029BD40

- **Verified C++** (`tree/src/unit_1029BCD0.cpp`): `XI_API void __cdecl fn_1029BD40(float param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static

### `0x1029C180` fn_1029C180

- **Verified C++** (`tree/src/unit_1029BCD0.cpp`): `XI_API void __cdecl fn_1029C180(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static

### `0x1029C1B0` fn_1029C1B0

- **Verified C++** (`tree/src/unit_1029BCD0.cpp`): `XI_API void __cdecl fn_1029C1B0(undefined4 param_1, undefined4 * param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqDebugPrintf`
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static
