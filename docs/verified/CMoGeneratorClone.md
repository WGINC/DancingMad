# CMoGeneratorClone

### `0x10047C30` CMoGeneratorClone::InitCloneFromSource

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `int CMoGeneratorClone::InitCloneFromSource(_DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10047C30 mov edx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoAttachments::Reset`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoGeneratorClone_InitCloneFromSource` (not stated)
- **DancingMad note:** Zeroes a block, copies transform fields (fixed + a variable-length waypoint-style array) from a source struct.

### `0x10047CE0` CMoGeneratorClone::FixupClonedPointers

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `_DWORD * CMoGeneratorClone::FixupClonedPointers()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 32 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 32, town PASS 58, town2 PASS 74, combat PASS 56, zonetoinn PASS 90
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10047CE3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoAttachments::ClearCaster`, `CMoAttachments::ClearTarget`, `CMoAttachments::SetCaster`, `CMoAttachments::SetTarget`, `CMoGeneratorClone::FindCmdByType`, `CMoGeneratorClone::ResolveTarget` ×2, `SharedConditionalStateReset`, `GetGlobal_1047D114`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoGeneratorClone_FixupClonedPointers` (confirmed)
- **DancingMad note:** Address-delta pointer repair, then classifies the clone by tags (verified strings 'weat'/'dust', zone codes). NOTE: despite the weather-string content, this class is used mostly by character-actor code (5 of 9 confirmed call sites) -- do not treat as weather-exclusive.

### `0x10048140` CMoGeneratorClone::UnlinkElemListA

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `void __thiscall CMoGeneratorClone::UnlinkElemListA(void * self, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10048164 mov dword ptr [ecx + 0xb0], edx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoResource::ReleaseChain`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Unlinks an element from the generator's first doubly linked element list (links at elem+0x14C/+0x150, head at this+0xB0) and releases a resource ref.

### `0x100492F0` CMoGeneratorClone::FindCmdByType

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `uint32_t * __thiscall CMoGeneratorClone::FindCmdByType(void * self, uint32_t param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 70 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100492F0 mov eax, dword ptr [ecx + 0xe4]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Scans the generator's packed command stream (this+0xE4) for the first record whose type byte equals a2.

### `0x10049570` CMoGeneratorClone::ResolveTarget

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `undefined4 __thiscall CMoGeneratorClone::ResolveTarget(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10049572 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoResource::FindByTypeAndId` ×2, `fn_10183420`
- **Reads globals:** `g_pZoneMap`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Resolves and caches the generator's target object from its header (type code + id), with a zone-map fallback for type 31.

### `0x10053450` CMoGeneratorClone::CopyParams

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `void __thiscall CMoGeneratorClone::CopyParams(void * self, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10053458 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003C740`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Copies generator parameter fields (+0x20..+0xEC, including bitfields at +0xD8) from a source generator, clearing pointer members +0xA4..+0xB0.

### `0x100536C0` CMoGeneratorClone::CreateInstance

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `int CMoGeneratorClone::CreateInstance(_DWORD *a2, _DWORD *a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 44 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 44, town PASS 43, town2 PASS 43, combat PASS 43, zonetoinn PASS 43
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100536CC mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocWithFallback`, `CMoAttachments::Reset`, `CMoAttachments::SetCaster`, `CMoAttachments::SetTarget`, `CMoGeneratorClone_VT_1032B114_Constructor`, `SharedConditionalStateReset`, `CMoGeneratorClone::CopyParams`, `CMoResource::RegisterInTypeList`, `CMoResource::FindByTypeAndId`, `MeshResourceMng_AllocHandle`
- **Reads globals:** `g_pMeshResourceMng`
- **Writes globals:** `byte_1047D12C`
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CMoGeneratorClone_CreateInstance` (confirmed)
- **DancingMad note:** The constructor/factory function -- allocates 252 bytes (matches the confirmed class size), sets up a second embedded vtable at +0x30, called from the 9 confirmed sites (5 in CXiSkeletonActor territory, 3 in CMoSchedularTask/CMoTask territory, 1 in CMoElem territory).

### `0x10053E00` CMoGeneratorClone::InitDefaultParams

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `int CMoGeneratorClone::InitDefaultParams()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10053E01 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Mem_AllocWithHeader12`, `MoProcessor_CallVSlot49`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CMoGeneratorClone_InitDefaultParams` (confirmed)
- **DancingMad note:** Lazy-init: allocates a 0x40-byte parameter block and defaults six consecutive float fields (+0x78-+0x8C) to 1.0. The same reset also happens inline inside CMoGeneratorClone_FixupClonedPointers -- not confirmed whether these two call sites are otherwise related.

### `0x100542F0` CMoGeneratorClone::Destructor

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `void __thiscall CMoGeneratorClone::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 28 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10048000 (tail_purges.json); entry ECX read: `0x100542F1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003B690`, `YmGenerater_Stop`, `NodePool_ReleaseNode`
- **Indirect calls:** 1, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Destructor of CMoGeneratorClone: detaches, deletes owned object, clears the back-pointer in its element and frees its handle before chaining to the generator base dtor.
