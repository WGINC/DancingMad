# sqhiNode

### `0x10291B70` fn_10291B70

- **Verified C++** (`tree/src/sqhiNode.cpp`): `XI_API undefined4 * __cdecl fn_10291B70(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `fn_10291BA0`
- **Run by a frame** (frame_set.json): static

### `0x10291BA0` fn_10291BA0

- **Verified C++** (`tree/src/sqhiNode.cpp`): `XI_API void __cdecl fn_10291BA0(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1027EB00`, `M4fSet`, `sub_1027EBD0`
- **Run by a frame** (frame_set.json): static

### `0x10291C50` fn_10291C50

- **Verified C++** (`tree/src/sqhiNode.cpp`): `XI_API void __cdecl fn_10291C50(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10291F00` fn_10291F00

- **Verified C++** (`tree/src/sqhiNode.cpp`): `XI_API void __cdecl fn_10291F00(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10291F10` fn_10291F10

- **Verified C++** (`tree/src/sqhiNode.cpp`): `XI_API void __cdecl fn_10291F10(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
