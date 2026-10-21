# Obj_104E1BF8

### `0x10120590` Obj_104E1BF8::ShapeMng_BindFontTexture

- **Verified C++** (`tree/src/Obj_104E1BF8.cpp`): `char Obj_104E1BF8::ShapeMng_BindFontTexture(int a2, _DWORD *a3, _DWORD *a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 67 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10120591 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `ShapeMng_LoadFontTextures`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static, self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Lazily loads the font textures, picks texture page 0 or 1 by comparing glyph code a2 with each page's first code, and binds it with SetTexture.

### `0x101207B0` Obj_104E1BF8::ShapeMng_BindDmgNumTexture

- **Verified C++** (`tree/src/Obj_104E1BF8.cpp`): `char Obj_104E1BF8::ShapeMng_BindDmgNumTexture(int a2, _DWORD *a3, _DWORD *a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 66 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x101207B1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `ShapeMng_LoadDmgNumTextures`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Damage-number counterpart of ShapeMng_BindFontTexture: lazily loads up to two textures and binds the one that matches code a2.
