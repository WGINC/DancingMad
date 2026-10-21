# CMoDistRingElem

### `0x10043710` CMoDistRingElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoDistRingElem.cpp`): `char ** __cdecl CMoDistRingElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistRingElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10043720` CMoDistRingElem::AllocRingGeometry

- **Verified C++** (`tree/src/CMoDistRingElem.cpp`): `void CMoDistRingElem::AllocRingGeometry()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 77 returned normally, 1220 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 77, town PASS 77, town2 PASS 77, combat PASS 77, zonetoinn PASS 77
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10043725 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`, `CMoDistMorphElem::ValidateMorphData`, `RegisterWithProcessor`, `Gfx_CalcFVFStride`, `??0exception@@QAE@XZ_1`, `StateBlock_ApplyTSS`, `operator_delete`, `Allocator_Generic`, `_atexit`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetVertexShader`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `CMoDistRingElem_AllocRingGeometry_staticGuard`, `g_scratchValue`, `0x1047BC0E`, `g_pResourceMng`
- **Writes globals:** `CMoDistRingElem_AllocRingGeometry_staticGuard`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistRingElem_AllocRingGeometry` (not stated)
- **DancingMad note:** Computes and allocates a buffer sized from ring-segment and ring-count fields.

### `0x10052FF0` CMoDistRingElem::vf012

- **Verified C++** (`tree/src/CMoDistRingElem.cpp`): `BOOL CMoDistRingElem::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10053000` CMoDistRingElem::set_field_1B6

- **Verified C++** (`tree/src/CMoDistRingElem.cpp`): `int CMoDistRingElem::set_field_1B6(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10053004 mov dword ptr [ecx + 0x1b6], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10053010` CMoDistRingElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoDistRingElem.cpp`): `int * CMoDistRingElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10053011 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
