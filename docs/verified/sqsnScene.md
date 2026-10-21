# sqsnScene

### `0x1028F8C0` sqsnSceneDraw

- **Verified C++** (`tree/src/sqsnScene.cpp`): `XI_API void __cdecl sqsnSceneDraw(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 64 returned normally, 267 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 64, town PASS 71, town2 PASS 72, combat PASS 71, zonetoinn PASS 72
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxSprite`, `sqgxTextureAdd` ×3, `sqgxTextureGetSize`, `sqgxTextureSet` ×2, `sqgxTextureDecal` ×2, `sqgxTextureClamp` ×2, `sqgxTextureStencilClear`, `sqgxTextureClear` ×4, `sqgxTextureDraw` ×7, `sqgxZTest` ×4, `sqgxBlendTrsp`, `sqgxBlendOff` ×2, `sqgxColor`, `sqgxMatrixCamera` ×2, `sqsnSceneLayerDraw` ×2, `sqsnSceneLayerDrawShadowed` ×2, `sqsnSceneLayerSnapShotComposite`, `nullsub_60` ×2, `sqsnSceneLayerSort`, `sqrdCamera_Apply` ×2
- **Reads constants** (.rdata): 4
- **Indirect calls:** 8, of which 8 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_sceneFadeMaskRT`, `g_pDancerDevice`, `g_pSqgxContext`, `g_sceneRT`, `g_sceneRT1`
- **Writes globals:** `g_sceneFadeMaskRT`, `g_sceneRT`, `g_sceneRT1`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws all scene layers: renders snapshot layers into ping-pong 1024x512 render targets and composites them, draws normal/shadowed layers with pre/post callbacks, and applies a stencil-masked fade when scene alpha < 1.
