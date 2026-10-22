# unit_10178790_ZoneMap

### `0x101787C0` fn_101787C0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_101787C0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 98 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101787C4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `ResourceHandle_IsResident`, `CMoResource_AddRefChain`, `sub_10072FD0`, `sub_100852D0`, `fn_100FC680`, `sub_10176DD0`, `sub_10178790`, `fn_10178AC0`, `sub_10178D90`, `sub_10178DD0`, `sub_1017A630`, `sub_10186D30`, `XiZone::FindSubArea`
- **Reads globals:** `g_pMeshResourceMng`
- **Writes globals:** `0x10376EE8`
- **Run by a frame** (frame_set.json): stack

### `0x10178A20` fn_10178A20

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10178A20(void * self_, int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10178A24 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100FC680`, `sub_10176DD0`, `fn_101779B0`, `fn_10178AC0`
- **Writes globals:** `0x10376EE8`
- **Run by a frame** (frame_set.json): static

### `0x10178AC0` fn_10178AC0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10178AC0(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10178AC6 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_101679A0`, `fn_1017B110`
- **Run by a frame** (frame_set.json): static

### `0x10178B30` fn_10178B30

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API uint32_t __thiscall fn_10178B30(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10178B32 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Camera_GetFrameScale`, `sub_10055130`, `sub_10055160`, `CTsZoneMap_LogZoneMetrics`, `CTsZoneMap::InitZBiasPresets`, `sub_10178250`, `fn_101787C0`, `ZoneMap_CreateVertexShaders`, `XiZone_Draw`, `sub_10183370`, `sub_10186E70`, `sub_101D2260`, `fn_101D29C0`
- **Reads constants** (.rdata): 2
- **Reads globals:** `0x10376FF0`, `0x1047BC8C`, `g_zoneLoggingActive`, `0x1065CA28`, `0x1065CA2C`
- **Writes globals:** `0x10631ED0`, `0x10631ED4`, `0x10631ED8`, `0x10631EDC`, `0x10631EE0`, `0x10631EE4`, `0x10631EE8`, `0x10631EEC`, `0x10631EF0`, `0x10631EF4`, `0x10631EF8`, `0x10631EFC`, `0x10631F00`, `0x10631F04`, `0x10631F08`, `0x10631F0C`, `0x1065CA2C`
- **Run by a frame** (frame_set.json): stack

### `0x10178F70` fn_10178F70

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10178F70(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10178F71 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100550F0`, `ZoneMap_TeardownStep`
- **Run by a frame** (frame_set.json): static

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

### `0x10179410` ZoneMap_CopyField342C8ToField39450

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall ZoneMap_CopyField342C8ToField39450(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10179410 mov eax, dword ptr [ecx + 0x342c8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Copies the dword at this+0x342C8 into this+0x39450.

### `0x10179420` fn_10179420

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10179420(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10179420 mov eax, dword ptr [ecx + 0x342c8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1017ADE0` ZoneMap_DrawMeshGroupsWithFog

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall ZoneMap_DrawMeshGroupsWithFog(CTsZoneMap *self_, _DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 58 returned normally, 359 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 58, town PASS 63, town2 PASS 63, combat PASS 63, zonetoinn PASS 63
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1017ADE4 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `ZoneMap_DrawMeshById`
- **Indirect calls:** 8, of which 8 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Sets the fog mode (table fog, vertex fog or range fog, chosen from CDx capability flags), then draws every mesh id listed in each group of the given zone block.

### `0x1017B110` fn_1017B110

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_1017B110(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 30 returned normally, 48 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1017B116 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `Mem_FreeObject`, `fn_100446A0`, `CMoResource::ReleaseChain` ×2, `MoRes_FreeIfUnreferenced` ×2, `fn_10170CD0`, `sub_1017A690`, `fn_10186DD0`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): static

### `0x1017B1E0` ZoneMap_TeardownStep

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall ZoneMap_TeardownStep(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 50 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1017B1E2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `CMoResource::ReleaseChain`, `MoRes_FreeIfUnreferenced`, `fn_10167950`, `sub_10174A60`, `fn_101784E0`, `fn_1017B110`
- **Reads globals:** `g_pMeshResourceMng`
- **Writes globals:** `0x10621C7C`, `0x10621C80`, `g_zoneLoggingActive`, `0x1065C4D4`, `0x1065C5D8`
- **Run by a frame** (frame_set.json): static

### `0x1017B510` Zone_RenderEnvironment

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall Zone_RenderEnvironment(CTsZoneMap *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 87 returned normally, 10225 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 87, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1017B524 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::GetTransformCached`, `Light_ApplyTimeOfDayTint`, `CDx::SetLight` ×2, `Camera_GetField50`, `Camera_GetMatrix154Ptr`, `Vec3_Copy`, `fn_10177FA0`, `ZoneMap_DrawMeshGroupsWithFog`, `sub_1017C8B0`, `XiZone_DrawElement` ×3, `fn_1017DE20` ×3, `fn_10182490`, `XiZone::GetDirLights`, `Env_ComputeAmbientFloat4`, `sub_101892B0`, `fn_1018B8F0`, `XiZone::GetDirLight`, `XiZone::GetAmbient`, `XiZone::GetFog`, `D3DXMatrixMultiply_Dispatch` ×5
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
- **Calls directly:** `CDx::SetTransform`, `Light_ApplyTimeOfDayTint` ×6, `CDx::SetLight` ×9, `CDx::DrawPrimitive` ×2, `CDx::DrawIndexedPrimitive`, `sub_1017A3F0`, `sub_10181BB0`, `XiZone::GetDirLights`, `fn_10188CA0` ×2, `Env_ComputeAmbient`, `Env_ComputeAmbientFloat4` ×2, `sub_10189120`, `D3DXMatrixMultiply_Dispatch` ×3, `D3DXMatrixTranspose_Dispatch` ×2, `sub_10311C2C`
- **Indirect calls:** 55, of which 20 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasPresetAux`, `g_zbiasZoneMesh`, `g_pXiZone`
- **Writes globals:** `g_zoneVsC15_x`, `g_zoneVsC15_y`, `g_zoneVsC15_z`, `g_zoneVsC15_w`, `g_zoneVsC16_x`, `g_zoneVsC16_y`, `g_zoneVsC16_z`, `g_zoneVsC16_w`, `g_zoneVsC17_x`, `g_zoneVsC17_y`, `g_zoneVsC17_z`, `g_zoneVsC17_w`, `g_zoneVsC18_x`
- **Run by a frame** (frame_set.json): self, stack

### `0x1017DE20` fn_1017DE20

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_1017DE20(float *self_, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 93 returned normally, 86 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 93, town PASS 100, town2 PASS 100, combat PASS 99, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1017DE30 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Light_ApplyTimeOfDayTint` ×6, `CDx::DrawIndexedPrimitive` ×2, `Gfx_SetZBias`, `sub_1017A3F0`, `sub_10181BB0` ×2, `fn_10188CA0`, `Env_ComputeAmbientFloat4` ×2, `sub_10189120`, `D3DXMatrixMultiply_Dispatch` ×3, `sub_10311C2C` ×30
- **Reads constants** (.rdata): 2
- **Indirect calls:** 28, of which 17 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasPresetAux`, `g_zbiasZoneMesh`, `g_zoneVsC15_x`, `g_zoneVsC15_y`, `g_zoneVsC15_z`, `g_zoneVsC15_w`, `g_zoneVsC16_x`, `g_zoneVsC16_y`, `g_zoneVsC16_z`, `g_zoneVsC16_w`, `g_zoneVsC17_x`, `g_zoneVsC17_y`, `g_zoneVsC17_z`, `g_zoneVsC17_w`, `g_zoneVsC18_x`, `Fn1017DE20_static_907C`, `Fn1017DE20_static_9080`, `Fn1017DE20_static_9084`, `g_pXiZone`
- **Writes globals:** `g_zoneVsC15_x`, `g_zoneVsC15_y`, `g_zoneVsC15_z`, `g_zoneVsC15_w`, `g_zoneVsC16_x`, `g_zoneVsC16_y`, `g_zoneVsC16_z`, `g_zoneVsC16_w`, `g_zoneVsC17_x`, `g_zoneVsC17_y`, `g_zoneVsC17_z`, `g_zoneVsC17_w`, `g_zoneVsC18_x`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x101811D0` fn_101811D0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_101811D0(void * self_, undefined4 param_1, float param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x101811D9 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10168FD0`, `fn_10181290`
- **Run by a frame** (frame_set.json): static, stack

### `0x10181210` fn_10181210

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10181210(void * self_, undefined4 param_1, float param_2, undefined4 param_3, float param_4, float * param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x10181217 add ecx, 0x178` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_101693B0`
- **Run by a frame** (frame_set.json): static, stack

### `0x10181290` fn_10181290

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10181290(void * self_, undefined4 param_1, float param_2, undefined4 param_3, float param_4, float * param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x101812B3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10181210` ×2
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static, stack

### `0x10181300` fn_10181300

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10181300(void * self_, undefined4 param_1, float param_2, undefined4 param_3, float * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1018130B mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10181210` ×2
- **Reads globals:** `0x1037731C`
- **Run by a frame** (frame_set.json): static

### `0x10181370` fn_10181370

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10181370(void * self_, float param_1, float param_2, float param_3, float param_4, float * param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x101813A6 add ecx, 0x178` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_1016B1D0`
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): stack

### `0x101813F0` ZoneMap_FindGroundHeight

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall ZoneMap_FindGroundHeight(void * self_, undefined4 param_1, float param_2, undefined4 param_3, float param_4, float * param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x10181421 lea esi, [ecx + 0x178]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1016A2D0` ×2
- **Reads constants** (.rdata): 2
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Finds the ground height at (x, z) by casting a vertical segment against the collision map at this+376; on a miss it retries in the other direction, and on a hit it writes the hit Y to *a6.

### `0x101814D0` fn_101814D0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_101814D0(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x101814DC mov eax, dword ptr [ecx + 0x16c]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10169290`
- **Reads globals:** `0x10377320`, `0x10377324`
- **Run by a frame** (frame_set.json): stack

### `0x10181590` fn_10181590

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10181590(void * self_, undefined4 xi_s1, undefined4 xi_s2, undefined4 xi_s3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 12 through its tail jump to 0x101693B0 (tail_purges.json); entry ECX read: `0x10181590 add ecx, 0x178` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x101819B0` fn_101819B0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_101819B0(void * self_, undefined4 param_1, float param_2, undefined4 param_3, float * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x101819BC fsub dword ptr [ecx + 0x170]` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10181210`
- **Run by a frame** (frame_set.json): static

### `0x10181A10` fn_10181A10

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10181A10(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10181A1F add ecx, 0x178` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1016E7E0`
- **Run by a frame** (frame_set.json): stack

### `0x10181F60` fn_10181F60

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API long double __cdecl fn_10181F60(float * param_1, float * param_2, float * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): self

### `0x10182490` fn_10182490

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __stdcall fn_10182490(float * param_1, float param_2, float param_3, float param_4, float param_5, float param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 24` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads constants** (.rdata): 2
- **Run by a frame** (frame_set.json): self

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

### `0x10183420` fn_10183420

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10183420(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10183429 lea esi, [ecx + 0x60]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10170F30`
- **Run by a frame** (frame_set.json): static

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
- **Calls directly:** `CDx::SetTransform`, `CDx::SetLight` ×11, `CDx::DrawPrimitive`, `sub_10181BB0`, `XiZone::GetDirLights` ×2, `fn_10188CA0` ×2, `Env_ComputeAmbient` ×2, `sub_10189120` ×2
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

### `0x10186DB0` fn_10186DB0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10186DB0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186DB3 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10186DD0`
- **Run by a frame** (frame_set.json): static

### `0x10186DD0` fn_10186DD0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __stdcall fn_10186DD0(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 38 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `fn_10187470`, `XiZone::FindSubArea`, `operator_delete`
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static

### `0x10186E90` fn_10186E90

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186E90(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186E90 lea eax, [ecx + 0xb4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186EA0` fn_10186EA0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186EA0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186EA0 lea eax, [ecx + 0xc4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186EB0` fn_10186EB0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186EB0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186EB0 lea eax, [ecx + 0xd4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186EC0` fn_10186EC0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186EC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186EC0 lea eax, [ecx + 0x24]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186EE0` fn_10186EE0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186EE0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186EE0 lea eax, [ecx + 0x44]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186F00` fn_10186F00

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F00(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F00 lea eax, [ecx + 0x64]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186F10` fn_10186F10

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F10(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F10 lea eax, [ecx + 0x74]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186F20` Env_GetColorPtr84

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall Env_GetColorPtr84(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F20 lea eax, [ecx + 0x84]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns this+0x84, the secondary RGB colour block that Env_ComputeAmbient uses when its mode is 1.

### `0x10186F30` fn_10186F30

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F30(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F30 lea eax, [ecx + 0x94]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186F40` fn_10186F40

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F40(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F40 mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x10186F50` fn_10186F50

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F50(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F50 mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x10186F70` fn_10186F70

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F70(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F70 lea eax, [ecx + 0xe4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186F80` fn_10186F80

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F80(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F80 lea eax, [ecx + 0xf4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186F90` fn_10186F90

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186F90(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186F90 lea eax, [ecx + 0x114]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x10186FA0` Env_GetAmbientColorPtr

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall Env_GetAmbientColorPtr(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186FA0 lea eax, [ecx + 0x104]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns this+0x104, the ambient RGB float triple of the environment.

### `0x10186FB0` fn_10186FB0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186FB0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186FB0 mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x10186FC0` fn_10186FC0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __thiscall fn_10186FC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186FC0 mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x10186FD0` fn_10186FD0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API long double __thiscall fn_10186FD0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186FD0 mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x10186FE0` fn_10186FE0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API long double __thiscall fn_10186FE0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186FE0 mov eax, dword ptr [ecx + 0x1c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10186FF0` fn_10186FF0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API long double __thiscall fn_10186FF0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10186FF0 mov eax, dword ptr [ecx + 0x1c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10187000` fn_10187000

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API undefined4 __thiscall fn_10187000(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187000 mov eax, dword ptr [ecx + 0x1c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10187020` fn_10187020

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API long double __thiscall fn_10187020(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187020 mov eax, dword ptr [ecx + 0x1c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x10187030` fn_10187030

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10187030(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 58 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187031 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10187030`, `fn_10188A10`
- **Run by a frame** (frame_set.json): static

### `0x10187050` Env_ApplyRecord

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall Env_ApplyRecord(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187052 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10188910`
- **Reads globals:** `0x10377894`, `0x10377898`, `0x1037789C`, `0x103778A0`, `0x103778A4`, `0x103778A8`, `0x103778AC`, `0x103778B0`, `0x103778B4`, `0x103778B8`, `0x103778BC`, `0x103778C0`, `0x103778C4`, `0x103778C8`, `0x103778CC`, `0x103778D0`, `0x103778D4`, `0x103778D8`, `0x103778DC`, `0x103778E0`, `0x103778E4`, `0x103778E8`, `0x103778EC`, `0x103778F0`, `0x103778F4`, `0x103778F8`, `0x103778FC`, `0x10377900`, `0x10377904`, `0x10377908`, `0x1037790C`, `0x10377910`, `0x10377914`, `0x10377918`, `0x1037791C`, `0x10377920`, `0x10377924`, `0x10377928`, `0x1037792C`, `0x10377930`, `0x10377934`, `0x10377938`, `0x1037793C`, `0x10377940`, `0x10377944`, `0x10377948`, `0x1037794C`, `0x10377950`, `0x10377954`, `0x10377958`, `0x1037795C`, `0x10377960`, `0x10377964`, `0x10377968`, `0x1037796C`, `0x10377970`, `0x10377974`, `0x10377978`, `0x1037797C`, `0x10377980`, `0x10377984`, `0x10377988`, `0x1037798C`, `0x10377990`, `0x10377994`, `0x10377998`, `0x1037799C`, `0x103779A0`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Env_ApplyRecord` (not stated)
- **DancingMad note:** Copies environment record fields into the environment object: fog color +0x114..+0x11C, wind-like vector +0x124..+0x12C, strength +0x134.

### `0x10187380` fn_10187380

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void * __thiscall fn_10187380(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187381 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Env_ApplyRecord`
- **Run by a frame** (frame_set.json): static

### `0x10187470` fn_10187470

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10187470(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187471 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10188900`, `fn_10188970`, `fn_10188A10`
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static

### `0x101874A0` fn_101874A0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API uint32_t __thiscall fn_101874A0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 58 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101874A1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_101874A0`, `fn_10187600`, `fn_101880C0`, `Env_RampWindStrength`, `fn_1018ADD0`
- **Run by a frame** (frame_set.json): static, self, stack

### `0x101875C0` fn_101875C0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_101875C0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101875C1 mov esi, dword ptr [ecx + 0x10]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1018AB40`
- **Run by a frame** (frame_set.json): static

### `0x101875E0` fn_101875E0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_101875E0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101875E1 mov esi, dword ptr [ecx + 0x10]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1018AAC0`
- **Run by a frame** (frame_set.json): static

### `0x10187600` fn_10187600

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10187600(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10187600 mov eax, dword ptr [ecx + 0x10]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10187720`
- **Reads globals:** `dword_1065CB18`
- **Run by a frame** (frame_set.json): static, stack

### `0x101880C0` fn_101880C0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_101880C0(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x101880C6 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10014E00`, `fn_10014E60`, `fn_10014E80`, `fn_10014EB0`, `fn_10014ED0`, `fn_10186FE0`, `fn_10186FF0`, `fn_10188190`, `sub_10311C2C` ×3
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static, stack

### `0x10188190` fn_10188190

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10188190(void * self_, uint8_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1018819C mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_100274B0` ×5, `fn_10186EA0`, `fn_10186EC0`, `fn_10186EE0`, `fn_10186F00`, `fn_10186F10`, `Env_GetColorPtr84`, `fn_10186F30`, `fn_10186F40`, `fn_10186F50`, `fn_10186F80`, `fn_10186F90`, `Env_GetAmbientColorPtr`, `fn_10186FB0`, `fn_10186FC0`
- **Reads constants** (.rdata): 1
- **Reads globals:** `0x103779A4`, `0x103779A8`, `0x103779AC`, `0x103779B0`, `0x103779B4`, `0x103779B8`, `0x103779BC`, `0x103779C0`, `g_pXiZone`
- **Run by a frame** (frame_set.json): static, stack

### `0x10188900` fn_10188900

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __cdecl fn_10188900(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static

### `0x10188910` fn_10188910

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void __thiscall fn_10188910(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10188918 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10188900`, `fn_101889A0`
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static

### `0x10188970` fn_10188970

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API void * __thiscall fn_10188970(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10188971 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10188900`
- **Run by a frame** (frame_set.json): static

### `0x101889A0` fn_101889A0

- **Verified C++** (`tree/src/unit_10178790_ZoneMap.cpp`): `XI_API int __cdecl fn_101889A0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10188900`
- **Run by a frame** (frame_set.json): static
