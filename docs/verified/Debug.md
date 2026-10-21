# Debug

### `0x10003B60` Debug_DrawTextTable

- **Verified C++** (`tree/src/Debug.cpp`): `XI_API int __thiscall Debug_DrawTextTable(_DWORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 42 returned normally, 1726 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 42, town PASS 42, town2 PASS 42, combat PASS 42, zonetoinn PASS 42
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10003B6F mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Debug_DrawWorldText`
- **Indirect calls:** 19, of which 19 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Sets up alpha-blended, fog-off text render states, then draws each active entry of a 2304-entry debug text table with 0x10003D70, and restores the Z states.

### `0x10003D70` Debug_DrawWorldText

- **Verified C++** (`tree/src/Debug.cpp`): `XI_API void __stdcall Debug_DrawWorldText(_DWORD *a1, const char *a2, int arg8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 292 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `Vec3_Add_10026FA0`, `Vec3_Scale`, `Gfx_ProjectWorldToClip`, `Gfx_NdcToScreen`, `??0Iostream_init@@QAE@XZ_0`, `nullsub_1`, `Mat4_SetIdentity`, `Mat4_SetTranslation`, `ShapeMng_GetFontGlyph`, `Obj_104E1BF8::ShapeMng_BindFontTexture`, `sub_10312150`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_debugTextQuad_p0_x`, `g_debugTextQuad_p0_y`, `g_debugTextQuad_p1_x`, `g_debugTextQuad_p1_y`, `g_debugTextQuad_p2_x`, `g_debugTextQuad_p2_y`, `g_debugTextQuad_p3_x`, `g_debugTextQuad_p3_y`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws a text string as textured glyph quads at a given world transform: builds the world matrix, looks up glyphs in font dword_104E1BF8, handles newlines, and calls DrawPrimitiveUP.
