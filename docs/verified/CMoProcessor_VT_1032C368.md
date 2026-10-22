# CMoProcessor_VT_1032C368

### `0x1006D3B0` CMoProcessor_VT_1032C368::vf012

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `float * CMoProcessor_VT_1032C368::vf012(float *a1, float *a2, float a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006D3E0` fn_1006D3E0

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `XI_API void __stdcall fn_1006D3E0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): self

### `0x1006D4D0` CMoProcessor_VT_1032C368::vf014

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `double CMoProcessor_VT_1032C368::vf014(float *a1, float *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); float result equal at its declared precision (the original returns ST0 unrounded); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006D580` fn_1006D580

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `XI_API long double __stdcall fn_1006D580(float * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 2
- **Run by a frame** (frame_set.json): self

### `0x1006D680` CMoProcessor_VT_1032C368::vf042

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `float * CMoProcessor_VT_1032C368::vf042(float *a1, float *a2, float *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006D6B0` CMoProcessor_VT_1032C368::vf043

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `float * CMoProcessor_VT_1032C368::vf043(float *a1, float *a2, float *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006D720` fn_1006D720

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `XI_API void __stdcall fn_1006D720(float * param_1, float * param_2, float * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x1006D980` CMoProcessor_VT_1032C368::vf021

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C368.cpp`): `float * CMoProcessor_VT_1032C368::vf021(float *a1, float *a2, float *a3, float a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
