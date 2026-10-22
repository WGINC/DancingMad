# CTsZoneMap

### `0x10177240` Gfx_AssembleVertexShader

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __thiscall Gfx_AssembleVertexShader(void *self_, int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 255 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10177252 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Gfx_ShaderSrc_GetText`, `Gfx_ShaderSrc_GetTextLength`, `_D3DXAssembleShader@24`, `_D3DXGetErrorStringA@12` ×2
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Assembles the vertex-shader source text held by this object, then creates a D3D8 vertex shader from the bytecode and the given declaration.

### `0x101773F0` fn_101773F0

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API undefined4 * __cdecl fn_101773F0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10177400` Gfx_SetZBias

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __cdecl Gfx_SetZBias(unsigned int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): self

### `0x10177420` ZoneMap_SetOverlayProjection

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API void __thiscall ZoneMap_SetOverlayProjection(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 200 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10177429 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `D3DXMatrixPerspectiveFovLH_static`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pCamera`
- **Run by a frame** (frame_set.json): stack

### `0x101779B0` fn_101779B0

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API undefined4 __thiscall fn_101779B0(void * self_, undefined4 * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 8 through its tail jump to 0x10173AE0 (tail_purges.json); entry ECX read: `0x101779B0 add ecx, 0x34330` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x101779C0` Gfx_SetupLineDrawState

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __cdecl Gfx_SetupLineDrawState(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 900 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`
- **Indirect calls:** 9, of which 9 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Prepares the device to draw untextured, unlit, vertex-coloured primitives: identity world matrix, no texture, FVF 0x142, and stage 0 selecting the current colour and alpha.

### `0x10177B40` Gfx_DrawQuadOutline

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __cdecl Gfx_DrawQuadOutline(float *a1, char a2, unsigned __int8 arg8, unsigned __int8 a4, char a5, char a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 38 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 6 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Draws a closed outline through four 3D points as a LINESTRIP, using one ARGB colour; when the last flag is 0 it turns the depth test off for the draw.

### `0x10177C50` Gfx_DrawLine3D

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __cdecl Gfx_DrawLine3D(int a1, int a2, int a3, int a4, int a5, int a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 6 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Draws a single coloured 3D line segment between two points.

### `0x10177CD0` fn_10177CD0

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __thiscall fn_10177CD0(void *self_, float *a2, int a3, float a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10177CE5 add ecx, 0x178` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Dbg_DrawWireMesh`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10177D00` fn_10177D00

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API void * __thiscall fn_10177D00(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 50 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10177D04 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10027990`, `fn_10054FC0`, `CMoTask_Constructor`, `fn_10167440`, `fn_10167800`, `fn_1016FC40`, `fn_101718E0`, `fn_10177FA0`, `fn_101784E0`
- **Writes globals:** `0x10376EE8`, `g_zbiasRestore`, `0x10621C70`, `0x10621C74`, `0x10621C78`, `0x10621C7C`, `0x10621C80`, `g_zbiasOverlay`, `g_zbiasPresetAux`, `g_zbiasZoneMesh`, `g_zoneLoggingActive`, `g_zbiasPreset_C4D0`, `0x1065C4D4`, `0x1065C5D8`
- **Run by a frame** (frame_set.json): static

### `0x10177FA0` fn_10177FA0

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API void __thiscall fn_10177FA0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10177FA1 mov ebp, dword ptr [ecx + 0x394a4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10178070` CTsZoneMap::CTsZoneMap_Destructor

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `char CTsZoneMap::CTsZoneMap_Destructor()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100747C0 (tail_purges.json); entry ECX read: `0x10178072 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100279A0`, `Vt1032B6D8_Destructor`, `Vt10336614_Destructor`, `Vt10336634_Destructor`, `Vt10336668_Destructor`, `Vt1033668C_Destructor`, `ZoneMap_ReleaseStateBlock`, `ZoneMap_TeardownStep`
- **Indirect calls:** 8, of which 8 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): CTsZoneMap destructor: restores the vtable, tears down the zone, deletes its vertex and pixel shaders, and destroys member subobjects.

### `0x101781D0` CTsZoneMap::InitZBiasPresets

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `int CTsZoneMap::InitZBiasPresets()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101781F7 mov dword ptr [ecx + 0x3954c], 0x3f800000` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_zbiasRestore`, `g_zbiasOverlay`, `g_zbiasPresetAux`, `g_zbiasZoneMesh`, `g_zbiasPreset_C4D0`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Initialises the global z-bias presets (zone mesh, aux, overlay, restore) and uses a smaller set when a CDx capability flag is set.

### `0x101784E0` fn_101784E0

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API void __cdecl fn_101784E0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Run by a frame** (frame_set.json): static

### `0x10178B00` ZoneMap_ReleaseStateBlock

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `XI_API int __thiscall ZoneMap_ReleaseStateBlock(CTsZoneMap *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10178B01 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10179390` CTsZoneMap::UpdateViewerPosition

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `void __thiscall CTsZoneMap::UpdateViewerPosition(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10179394 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetField50` ×2, `Vec3_Copy`, `fn_1016C150`
- **Run by a frame** (frame_set.json): static, stack

### `0x10182700` CTsZoneMap::DrawProjectedTexture

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `float * CTsZoneMap::DrawProjectedTexture(float *arg0, int a3, IDirect3DBaseTexture8 *a4, float a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 55 returned normally, 400 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 55, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 71
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10182715 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `GetPtr8IfField60Set`, `Mat44_Multiply` ×3, `sub_10311C2C` ×2
- **Reads constants** (.rdata): 3
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `CTsZoneMap_DrawProjectedTexture_m30`, `CTsZoneMap_DrawProjectedTexture_m31`, `CTsZoneMap_DrawProjectedTexture_m32`, `CTsZoneMap_DrawProjectedTexture_m00`, `CTsZoneMap_DrawProjectedTexture_m11`, `CTsZoneMap_DrawProjectedTexture_m22`, `g_pCDx`
- **Writes globals:** `CTsZoneMap_DrawProjectedTexture_m00`, `CTsZoneMap_DrawProjectedTexture_m22`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Projects texture a4 onto the zone meshes in the 3x3 grid of 4-unit cells around position a2, using a texture matrix built from translate(-pos), scale(1/a5) and an offset. (pseudocode truncated)

### `0x101844C0` CTsZoneMap::ModelActor_Draw

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `void CTsZoneMap::ModelActor_Draw(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 65 returned normally, 18903 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 65, town PASS 77, town2 PASS 76, combat PASS 77, zonetoinn PASS 76
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x101844D1 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::SetLight` ×5, `CDx::DrawPrimitive`, `Gfx_SetZBias`, `ZoneMap_FindLight`, `XiZone::GetDirLights`, `XiZone::GetDirLight`, `XiZone::GetAmbient`, `XiZone::GetFog`
- **Indirect calls:** 56, of which 53 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_zbiasZoneMesh`, `g_pXiZone`, `C`
- **Run by a frame** (frame_set.json): self, stack

### `0x10184FE0` CTsZoneMap::DrawProjectedShadow

- **Verified C++** (`tree/src/CTsZoneMap.cpp`): `int CTsZoneMap::DrawProjectedShadow(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 58
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10184FF5 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::DrawPrimitiveUP`, `GetPtr8IfField60Set`, `Gfx_SetZBias` ×2, `ZoneMap_SetOverlayProjection`, `sub_10311C2C` ×5
- **Reads constants** (.rdata): 4
- **Indirect calls:** 20, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_projectedShadowBiasX`, `c_projectedShadowBiasY`, `c_projectedShadowBiasZ`, `g_pCDx`, `g_zbiasRestore`, `g_zbiasOverlay`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Projects a darkening texture (multiplicative blend) onto the zone meshes in the 3x3 grid around position a1 with radius a2. This looks like a ground shadow or decal. (pseudocode truncated)
