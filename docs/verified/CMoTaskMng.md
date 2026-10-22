# CMoTaskMng

### `0x10011950` CMoTaskMng::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoTaskMng.cpp`): `_DWORD * CMoTaskMng::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10011951 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CMoTaskMng_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10074A10` CMoTaskMng::Forward10075120

- **Verified C++** (`tree/src/CMoTaskMng.cpp`): `void __stdcall CMoTaskMng::Forward10075120(undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 4 through its tail jump to 0x10075120 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads globals:** `dword_1047D140`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Calls sub_10075120 on the task manager singleton dword_1047D140 with a1.

### `0x10074B50` CMoTaskMng::GetRuntimeClass

- **Verified C++** (`tree/src/CMoTaskMng.cpp`): `char ** __cdecl CMoTaskMng::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoTaskMng_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10074BA0` fn_10074BA0

- **Verified C++** (`tree/src/CMoTaskMng.cpp`): `XI_API void __thiscall fn_10074BA0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10074BA3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoTask::ResetFields` ×3, `fn_10074DF0`
- **Run by a frame** (frame_set.json): static

### `0x10074C30` CMoTaskMng::DrawAll

- **Verified C++** (`tree/src/CMoTaskMng.cpp`): `undefined4 __thiscall CMoTaskMng::DrawAll(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 36 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10074C31 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self, stack
