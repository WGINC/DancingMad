# unit_1027CCF0

### `0x1027CCF0` fn_1027CCF0

- **Verified C++** (`tree/src/unit_1027CCF0.cpp`): `XI_API void __cdecl fn_1027CCF0(undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1027CFD0`
- **Run by a frame** (frame_set.json): static

### `0x1027CD30` fn_1027CD30

- **Verified C++** (`tree/src/unit_1027CCF0.cpp`): `XI_API void __cdecl fn_1027CD30(int param_1, int param_2, float * param_3, undefined4 param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1027A8A0`, `sub_1027C900` ×2, `fn_1027EAF0`, `M4fSet`, `M4fTransform`, `sqMatrix4_10280140`
- **Run by a frame** (frame_set.json): static

### `0x1027CFD0` fn_1027CFD0

- **Verified C++** (`tree/src/unit_1027CCF0.cpp`): `XI_API void __cdecl fn_1027CFD0(int param_1, int param_2, float * param_3, float * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1027C900` ×2, `fn_1027EAF0`, `M4fSet`, `M4fTransform`, `sqMatrix4_10280140`
- **Run by a frame** (frame_set.json): static
