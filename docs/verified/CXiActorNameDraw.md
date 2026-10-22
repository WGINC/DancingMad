# CXiActorNameDraw

### `0x100817F0` CXiActorNameDraw::SetRenderState

- **Verified C++** (`tree/src/CXiActorNameDraw.cpp`): `int __cdecl CXiActorNameDraw::SetRenderState()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Reads constants** (.rdata): 1
- **Indirect calls:** 23, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pSceneState`, `g_pActorDrawListHead`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiActorNameDraw_SetRenderState` (not stated)
- **DancingMad note:** Gated on a render-pass check (g_currentRenderPass == 0x60). Sets a complete, precisely-verified render state for alpha-cutout, alpha-blended billboard text: ZWRITEENABLE=1, FOGENABLE=0, ALPHATESTENABLE=1, ALPHAFUNC=5 (GREATEREQUAL), ALPHAREF=0, ALPHABLENDENABLE=1, SRCBLEND=5 (SRCALPHA), DESTBLEND=6 (INVSRCALPHA) -- every state ID and value checked against the real D3D9 enum. Continues into texture-stage-state calls not fully catalogued.
