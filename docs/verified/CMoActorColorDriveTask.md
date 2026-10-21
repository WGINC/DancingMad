# CMoActorColorDriveTask

### `0x100569A0` CMoActorColorDriveTask::GetRuntimeClass

- **Verified C++** (`tree/src/CMoActorColorDriveTask.cpp`): `char ** __cdecl CMoActorColorDriveTask::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoActorColorDriveTask_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10062FE0` CMoActorColorDriveTask::vf011

- **Verified C++** (`tree/src/CMoActorColorDriveTask.cpp`): `int CMoActorColorDriveTask::vf011()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100569C0 (tail_purges.json); entry ECX read: `0x10062FE0 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10062FF0` CMoActorColorDriveTask::vf012

- **Verified C++** (`tree/src/CMoActorColorDriveTask.cpp`): `tagRECT * CMoActorColorDriveTask::vf012(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x1005FE30 (tail_purges.json); entry ECX read: `0x10062FF0 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
