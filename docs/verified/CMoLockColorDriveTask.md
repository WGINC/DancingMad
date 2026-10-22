# CMoLockColorDriveTask

### `0x10056960` CMoLockColorDriveTask::GetRuntimeClass

- **Verified C++** (`tree/src/CMoLockColorDriveTask.cpp`): `char ** __cdecl CMoLockColorDriveTask::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoLockColorDriveTask_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1005F3C0` CMoLockColorDriveTask::vf8

- **Verified C++** (`tree/src/CMoLockColorDriveTask.cpp`): `char CMoLockColorDriveTask::vf8()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1005F3CB fsubr dword ptr [ecx + 0x74]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100630F0` CMoLockColorDriveTask::vf011

- **Verified C++** (`tree/src/CMoLockColorDriveTask.cpp`): `int CMoLockColorDriveTask::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x10056980 (tail_purges.json); entry ECX read: `0x100630F0 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10063100` CMoLockColorDriveTask::vf012

- **Verified C++** (`tree/src/CMoLockColorDriveTask.cpp`): `int CMoLockColorDriveTask::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x1005F660 (tail_purges.json); entry ECX read: `0x10063100 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
