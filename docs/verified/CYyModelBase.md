# CYyModelBase

### `0x100298A0` CYyModelBase::GetRuntimeClass

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `char ** __cdecl CYyModelBase::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelBase_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10029DB0` CYyModelBase::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `int * CYyModelBase::ScalarDeletingDtor(char a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10029DB1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CYyModelBase_Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): stack

### `0x1002A3B0` CYyModelBase::DrawLit

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `int CYyModelBase::DrawLit(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 53 returned normally, 844 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 53, town PASS 100, town2 PASS 81, combat PASS 94, zonetoinn PASS 94
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1002A3B4 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetLight`, `CYyModelBase_GetPartList`, `CYyTexMng_FindByNameInResource`, `CYyVbMng::AcquireVertexBuffer` ×4, `CYyVbMng_ReleaseVertexBuffer` ×4
- **Indirect calls:** 7, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_texNameCubemapSpec`, `g_pCDx`, `g_ambientColor`, `g_vertexBuffer_7540`, `g_pTextureMng`, `g_pVbMng`, `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws all model parts with scene lighting: sets ambient and up to N lights from the light table, ensures per-part dynamic vertex buffers, calls each part's draw method, then disables lights 0-3.
