# unit_10011A00_Post

### `0x10011A00` Frame_Render

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API unsigned __int8 __thiscall Frame_Render(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 68 returned normally, 536 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 68, town PASS 57, town2 PASS 57, combat PASS 57, zonetoinn PASS 57
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10011A14 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10001E70`, `DebugOverlay_Draw`, `sub_10005A40`, `fn_10008830`, `fn_100088F0`, `CDx::SetClearColor`, `CDx::TestCooperativeLevel`, `CDx::Present`, `CDx::BeginScene`, `CDx::EndScene`, `CDx::SetDefaultRenderState` ×2, `CDx::SetViewport`, `CDx::PushRenderTarget` ×3, `CDx::SetTexture` ×4, `fn_1000A390` ×2, `CDx::DrawTextureToViewport` ×2, `CDx::PushRenderTargetRet1`, `CDx::DrawFadeQuad`, `CDx::Post_DepthBlurComposite`, `sub_1000ABE0`, `CDx::StepFadeCounter`, `fn_1000BB10`, `fn_1000BB20`, `CDx::DrawStereoOddFrameOverlay`, `CDx::SetTransform` ×2, `CDx::CompositeSceneToBackBuffer`, `j_CEnv_UpdateDualTargetMode`, `CEnv::IsStereoMode`, `fn_10010520` ×2, `App_SetSeqStep`, `Post_Afterimage`, `Post_FlashAndZoomFeedback`, `fn_100139E0`, `fn_10013AC0`, `App_StepGameState5Connect`, `App_StepGameState6`, `App_StepGameState7`, `App_StepGameState8`, `App_StepGameState9`, `fn_10014170`, `fn_100149B0`, `fn_10014A20`, `sub_10014A30`, `sub_10014AD0`, `Camera_ApplyViewProjection`, `fn_10015740`, `fn_100163C0`, `fn_100163E0`, `App_SetGlobal_104569C8` ×2, `fn_10016410`, `App_SetErrorCode` ×3, `GammaRamp_ApplyIfChanged`, `_exit_0` ×4, `fn_100185A0`, `sub_10018850`, `Gfx_ProjectWorldToClip`, `Mat4_TransformPointInPlace`, `fn_100361D0`, `fn_10036230`, `Font_QueueText`, `Font_DrawPass`, `TexMgr_UploadPumpEntry`, `CMoResource_AddRefChain`, `sub_100731B0`, `CMoTaskMng::DrawAll`, `fn_100DA6A0`, `GameMode_PollPendingState`, `fn_100DB790` ×2, `fn_100DBE50`, `fn_101037F0`, `fn_10123E90`, `fn_101248A0`, `fn_10153FF0`, `fn_10154860`, `fn_101579C0`, `MenuMng_OpenByName`, `sub_1015F6A0`, `sub_1015FA00`, `Gfx_SetDefault2DStates`, `Gfx_DisableFogAndAlphaBlend`, `fn_10186FE0`, `fn_10187000`, `XiZone::GetInstance`, `XiZone::DrawScene`, `sub_1018C2B0`, `fn_1019C3E0` ×3, `fn_1019C5B0`, `fn_101A2E80`, `fn_101AB770`, `fn_101AB820`, `fn_101AE3E0`, `fn_101BCE30`, `fn_101C46A0`, `fn_101C4CC0`, `fn_101C4CD0`, `fn_101C4CE0`, `fn_101C4D10`, `CopyrightText_Draw`, `sub_101D0C70`, `fn_101D5680`, `CXiMovie::DrawFrame`, `Ui_KeyPrompt_Init`, `fn_10245B50`, `StDancer_Update`, `Dancer_WorldEnd`, `fn_10253670` ×2, `fn_1025B560`, `fn_1025E0B0` ×2, `fn_1025E0E0`, `fn_1025E0F0`, `sub_10311C2C` ×4, `__snprintf`
- **Calls imports:** `GetLocalTime`
- **Reads constants** (.rdata): 12
- **Indirect calls:** 51, of which 32 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_screenFadeLevel`, `g_frameCounterLastSecond`, `g_pGameMode`, `g_pApp`, `g_pAppSettings`, `g_pDebugOverlay`, `g_pAppInputState`, `g_pCDx`, `g_pEnv`, `g_pCamera`, `Code`, `dword_10456948`, `dword_10456950`, `dword_10456954`, `dword_10456958`, `dword_1045695C`, `g_frameStepFps`, `g_frameStepRingIndex`, `g_pSceneState`, `g_windowMode`, `g_depthBlurEnabled_Dead`, `g_cfg0022`, `g_pObj_Vtbl10329F8C`, `g_pXiOpening`, `g_pTextureMng`, `g_pMeshResourceMng`, `dword_1047D140`, `g_pCursor`, `g_pTargetMng`, `g_screenRectTopLeft`, `0x106218B6`, `g_screenRectBottomRight`, `0x106218BA`, `g_pXiZone`, `dword_1066279C`, `dword_106627EC`, `dword_10662DA8`, `ArgList`, `g_pFileMng`, `C`, `g_pMovie`, `g_pKeyPrompt`, `g_pStDancer`, `byte_10669420`
- **Writes globals:** `g_frameCounterLastSecond`, `g_frameMeshRes`, `Code`, `g_modelsDrawnThisFrame`, `g_modelDrawCallCount`, `dword_10456948`, `dword_1045694C`, `dword_10456950`, `dword_10456954`, `dword_10456958`, `dword_1045695C`, `g_frameStepFps`, `g_frameStepRingIndex`, `g_cfg0023`, `byte_1047D694`, `XiControlActor_isFirstPersonView`, `XiControlActor_isAutoRunning`, `g_screenRectTopLeft`, `0x106218B6`, `g_screenRectBottomRight`, `0x106218BA`, `dword_10669014`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `Frame_Render` (not stated)
- **DancingMad note:** Per-frame render function: TestCooperativeLevel, BeginScene, ~180 calls, EndScene, Present. 18-case state machine on this+0x44 (table 0x10012EEC).

### `0x10012F40` Post_Afterimage

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API int __cdecl Post_Afterimage(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 2268 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetDefaultRenderState`, `CDx::PushRenderTarget` ×2, `CDx::SetTexture` ×2, `CDx::DrawTextureToViewport` ×3, `CEnv::IsStereoMode`, `sub_10311C2C`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 21, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pEnv`, `g_afterimageStrength`, `g_afterimageTex`, `g_afterimageState`, `g_afterimagePhase`
- **Writes globals:** `g_afterimageState`, `g_afterimageBufferState`, `g_afterimagePhase`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Post_Afterimage` (not stated)
- **DancingMad note:** Full-res afterimage: blends the previous copy (g_afterimageTex) over the scene with alpha g_afterimageStrength*255, then re-copies. Textures are created by the scheduler opcode interpreter.

### `0x100132B0` Post_FlashAndZoomFeedback

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API int __thiscall Post_FlashAndZoomFeedback(void *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 3334 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100132B5 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::GetRenderTargetTop` ×2, `CDx::PushRenderTarget` ×4, `CDx::SetTexture` ×4, `CDx::DrawTextureToViewport` ×2, `CDx::DrawTexturedScreenQuad` ×2, `CDx::DrawPrimitiveUP` ×2, `CEnv::IsStereoMode` ×2
- **Reads constants** (.rdata): 1
- **Indirect calls:** 41, of which 19 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pEnv`, `g_feedbackBufferIndex`, `g_feedbackTexHalfRes`
- **Writes globals:** `g_feedbackQuad`, `g_flashQuadVerts_v0_y`, `g_flashQuadVerts_v1_x`, `g_flashQuadVerts_v1_y`, `g_flashQuadVerts_v2_x`, `g_flashQuadVerts_v2_y`, `g_flashQuadVerts_v3_x`, `g_flashQuadVerts_v3_y`, `g_feedbackBufferIndex`, `g_feedbackBufferState`, `g_feedbackActive`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Post_FlashAndZoomFeedback` (not stated)
- **DancingMad note:** (a) additive full-screen flash (colour app+0x324, alpha 2*app+0x327); (b) zoom-feedback trail: blends the previous half-res accumulation (g_feedbackTexHalfRes) over the scene with tint app+0x32C, alpha 2*app+0x32F, UV zoom app+0x330, then copies the scene back.

### `0x100139E0` fn_100139E0

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API undefined4 __thiscall fn_100139E0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100139E1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `App_AdvanceSeqStep`, `CXiOpening::Constructor`, `fn_10018840`, `Mem_AllocDefault`, `_strncpy`, `sub_10313520`
- **Calls imports:** `GetCurrentDirectoryA`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pAppSettings`, `g_pXiOpening`
- **Writes globals:** `g_pXiOpening`
- **Run by a frame** (frame_set.json): static

### `0x10013AC0` fn_10013AC0

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API undefined4 __cdecl fn_10013AC0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10013AD0` App_StepGameState5Connect

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API char __thiscall App_StepGameState5Connect(int self_, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 102 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10013AD4 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetClearColor`, `App_AdvanceSeqStep` ×3, `App_SetGlobal_104569C8`, `CYyCamMng2::CreateGlobal`, `CYyCamMng2::CallGlobalVfunc1`, `Vec3_Copy`, `Actor_ResetDrawLists`, `Call1008A0E0With2`, `GameMode_GetField98`, `GameMode_OpenTacticsUrl`, `GameSystems_InitializeAll`, `Game_DestroyGlobalObjects`, `CTsZoneMap_UpdateViewerPosition`, `ZoneMap_CopyField342C8ToField39450`, `ZoneMap_FindGroundHeight`, `fn_101AB6D0`, `fn_101AB720`, `LobbyThread_Start`, `Lobby_DestroyThreadPool`, `thunk_sub_10245BB0`
- **Indirect calls:** 10, of which 7 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pGameMode`, `g_pCDx`, `dword_1045694C`, `g_countdown_10456978`, `g_pZoneMap`
- **Writes globals:** `dword_1045694C`, `g_countdown_10456978`, `dword_10669014`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Step function for Frame_Render game state 5: sets up fog render states, initialises game systems and starts the lobby thread, polls the connection (updating the zone map around the player), then runs a 60-frame countdown before finishing.

### `0x10013DF0` App_StepGameState6

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API char __thiscall App_StepGameState6(_WORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 85, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10013DF1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetClearParams`, `App_RegisterSystemDats`, `App_AdvanceSeqStep` ×5, `Unit10086E90_ResetGlobals`, `GameMode_PollPendingState` ×3, `GameMode_RequestState` ×3, `MenuMng_OpenByName`, `Ui_KeyPrompt_Init`
- **Reads globals:** `g_pGameMode`, `g_pCDx`, `g_pKeyPrompt`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Frame_Render state-6 sequence: registers system DATs, loads the 'menu chdummy' resource, sets clear params, resets game data, then issues requests 6, 7 and 9 to off_103601BC, waiting for each to finish (>200 = failure).

### `0x10013F10` App_StepGameState7

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API char __thiscall App_StepGameState7(_WORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 85, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10013F11 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetClearParams`, `App_AdvanceSeqStep` ×5, `Unit10086E90_ResetGlobals`, `GameMode_PollPendingState` ×3, `GameMode_RequestState` ×3, `MenuMng_OpenByName`, `Ui_KeyPrompt_Init`
- **Reads globals:** `g_pGameMode`, `g_pCDx`, `g_pKeyPrompt`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Frame_Render state-7 sequence: like state 6 but without the DAT registration, issuing requests 6, 8 and 9.

### `0x10014030` App_StepGameState8

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API char __thiscall App_StepGameState8(_WORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 85, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10014031 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetClearParams`, `App_RegisterSystemDats`, `App_AdvanceSeqStep` ×3, `Unit10086E90_ResetGlobals`, `GameMode_PollPendingState` ×2, `GameMode_RequestState` ×2, `MenuMng_OpenByName`, `Ui_KeyPrompt_Init`
- **Reads globals:** `g_pGameMode`, `g_pCDx`, `g_pKeyPrompt`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Frame_Render state-8 sequence: registers DATs and resets data like state 6, skips request 6, then issues requests 8 and 9.

### `0x10014120` App_StepGameState9

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API bool __cdecl App_StepGameState9(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 70 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 70, town PASS 70, town2 PASS 70, combat PASS 70, zonetoinn PASS 70
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx::SetClearParams`, `App_RegisterSystemDats`, `Unit10086E90_ResetGlobals`, `MenuMng_OpenByName`, `Ui_KeyPrompt_Init`
- **Reads globals:** `g_pCDx`, `g_pKeyPrompt`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Frame_Render state-9 action: registers DATs, loads 'menu chdummy', sets clear params and resets game data in one call; returns the reset result.

### `0x10014170` fn_10014170

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API undefined4 __thiscall fn_10014170(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10014170 movsx eax, word ptr [ecx + 4]` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Game_InGameSubState0`, `sub_10014200`, `fn_100142A0`, `fn_100142B0`, `fn_10014350`
- **Run by a frame** (frame_set.json): static, stack

### `0x100141C0` fn_100141C0

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API char __thiscall fn_100141C0(_WORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100141C6 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx::StepFadeCounter`, `App_AdvanceSeqStep`
- **Reads globals:** `g_pAppSettings`, `g_pCDx`
- **Writes globals:** `word_104568F8`
- **Run by a frame** (frame_set.json): static

### `0x10014220` fn_10014220

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API undefined4 __thiscall fn_10014220(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10014221 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CYyCamMng2::CreateGlobal` ×3, `fn_100DB930`, `fn_100FC160`
- **Reads globals:** `g_pGameMode`, `dword_104DFD98`
- **Writes globals:** `0x104570E0`
- **Run by a frame** (frame_set.json): static

### `0x100142A0` fn_100142A0

- **Verified C++** (`tree/src/unit_10011A00_Post.cpp`): `XI_API undefined4 __thiscall fn_100142A0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Calls directly:** `App_AdvanceSeqStep`
- **Run by a frame** (frame_set.json): static
