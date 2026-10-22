# CXiOpening

### `0x100186C0` CXiOpening::Constructor

- **Verified C++** (`tree/src/CXiOpening.cpp`): `void * CXiOpening::Constructor(char *Source)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 36 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 36, town PASS 36, town2 PASS 36, combat PASS 36, zonetoinn PASS 36
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100186C2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `GammaRamp_SetRGB`, `GammaRamp_GetRGB`, `OpeningSubtitle_Constructor`, `OpeningSubtitle_Reset`, `Vt10329FE0_Constructor`, `Vt10329FE0_Reset`, `Allocator_Generic` ×2, `_strncpy`
- **Reads globals:** `g_pCDx`, `g_pSceneState`
- **Writes globals:** `dword_10456D20`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Constructs CXiOpening: saves the current gamma and forces it to 1.0 when supported, copies the name, and creates the subtitle (region-dependent) and helper sub-objects.

### `0x100187D0` CXiOpening::CXiOpening_Destructor

- **Verified C++** (`tree/src/CXiOpening.cpp`): `CDx * CXiOpening::CXiOpening_Destructor()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 151 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100187D1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `GammaRamp_SetRGB`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): CXiOpening destructor body: deletes the two sub-objects and restores the saved gamma values.
