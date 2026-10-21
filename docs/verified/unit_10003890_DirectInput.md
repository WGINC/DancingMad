# unit_10003890_DirectInput

### `0x10003890` fn_10003890

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __thiscall fn_10003890(_DWORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): NOT VERIFIED -- UNRESOLVED
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100038A2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×3, `CDx::GetTransformCached`, `CDx::DrawPrimitiveUP` ×2, `Vec4_Copy`, `Vec3_Sub`, `fn_10027990` ×3, `fn_100279A0` ×3, `Mat4_SetIdentity` ×2, `Mat4_PostRotateY`, `Mat4_SetTranslation` ×2
- **Indirect calls:** 13, of which 9 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_debugLineVerts_v0_color`
- **Run by a frame** (frame_set.json): static

### `0x10005600` fn_10005600

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __thiscall fn_10005600(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10005640 cmp dword ptr [ecx + 0x90], edx` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX untouched (reg_keeps.json)
- **Reads globals:** `0x10455C37`, `0x10455C41`, `0x10455C42`
- **Writes globals:** `0x10455C37`, `0x10455C40`, `0x10455C41`, `0x10455C42`
- **Run by a frame** (frame_set.json): static

### `0x10005660` fn_10005660

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void * __thiscall fn_10005660(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10005660 mov edx, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Writes globals:** `0x10455C3E`
- **Run by a frame** (frame_set.json): static

### `0x100059C0` fn_100059C0

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API undefined4 __cdecl fn_100059C0(uint32_t param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `0x10455C35`
- **Run by a frame** (frame_set.json): static

### `0x10005A00` fn_10005A00

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API undefined4 __cdecl fn_10005A00(uint32_t param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10007860` fn_10007860

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __stdcall fn_10007860(uint32_t param_1, undefined4 xi_s2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10080DC0`, `sub_1015DD50`, `sub_1015DD70` ×2, `sub_101B36F0`, `sub_10312AD3`, `sub_10312BDB`
- **Reads globals:** `0x10578490`, `0x1062193C`, `0x10662D40`
- **Run by a frame** (frame_set.json): static

### `0x10007E20` DirectInput_InstallKeyboard

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API undefined4 __thiscall DirectInput_InstallKeyboard(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 370 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10007E24 lea esi, [ecx + 0x88]` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Indirect calls:** 5, of which 5 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pApp`, `g_windowMode`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `DirectInput_InstallKeyboard` (confirmed)
- **DancingMad note:** CreateDevice(&GUID_SysKeyboard, ...) -- confirmed byte-for-byte ({6F1D2B61-D5A0-11CF-BFC7-444553540000}). Shared per-device sequence (also used by InstallMouse/InstallJoystick): CreateDevice (vtable+12), SetProperty(DIPROP_BUFFERSIZE, 320) (vtable+24), SetDataFormat (vtable+44, data size 256 -- the c_dfDIKeyboard signature, second independent confirmation), SetCooperativeLevel (vtable+52), Acquire (vtable+28).

### `0x10007EF0` DirectInput_InstallMouse

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API char __thiscall DirectInput_InstallMouse(_DWORD **self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 15 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10007F0E mov eax, dword ptr [ecx + 0x84]` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx_ShowCursor`
- **Indirect calls:** 7, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pApp`, `g_pCDx`, `g_windowMode`, `g_cfgHardwareMouse`
- **Writes globals:** `g_mouseAcquired`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `DirectInput_InstallMouse` (confirmed)
- **DancingMad note:** CreateDevice(&GUID_SysMouse, ...) -- confirmed byte-for-byte ({6F1D2B60-D5A0-11CF-BFC7-444553540000}), stored in a 16-byte GUID array immediately after GUID_SysKeyboard. Same per-device sequence as DirectInput_InstallKeyboard.

### `0x100083D0` DirectInput_InstallJoystick

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API undefined4 __thiscall DirectInput_InstallJoystick(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 125 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100083E0 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10008770` ×3, `sub_10008D90`, `sub_10008E10`
- **Indirect calls:** 17, of which 6 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pApp`, `0x10455C24`, `0x10455C37`, `0x10455C38`, `0x10455C39`
- **Writes globals:** `0x10455C24`, `0x10455C28`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `DirectInput_InstallJoystick` (confirmed)
- **DancingMad note:** Joystick/gamepad setup with force feedback. EnumDevices filtered to device class 4 (DI8DEVCLASS_GAMECTRL), SetProperty(DIPROP_RANGE, -127..127) across 8 axes, a POV-hat enumeration callback, and a real CreateEffect call (vtable+72) creating a GUID_ConstantForce effect (confirmed byte-for-byte, {13541C20-8E33-11D0-9AD0-00A0C9A06E35}) -- the object DirectInput_ApplyRumble drives via SetParameters. NOT confirmed which of CDx's 4 CAcc-shaped member slots this device occupies.

### `0x10008770` fn_10008770

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API undefined4 __thiscall fn_10008770(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 92 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10008777 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Indirect calls:** 3, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x10455C28`
- **Writes globals:** `0x10455C28`
- **Run by a frame** (frame_set.json): static

### `0x100087D0` fn_100087D0

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __stdcall fn_100087D0(int param_1, int param_2, undefined4 xi_s3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 146 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pAppInputState`
- **Run by a frame** (frame_set.json): static

### `0x10008830` fn_10008830

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API undefined4 __thiscall fn_10008830(void * self_, uint32_t param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10008838 mov eax, dword ptr [ecx + 0xc94]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCursor`
- **Run by a frame** (frame_set.json): static, self

### `0x100088F0` fn_100088F0

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __thiscall fn_100088F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 53 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100088F1 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10124930` ×2, `fn_101249E0` ×2, `fn_10124A00`, `fn_10124AB0`, `fn_10124AD0`, `fn_10124B50`
- **Reads globals:** `0x10455C3A`, `g_pCursor`
- **Run by a frame** (frame_set.json): static

### `0x100089D0` fn_100089D0

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __thiscall fn_100089D0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 46 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100089D2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `DirectInput_InstallMouse`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_mouseAcquired`, `0x10456549`
- **Writes globals:** `0x10456549`
- **Run by a frame** (frame_set.json): static
