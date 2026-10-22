# CMoPathDriveActorTask

### `0x10056940` CMoPathDriveActorTask::GetRuntimeClass

- **Verified C++** (`tree/src/CMoPathDriveActorTask.cpp`): `char ** __cdecl CMoPathDriveActorTask::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoPathDriveActorTask_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1005E9C0` CMoPathDriveActorTask::vf8

- **Verified C++** (`tree/src/CMoPathDriveActorTask.cpp`): `undefined4 __thiscall CMoPathDriveActorTask::vf8(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 90 returned normally, 4 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1005E9CF mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CYyObject_IsKindOf` ×2, `sub_1003B6D0` ×9, `fn_10054500`, `fn_100547A0` ×2, `sub_10055AD0`, `sub_1005ED30` ×2, `sub_1005ED90`, `sub_1005EDC0`, `?SetDragRect@CBaseCamera@@UAEXAAUtagRECT@@@Z` ×2, `sub_1005EEC0`, `fn_1005EEF0`, `fn_10063B20`, `fn_10063C30`, `fn_100A57C0`
- **Reads constants** (.rdata): 6
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): stack

### `0x1005EEF0` fn_1005EEF0

- **Verified C++** (`tree/src/CMoPathDriveActorTask.cpp`): `XI_API undefined4 __thiscall fn_1005EEF0(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 88 returned normally, 7 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1005EEF5 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec4_Copy`, `CYyObject_IsKindOf` ×2, `sub_1003B6D0` ×9, `fn_10063C30`, `fn_100A57C0`
- **Reads constants** (.rdata): 4
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack

### `0x100630A0` CMoPathDriveActorTask::vf011

- **Verified C++** (`tree/src/CMoPathDriveActorTask.cpp`): `int CMoPathDriveActorTask::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x10056960 (tail_purges.json); entry ECX read: `0x100630A0 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100630B0` CMoPathDriveActorTask::vf012

- **Verified C++** (`tree/src/CMoPathDriveActorTask.cpp`): `int CMoPathDriveActorTask::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x1005F3F0 (tail_purges.json); entry ECX read: `0x100630B0 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
