# CMoGeneratorClone

### `0x10047C30` CMoGeneratorClone::InitCloneFromSource

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `int CMoGeneratorClone::InitCloneFromSource(_DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10047C30 mov edx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoAttachments_Reset`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoGeneratorClone_InitCloneFromSource` (not stated)
- **DancingMad note:** Zeroes a block, copies transform fields (fixed + a variable-length waypoint-style array) from a source struct.

### `0x10047CE0` CMoGeneratorClone::FixupClonedPointers

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `_DWORD * CMoGeneratorClone::FixupClonedPointers()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 32 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 32, town PASS 58, town2 PASS 74, combat PASS 56, zonetoinn PASS 90
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10047CE3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoAttachments_ClearCaster`, `CMoAttachments_ClearTarget`, `CMoAttachments_SetCaster`, `CMoAttachments_SetTarget`, `CMoGeneratorClone_FindCmdByType`, `CMoGeneratorClone_ResolveTarget` ×2, `SharedConditionalStateReset`, `GetGlobal_1047D114`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoGeneratorClone_FixupClonedPointers` (confirmed)
- **DancingMad note:** Address-delta pointer repair, then classifies the clone by tags (verified strings 'weat'/'dust', zone codes). NOTE: despite the weather-string content, this class is used mostly by character-actor code (5 of 9 confirmed call sites) -- do not treat as weather-exclusive.

### `0x100536C0` CMoGeneratorClone::CreateInstance

- **Verified C++** (`tree/src/CMoGeneratorClone.cpp`): `int CMoGeneratorClone::CreateInstance(_DWORD *a2, _DWORD *a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 44 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 44, town PASS 43, town2 PASS 43, combat PASS 43, zonetoinn PASS 43
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100536CC mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocWithFallback`, `CMoAttachments_Reset`, `CMoAttachments_SetCaster`, `CMoAttachments_SetTarget`, `CMoGeneratorClone_VT_1032B114_Constructor`, `SharedConditionalStateReset`, `CMoGeneratorClone_CopyParams`, `CMoResource_RegisterInTypeList`, `CMoResource_FindByTypeAndId`, `MeshResourceMng_AllocHandle`
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
