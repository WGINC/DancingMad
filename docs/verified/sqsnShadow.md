# sqsnShadow

### `0x102A21F0` sqsnShadowVolumeDraw

- **Verified C++** (`tree/src/sqsnShadow.cpp`): `XI_API void __cdecl sqsnShadowVolumeDraw(int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `M4fTransform`, `sqMatrix4_1027F0E0`, `sqDebugPrintf` ×2, `sqsnShadowVolumeExtrudeTriList`, `sqsnShadowVolumeExtrudeTriStrip`, `sqsnShadowVolumeSetPass` ×3, `sqsnShadowComputeFacing`, `sqsnShadowVolumeBeginVB`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 3, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pDancerDevice`, `g_pSqgxContext`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Draws a stencil shadow volume for a tri-strip shape: transforms light to object space, computes facing, extrudes strips/lists into the VB, then renders it in INCR and DECR passes.
