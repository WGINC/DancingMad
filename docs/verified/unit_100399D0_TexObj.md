# unit_100399D0_TexObj

### `0x10039A80` TexObj_Create

- **Verified C++** (`tree/src/unit_100399D0_TexObj.cpp`): `XI_API char __thiscall TexObj_Create(int self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 65 returned normally, 78 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 65, town PASS 63, town2 PASS 63, combat PASS 63, zonetoinn PASS 63
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10039A86 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `TexObj_Upload`, `_D3DXCheckTextureRequirements@28` ×2, `_D3DXCreateTexture@32`, `_D3DXCreateCubeTexture@28` ×4
- **Indirect calls:** 3, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_cfgMapCompression`, `g_cfgTextureCompression`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `TexObj_Create` (not stated)
- **DancingMad note:** Chooses the final format and creates the D3D texture: A1R5G5B5 / A8R8G8B8, or DXT1 (16-bit sources) / DXT3 (32-bit sources) when the object's compression class (flags>>4&0xF) is allowed by g_cfgTextureCompression (registry 0018) or, for class 10, g_cfgMapCompression (registry 0019). Mip count forced to 1 below 32 px. Non-power-of-two sizes are read back after upload. Then calls TexObj_Upload.

### `0x10039E50` TexObj_Upload

- **Verified C++** (`tree/src/unit_100399D0_TexObj.cpp`): `XI_API int __thiscall TexObj_Upload(void *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 5 returned normally, 24 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned; gates: fuzz PASS 5, town PASS 4, town2 PASS 4, combat PASS 4, zonetoinn PASS 4
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10039E56 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Tex_HeightToNormalMap`, `_D3DXLoadSurfaceFromMemory@40` ×3, `_D3DXCreateTexture@32` ×3, `_D3DXLoadSurfaceFromSurface@32` ×6
- **Indirect calls:** 40, of which 25 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `TexObj_Upload` (not stated)
- **DancingMad note:** CPU-converts a texture object into a staging D3DXCreateTexture surface (LockRect/UnlockRect; rows flipped, CLUT expanded for 4/8-bit, PS2 alpha range kept), then D3DXLoadSurfaceFromSurface into level 0 (FILTER_NONE; this is where DXT encoding happens) and builds mips level-by-level (FILTER_BOX). Precompressed DXT data goes straight in via D3DXLoadSurfaceFromMemory (FOURCC table 0x10351C94). Cube faces per face.
