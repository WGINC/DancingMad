# CMoDX

### `0x10069D60` CMoDX::GetRuntimeClass

- **Verified C++** (`tree/src/CMoDX.cpp`): `char ** __cdecl CMoDX::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoDX_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10069DB0` CMoDX::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoDX.cpp`): `_BYTE * CMoDX::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10069DB1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CMoDX_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006A150` CMoDX::CreateTexture

- **Verified C++** (`tree/src/CMoDX.cpp`): `undefined4 __thiscall CMoDX::CreateTexture(void * self, undefined4 param_1, undefined4 param_2, undefined4 * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1006A158 mov ecx, dword ptr [ecx + 0xdc8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::CreateTexture`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates a WxH single-level texture through the CDx renderer.

### `0x1006A480` CMoDX::SetWorldMatrix

- **Verified C++** (`tree/src/CMoDX.cpp`): `void __thiscall CMoDX::SetWorldMatrix(void * self, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1006A484 mov ecx, dword ptr [ecx + 0xdc8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets the D3D world transform.

### `0x1006A4C0` CMoDX::PushViewMatrix

- **Verified C++** (`tree/src/CMoDX.cpp`): `void __thiscall CMoDX::PushViewMatrix(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006A4C1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_1006A540`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Saves the current view matrix onto an 8-deep stack in CMoDX.

### `0x1006A4F0` CMoDX::PopViewMatrix

- **Verified C++** (`tree/src/CMoDX.cpp`): `void __thiscall CMoDX::PopViewMatrix(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006A4F0 mov eax, dword ptr [ecx + 0xea4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoDX::SetViewMatrix`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Pops the view-matrix stack and restores the saved matrix as D3D view transform.

### `0x1006A520` CMoDX::SetViewMatrix

- **Verified C++** (`tree/src/CMoDX.cpp`): `void __thiscall CMoDX::SetViewMatrix(void * self, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1006A524 mov ecx, dword ptr [ecx + 0xdc8]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets the D3D view transform.

### `0x1006B2B0` CMoDX::CreateAndInitSystem

- **Verified C++** (`tree/src/CMoDX.cpp`): `_DWORD * CMoDX::CreateAndInitSystem()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 99, town PASS 96, town2 PASS 96, combat PASS 96, zonetoinn PASS 96
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocDefault` ×4, `Mo_InitSharedRenderResources`, `fn_100555D0`, `CMoDX_Initialize`, `CMoDxStatusMng::Constructor`, `VBPool_Constructor`, `CMoOcclusionMng_Constructor`, `j_OcclusionMng_CreateTarget` ×2, `CMoResource::FindByTypeAndId`, `MeshResourceMng_LoadSystemResources`, `Gfx_InitCubeMapTextures`
- **Reads globals:** `g_pCDx`, `g_pMeshResourceMng`
- **Writes globals:** `g_pResourceMng`, `g_pDxStatusMng`, `g_pVbPool`, `g_pOcclusionMng`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates the CMoDX singleton (g_pResourceMng) and initializes the effect/model subsystem: VB pool, mesh resource root, shared render resources, status manager and occlusion manager.
