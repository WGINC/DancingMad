# StAvatar

### `0x1024D180` StAvatar_Teardown

- **Verified C++** (`tree/src/StAvatar.cpp`): `XI_API uint32_t __cdecl StAvatar_Teardown(uint32_t * param_1, uint32_t param_2, uint32_t param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `StAvatar_SwitchMusicTask`, `StAvatar_ReleaseResources`, `fn_1024D400`, `fn_1024D470`, `fn_1024D4A0`, `fn_1024D540`, `fn_1024D5C0`, `StAvatar_StopAndFreeBuffers`, `fn_102506C0`, `sub_10252610` ×2
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StAvatar_Teardown` (not stated)
- **DancingMad note:** Calls StAvatar_ReleaseResources plus ~9 other cleanup sub-functions -- the larger orchestrating teardown method. One callee (StAvatar_SwitchMusicTask) breaks the pattern of staying within the dancer address range, a real cross-connection to CYyMusicLoadTask.

### `0x1024D2C0` StAvatar_ReleaseResources

- **Verified C++** (`tree/src/StAvatar.cpp`): `XI_API undefined4 __cdecl StAvatar_ReleaseResources(uint32_t * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 50 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `StChannelItemClear` ×3, `fn_10252C10` ×2, `fn_10253210`, `sqFree` ×2
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StAvatar_ReleaseResources` (confirmed)
- **DancingMad note:** Confirmed real StAvatar method via two sqFree() calls tagged with StAvatar.cpp line numbers (352, 359) -- D:\build0001\FFXi_Win\Main\dancer\StAvatar.cpp.
