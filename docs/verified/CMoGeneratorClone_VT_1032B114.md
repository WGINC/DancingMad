# CMoGeneratorClone_VT_1032B114

### `0x10047FE0` CMoGeneratorClone_VT_1032B114::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoGeneratorClone_VT_1032B114.cpp`): `void * CMoGeneratorClone_VT_1032B114::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10047FE1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoGeneratorClone_VT_1032B114::Destructor`
- **Run by a frame** (frame_set.json): stack

### `0x10048000` CMoGeneratorClone_VT_1032B114::Destructor

- **Verified C++** (`tree/src/CMoGeneratorClone_VT_1032B114.cpp`): `void __thiscall CMoGeneratorClone_VT_1032B114::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 13 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10048005 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `ReleaseSubObjectIfPresent`, `fn_1003B690`, `YmGenerater_Stop`, `Mem_FreeWithHeader12`, `CMoResource::Destructor`, `MoRes_FreeIfUnreferenced`, `fn_10074310`, `ResourceIter_FindNext`
- **Indirect calls:** 1, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Destructor of the generator base: frees resources of type 5 that reference this generator, detaches, deletes owned objects and runs the CMoResource base dtor.
