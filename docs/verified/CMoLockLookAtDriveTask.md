# CMoLockLookAtDriveTask

### `0x10056980` CMoLockLookAtDriveTask::GetRuntimeClass

- **Verified C++** (`tree/src/CMoLockLookAtDriveTask.cpp`): `char ** __cdecl CMoLockLookAtDriveTask::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoLockLookAtDriveTask_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1005F540` CMoLockLookAtDriveTask::vf8

- **Verified C++** (`tree/src/CMoLockLookAtDriveTask.cpp`): `char CMoLockLookAtDriveTask::vf8()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 20 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 20, town PASS 20, town2 PASS 20, combat PASS 20, zonetoinn PASS 20
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1005F542 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `sub_1003B6D0` ×7
- **Reads constants** (.rdata): 2
- **Indirect calls:** 7, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10062F80` CMoLockLookAtDriveTask::vf011

- **Verified C++** (`tree/src/CMoLockLookAtDriveTask.cpp`): `int CMoLockLookAtDriveTask::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100569A0 (tail_purges.json); entry ECX read: `0x10062F80 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10062F90` CMoLockLookAtDriveTask::vf012

- **Verified C++** (`tree/src/CMoLockLookAtDriveTask.cpp`): `int CMoLockLookAtDriveTask::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x1005F990 (tail_purges.json); entry ECX read: `0x10062F90 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
