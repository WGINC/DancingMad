# CMoTask_VT_1032C908

### `0x10072A30` CMoTask_VT_1032C908::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoTask_VT_1032C908.cpp`): `void * CMoTask_VT_1032C908::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10072A31 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoTask_VT_1032C908_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
