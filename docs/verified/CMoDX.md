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

### `0x1006B2B0` CMoDX::CreateAndInitSystem

- **Verified C++** (`tree/src/CMoDX.cpp`): `_DWORD * CMoDX::CreateAndInitSystem()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 99, town PASS 96, town2 PASS 96, combat PASS 96, zonetoinn PASS 96
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocDefault` ×4, `Mo_InitSharedRenderResources`, `sub_100555D0`, `CMoDX_Initialize`, `CMoDxStatusMng_Constructor`, `VBPool_Constructor`, `CMoOcclusionMng_Constructor`, `j_OcclusionMng_CreateTarget` ×2, `CMoResource_FindByTypeAndId`, `MeshResourceMng_LoadSystemResources`, `Gfx_InitCubeMapTextures`
- **Reads globals:** `g_pCDx`, `g_pMeshResourceMng`
- **Writes globals:** `g_pResourceMng`, `g_pDxStatusMng`, `g_pVbPool`, `g_pOcclusionMng`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates the CMoDX singleton (g_pResourceMng) and initializes the effect/model subsystem: VB pool, mesh resource root, shared render resources, status manager and occlusion manager.
