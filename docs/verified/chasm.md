# chasm

### `0x10273920` chasm_10273920

- **Verified C++** (`tree/src/chasm.cpp`): `XI_API void __cdecl chasm_10273920(uint8_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqFree` ×2, `fn_1027E0D0` ×2
- **Run by a frame** (frame_set.json): static

### `0x10273D60` fn_10273D60

- **Verified C++** (`tree/src/chasm.cpp`): `XI_API undefined4 __cdecl fn_10273D60(int param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10274370`
- **Run by a frame** (frame_set.json): static

### `0x10273E80` fn_10273E80

- **Verified C++** (`tree/src/chasm.cpp`): `XI_API undefined4 __cdecl fn_10273E80(int param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026F900` ×4, `fn_10273E80` ×2
- **Run by a frame** (frame_set.json): static
