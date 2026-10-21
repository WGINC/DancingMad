# sqmoFrameChannel

### `0x10293F80` fn_10293F80

- **Verified C++** (`tree/src/sqmoFrameChannel.cpp`): `XI_API undefined4 * __cdecl fn_10293F80(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40`, `fn_10293FA0`
- **Run by a frame** (frame_set.json): static

### `0x10293FA0` fn_10293FA0

- **Verified C++** (`tree/src/sqmoFrameChannel.cpp`): `XI_API void __cdecl fn_10293FA0(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x102944E0` fn_102944E0

- **Verified C++** (`tree/src/sqmoFrameChannel.cpp`): `XI_API void __cdecl fn_102944E0(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1027D650`
- **Run by a frame** (frame_set.json): static
