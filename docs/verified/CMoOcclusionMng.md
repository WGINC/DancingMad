# CMoOcclusionMng

### `0x1006C130` CMoOcclusionMng::GetRuntimeClass

- **Verified C++** (`tree/src/CMoOcclusionMng.cpp`): `char ** __cdecl CMoOcclusionMng::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoOcclusionMng_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1006C1C0` CMoOcclusionMng::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoOcclusionMng.cpp`): `int * CMoOcclusionMng::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1006C1C1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CMoOcclusionMng_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006C220` CMoOcclusionMng::OcclusionMng_CreateTarget

- **Verified C++** (`tree/src/CMoOcclusionMng.cpp`): `_DWORD * CMoOcclusionMng::OcclusionMng_CreateTarget()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006C22B mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::CreateTexture`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static
