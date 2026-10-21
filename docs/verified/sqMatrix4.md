# sqMatrix4

### `0x1027FCC0` sqMatrix4_1027FCC0

- **Verified C++** (`tree/src/sqMatrix4.cpp`): `XI_API long double __cdecl sqMatrix4_1027FCC0(float * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10296410` ×4, `fn_102967E0` ×4
- **Run by a frame** (frame_set.json): static

### `0x10280140` sqMatrix4_10280140

- **Verified C++** (`tree/src/sqMatrix4.cpp`): `XI_API void __cdecl sqMatrix4_10280140(float * param_1, float * param_2, float * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x10280650` fn_10280650

- **Verified C++** (`tree/src/sqMatrix4.cpp`): `XI_API void __cdecl fn_10280650(int param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_1027EBD0`
- **Run by a frame** (frame_set.json): static

### `0x102806B0` fn_102806B0

- **Verified C++** (`tree/src/sqMatrix4.cpp`): `XI_API void __cdecl fn_102806B0(int param_1, float param_2, float param_3, float param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
