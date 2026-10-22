# CYyMusicLoadTask

### `0x100378B0` fn_100378B0

- **Verified C++** (`tree/src/CYyMusicLoadTask.cpp`): `XI_API void __cdecl fn_100378B0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100382A0`, `fn_10246770`, `fn_102467A0`, `sub_10311C2C` ×2
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x103517F4`, `0x103517F8`, `0x1046393C`, `0x10463944`, `0x10463948`
- **Writes globals:** `0x10463909`, `0x10463940`, `0x10463944`, `0x10463948`
- **Run by a frame** (frame_set.json): static

### `0x10037960` StAvatar_SwitchMusicTask

- **Verified C++** (`tree/src/CYyMusicLoadTask.cpp`): `XI_API void __cdecl StAvatar_SwitchMusicTask(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 99 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Mem_AllocFromArea`, `CMoTask_Constructor`, `CMoTask::ResetFields`, `CMoTask_RegisterWithMng`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x10463944`, `0x10463948`
- **Writes globals:** `0x10463944`, `0x10463948`, `g_resourcesDirty`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StAvatar_SwitchMusicTask` (confirmed)
- **DancingMad note:** Called from within StAvatar's teardown chain. Constructs/swaps the active CYyMusicLoadTask (CYyMusicLoadTask_vtbl), stopping the previous one via a virtual call first. Sets what read as volume/fade params (127, 127, 30). Real, confirmed connection between avatar/dance-state teardown and a music-track transition.
