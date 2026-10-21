# CYyTex

### `0x10039790` CYyTex::GetRuntimeClass

- **Verified C++** (`tree/src/CYyTex.cpp`): `_UNKNOWN ** __cdecl CYyTex::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CYyTex_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10039920` TexObj_Constructor

- **Verified C++** (`tree/src/CYyTex.cpp`): `XI_API undefined4 __thiscall TexObj_Constructor(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10039921 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10039830`
- **Reads globals:** `0x1047B968`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `TexObj_Constructor` (not stated)
- **DancingMad note:** 72-byte texture object: +0x1C CLUT, +0x20 pixels, +0x24/+0x26 w/h, +0x28 src bpp, +0x29 dst format (bit7 = precompressed), +0x2A mips, +0x2C flags, +0x38 next, +0x3C state, +0x40 IDirect3DTexture8*, +0x44 IDirect3DCubeTexture8*.

### `0x10039950` CYyTex::ScalarDeletingDtor

- **Verified C++** (`tree/src/CYyTex.cpp`): `_DWORD * CYyTex::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10039951 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `CYyTex_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
