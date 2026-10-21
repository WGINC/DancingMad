# CDx

### `0x10008F80` CDx::GetRuntimeClass

- **Verified C++** (`tree/src/CDx.cpp`): `_UNKNOWN ** __cdecl CDx::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CDx_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10009100` CDx::ScalarDeletingDtor

- **Verified C++** (`tree/src/CDx.cpp`): `void * CDx::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10009101 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx_Destructor`, `thunk_sub_10028AA0`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100091B0` CDx::Initialize

- **Verified C++** (`tree/src/CDx.cpp`): `char CDx::Initialize()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 900 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100091B8 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `_strrchr` ×2
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::GetDeviceCaps`, `IDirect3DDevice8::GetDisplayMode`
- **Calls imports:** `GetCurrentDirectoryA`, `LoadCursorA`, `LoadCursorFromFileA`, `SetCursor`
- **Indirect calls:** 9, of which 9 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_strBackslash`, `c_strSlash`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_Initialize` (not stated)
- **DancingMad note:** CheckDeviceFormat x3, multisample checks x2, loads mousenor.ani. Queries shader-model support (verified D3DVS_VERSION/D3DPS_VERSION constants) and texture-stage count (8 vs 16, gated on a capability bit).

### `0x10009620` CDx::SetDefaultRenderTargets

- **Verified C++** (`tree/src/CDx.cpp`): `char CDx::SetDefaultRenderTargets(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10009628 mov dword ptr [ecx + 0x90], eax` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Stores the default back-buffer and depth-stencil surfaces in CDx (+0x90/+0x94) and returns 1.

### `0x10009640` CDx::SetClearParams

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetClearParams(int a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10009648 mov dword ptr [ecx + 0x164], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Stores Clear() parameters (flags, color, Z, stencil) in CDx fields +0x164..+0x170.

### `0x10009670` CDx::SetClearColor

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetClearColor(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10009674 mov dword ptr [ecx + 0x168], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets only the stored clear colour (CDx +0x168).

### `0x100096B0` CDx::EndClearBegin

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::EndClearBegin(int a2, int a3, int a4, int a5, int a6, int a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x100096B2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::BeginScene`, `CDx::EndScene`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::Clear`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pAppSettings`
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_EndClearBegin` (not stated)
- **DancingMad note:** EndScene, Clear (adds stencil flag if holder+0x5C set), BeginScene.

### `0x10009710` CDx::TestCooperativeLevel

- **Verified C++** (`tree/src/CDx.cpp`): `bool CDx::TestCooperativeLevel()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10009710 mov eax, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::TestCooperativeLevel`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_TestCooperativeLevel` (not stated)
- **DancingMad note:** Device-lost check at frame start.

### `0x10009720` CDx::Present

- **Verified C++** (`tree/src/CDx.cpp`): `int __cdecl CDx::Present()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 124 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `nullsub_13`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pD3DHolder`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CDx_Present` (not stated)
- **DancingMad note:** Loads g_pD3DHolder and tail-jumps to D3DHolder_Present. Sole caller: Frame_Render.

### `0x10009730` CDx::BeginScene

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::BeginScene()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10009730 mov eax, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::BeginScene`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CDx_BeginScene` (not stated)
- **DancingMad note:** thiscall shim: device->BeginScene.

### `0x10009740` CDx::EndScene

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::EndScene()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10009740 mov eax, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::EndScene`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CDx_EndScene` (not stated)
- **DancingMad note:** thiscall shim: device->EndScene.

### `0x100097F0` CDx::SetCursorShape

- **Verified C++** (`tree/src/CDx.cpp`): `HCURSOR CDx::SetCursorShape(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 77 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 77, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100097F7 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Cursor_GetHwCursorSlot`
- **Calls imports:** `LoadCursorA`, `SetCursor`
- **Reads globals:** `g_cfgHardwareMouse`, `g_pCursor`
- **Run by a frame** (frame_set.json): static, self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): When the hardware cursor is enabled, maps a cursor state (0-6) to one of the cached HCURSOR slots at CDx+0xA04, loading IDC_ARROW on first use, and calls SetCursor.

### `0x10009920` CDx::SetDefaultRenderState

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetDefaultRenderState()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 2384 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10009922 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10009870` ×2, `sub_100098E0` ×2
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×48, `IDirect3DDevice8::SetTextureStageState`
- **Indirect calls:** 49, of which 49 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_SetDefaultRenderState` (not stated)
- **DancingMad note:** 345 instructions of SetRenderState/SetTextureStageState defaults; called at frame start.

### `0x10009DC0` CDx::SetViewport

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetViewport(const void *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10009DC0 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_SetViewport` (not stated)
- **DancingMad note:** device->SetViewport.

### `0x10009E00` CDx::GetRenderTargetTop

- **Verified C++** (`tree/src/CDx.cpp`): `unsigned __int8 * CDx::GetRenderTargetTop()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10009E02 mov al, byte ptr [ecx + 0x158]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **DancingMad name:** `CDx_GetRenderTargetTop` (not stated)
- **DancingMad note:** Returns &CDx[0x98 + depth*24], depth = byte CDx+0x158 (render-target stack).

### `0x10009E20` CDx::PushRenderTarget

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::PushRenderTarget(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx_PushRenderTargetTexture`
- **Run by a frame** (frame_set.json): static, stack

### `0x1000A1D0` CDx::SetTexture

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetTexture(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000A1D1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx_PopRenderTarget`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetTexture`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CDx_SetTexture` (not stated)
- **DancingMad note:** device->SetTexture. 19 callers.

### `0x1000A3B0` CDx::DrawScreenQuadAtDepth

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::DrawScreenQuadAtDepth(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 200 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000A3B7 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::GetRenderTargetTop` ×2, `CDx::DrawPrimitiveUP`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetTexture`, `IDirect3DDevice8::SetVertexShader`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_DrawScreenQuadAtDepth` (not stated)
- **DancingMad note:** Screen quad (FVF XYZRHW|DIFFUSE|TEX1) covering the current target at a given z.

### `0x1000A5A0` CDx::DrawTexturedScreenQuad

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::DrawTexturedScreenQuad(int a1, int a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 200 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x1000A5A4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetTexture`, `IDirect3DDevice8::SetVertexShader`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Draws a pre-transformed textured quad: builds 4 XYZRHW\|DIFFUSE\|TEX1 vertices from a pixel rect (with -0.5 offset), UV rect and colour, binds the texture to stage 0 and draws a triangle strip.

### `0x1000A6E0` CDx::CreateTexture

- **Verified C++** (`tree/src/CDx.cpp`): `_DWORD * CDx::CreateTexture(unsigned __int16 width, unsigned __int16 height, _DWORD * a4, int a5, int a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 229 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town UNRESOLVED 0, town2 UNRESOLVED 0, combat UNRESOLVED 0, zonetoinn UNRESOLVED 0
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x1000A6ED mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::CreateTexture` ×5
- **Indirect calls:** 6, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_CreateTexture` (not stated)
- **DancingMad note:** Sole texture-creation wrapper; format passed as variable. 10 calling functions.

### `0x1000A800` CDx::PushRenderTargetRet1

- **Verified C++** (`tree/src/CDx.cpp`): `char CDx::PushRenderTargetRet1(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx::PushRenderTarget`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Calls CDx_PushRenderTarget with the same arguments and returns 1.

### `0x1000A820` CDx::DrawFadeQuad

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::DrawFadeQuad(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 1552 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000A825 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetDefaultRenderState` ×2, `CDx::GetRenderTargetTop` ×8, `CDx::DrawPrimitiveUP`
- **Indirect calls:** 18, of which 18 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Writes globals:** `g_fadeQuadVerts`, `g_fadeQuadVerts_v0_y`, `g_fadeQuadVerts_v0_color`, `g_fadeQuadVerts_v1_x`, `g_fadeQuadVerts_v1_y`, `g_fadeQuadVerts_v1_color`, `g_fadeQuadVerts_v2_x`, `g_fadeQuadVerts_v2_y`, `g_fadeQuadVerts_v2_color`, `g_fadeQuadVerts_v3_x`, `g_fadeQuadVerts_v3_y`, `g_fadeQuadVerts_v3_color`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CDx_DrawFadeQuad` (not stated)
- **DancingMad note:** Global fade quad: alpha <= 0x80 darkens (fade to black), > 0x80 adds (fade to white).

### `0x1000AAB0` CDx::Post_DepthBlurComposite

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::Post_DepthBlurComposite(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 1500 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000AAB1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetDefaultRenderState`, `CDx::DrawScreenQuadAtDepth`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×5, `IDirect3DDevice8::SetTextureStageState` ×10
- **Indirect calls:** 15, of which 15 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Post_DepthBlurComposite` (not stated)
- **DancingMad note:** Draws the 256x256 downsampled scene copy back as a screen quad at a projected depth with Z-test on / Z-write off (distance blur). Only reachable when g_depthBlurEnabled_Dead != 0, which never happens in the shipping client.

### `0x1000BB90` CDx::DrawStereoOddFrameOverlay

- **Verified C++** (`tree/src/CDx.cpp`): `char CDx::DrawStereoOddFrameOverlay(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 384 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1000BB98 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::DrawPrimitiveUP`, `CEnv_IsStereoMode`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×4, `IDirect3DDevice8::SetTexture`, `IDirect3DDevice8::SetVertexShader`
- **Indirect calls:** 6, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `CDx_DrawStereoOddFrameOverlay_staticGuard`, `g_pEnv`
- **Writes globals:** `CDx_DrawStereoOddFrameOverlay_staticGuard`, `CDx_DrawStereoOddFrameOverlay_quadVerts`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v0_y`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v0_z`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v0_rhw`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v0_color`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v0_u`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v0_v`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_x`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_y`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_z`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_rhw`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_color`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_u`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v1_v`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_x`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_y`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_z`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_rhw`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_color`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_u`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v2_v`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_x`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_y`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_z`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_rhw`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_color`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_u`, `CDx_DrawStereoOddFrameOverlay_quadVerts_v3_v`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_DrawStereoOddFrameOverlay` (medium)
- **DancingMad note:** Stereo mode only: draws the 1x16 texture CDx+0x82C stretched as a screen-space quad (FVF 0x144, Z off) over a caller rect. Frame_Render calls it only on odd values of the CEnv+0x1C 0..3 counter -- a per-frame alternating overlay, consistent with a frame-sequential/shutter sync signal. Output-format detail is Medium confidence.

### `0x1000BD50` CDx::SetTransform

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetTransform(int a2, const void *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000BD59 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_SetTransform` (not stated)
- **DancingMad note:** Caches matrix (WORLD +0x93C, VIEW +0x97C, PROJECTION +0x9BC) then device->SetTransform. 51 callers.

### `0x1000BDB0` CDx::GetTransformCached

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::GetTransformCached(int a2, void *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000BDF5 lea esi, [ecx + 0x97c]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **DancingMad name:** `CDx_GetTransformCached` (not stated)
- **DancingMad note:** Copies WORLD/VIEW/PROJECTION back out of CDx cache.

### `0x1000BF30` CDx::SetLight

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::SetLight(int a2, float *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 3 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000BF39 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Light_ApplyTimeOfDayTint`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetLight` ×2
- **Reads constants** (.rdata): 1
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CDx_SetLight` (not stated)
- **DancingMad note:** device->SetLight. 34 callers. CORRECTED and fully resolved (was named RenderCommand_ValidateAndDispatch on a guess). This is D3D's real light-setting pipeline. Validates a light entry from g_lightTable against the real D3D8 D3DLIGHTTYPE enum exactly: tag 1 (D3DLIGHT_POINT) requires Range/Falloff >= 0, tag 3 (D3DLIGHT_DIRECTIONAL) requires a non-zero Direction vector. Rejects with the real D3DERR_INVALIDCALL HRESULT (0x8876086C) on failure -- verified precisely. On success, calls Light_ApplyTimeOfDayTint, then dispatches to the real device SetLight-equivalent virtual call (vtable offset 0xB0).

### `0x1000C0B0` CDx::CompositeSceneToBackBuffer

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::CompositeSceneToBackBuffer(int a1, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 3394 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1000C0B7 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::PushRenderTarget`, `CDx::SetTexture`, `CDx::DrawTexturedScreenQuad` ×2, `CDx::DrawPrimitiveUP` ×2, `CEnv_IsStereoMode`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×16, `IDirect3DDevice8::SetTextureStageState` ×36, `IDirect3DDevice8::SetVertexShader`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 56, of which 56 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pEnv`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CDx_CompositeSceneToBackBuffer` (not stated)
- **DancingMad note:** Final composite: draws scene target A over the window viewport with LINEAR filtering and MODULATE2X - this is where the background resolution is upscaled to the window. In stereo mode (registry 0030; left eye = A, right eye = B) A and B are first packed side by side into the target at CDx+0x824 and drawn with alpha test.

### `0x1000C6E0` CDx::CreateStereoResources

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::CreateStereoResources(unsigned __int16 a1, unsigned __int16 a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000C6EA mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::CreateTexture`, `CDx::ReleaseStereoResources`, `CDx::CreateRampTexture1x16`, `CDx::CreateRampTextures1024x2` ×2, `nullsub_38`
- **Reads globals:** `g_pEnv`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_CreateStereoResources` (not stated)
- **DancingMad note:** When CEnv+0x18: two 1024x2 two-row mask textures via CDx_CreateRampTextures1024x2 (+0x814 rows magenta/green, +0x81C rows green/magenta, alpha 0x80), a 1x16 A8R8G8B8 texture at +0x82C via CDx_CreateRampTexture1x16, and the side-by-side pack target at +0x824. On any failure: calls 0x1000D620 (an empty stub in this build) and releases everything.

### `0x1000C7C0` CDx::ReleaseStereoResources

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::ReleaseStereoResources()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 464 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1000C7C1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 6, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_ReleaseStereoResources` (not stated)
- **DancingMad note:** Releases +0x814/+0x81C/+0x824/+0x82C.

### `0x1000C850` CDx::CreateRampTexture1x16

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::CreateRampTexture1x16(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 32 returned normally, 68 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 32, town PASS 32, town2 PASS 32, combat PASS 32, zonetoinn PASS 32
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1000C86B mov ecx, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `_D3DXCreateTexture@32`
- **Indirect calls:** 2, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pEnv`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_CreateRampTexture1x16` (not stated)
- **DancingMad note:** Procedural 1x16 A8R8G8B8 ramp texture (D3DXCreateTexture + LockRect).

### `0x1000C900` CDx::CreateRampTextures1024x2

- **Verified C++** (`tree/src/CDx.cpp`): `char CDx::CreateRampTextures1024x2(IDirect3DTexture8 **a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 32 returned normally, 68 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 32, town PASS 34, town2 PASS 34, combat PASS 34, zonetoinn PASS 34
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000C909 mov dword ptr [esp + 4], ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `_D3DXCreateTexture@32`
- **Indirect calls:** 2, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pEnv`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_CreateRampTextures1024x2` (not stated)
- **DancingMad note:** Two procedural 1024x2 A8R8G8B8 ramp textures from a colour table.

### `0x1000CA00` CDx::GetStereoSecondEyeTarget

- **Verified C++** (`tree/src/CDx.cpp`): `char CDx::GetStereoSecondEyeTarget(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 44 returned normally, 56 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 44, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1000CA05 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CEnv_IsStereoMode`
- **Indirect calls:** 8, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pEnv`, `pTexture`, `g_translucentTargetEye2`
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_GetStereoSecondEyeTarget` (not stated)
- **DancingMad note:** Called by every CDx draw entry point. If CDx+0x828 (stereo-draw flag) and stereo mode are on and the current RT is scene A or B, returns scene B colour (+0x198) and depth (+0x1A8) so the draw is repeated for the second eye.

### `0x1000CB20` CDx::DrawPrimitive

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::DrawPrimitive(int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 168 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1000CB28 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::PushRenderTarget`, `CDx_PopRenderTargetDefault`, `CDx::GetStereoSecondEyeTarget`, `CDx::ApplyStereoEyeProjection` ×2, `CDx::RestoreProjection` ×2
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::DrawPrimitive` ×3
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_DrawPrimitive` (not stated)
- **DancingMad note:** device->DrawPrimitive. 8 calling functions.

### `0x1000CC00` CDx::DrawIndexedPrimitive

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::DrawIndexedPrimitive(int a1, int a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 169 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x1000CC08 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::PushRenderTarget`, `CDx_PopRenderTargetDefault`, `CDx::GetStereoSecondEyeTarget`, `CDx::ApplyStereoEyeProjection` ×2, `CDx::RestoreProjection` ×2
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::DrawIndexedPrimitive` ×3
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CDx_DrawIndexedPrimitive` (not stated)
- **DancingMad note:** device->DrawIndexedPrimitive. 5 calling functions.

### `0x1000CD00` CDx::DrawPrimitiveUP

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::DrawPrimitiveUP(int a1, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 168 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1000CD08 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::PushRenderTarget`, `CDx_PopRenderTargetDefault`, `CDx::GetStereoSecondEyeTarget`, `CDx::ApplyStereoEyeProjection` ×2, `CDx::RestoreProjection` ×2
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::DrawPrimitiveUP` ×3
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `CDx_DrawPrimitiveUP` (not stated)
- **DancingMad note:** device->DrawPrimitiveUP. 50 calling functions engine-wide -- the dominant draw path.

### `0x1000CF20` CDx::ApplyStereoEyeProjection

- **Verified C++** (`tree/src/CDx.cpp`): `void CDx::ApplyStereoEyeProjection()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1000CF24 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `??0Iostream_init@@QAE@XZ_0`, `nullsub_1`, `Mat4_SetIdentity`, `Mat4_PreMultiply`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetTransform`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_stereoEyeOffset`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_ApplyStereoEyeProjection` (not stated)
- **DancingMad note:** Stereo: builds identity, sets _41 (X translation) to -g_stereoEyeOffset for eye 0 (CDx+0x810==0) or +g_stereoEyeOffset for eye 1, multiplies into the saved projection (CDx+0x9BC) and SetTransform(D3DTS_PROJECTION).

### `0x1000CF90` CDx::RestoreProjection

- **Verified C++** (`tree/src/CDx.cpp`): `int CDx::RestoreProjection()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1000CF90 mov eax, dword ptr [ecx + 0xc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetTransform`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CDx_RestoreProjection` (not stated)
- **DancingMad note:** Stereo: SetTransform(D3DTS_PROJECTION, CDx+0x9BC).
