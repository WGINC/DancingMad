# sqskJoint

### `0x10291360` fn_10291360

- **Verified C++** (`tree/src/sqskJoint.cpp`): `XI_API undefined4 * __cdecl fn_10291360(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `fn_10291390`
- **Run by a frame** (frame_set.json): static

### `0x10291390` fn_10291390

- **Verified C++** (`tree/src/sqskJoint.cpp`): `XI_API void __cdecl fn_10291390(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `fn_10274640`, `fn_10274670`, `fn_1027A6F0`, `fn_10289F50`
- **Run by a frame** (frame_set.json): static

### `0x10291460` fn_10291460

- **Verified C++** (`tree/src/sqskJoint.cpp`): `XI_API void __cdecl fn_10291460(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
