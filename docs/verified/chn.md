# chn

### `0x1027DB80` fn_1027DB80

- **Verified C++** (`tree/src/chn.cpp`): `XI_API void __cdecl fn_1027DB80(uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_10285740` ×2
- **Run by a frame** (frame_set.json): static

### `0x1027DCC0` fn_1027DCC0

- **Verified C++** (`tree/src/chn.cpp`): `XI_API uint32_t * __cdecl fn_1027DCC0(uint32_t * param_1, uint32_t param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275090` ×2, `fn_1027DF70`, `fn_10284F20`, `fn_1028D990`, `fn_102960A0`, `_strncpy`
- **Run by a frame** (frame_set.json): static

### `0x1027DD70` fn_1027DD70

- **Verified C++** (`tree/src/chn.cpp`): `XI_API void __cdecl fn_1027DD70(uint8_t * param_1, undefined4 xi_s2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1027DF70` fn_1027DF70

- **Verified C++** (`tree/src/chn.cpp`): `XI_API int __cdecl fn_1027DF70(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1027E060` fn_1027E060

- **Verified C++** (`tree/src/chn.cpp`): `XI_API void __cdecl fn_1027E060(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x1028D6F0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1027E0D0` fn_1027E0D0

- **Verified C++** (`tree/src/chn.cpp`): `XI_API void __cdecl fn_1027E0D0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
