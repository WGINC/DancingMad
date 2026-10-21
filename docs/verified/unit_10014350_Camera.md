# unit_10014350_Camera

### `0x10014CF0` Camera_GetFrameScale

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API long double __cdecl Camera_GetFrameScale(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 1
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns the float at g_pCamera+0x28, clamped to a minimum of 1.0.

### `0x10014D20` fn_10014D20

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API long double __cdecl fn_10014D20(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 1
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10015510` Camera_ApplyViewProjection

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl Camera_ApplyViewProjection(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 54 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 54, town PASS 59, town2 PASS 59, combat PASS 59, zonetoinn PASS 59
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×2, `Camera_SetViewMatrix`, `Camera_GetField50` ×6, `Camera_GetMatrix154Ptr`, `Camera_BuildProjection`, `Camera_UpdateController`, `sub_10021AE0`, `sub_10021B70`, `CameraCache_CacheViewProjection`, `sub_10044540`, `sub_10069F90`, `sub_1006A180`
- **Reads globals:** `g_pCDx`, `g_pCamera`, `g_pMoCamera`, `g_pResourceMng`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `Camera_ApplyViewProjection` (not stated)
- **DancingMad note:** Builds and sets D3DTS_VIEW then D3DTS_PROJECTION from the camera object at 0x104568FC.

### `0x100157E0` App_WinMain

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API int __cdecl App_WinMain(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `App_SetCommandLine`, `App_FreeCommandLine`, `App_DetectDat11`, `App_CreateConfig`, `App_DestroyConfig`, `Gfx_CreateD3DHolder` ×2, `Gfx_DestroyD3DHolder` ×2, `App_RunWithCOM`, `App_InitDataPaths`, `App_DestroyDataPaths`, `App_CheckOSVersion`, `App_IsRegistryFlagSet`, `App_InitSoundSystem`, `thunk_sub_10035900`, `App_SetGlobal_104569E8`, `App_SetErrorCode` ×2, `App_CreateMainWindow`, `App_DestroyMainWindow`, `App_LoadImeUiDll`, `App_UninitImeUi`, `App_EnableImeUi`, `App_LoadKeyInputDll`, `App_UnloadKeyInputDll`, `Thunk_FnTable694`
- **Reads globals:** `g_pAppSettings`, `g_pD3DHolder`, `hWnd`, `hmod`, `g_cmdLine`, `g_sceneStateStorage_30`, `g_installDir`, `g_sceneStateStorage_4C`, `phkResult`, `g_sceneStateStorage_68`, `g_sceneStateStorage_70`, `g_pSceneState`, `xRight`, `g_windowMode`, `g_cfgSoundEnabled`, `yBottom`
- **Writes globals:** `hWnd`, `g_sceneStateStorage_68`, `g_pSceneState`, `g_pHostFuncTable`, `g_pFileMng`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Process-level startup and shutdown: reads the command line and config, picks the data path, checks the OS, creates the 'FinalFantasyXI' window, IME/keyinput DLLs and D3D holder (retrying), inits sound and runs the app, then tears everything down in reverse.

### `0x100161B0` App_CreateRendererAndApp

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API char __cdecl App_CreateRendererAndApp(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 29 returned normally, 70 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 29, town PASS 29, town2 PASS 29, combat PASS 29, zonetoinn PASS 29
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CApp_Constructor`, `CDx_Constructor`, `CDx::SetDefaultRenderTargets`, `App_BeginTimerPeriod`, `sub_100191D0`, `Mem_AllocDefault` ×2, `ShapeMng_Init`, `MenuMng_Init`
- **Indirect calls:** 4, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pD3DHolder`, `g_pCDx`, `hWnd`, `hmod`, `g_installDir`, `g_sceneStateStorage_38`, `g_sceneStateStorage_3C`, `xRight`, `yBottom`
- **Writes globals:** `g_pApp`, `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates CDx (2640 bytes) from the D3DHolder device, stores the back-buffer size and default back-buffer/depth surfaces, constructs CApp (dword_103D3C64), begins the timer period and creates helper objects.

### `0x10016320` fn_10016320

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API _DWORD * __cdecl fn_10016320(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): no gate line
- **Convention facts:** pops 0 through its tail jump to 0x1015D9E0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_100191B0`, `sub_10120200`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pApp`, `g_pCDx`
- **Writes globals:** `g_pApp`, `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10017230` GammaRamp_ApplyIfChanged

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall GammaRamp_ApplyIfChanged(int self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 5 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10017231 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `GammaRamp_BuildRamps`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_windowMode`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): If the requested RGB gamma differs from the applied value, copies it over, rebuilds the ramps and calls SetGammaRamp (fullscreen mode 0 only).

### `0x10017310` fn_10017310

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API int __stdcall fn_10017310(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 26900 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 15, of which 15 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_rampGraphVerts`, `g_rampGraphVerts_v0_y`, `g_rampGraphVerts_v0_color`, `g_rampGraphVerts_v1_x`, `g_rampGraphVerts_v1_y`, `g_rampGraphVerts_v1_color`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
