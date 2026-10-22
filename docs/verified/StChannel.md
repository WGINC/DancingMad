# StChannel

### `0x10251070` fn_10251070

- **Verified C++** (`tree/src/StChannel.cpp`): `XI_API uint32_t __cdecl fn_10251070(uint32_t * param_1, int param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10017D20`, `fn_1026EF00`, `sub_1026EFB0`, `sub_1026F080`, `fn_1026F4F0`, `fn_1026F9A0`, `sub_10311C2C`
- **Run by a frame** (frame_set.json): static

### `0x10251160` fn_10251160

- **Verified C++** (`tree/src/StChannel.cpp`): `XI_API undefined4 __cdecl fn_10251160(uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10251180` fn_10251180

- **Verified C++** (`tree/src/StChannel.cpp`): `XI_API undefined4 __cdecl fn_10251180(uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `fn_101C4A30`
- **Reads globals:** `g_pFileMng`
- **Run by a frame** (frame_set.json): static

### `0x102511B0` fn_102511B0

- **Verified C++** (`tree/src/StChannel.cpp`): `XI_API undefined4 __cdecl fn_102511B0(uint8_t * param_1, float param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `fn_1026F4F0`
- **Run by a frame** (frame_set.json): static

### `0x10251200` fn_10251200

- **Verified C++** (`tree/src/StChannel.cpp`): `XI_API undefined4 __cdecl fn_10251200(uint8_t * param_1, undefined4 param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026F4F0`, `fn_1027DD70`, `fn_102857D0`, `fn_102857E0` ×2, `fn_102857F0`
- **Run by a frame** (frame_set.json): static

### `0x102512B0` StChannelItemClear

- **Verified C++** (`tree/src/StChannel.cpp`): `XI_API undefined4 __cdecl StChannelItemClear(uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqFree`, `sub_10285740`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StChannelItemClear` (not stated)
- **DancingMad note:** Matches the StModelItemClear naming pattern. Checks a 'valid' flag, dispatches cleanup based on whether the item was built via sqmoChannelBuildSQO (calls its own release) or just holds a raw loaded buffer (frees it directly via sqFree). Called repeatedly inside StAvatar_ReleaseResources's array-clearing loops.
