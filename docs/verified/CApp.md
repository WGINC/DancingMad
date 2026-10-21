# CApp

### `0x10001520` CApp::RunMainLoop

- **Verified C++** (`tree/src/CApp.cpp`): `char CApp::RunMainLoop()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 75 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 75, town PASS 64, town2 PASS 64, combat PASS 64, zonetoinn PASS 64
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10001525 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `App_ForceForegroundWindow` ×2, `App_PreTranslateInputMessage`, `App_RenderFrameMaskedFPU`, `App_CreateInputSystem`, `CApp_CopyTextToClipboard` ×2, `CDx::Initialize`, `App_Constructor`, `App_SetSeqStep`, `App_InitScene`, `sub_10014C10`, `Allocator_Generic`
- **Calls imports:** `DispatchMessageA`, `GetWindowRect`, `TranslateMessage`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pCamera`
- **Writes globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): CApp main loop: initialises CDx and input, creates the app/camera object, runs App_InitScene until done, then pumps PeekMessage and renders frames until WM_QUIT, finally running shutdown.
