# CMoTask_VT_1032AF60

### `0x10043A90` CMoTask_VT_1032AF60::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoTask_VT_1032AF60.cpp`): `void * CMoTask_VT_1032AF60::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10043A91 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoTask_VT_1032AF60_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
