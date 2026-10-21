# sqgxTexture

### `0x10281830` sqgxTextureAdd

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int __cdecl sqgxTextureAdd(int a1, int a2, IDirect3DTexture8 *a3, _BYTE *a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 79 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 79, town PASS 45, town2 PASS 45, combat PASS 45, zonetoinn PASS 45
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxTextureCreateFromImage`, `sqgxCeilLog2` ×2, `sqDebugPrintf` ×3
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`, `g_counter_109A261C`
- **Writes globals:** `g_counter_109A261C`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Finds or creates a texture slot (w, h, depth) in the sqgxTexture table and returns its index (maximum 512). With image data it uploads it; without data it creates a render-target texture.

### `0x102819D0` sqgxTextureClutAdd

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int __cdecl sqgxTextureClutAdd(int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 49 returned normally, 49 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 49, town PASS 49, town2 PASS 49, combat PASS 49, zonetoinn PASS 49
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Allocates a free palette slot (1-255) and loads 256 entries from RGB or RGBA source data (stride a2) into the device palette, returning the slot.

### `0x10281D60` sqgxTextureClut

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int __cdecl sqgxTextureClut(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 79 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Selects texture palette a1, or for -1 selects palette 0 when the current context texture is 8-bit.

### `0x10281DB0` sqgxTextureUpdate

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int __cdecl sqgxTextureUpdate(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 1134 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 21, of which 15 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`, `g_sqgxRenderStateDirty`
- **Writes globals:** `g_sqgxRenderStateDirty`
- **Run by a frame** (frame_set.json): static

### `0x10282010` sqgxTextureStencilClear

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int __cdecl sqgxTextureStencilClear(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`
- **Run by a frame** (frame_set.json): static

### `0x10282030` sqgxTextureClear

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int __cdecl sqgxTextureClear(float *a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10311C2C` ×3
- **Reads constants** (.rdata): 1
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`
- **Run by a frame** (frame_set.json): static

### `0x102820E0` sqgxTextureDrawZ

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int * __cdecl sqgxTextureDrawZ(IDirect3DSurface8 *a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 193 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 99, town PASS 98, town2 PASS 98, combat PASS 97, zonetoinn PASS 98
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Makes sqgxTexture slot a1 the current render target, using the back buffer when the slot is the default frame buffer, and pairs it with the slot's depth surface or the default one.

### `0x10282190` sqgxTextureDraw

- **Verified C++** (`tree/src/sqgxTexture.cpp`): `XI_API int * __cdecl sqgxTextureDraw(int a1, char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 144 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxPixelSize`, `sqgxViewport`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static
