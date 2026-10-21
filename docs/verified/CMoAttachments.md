# CMoAttachments

### `0x1003B530` CMoAttachments::GetRuntimeClass

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `char ** __cdecl CMoAttachments::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoAttachments_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1003B540` fn_1003B540

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `XI_API void * __thiscall fn_1003B540(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003B541 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoAttachments::Reset`, `ActorHandle_Constructor` ×2
- **Run by a frame** (frame_set.json): static

### `0x1003B570` CMoAttachments::vf004

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `char CMoAttachments::vf004()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1003B580` CMoAttachments::vf005

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `char CMoAttachments::vf005()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1003B590` CMoAttachments::vf006

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `int CMoAttachments::vf006()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1003B5A0` CMoAttachments::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `_DWORD * CMoAttachments::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003B5A1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `ReleaseSubObjectIfPresent`, `operator_delete`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1003B640` CMoAttachments::Reset

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `void __thiscall CMoAttachments::Reset(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003B642 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10081530` ×2
- **Reads globals:** `0x10351D00`, `0x10351D04`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Clears the caster/target pointers and auxiliary fields and resets both handle members to their default values.

### `0x1003B750` CMoAttachments::ClearCaster

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `void __thiscall CMoAttachments::ClearCaster(void * self, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003B757 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003C6E0`, `fn_10081530`
- **Reads globals:** `0x10351D08`, `0x10351D0C`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Optionally unlinks from the current caster, then nulls the caster pointer (this+3) and resets its handle.

### `0x1003B780` CMoAttachments::ClearTarget

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `void __thiscall CMoAttachments::ClearTarget(void * self, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003B787 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003C700`, `fn_10081530`
- **Reads globals:** `0x10351D10`, `0x10351D14`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Optionally unlinks from the current target, then nulls the target pointer (this+4) and resets its handle.

### `0x1003B7B0` CMoAttachments::SetCaster

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `void __thiscall CMoAttachments::SetCaster(void * self, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 64 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003B7B3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1003B6D0` ×3, `sub_100814F0`, `fn_10081530`, `fn_10085500`, `fn_10085D50`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x10351D18`, `0x10351D1C`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): If the caster changes, notifies the old caster (vtable+1000 detach), stores the new caster at this+3, captures its handle and registers this attachment with it.

### `0x1003B830` CMoAttachments::SetTarget

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `undefined4 __thiscall CMoAttachments::SetTarget(void * self, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 64 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003B833 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1003B700` ×3, `sub_100814F0`, `fn_10081530`, `fn_10085500`, `fn_10085D60`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x10351D20`, `0x10351D24`
- **Run by a frame** (frame_set.json): static, self, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): If the target changes, notifies the old target (vtable+1004 detach), stores the new target at this+4, captures its handle and registers this attachment with it.

### `0x1003B8B0` fn_1003B8B0

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `XI_API int __thiscall fn_1003B8B0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyObject_IsKindOf` ×2, `sub_1003B6D0` ×2
- **Run by a frame** (frame_set.json): static, stack

### `0x1003B900` fn_1003B900

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `XI_API int __thiscall fn_1003B900(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyObject_IsKindOf` ×2, `sub_1003B6D0`, `sub_1003B700`
- **Run by a frame** (frame_set.json): static

### `0x1003BD90` fn_1003BD90

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `XI_API void __cdecl fn_1003BD90(undefined4 param_1, undefined4 param_2, int * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 99 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack

### `0x1003BE10` fn_1003BE10

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `XI_API double __thiscall fn_1003BE10(int self_, _DWORD *a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 65 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 85, town PASS 84, town2 PASS 84, combat PASS 84, zonetoinn PASS 85
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1003BE1B mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1003B6D0` ×5, `sub_1003B700` ×5, `sub_1003B980` ×5, `sub_1003BA20` ×20, `fn_1003BD90` ×4, `fn_1006AD30`, `MoProcessor_CallVSlot49` ×6, `fn_100845E0`, `fn_101773F0` ×4, `fn_10186E90`, `fn_10186EB0`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 9, of which 7 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`, `g_pProcessor`, `g_pXiZone`
- **Run by a frame** (frame_set.json): static, self, stack
