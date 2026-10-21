# CMoAttachments

### `0x1003B530` CMoAttachments::GetRuntimeClass

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `char ** __cdecl CMoAttachments::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoAttachments_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

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

### `0x1003BE10` fn_1003BE10

- **Verified C++** (`tree/src/CMoAttachments.cpp`): `XI_API double __thiscall fn_1003BE10(int self_, _DWORD *a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 65 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 85, town PASS 84, town2 PASS 84, combat PASS 84, zonetoinn PASS 85
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1003BE1B mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1003B6D0` ×5, `sub_1003B700` ×5, `sub_1003B980` ×5, `sub_1003BA20` ×20, `sub_1003BD90` ×4, `sub_1006AD30`, `MoProcessor_CallVSlot49` ×6, `sub_100845E0`, `sub_101773F0` ×4, `sub_10186E90`, `sub_10186EB0`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 9, of which 7 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`, `g_pProcessor`, `g_pXiZone`
- **Run by a frame** (frame_set.json): static, self, stack
