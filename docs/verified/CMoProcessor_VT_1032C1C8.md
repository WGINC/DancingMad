# CMoProcessor_VT_1032C1C8

### `0x1006CC40` CMoProcessor_VT_1032C1C8::vf008

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `int CMoProcessor_VT_1032C1C8::vf008(void * a1, void * a2, void * a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x1006CC40 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): self

### `0x1006CC50` CMoProcessor_VT_1032C1C8::vf010

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `int CMoProcessor_VT_1032C1C8::vf010(void * a1, void * a2, void * a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x1006CC50 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006CC60` CMoProcessor_VT_1032C1C8::vf040

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `int CMoProcessor_VT_1032C1C8::vf040(float * a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x1006CC60 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): self

### `0x1006CC70` CMoProcessor_VT_1032C1C8::vf038

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `int CMoProcessor_VT_1032C1C8::vf038(float * a1, float * a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x1006CC70 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006CC80` CMoProcessor_VT_1032C1C8::vf046

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `int CMoProcessor_VT_1032C1C8::vf046(void * a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x1006CC80 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006CC90` CMoProcessor_VT_1032C1C8::vf045

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `int CMoProcessor_VT_1032C1C8::vf045(void * a1, void * a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** entry ECX read: `0x1006CC90 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006CCD0` CMoProcessor_VT_1032C1C8::CMoProcessor_GetRuntimeClass

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `char ** __cdecl CMoProcessor_VT_1032C1C8::CMoProcessor_GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoProcessor_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10070780` CMoProcessor_VT_1032C1C8::vf012

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `float * CMoProcessor_VT_1032C1C8::vf012(float *a1, float *a2, float a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 12 through its tail jump to 0x1006D3B0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070790` CMoProcessor_VT_1032C1C8::vf014

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `double CMoProcessor_VT_1032C1C8::vf014(float *a1, float *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); float result equal at its declared precision (the original returns ST0 unrounded); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070860` CMoProcessor_VT_1032C1C8::vf041

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `void CMoProcessor_VT_1032C1C8::vf041(float *a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x1006D5D0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070AA0` CMoProcessor_VT_1032C1C8::vf018

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `float * CMoProcessor_VT_1032C1C8::vf018(float *a1, float *a2, float *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 12 through its tail jump to 0x1006D7E0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070AB0` CMoProcessor_VT_1032C1C8::vf017

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `float * CMoProcessor_VT_1032C1C8::vf017(float *a1, float *a2, float *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 12 through its tail jump to 0x1006D870 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070AC0` CMoProcessor_VT_1032C1C8::vf016

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `float * CMoProcessor_VT_1032C1C8::vf016(float *a1, float *a2, float *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 12 through its tail jump to 0x1006D900 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070AD0` CMoProcessor_VT_1032C1C8::vf021

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `float * CMoProcessor_VT_1032C1C8::vf021(float *a1, float *a2, float *a3, float a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 16 through its tail jump to 0x1006D980 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070D80` CMoProcessor_VT_1032C1C8::vf032

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `void CMoProcessor_VT_1032C1C8::vf032(float * a1, int a2, int a3, float * a4, float * a5, float a6, float a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 28 through its tail jump to 0x1006E7D0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070E20` CMoProcessor_VT_1032C1C8::vf033

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `float * CMoProcessor_VT_1032C1C8::vf033(float *a1, float *a2, int a3, float *a4, float *a5, float a6, float a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 28 through its tail jump to 0x1006EB70 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070E40` CMoProcessor_VT_1032C1C8::vf035

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `CMoProcessor * CMoProcessor_VT_1032C1C8::vf035(float *a2, float *a3, int a4, int a5, int a6, float a7, float a8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 28 through its tail jump to 0x1006ED10 (tail_purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10070E60` CMoProcessor_VT_1032C1C8::vf036

- **Verified C++** (`tree/src/CMoProcessor_VT_1032C1C8.cpp`): `CMoProcessor * CMoProcessor_VT_1032C1C8::vf036(float *a1, float *a2, int a3, int a4, const void *a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 20 through its tail jump to 0x1006E970 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
