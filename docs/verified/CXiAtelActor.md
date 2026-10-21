# CXiAtelActor

### `0x10086210` Actor_DrawWorldText

- **Verified C++** (`tree/src/CXiAtelActor.cpp`): `XI_API void __cdecl Actor_DrawWorldText(_DWORD *a1, const char *a2, float a3, unsigned int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 216 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `Camera_GetViewportWidth` ×2, `Camera_GetViewportHeight` ×2, `Vec2_Add`, `Vec2_AddScalar`, `Gfx_ProjectWorldToClip`, `Gfx_NdcToScreen`, `??0Iostream_init@@QAE@XZ_0`, `nullsub_1`, `Mat4_SetIdentity`, `Mat4_SetTranslation`, `ShapeMng_GetFontGlyph`, `Obj_104E1BF8::ShapeMng_BindFontTexture`, `sub_10311C2C` ×5
- **Reads constants** (.rdata): 8
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_worldTextQuad`, `g_worldTextQuad_v0_y`, `g_worldTextQuad_v1_x`, `g_worldTextQuad_v1_y`, `g_worldTextQuad_v2_x`, `g_worldTextQuad_v2_y`, `g_worldTextQuad_v3_x`, `g_worldTextQuad_v3_y`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws a text string at a 3D position. It sets the world transform from matrix a1, projects the point, culls it if it falls more than 100px off-screen, scales by viewport/426.7*a3, expands special glyph codes 0xC8-0xCD, measures the glyphs through the font (sub_10120510 on dword_104E1BF8) and draws the quads with DrawPrimitiveUP. (pseudocode truncated)

### `0x10086900` fn_10086900

- **Verified C++** (`tree/src/CXiAtelActor.cpp`): `XI_API void __cdecl fn_10086900(_DWORD *a1, const char *a2, float a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 172 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `Camera_GetViewportWidth` ×2, `Camera_GetViewportHeight` ×2, `Vec2_Add`, `Vec2_AddScalar`, `Gfx_ProjectWorldToClip`, `Gfx_NdcToScreen`, `??0Iostream_init@@QAE@XZ_0`, `nullsub_1`, `Mat4_SetIdentity`, `Mat4_SetTranslation`, `ShapeMng_GetFontGlyph` ×2, `Obj_104E1BF8::ShapeMng_BindFontTexture`, `sub_10311C2C` ×2
- **Reads constants** (.rdata): 6
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_worldTextQuad`, `g_worldTextQuad_v0_y`, `g_worldTextQuad_v1_x`, `g_worldTextQuad_v1_y`, `g_worldTextQuad_v2_x`, `g_worldTextQuad_v2_y`, `g_worldTextQuad_v3_x`, `g_worldTextQuad_v3_y`
- **Run by a frame** (frame_set.json): self, stack
