# unit_10178790_ZoneMap

### `0x101791F0` ZoneMap_DrawBox

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall ZoneMap_DrawBox(void *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 600 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101791F6 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::DrawIndexedPrimitive`
- **Indirect calls:** 6, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_boxIB`, `g_boxPositionVB`, `g_boxStream1VB`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Draws an indexed box mesh (24 vertices, 12 triangles) from two vertex streams with no texture and clockwise culling.

### `0x101792A0` ZoneMap_CreateVertexShaders

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall ZoneMap_CreateVertexShaders(char *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 200 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101792A6 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates the zone map's two fixed-function vertex shaders from static declarations.

### `0x1017ADE0` ZoneMap_DrawMeshGroupsWithFog

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall ZoneMap_DrawMeshGroupsWithFog(CTsZoneMap *self_, _DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 58 returned normally, 359 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 58, town PASS 63, town2 PASS 63, combat PASS 63, zonetoinn PASS 63
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1017ADE4 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `ZoneMap_DrawMeshById`
- **Indirect calls:** 8, of which 8 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Sets the fog mode (table fog, vertex fog or range fog, chosen from CDx capability flags), then draws every mesh id listed in each group of the given zone block.

### `0x1017B510` Zone_RenderEnvironment

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall Zone_RenderEnvironment(CTsZoneMap *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 87 returned normally, 10225 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 87, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1017B524 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::GetTransformCached`, `Light_ApplyTimeOfDayTint`, `CDx::SetLight` ×2, `Camera_GetField50`, `Camera_GetMatrix154Ptr`, `Vec3_Copy`, `sub_10177FA0`, `ZoneMap_DrawMeshGroupsWithFog`, `sub_1017C8B0`, `XiZone_DrawElement` ×3, `fn_1017DE20` ×3, `sub_10182490`, `XiZone_GetDirLights`, `Env_ComputeAmbientFloat4`, `sub_101892B0`, `sub_1018B8F0`, `XiZone_GetDirLight`, `XiZone_GetAmbient`, `XiZone_GetFog`, `D3DXMatrixMultiply_Dispatch` ×5
- **Reads constants** (.rdata): 2
- **Indirect calls:** 118, of which 111 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pCamera`, `g_cfg0000`, `g_zbiasZoneMesh`, `g_pXiZone`
- **Writes globals:** `dword_10631F14`, `dword_1065C4C8`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `Zone_RenderEnvironment` (not stated) — differs from this repository's `XiZone_Draw`
- **DancingMad note:** Sets D3DTS_PROJECTION plus fog table/vertex/range modes, fog color/start/end and ambient from the renderer block +0x39250..+0x3925C (filled via XiZone_GetFog/GetAmbient). Likely the sky/far-environment pass; not fully decoded.

### `0x1017C9C0` fn_1017C9C0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_1017C9C0(CTsZoneMap *self_, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 1371 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 95, town PASS 93, town2 PASS 93, combat PASS 94, zonetoinn PASS 93
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1017C9D0 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `Light_ApplyTimeOfDayTint` ×6, `CDx::SetLight` ×9, `CDx::DrawPrimitive` ×2, `CDx::DrawIndexedPrimitive`, `sub_1017A3F0`, `sub_10181BB0`, `XiZone_GetDirLights`, `sub_10188CA0` ×2, `Env_ComputeAmbient`, `Env_ComputeAmbientFloat4` ×2, `sub_10189120`, `D3DXMatrixMultiply_Dispatch` ×3, `D3DXMatrixTranspose_Dispatch` ×2, `sub_10311C2C`
- **Indirect calls:** 55, of which 20 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasPresetAux`, `g_zbiasZoneMesh`, `g_pXiZone`
- **Writes globals:** `g_zoneVsC15_x`, `g_zoneVsC15_y`, `g_zoneVsC15_z`, `g_zoneVsC15_w`, `g_zoneVsC16_x`, `g_zoneVsC16_y`, `g_zoneVsC16_z`, `g_zoneVsC16_w`, `g_zoneVsC17_x`, `g_zoneVsC17_y`, `g_zoneVsC17_z`, `g_zoneVsC17_w`, `g_zoneVsC18_x`
- **Run by a frame** (frame_set.json): self, stack

### `0x1017DE20` fn_1017DE20

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_1017DE20(float *self_, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 93 returned normally, 86 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 93, town PASS 100, town2 PASS 100, combat PASS 99, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1017DE30 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Light_ApplyTimeOfDayTint` ×6, `CDx::DrawIndexedPrimitive` ×2, `Gfx_SetZBias`, `sub_1017A3F0`, `sub_10181BB0` ×2, `sub_10188CA0`, `Env_ComputeAmbientFloat4` ×2, `sub_10189120`, `D3DXMatrixMultiply_Dispatch` ×3, `sub_10311C2C` ×30
- **Reads constants** (.rdata): 2
- **Indirect calls:** 28, of which 17 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasPresetAux`, `g_zbiasZoneMesh`, `g_zoneVsC15_x`, `g_zoneVsC15_y`, `g_zoneVsC15_z`, `g_zoneVsC15_w`, `g_zoneVsC16_x`, `g_zoneVsC16_y`, `g_zoneVsC16_z`, `g_zoneVsC16_w`, `g_zoneVsC17_x`, `g_zoneVsC17_y`, `g_zoneVsC17_z`, `g_zoneVsC17_w`, `g_zoneVsC18_x`, `Fn1017DE20_static_907C`, `Fn1017DE20_static_9080`, `Fn1017DE20_static_9084`, `g_pXiZone`
- **Writes globals:** `g_zoneVsC15_x`, `g_zoneVsC15_y`, `g_zoneVsC15_z`, `g_zoneVsC15_w`, `g_zoneVsC16_x`, `g_zoneVsC16_y`, `g_zoneVsC16_z`, `g_zoneVsC16_w`, `g_zoneVsC17_x`, `g_zoneVsC17_y`, `g_zoneVsC17_z`, `g_zoneVsC17_w`, `g_zoneVsC18_x`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10182F10` Gfx_DrawWireBox

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __stdcall Gfx_DrawWireBox(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 400 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP` ×3
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_upVerts_1C90`, `g_upVerts_1C90_v0_y`, `g_upVerts_1C90_v0_z`, `g_upVerts_1C90_v0_diffuse`, `g_upVerts_1C90_v0_u`, `g_upVerts_1C90_v0_v`, `g_upVerts_1C90_v1_x`, `g_upVerts_1C90_v1_y`, `g_upVerts_1C90_v1_z`, `g_upVerts_1C90_v1_diffuse`, `g_upVerts_1C90_v1_u`, `g_upVerts_1C90_v1_v`, `g_upVerts_1C90_v2_x`, `g_upVerts_1C90_v2_y`, `g_upVerts_1C90_v2_z`, `g_upVerts_1C90_v2_diffuse`, `g_upVerts_1C90_v2_u`, `g_upVerts_1C90_v2_v`, `g_upVerts_1C90_v3_x`, `g_upVerts_1C90_v3_y`, `g_upVerts_1C90_v3_z`, `g_upVerts_1C90_v3_diffuse`, `g_upVerts_1C90_v3_u`, `g_upVerts_1C90_v3_v`, `g_upVerts_1C90_v4_x`, `g_upVerts_1C90_v4_y`, `g_upVerts_1C90_v4_z`, `g_upVerts_1C90_v4_diffuse`, `g_upVerts_1C90_v4_u`, `g_upVerts_1C90_v4_v`, `g_upVerts_1C90_v5_x`, `g_upVerts_1C90_v5_y`, `g_upVerts_1C90_v5_z`, `g_upVerts_1C90_v5_diffuse`, `g_upVerts_1C90_v5_u`, `g_upVerts_1C90_v5_v`, `g_upVerts_1C90_v6_x`, `g_upVerts_1C90_v6_y`, `g_upVerts_1C90_v6_z`, `g_upVerts_1C90_v6_diffuse`, `g_upVerts_1C90_v6_u`, `g_upVerts_1C90_v6_v`, `g_upVerts_1C90_v7_x`, `g_upVerts_1C90_v7_y`, `g_upVerts_1C90_v7_z`, `g_upVerts_1C90_v7_diffuse`, `g_upVerts_1C90_v7_u`, `g_upVerts_1C90_v7_v`, `g_upVerts_1D50`, `g_upVerts_1D50_v0_y`, `g_upVerts_1D50_v0_z`, `g_upVerts_1D50_v0_diffuse`, `g_upVerts_1D50_v0_u`, `g_upVerts_1D50_v0_v`, `g_upVerts_1D50_v1_x`, `g_upVerts_1D50_v1_y`, `g_upVerts_1D50_v1_z`, `g_upVerts_1D50_v1_diffuse`, `g_upVerts_1D50_v1_u`, `g_upVerts_1D50_v1_v`, `g_upVerts_1D50_v2_x`, `g_upVerts_1D50_v2_y`, `g_upVerts_1D50_v2_z`, `g_upVerts_1D50_v2_diffuse`, `g_upVerts_1D50_v2_u`, `g_upVerts_1D50_v2_v`, `g_upVerts_1D50_v3_x`, `g_upVerts_1D50_v3_y`, `g_upVerts_1D50_v3_z`, `g_upVerts_1D50_v3_diffuse`, `g_upVerts_1D50_v3_u`, `g_upVerts_1D50_v3_v`, `g_upVerts_1D50_v4_x`, `g_upVerts_1D50_v4_y`, `g_upVerts_1D50_v4_z`, `g_upVerts_1D50_v4_diffuse`, `g_upVerts_1D50_v4_u`, `g_upVerts_1D50_v4_v`, `g_upVerts_1E10`, `g_upVerts_1E10_v0_y`, `g_upVerts_1E10_v0_z`, `g_upVerts_1E10_v0_diffuse`, `g_upVerts_1E10_v0_u`, `g_upVerts_1E10_v0_v`, `g_upVerts_1E10_v1_x`, `g_upVerts_1E10_v1_y`, `g_upVerts_1E10_v1_z`, `g_upVerts_1E10_v1_diffuse`, `g_upVerts_1E10_v1_u`, `g_upVerts_1E10_v1_v`, `g_upVerts_1E10_v2_x`, `g_upVerts_1E10_v2_y`, `g_upVerts_1E10_v2_z`, `g_upVerts_1E10_v2_diffuse`, `g_upVerts_1E10_v2_u`, `g_upVerts_1E10_v2_v`, `g_upVerts_1E10_v3_x`, `g_upVerts_1E10_v3_y`, `g_upVerts_1E10_v3_z`, `g_upVerts_1E10_v3_diffuse`, `g_upVerts_1E10_v3_u`, `g_upVerts_1E10_v3_v`, `g_upVerts_1E10_v4_x`, `g_upVerts_1E10_v4_y`, `g_upVerts_1E10_v4_z`, `g_upVerts_1E10_v4_diffuse`, `g_upVerts_1E10_v4_u`, `g_upVerts_1E10_v4_v`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Draws an axis-aligned bounding box as a wireframe: two closed rectangles (bottom and top faces) plus four vertical edges, unlit, colour 0x8000FFC0.

### `0x10183490` fn_10183490

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API float * __thiscall fn_10183490(float *self_, float *pM1, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 89 returned normally, 2284 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 89, town PASS 94, town2 PASS 94, combat PASS 94, zonetoinn PASS 94
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10183497 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitive`, `Gfx_SetZBias` ×2, `sub_10181BB0`, `D3DXMatrixMultiply_Dispatch`
- **Indirect calls:** 10, of which 10 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasRestore`, `g_zbiasPreset_C4D0`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10183760` fn_10183760

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API char __thiscall fn_10183760(float *self_, float *pM1, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 79 returned normally, 1591 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 79, town PASS 81, town2 PASS 81, combat PASS 81, zonetoinn PASS 81
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1018376F mov dword ptr [esp + 8], ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitive`, `Gfx_SetZBias` ×2, `sub_10182070`, `D3DXMatrixMultiply_Dispatch`
- **Indirect calls:** 44, of which 44 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasRestore`, `g_zbiasPreset_C4D0`
- **Run by a frame** (frame_set.json): stack

### `0x10183DA0` ZoneMap_DrawMeshById

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API _DWORD * __thiscall ZoneMap_DrawMeshById(int self_, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 5 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10183DAB mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::SetLight` ×11, `CDx::DrawPrimitive`, `sub_10181BB0`, `XiZone_GetDirLights` ×2, `sub_10188CA0` ×2, `Env_ComputeAmbient` ×2, `sub_10189120` ×2
- **Indirect calls:** 29, of which 11 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): stack

### `0x10184C90` fn_10184C90

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10184C90(void *self_, int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10184C97 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `Mat44_Multiply` ×2, `Mat4_SetIdentity_2` ×2, `Gfx_SetZBias` ×2, `ZoneMap_SetOverlayProjection`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 16, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_overlayScaleX`, `g_overlayScaleY`, `g_overlayScaleZ`, `g_pCDx`, `g_zbiasRestore`, `g_zbiasOverlay`
- **Writes globals:** `g_overlayScaleX`, `g_overlayScaleZ`
- **Run by a frame** (frame_set.json): self, stack

### `0x10185CA0` fn_10185CA0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10185CA0(void *self_, float *a1, float *a2, IDirect3DBaseTexture8 *a3, float a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 65 returned normally, 1635 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 65, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 68
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10185CB5 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `GetPtr8IfField60Set`, `Mat44_Multiply` ×4, `Gfx_SetZBias` ×2, `ZoneMap_SetOverlayProjection`, `sub_10311C2C` ×5
- **Reads constants** (.rdata): 4
- **Indirect calls:** 21, of which 21 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `Fn10185CA0_m30`, `Fn10185CA0_m31`, `Fn10185CA0_m32`, `Fn10185CA0_m00`, `Fn10185CA0_m11`, `Fn10185CA0_m22`, `g_pCDx`, `g_zbiasRestore`, `g_zbiasOverlay`
- **Writes globals:** `Fn10185CA0_m00`, `Fn10185CA0_m22`
- **Run by a frame** (frame_set.json): self, stack
