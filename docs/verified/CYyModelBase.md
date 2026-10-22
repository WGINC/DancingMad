# CYyModelBase

### `0x100298A0` CYyModelBase::GetRuntimeClass

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `char ** __cdecl CYyModelBase::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyModelBase_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10029D30` fn_10029D30

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `XI_API void * __thiscall fn_10029D30(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10029D32 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1001ABF0`, `fn_10034230`
- **Reads globals:** `0x103514F4`, `0x103514F8`, `0x103514FC`
- **Run by a frame** (frame_set.json): static

### `0x10029DB0` CYyModelBase::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `int * CYyModelBase::ScalarDeletingDtor(char a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10029DB1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CYyModelBase::Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): stack

### `0x10029DD0` CYyModelBase::Destructor

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `void __thiscall CYyModelBase::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 152 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10034270 (tail_purges.json); entry ECX read: `0x10029DD2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_1001AC30`, `sub_1001B140`, `CMoResource::ReleaseChain`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): CYyModelBase destructor: sets vtable, releases its resource, deletes owned objects at +4 and +0x20, destroys two 7-element member arrays and the list at +8.

### `0x10029E50` CYyModelBase::SetResourceAndRebuild

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `void __thiscall CYyModelBase::SetResourceAndRebuild(void * self, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10029E55 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1002A0C0`, `fn_100342A0`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Stores a resource handle at +0xC, refreshes the list at +8 and rebuilds the model.

### `0x10029E70` CYyModelBase::GetPartList

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `int __thiscall CYyModelBase::GetPartList(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10029E70 lea eax, [ecx + 0x20]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns the address of the part list at this+0x20.

### `0x10029F70` CYyModelBase::AddPartFromResource

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `undefined4 * __thiscall CYyModelBase::AddPartFromResource(void * self, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 56 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10029F78 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10025010`, `fn_100250F0`, `fn_10029C90`, `fn_10029F00`, `fn_1002A0C0`, `Mem_AllocDefault` ×2, `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Creates a model part for a resource handle (60-byte CYyModelDt for type 0, 456-byte object for type 1), links it into the model and rebuilds.

### `0x1002A3B0` CYyModelBase::DrawLit

- **Verified C++** (`tree/src/CYyModelBase.cpp`): `int CYyModelBase::DrawLit(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 53 returned normally, 844 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 53, town PASS 100, town2 PASS 81, combat PASS 94, zonetoinn PASS 94
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1002A3B4 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetLight`, `CYyModelBase::GetPartList`, `CYyTexMng::FindByNameInResource`, `CYyVbMng::AcquireVertexBuffer` ×4, `CYyVbMng::ReleaseVertexBuffer` ×4
- **Indirect calls:** 7, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_texNameCubemapSpec`, `g_pCDx`, `g_ambientColor`, `g_vertexBuffer_7540`, `g_pTextureMng`, `g_pVbMng`, `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws all model parts with scene lighting: sets ambient and up to N lights from the light table, ensures per-part dynamic vertex buffers, calls each part's draw method, then disables lights 0-3.
