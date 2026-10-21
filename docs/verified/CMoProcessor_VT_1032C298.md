# CMoProcessor_VT_1032C298

### `0x1006D380` CMoProcessor_VT_1032C298::vf007

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C298.cpp`): `float * CMoProcessor_VT_1032C298::vf007(float *a1, float a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x1006F5B0` CMoProcessor_VT_1032C298::vf014

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C298.cpp`): `double CMoProcessor_VT_1032C298::vf014(float *a1, float *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); float result equal at its declared precision (the original returns ST0 unrounded); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006FA30` CMoProcessor_VT_1032C298::vf021

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C298.cpp`): `float * CMoProcessor_VT_1032C298::vf021(float *a1, float *a2, float *a3, float a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 16 through its tail jump to 0x1006D980 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070020` CMoProcessor_VT_1032C298::vf035

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C298.cpp`): `CMoProcessor * CMoProcessor_VT_1032C298::vf035(float *a2, float *a3, int a4, int a5, int a6, float a7, float a8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 28 through its tail jump to 0x1006ED10 (tail_purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): self

### `0x10070040` CMoProcessor_VT_1032C298::vf036

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C298.cpp`): `CMoProcessor * CMoProcessor_VT_1032C298::vf036(float *a1, float *a2, int a3, int a4, const void *a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 20 through its tail jump to 0x1006E970 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
