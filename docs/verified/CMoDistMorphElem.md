# CMoDistMorphElem

### `0x1003F440` CMoDistMorphElem::ApplyMorph

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `int CMoDistMorphElem::ApplyMorph(int a2, _DWORD *a3, int a4, int a5, _DWORD *C, char a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 61 returned normally, 180 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 61, town PASS 57, town2 PASS 57, combat PASS 57, zonetoinn PASS 57
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x1003F442 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×2, `Mem_FreeObject`, `CMoDistMorphElem::ComputeMorphHandle`, `VertexBatch_BindAndDraw`, `DynVB_Reserve`, `DynVB_Lock`, `DynVB_Unlock`, `??0exception@@QAE@XZ_1`, `StateBlock_ApplyTSS`, `MoProcessor_CallVSlot49`, `TextureHolder_BindWarped`, `_atexit`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×4, `IDirect3DDevice8::SetTextureStageState` ×2
- **Indirect calls:** 6, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `CMoDistMorphElem_ApplyMorph_staticGuards`, `g_pDynVB_FVF152`, `g_pResourceMng`, `g_pProcessor`
- **Writes globals:** `CMoDistMorphElem_ApplyMorph_staticGuards`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistMorphElem_ApplyMorph` (not stated)
- **DancingMad note:** The actual morph-apply function, called with the cached handle and both morph field addresses from CMoDistMorphElem_UpdateMorphBlend.

### `0x1003F8A0` CMoDistMorphElem::ComputeMorphHandle

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `_DWORD * CMoDistMorphElem::ComputeMorphHandle(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 63 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 63, town PASS 58, town2 PASS 58, combat PASS 59, zonetoinn PASS 58
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1003F8A6 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocObject`
- **Reads constants** (.rdata): 4
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistMorphElem_ComputeMorphHandle` (not stated)
- **DancingMad note:** Lazily computes and caches a morph-target handle (this+0x1BC) from two field addresses (this+0x1A8, this+0x194). Invalidated (reset to 0) at the end of each update call -- a transient per-call cache, not a persistent optimization.

### `0x10042D00` CMoDistMorphElem::ValidateMorphData

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `char __stdcall CMoDistMorphElem::ValidateMorphData(int a1, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 39 returned normally, 156 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 39, town PASS 46, town2 PASS 54, combat PASS 50, zonetoinn PASS 55
- **Convention facts:** `ret 16` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::GetRenderTargetTop` ×10, `VertexBatch_BindAndDraw`, `DynVB_Reserve`, `DynVB_Lock`, `DynVB_Unlock`, `sub_1006A060`, `sub_1006A0E0`, `??0exception@@QAE@XZ_1`, `StateBlock_ApplyRSTSS`, `_atexit`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×2, `IDirect3DDevice8::SetTexture` ×2
- **Reads constants** (.rdata): 3
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `CMoDistMorphElem_ValidateMorphData_staticGuards`, `g_pMoAccumTarget`, `g_pDynVB_FVF144`, `g_pResourceMng`, `g_pProcessor`
- **Writes globals:** `CMoDistMorphElem_ValidateMorphData_staticGuards`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CMoDistMorphElem_ValidateMorphData` (not stated)
- **DancingMad note:** Validates morph blend data; CMoDistMorphElem_UpdateMorphBlend early-exits if this returns false.

### `0x10043580` CMoDistMorphElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `char ** __cdecl CMoDistMorphElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistMorphElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10043590` CMoDistMorphElem::UpdateMorphBlend

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `char CMoDistMorphElem::UpdateMorphBlend()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 53 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 98, town2 PASS 98, combat PASS 98, zonetoinn PASS 98
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10043594 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoDistMorphElem::ApplyMorph`, `CMoDistMorphElem::ComputeMorphHandle`, `CMoDistMorphElem::ValidateMorphData`, `RegisterWithProcessor`, `CMoDX_SetWorldMatrix`, `CMoDX_GetWorldMatrix`, `MoProcessor_CallVSlot49`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`, `g_pProcessor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistMorphElem_UpdateMorphBlend` (not stated)
- **DancingMad note:** Full lookup/validate/apply/double-buffer cycle for a morph target.

### `0x10052E40` CMoDistMorphElem::vf012

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `BOOL CMoDistMorphElem::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10052E50` CMoDistMorphElem::set_field_1C0

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `int CMoDistMorphElem::set_field_1C0(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052E54 mov dword ptr [ecx + 0x1c0], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10052E60` CMoDistMorphElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoDistMorphElem.cpp`): `int * CMoDistMorphElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052E61 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CXi471011C8_VT_1032AC90_Dtor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
