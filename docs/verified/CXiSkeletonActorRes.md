# CXiSkeletonActorRes

### `0x100C51B0` CXiSkeletonActorRes::GetRuntimeClass

- **Verified C++** (`tree/src/CXiSkeletonActorRes.cpp`): `char ** __cdecl CXiSkeletonActorRes::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActorRes_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x100D7000` CXiSkeletonActorRes::ScalarDeletingDtor

- **Verified C++** (`tree/src/CXiSkeletonActorRes.cpp`): `_DWORD * CXiSkeletonActorRes::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D7001 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CXiSkeletonActorRes::Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100D7020` CXiSkeletonActorRes::Constructor

- **Verified C++** (`tree/src/CXiSkeletonActorRes.cpp`): `_DWORD * CXiSkeletonActorRes::Constructor(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100D7021 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoTask_Constructor`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiSkeletonActorRes_Constructor` (not stated)
- **DancingMad note:** Constructs the 72-byte async skeleton-load task: sets the manual vtable, stores the linked actor at +0x34 (read back by CXiSkeletonActorRes_GetLinkedActor) and the completion callback at +0x38. The task's destructor (CXiSkeletonActorRes_Destructor, if named) clears g_pActiveSkeletonActorRes if it points at this task and clears actor+0xA08 -- the actor owns the task.

### `0x100D7050` CXiSkeletonActorRes::Destructor

- **Verified C++** (`tree/src/CXiSkeletonActorRes.cpp`): `char CXiSkeletonActorRes::Destructor()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100747C0 (tail_purges.json); entry ECX read: `0x100D7051 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CXiSkeletonActorRes::CXiSkeletonActorRes_GetLinkedActor`
- **Reads globals:** `g_pActiveSkeletonActorRes`
- **Writes globals:** `g_pActiveSkeletonActorRes`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActorRes_Destructor` (not stated)
- **DancingMad note:** Restores the vtable, clears g_pActiveSkeletonActorRes if it points at this task, clears the linked actor's +0xA08 back-reference, then runs the CMoTask base destructor (sub_100747C0).

### `0x100D7090` CXiSkeletonActorRes::CXiSkeletonActorRes_GetLinkedActor

- **Verified C++** (`tree/src/CXiSkeletonActorRes.cpp`): `int CXiSkeletonActorRes::CXiSkeletonActorRes_GetLinkedActor()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D7090 mov eax, dword ptr [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActorRes_GetLinkedActor` (not stated)
- **DancingMad note:** Simple getter returning this+0x34.

### `0x100D70A0` CXiSkeletonActorRes::ProcessLoadState

- **Verified C++** (`tree/src/CXiSkeletonActorRes.cpp`): `char CXiSkeletonActorRes::ProcessLoadState()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 23 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D70A2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CXiActor_GetModelByteEE`, `CXiSkeletonActorRes::CXiSkeletonActorRes_GetLinkedActor`
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pActiveSkeletonActorRes`
- **Writes globals:** `g_pActiveSkeletonActorRes`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActorRes_ProcessLoadState` (not stated)
- **DancingMad note:** State machine for the async skeleton load: reads the load state at +0x3C, uses CXiSkeletonActorRes_GetLinkedActor, and gates assignment of g_pActiveSkeletonActorRes.
