# unit_100014A0_Gfx

### `0x10001B50` App_RenderFrameMaskedFPU

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API undefined4 __cdecl App_RenderFrameMaskedFPU(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Frame_Render`, `sub_100DAF30`, `sub_10311C7A` ×4
- **Reads globals:** `g_pGameMode`, `g_pCamera`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Masks all FPU exceptions, calls Frame_Render(g_pCamera), restores the FPU control word, and on success runs an update on off_103601BC; returns success.

### `0x10001BB0` App_CreateInputSystem

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API undefined4 __stdcall App_CreateInputSystem(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10005660`, `sub_100058F0`, `Allocator_Generic`
- **Writes globals:** `g_pAppInputState`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Allocates a 0xDC4-byte input object into dword_10455C20, constructs it and initialises it with the HINSTANCE.

### `0x10001D90` fn_10001D90

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API void __cdecl fn_10001D90(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CTkMouse_OnMouseMove`, `fn_1015EDB0`, `fn_1025E210`
- **Reads globals:** `g_pCursor`
- **Run by a frame** (frame_set.json): static

### `0x10001E70` fn_10001E70

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API undefined4 __cdecl fn_10001E70(char * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `operator_delete`, `Allocator_Generic`
- **Reads globals:** `c_strSpace`, `0x103D3C88`
- **Writes globals:** `0x103D3C88`
- **Run by a frame** (frame_set.json): static

### `0x10001F20` fn_10001F20

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API undefined4 __cdecl fn_10001F20(undefined4 param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10001F40`
- **Run by a frame** (frame_set.json): static

### `0x10001F40` fn_10001F40

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char * __cdecl fn_10001F40(char * param_1, char * param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 79 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10311EB0` ×3
- **Reads globals:** `0x103D3C88`
- **Run by a frame** (frame_set.json): static

### `0x10002040` Gfx_CopySurfaceRectToTexture

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char __cdecl Gfx_CopySurfaceRectToTexture(struct IDirect3DSurface8 *a1, const struct tagRECT *a2, unsigned int *a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 98 returned normally, 257 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 98, town PASS 97, town2 PASS 98, combat PASS 98, zonetoinn PASS 98
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Gfx_ProbeDeviceCaps`, `CDx::CreateTexture` ×2, `_D3DXLoadSurfaceFromSurface@32`
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Creates a texture the size of a rect (falling back to 512x512), copies a source-surface region into level 0 with D3DXLoadSurfaceFromSurface, passes the surface to a follow-up routine, then releases everything.

### `0x10002130` Gfx_ProbeDeviceCaps

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char __cdecl Gfx_ProbeDeviceCaps(int a1, unsigned int *a2, int *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 21 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 21, town PASS 21, town2 PASS 21, combat PASS 21, zonetoinn PASS 21
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10002440` ×4
- **Indirect calls:** 6, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Gfx_ProbeDeviceCaps` (not stated)
- **DancingMad note:** CheckDeviceType + CheckDeviceFormat probes, including DXT1/DXT3/DXT5.

### `0x10002440` fn_10002440

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API uint32_t __cdecl fn_10002440(uint32_t param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x10002BE0` Gfx_IsGammaSupported

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API unsigned __int8 __cdecl Gfx_IsGammaSupported(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns CDx byte +0x915 (0 if there is no CDx); the flag that gates gamma-ramp save and restore.

### `0x10002C00` Gfx_SetGammaRGB

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API CDx * __cdecl Gfx_SetGammaRGB(int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `GammaRamp_SetRGB`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets the R/G/B gamma values of the CDx gamma-ramp object.

### `0x10002C30` Gfx_SetGammaR

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API CDx * __cdecl Gfx_SetGammaR(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Gfx_SetGammaRGB`, `GammaRamp_GetRGB`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets only the red gamma component, keeping green and blue.

### `0x10002C80` Gfx_SetGammaG

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API CDx * __cdecl Gfx_SetGammaG(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Gfx_SetGammaRGB`, `GammaRamp_GetRGB`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets only the green gamma component, keeping red and blue.

### `0x10002CD0` Gfx_SetGammaB

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API CDx * __cdecl Gfx_SetGammaB(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Gfx_SetGammaRGB`, `GammaRamp_GetRGB`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Sets only the blue gamma component, keeping red and green.

### `0x10002D20` Gfx_GetGammaRGB

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API int __cdecl Gfx_GetGammaRGB(int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `GammaRamp_GetRGB`
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Reads the three gamma components into the caller's out-pointers.

### `0x10002D80` fn_10002D80

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API long double __cdecl fn_10002D80(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Calls directly:** `sub_10087110`
- **Reads constants** (.rdata): 1
- **Reads globals:** `0x10456A68`
- **Run by a frame** (frame_set.json): static, self

### `0x10002E60` fn_10002E60

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API void __cdecl fn_10002E60(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10002E80 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x10456BE8`
- **Run by a frame** (frame_set.json): static

### `0x10002E80` fn_10002E80

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API void __cdecl fn_10002E80(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10002EC0`, `fn_10002EE0`, `fn_100153A0`
- **Run by a frame** (frame_set.json): static

### `0x10002EC0` fn_10002EC0

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API long double __cdecl fn_10002EC0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10002EE0` fn_10002EE0

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API long double __cdecl fn_10002EE0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10002F20` Gfx_CreateD3DHolder

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char __cdecl Gfx_CreateD3DHolder(int a1, int a2, int a3, char a4, char a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 5 argument slot(s) (cdecl_args.json)
- **Calls directly:** `D3DHolder_Constructor`, `D3DHolder_Initialize`, `Allocator_Generic`
- **Reads globals:** `g_pD3DHolder`
- **Writes globals:** `g_pD3DHolder`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `Gfx_CreateD3DHolder` (not stated)
- **DancingMad note:** Allocates the 0x478-byte D3D holder, stores it in g_pD3DHolder, and runs device bootstrap.

### `0x10003040` Gfx_DestroyD3DHolder

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API int __cdecl Gfx_DestroyD3DHolder(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 98, town2 PASS 98, combat PASS 98, zonetoinn PASS 98
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `nullsub_71`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pD3DHolder`
- **Writes globals:** `g_pD3DHolder`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Releases and deletes g_pD3DHolder through its virtual deleting destructor and clears it.

### `0x100031F0` Gfx_D3DBootstrap

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char __thiscall Gfx_D3DBootstrap(int self_, int a2, int a3, int a4, char a5, char a6, int a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 27 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 27, town PASS 27, town2 PASS 27, combat PASS 27, zonetoinn PASS 27
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x100031FB mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Gfx_TryCreateDeviceForMode` ×4, `Direct3DCreate8`, `Allocator_Generic`
- **Indirect calls:** 3, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `dword_10456A80`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `Gfx_D3DBootstrap` (not stated)
- **DancingMad note:** Direct3DCreate8(220 = DX8.1) -> holder+4; GetAdapterModeCount -> +0x40; enumerates modes (640x480..2048x2048, X8R8G8B8/A8R8G8B8) into +0x44.

### `0x100033C0` Gfx_TryCreateDeviceForMode

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char __thiscall Gfx_TryCreateDeviceForMode(_DWORD **self_, int a2, int a3, int a4, char a5, char a6, int a7, int a8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 99, town2 PASS 99, combat PASS 99, zonetoinn PASS 99
- **Convention facts:** `ret 28` (purges.json); entry ECX read: `0x100033C8 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `D3DHolder_CheckDepthFormat`, `Gfx_CreateDevice`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `Gfx_TryCreateDeviceForMode` (not stated)
- **DancingMad note:** Called twice (arg 0 then 1): first-attempt-then-fallback wrapper around Gfx_CreateDevice.

### `0x100034B0` Gfx_CreateDevice

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API char __thiscall Gfx_CreateDevice(_DWORD *self_, int a2, int a3, int a4, int a5, int a6, char a7, char a8, int a9)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 182 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 32` (purges.json); entry ECX read: `0x100034B7 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pAppSettings`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `Gfx_CreateDevice` (not stated)
- **DancingMad note:** GetDeviceCaps, fills D3DPRESENT_PARAMETERS, IDirect3D8::CreateDevice with BehaviorFlags 0x40 (HW VP) or 0x20 (SW VP) by argument; device -> holder+8.

### `0x100035F0` fn_100035F0

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API void * __thiscall fn_100035F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100035F1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10003640`, `fn_10003660`
- **Run by a frame** (frame_set.json): static

### `0x10003640` fn_10003640

- **Verified C++** (`tree/src/unit_100014A0_Gfx.cpp`): `XI_API void __thiscall fn_10003640(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10003640 add ecx, 4` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
