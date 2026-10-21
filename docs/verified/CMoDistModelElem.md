# CMoDistModelElem

### `0x10040670` CMoDistModelElem::DrawMesh

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `int CMoDistModelElem::DrawMesh(int a1, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 42 returned normally, 53 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 42, town PASS 25, town2 PASS 25, combat PASS 25, zonetoinn PASS 43
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10040675 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×2, `sub_1003FCB0` ×2, `sub_1003FCE0` ×3, `sub_1003FCF0` ×5, `VertexBatch_BindAndDraw` ×6, `??0exception@@QAE@XZ_1` ×5, `StateBlock_ApplyTSS` ×5, `MoProcessor_CallVSlot49`, `TextureHolder_BindWarped`, `_atexit` ×5
- **Indirect calls:** 8, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `CMoDistModelElem_DrawMesh_staticGuards`, `g_pDynVB_FVF152`, `g_pResourceMng`, `g_pProcessor`
- **Writes globals:** `CMoDistModelElem_DrawMesh_staticGuards`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Sets alpha test/texture factor and the element's shader constants and transforms, then draws the distorted model mesh as triangle lists, handling the type-5..7 offset case, and restores states.

### `0x100431A0` CMoDistModelElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `char ** __cdecl CMoDistModelElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDistModelElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x100431B0` fn_100431B0

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `XI_API int __thiscall fn_100431B0(void *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 388 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 97, town2 PASS 96, combat PASS 98, zonetoinn PASS 96
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100431B1 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::SetTransform`, `RegisterWithProcessor`, `??0exception@@QAE@XZ_1`, `StateBlock_ApplyTSS`, `MoProcessor_CallVSlot49`, `XiZone_DrawModelAtMatrix`, `_atexit`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState`, `IDirect3DDevice8::SetTextureStageState` ×4
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `Fn100431B0_staticGuards`, `g_scratchValue`, `g_pResourceMng`, `g_pProcessor`, `g_pZoneMap`
- **Writes globals:** `Fn100431B0_staticGuards`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10043320` CMoDistModelElem::BuildDistortedMesh

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `void CMoDistModelElem::BuildDistortedMesh()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 58 returned normally, 15 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 58, town PASS 26, town2 PASS 26, combat PASS 26, zonetoinn PASS 58
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10043327 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10002D80`, `Mem_AllocObject`, `Mem_FreeObject` ×2, `sub_1003FCB0`, `MoElem_GetVertexData`, `CMoDistModelElem::DrawMesh` ×2, `CMoDistMorphElem::ValidateMorphData`, `DynVB_Reserve`, `DynVB_Lock`, `DynVB_Unlock`, `CMoDX_SetWorldMatrix`, `CMoDX_GetWorldMatrix`, `MoProcessor_CallVSlot49`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDynVB_FVF152`, `g_pResourceMng`, `g_pProcessor`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CMoDistModelElem_BuildDistortedMesh` (not stated)
- **DancingMad note:** Allocates and populates a geometry buffer sized to the source model's triangle count.

### `0x10052F40` CMoDistModelElem::vf012

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `BOOL CMoDistModelElem::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10052F50` CMoDistModelElem::set_field_194

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `int CMoDistModelElem::set_field_194(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052F54 mov dword ptr [ecx + 0x194], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10052F60` CMoDistModelElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoDistModelElem.cpp`): `int * CMoDistModelElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10052F61 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
