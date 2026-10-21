# CYyIcon

### `0x10026990` CYyIcon::Draw

- **Verified C++** (`tree/src/CYyIcon.cpp`): `int CYyIcon::Draw(int a1, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 361 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10026996 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws the icon's texture as a screen quad at (x,y) sized to the texture with the given colour, optionally with alpha blending.

### `0x10026C70` CYyIcon::DrawSubRect

- **Verified C++** (`tree/src/CYyIcon.cpp`): `int CYyIcon::DrawSubRect(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 134 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 36` (purges.json); entry ECX read: `0x10026C71 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws a sub-rectangle of the icon's texture (source x,y,w,h) to a destination rectangle on screen with the given colour.
