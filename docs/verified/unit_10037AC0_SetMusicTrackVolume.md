# unit_10037AC0_SetMusicTrackVolume

### `0x10038520` Font_DrawPass

- **Verified C++** (`tree/src/unit_10037AC0_SetMusicTrackVolume.cpp`): `XI_API int __cdecl Font_DrawPass(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 12 returned normally, 1336 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 12, town PASS 12, town2 PASS 12, combat PASS 12, zonetoinn PASS 12
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Font_DrawString`, `Font_BindGlyphTexture`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 16, of which 16 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `dword_10463950`, `dword_1047B950`, `g_pFontGlyphs`
- **Writes globals:** `dword_1047B950`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets 2D alpha-blended, no-Z/fog/lighting state, draws every queued text string via Font_DrawString, clears the queue and restores blend/Z.

### `0x10038720` Font_DrawString

- **Verified C++** (`tree/src/unit_10037AC0_SetMusicTrackVolume.cpp`): `XI_API unsigned __int8 * __cdecl Font_DrawString(unsigned __int8 *a1, float a2, float arg8, float a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 24 returned normally, 174795 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 24, town PASS 24, town2 PASS 24, combat PASS 24, zonetoinn PASS 24
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`, `Font_DecodeNextChar`, `Font_AddGlyphAdvance`, `sub_10311C2C` ×4
- **Reads constants** (.rdata): 5
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Draws a string glyph by glyph as textured quads from a 64x128-cell font atlas, advancing x by glyph width and handling newline (16px*scale line height).
