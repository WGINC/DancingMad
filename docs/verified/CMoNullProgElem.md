# CMoNullProgElem

### `0x10047560` CMoNullProgElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoNullProgElem.cpp`): `char ** __cdecl CMoNullProgElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoNullProgElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x100531A0` CMoNullProgElem::SetField138

- **Verified C++** (`tree/src/CMoNullProgElem.cpp`): `void CMoNullProgElem::SetField138()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100531A0 mov dword ptr [ecx + 0x138], 0x3f800000` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoNullProgElem_SetField138` (confirmed)
- **DancingMad note:** CMoNullProgElem's ACTUAL confirmed slot 11 -- a trivial one-line setter (this+0x138 = 1.0f). Distinct from 0x100531D0, which was wrongly attributed to this class in an earlier pass.

### `0x100531B0` CMoNullProgElem::Destructor

- **Verified C++** (`tree/src/CMoNullProgElem.cpp`): `int * CMoNullProgElem::Destructor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100531B1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoNullProgElem_Destructor` (confirmed)
- **DancingMad note:** CMoNullProgElem's real, accessor-confirmed destructor. Calls only CMoElemFamily_SharedCleanup and SharedDeleteHelper -- never calls 0x100531D0, which is how the SharedConditionalStateReset misattribution was caught and corrected.
