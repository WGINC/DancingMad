# CXiMovie

### `0x10026AD0` CXiMovie::Draw

- **Verified C++** (`tree/src/CXiMovie.cpp`): `int CXiMovie::Draw(int a1, int a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 554 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x10026AD4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 8, of which 8 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): stack

### `0x1021D4C0` CXiMovie::DrawFrame

- **Verified C++** (`tree/src/CXiMovie.cpp`): `int __cdecl CXiMovie::DrawFrame(int rcLeft, int rcTop, int rcRight, int rcBottom, float * scale)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 25 returned normally, 51 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 25, town PASS 32, town2 PASS 31, combat PASS 33, zonetoinn PASS 30
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetDefaultRenderState` ×2, `CDx::DrawPrimitiveUP`, `Movie_Update`, `Movie_GetCurrentTexture` ×3, `sub_10311C2C` ×4
- **Indirect calls:** 16, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pMovie`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws the current movie frame texture as a screen-space textured quad (no Z, fog, lighting or blending), with the rectangle scaled from the surface description.
