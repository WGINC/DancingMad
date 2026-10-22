# CYyModelDt

### `0x100224D0` CYyModelDt::PrepareRenderState

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `char CYyModelDt::PrepareRenderState(int a2, int arg4, int a3, int a5, int a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 71 returned normally, 245 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 71, town PASS 84, town2 PASS 84, combat PASS 84, zonetoinn PASS 83
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x100224D7 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetLight`, `CDx::DrawPrimitive` ×4, `CYyModelDt::SetVertexShader` ×3, `CYyModelDt_ExpandTriList`, `CYyModelDt_ExpandTriStrip`, `SkinVertices`, `Model_BeginOffscreenPass` ×2, `Model_EndOffscreenPassBindTextures` ×2, `CYyTexMng::FindByNameInResource`, `sub_10311C2C` ×2
- **Calls imports:** `Sleep` ×4
- **Reads constants** (.rdata): 3
- **Indirect calls:** 53, of which 18 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_ps2White`, `0x103515BE`, `g_pCDx`, `g_modelLightDiffuseR`, `g_modelLightDiffuseG`, `g_modelLightDiffuseB`, `CYyModelDt_PrepareRenderState_passToken`, `dword_104570F4`, `g_vertexBuffer_7150`, `g_vertexBuffer_7154`, `dword_1045745C`, `g_skinningCapabilityFlag`, `g_modelColor`, `0x104574AE`, `g_lineVertexCursor`, `g_stripVertexCursor`, `g_pTextureMng`
- **Writes globals:** `g_modelLightDiffuseR`, `g_modelLightDiffuseG`, `g_modelLightDiffuseB`, `g_alignedBufferSize`, `CYyModelDt_PrepareRenderState_passToken`, `dword_10456E48`, `0x10457210`, `0x10457214`, `0x10457218`, `g_lineVertexCursor`, `g_stripVertexCursor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_PrepareRenderState` (confirmed)
- **DancingMad note:** Computes a DMA-aligned buffer size, checks/clears a dirty flag, sets D3DRS_TEXTUREFACTOR (state ID 0x3C, confirmed -- NOT level-of-detail despite an earlier guess) from four packed globals, calls SkinVertices directly (gated on g_skinningCapabilityFlag), and copies a 26-entry global table into a staging buffer.

### `0x10022FA0` CYyModelDt::SetVertexShader

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `int __cdecl CYyModelDt::SetVertexShader(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 83 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_vertexShader_6E4C`
- **Writes globals:** `g_vertexShader_6E4C`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Caches a vertex shader/FVF handle in g_vertexShader_6E4C and sets it on the device when non-zero.

### `0x100231C0` CYyModelDt::PrepareRenderStateSimple

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `unsigned __int16 CYyModelDt::PrepareRenderStateSimple(int a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SkinVerticesSimple`
- **Writes globals:** `g_alignedBufferSize`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_PrepareRenderStateSimple` (not stated)
- **DancingMad note:** Simpler, differently-gated variant of CYyModelDt_PrepareRenderState, calling into SkinVerticesSimple.

### `0x10025030` CYyModelDt::PrepareRenderStateEntry

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `char CYyModelDt::PrepareRenderStateEntry(int a2, int a3, int a4, int a5, int a6, int a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x10025030 mov eax, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelDt::PrepareRenderState`, `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_PrepareRenderStateEntry` (not stated)
- **DancingMad note:** Resolves the mesh resource via g_pMeshResourceMng and dispatches into CYyModelDt_PrepareRenderState.

### `0x10025060` CYyModelDt::PrepareRenderStateSimpleEntry

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `unsigned __int16 CYyModelDt::PrepareRenderStateSimpleEntry(int a2, int a3, int a4, int a5, int a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x10025060 mov eax, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelDt::PrepareRenderStateSimple`, `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_PrepareRenderStateSimpleEntry` (not stated)
- **DancingMad note:** Resolves the mesh resource via g_pMeshResourceMng and dispatches into CYyModelDt_PrepareRenderStateSimple.

### `0x10025180` CYyModelDt::GetElementCount

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `__int16 CYyModelDt::GetElementCount()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10025180 mov eax, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_GetElementCount` (not stated)
- **DancingMad note:** Plain getter for the resource's +0x40 count field.

### `0x100251A0` CYyModelDt::MarkReferencedBones

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `int CYyModelDt::MarkReferencedBones(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 67 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 67, town PASS 45, town2 PASS 58, combat PASS 47, zonetoinn PASS 20
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100251A0 mov eax, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_MarkReferencedBones` (not stated)
- **DancingMad note:** For each of N entries in the resource's own index array, sets a flag byte at that index's position in a caller-supplied array -- likely marks which bones matter for this mesh piece.

### `0x10029880` CYyModelDt::GetRuntimeClass

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `char ** __cdecl CYyModelDt::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelDt_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10029CB0` CYyModelDt::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `_DWORD * CYyModelDt::ScalarDeletingDtor(char a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10029CB1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelDtBase_Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1002A000` CYyModelDt::PrepareRenderStateV2Entry

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `void __thiscall CYyModelDt::PrepareRenderStateV2Entry(void * self, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x1002A008 mov ecx, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelDt::SkinAndDrawV2`, `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): self, stack

### `0x1002A040` CYyModelDt::PrepareRenderStateV2SimpleEntry

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `void __thiscall CYyModelDt::PrepareRenderStateV2SimpleEntry(void * self, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x1002A048 mov ecx, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10030BD0`, `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): self, stack

### `0x1002DC10` CYyModelDt::SkinAndDrawV2

- **Verified C++** (`tree/src/CYyModelDt.cpp`): `__int16 CYyModelDt::SkinAndDrawV2(int a2, int a3, int _180, int a5, _DWORD *a6, _DWORD *a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 67 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 67, town PASS 58, town2 PASS 24, combat PASS 58, zonetoinn PASS 24
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x1002DC17 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetLight`, `CDx::DrawIndexedPrimitive` ×16, `ProjTex_BeginPass` ×2, `ProjTex_EndPass` ×2, `EnvMap_BeginPass` ×2, `EnvMap_EndPass` ×2, `Gfx_SetStreamSourceCached` ×48, `Gfx_ApplyCachedVertexShader` ×6, `Gfx_SetVertexShaderCached` ×3, `Model_SkinVerticesCpu`, `Model_BeginOffscreenPass` ×2, `Model_EndOffscreenPassBindTextures` ×2, `CYyTexMng::FindByNameInResource`, `sub_10311C2C` ×5
- **Calls imports:** `Sleep` ×4
- **Reads constants** (.rdata): 2
- **Indirect calls:** 63, of which 50 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_ps2White`, `0x103515BE`, `g_pCDx`, `g_modelDrawCallCount`, `dword_104570F4`, `g_envMapEnabled`, `g_ambientColor`, `g_ambientColorG`, `g_ambientColorR`, `g_ambientColorA`, `g_projTexEnabled`, `dword_1045745C`, `g_skinningCapabilityFlag`, `g_modelPrimitiveCount`, `g_modelColor`, `0x104574AE`, `g_skinLightDiffuseR`, `g_skinLightDiffuseG`, `g_skinLightDiffuseB`, `dword_1045B618`, `0x1045B61A`, `CYyModelDt_SkinAndDrawV2_passToken`, `g_boneWeightMatrixTable`, `g_pTextureMng`
- **Writes globals:** `g_modelDrawCallCount`, `g_modelPrimitiveCount`, `g_boneWeightMatrixTableCur`, `g_skinLightDiffuseR`, `g_skinLightDiffuseG`, `g_skinLightDiffuseB`, `dword_1045B618`, `0x1045B61A`, `dword_1045B61C`, `dword_1045B620`, `CYyModelDt_SkinAndDrawV2_passToken`, `dword_1045B64C`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Locks the model's position/normal VBs (Sleep(0) retry), runs CPU skinning (sub_1002F1D0), unlocks, then sets texture-factor/stage state and walks the model's command stream issuing SetStreamSource/SetIndices/DrawIndexedPrimitive per material. (pseudocode truncated)
