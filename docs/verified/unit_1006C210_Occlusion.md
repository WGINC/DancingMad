# unit_1006C210_Occlusion

### `0x1006C280` Occlusion_QueryScreenRect

- **Verified C++** (`tree/src/unit_1006C210_Occlusion.cpp`): `XI_API int __thiscall Occlusion_QueryScreenRect(__int16 *self_, float *a2, int a3, int a4, int a5, int a6, int a7, int a8, char a9, int a10)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 36` (purges.json); entry ECX read: `0x1006C287 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `nullsub_36`, `nullsub_37`, `Occlusion_QueryScreenRectImpl`, `OcclusionMng_Prepare`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `Occlusion_QueryScreenRect` (not stated)
- **DancingMad note:** Screen-rect occlusion test (ret 0x24); clears CDx+0x828 so the test quad is not duplicated for stereo; calls Occlusion_QueryScreenRectImpl.

### `0x1006C300` Occlusion_QueryScreenRectImpl

- **Verified C++** (`tree/src/unit_1006C210_Occlusion.cpp`): `XI_API int __thiscall Occlusion_QueryScreenRectImpl(__int16 *self_, float *arg0, int a2, int a5, int a6, int a7, int a8, int _60, char a9, int a10)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 54 returned normally, 2 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 54, town PASS 53, town2 PASS 52, combat PASS 54, zonetoinn PASS 53
- **Convention facts:** `ret 36` (purges.json); entry ECX read: `0x1006C30B mov dword ptr [esp + 0x14], ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::GetRenderTargetTop` ×8, `DrawScreenProbe`, `sub_1006C8B0`, `sub_10311C2C` ×4
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×2
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `Occlusion_QueryScreenRectImpl` (not stated)
- **DancingMad note:** Draws the occlusion test quad (via 0x1006C530) against render-target data.

### `0x1006C530` Occlusion_DrawQuery

- **Verified C++** (`tree/src/unit_1006C210_Occlusion.cpp`): `XI_API int __stdcall Occlusion_DrawQuery(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 500 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 99, town2 PASS 99, combat PASS 97, zonetoinn PASS 98
- **Convention facts:** `ret 36` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10009EA0`, `sub_10009EE0`, `sub_1000A200`, `sub_1000A230`, `sub_1000A390`, `CDx::DrawPrimitiveUP` ×3, `Gfx_CalcFVFStride` ×3, `??0exception@@QAE@XZ_1` ×2, `StateBlock_ApplyRSTSS` ×2, `_atexit` ×2
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState`, `IDirect3DDevice8::SetTexture`, `IDirect3DDevice8::SetVertexShader` ×3
- **Reads constants** (.rdata): 1
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pResourceMng`, `g_pOcclusionMng`, `Fn1006C530_staticGuards`
- **Writes globals:** `Fn1006C530_quadVerts`, `Fn1006C530_quadVerts_v0_y`, `Fn1006C530_quadVerts_v1_x`, `Fn1006C530_quadVerts_v1_y`, `Fn1006C530_quadVerts_v2_x`, `Fn1006C530_quadVerts_v2_y`, `Fn1006C530_quadVerts_v3_x`, `Fn1006C530_quadVerts_v3_y`, `Fn1006C530_quadVerts2`, `Fn1006C530_quadVerts2_v0_y`, `Fn1006C530_quadVerts2_v0_z`, `Fn1006C530_quadVerts2_v1_x`, `Fn1006C530_quadVerts2_v1_y`, `Fn1006C530_quadVerts2_v1_z`, `Fn1006C530_quadVerts2_v2_x`, `Fn1006C530_quadVerts2_v2_y`, `Fn1006C530_quadVerts2_v2_z`, `Fn1006C530_quadVerts2_v3_x`, `Fn1006C530_quadVerts2_v3_y`, `Fn1006C530_quadVerts2_v3_z`, `Fn1006C530_quadVerts3_v0_u`, `Fn1006C530_quadVerts3_v0_v`, `Fn1006C530_quadVerts3_v1_x`, `Fn1006C530_quadVerts3_v1_u`, `Fn1006C530_quadVerts3_v1_v`, `Fn1006C530_quadVerts3_v2_y`, `Fn1006C530_quadVerts3_v2_u`, `Fn1006C530_quadVerts3_v2_v`, `Fn1006C530_quadVerts3_v3_x`, `Fn1006C530_quadVerts3_v3_y`, `Fn1006C530_quadVerts3_v3_u`, `Fn1006C530_quadVerts3_v3_v`, `Fn1006C530_staticGuards`
- **Run by a frame** (frame_set.json): static, stack

### `0x1006C9B0` OcclusionMng_Prepare

- **Verified C++** (`tree/src/unit_1006C210_Occlusion.cpp`): `XI_API int __thiscall OcclusionMng_Prepare(_DWORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 70 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 70, town PASS 70, town2 PASS 70, combat PASS 70, zonetoinn PASS 70
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006C9B4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoOcclusionMng::OcclusionMng_CreateTarget`
- **Indirect calls:** 4, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pOcclusionMng`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates the 16x16 occlusion target on first use, reads the scene target surface desc, and caches an AddRef'd pointer to the target in the query.
