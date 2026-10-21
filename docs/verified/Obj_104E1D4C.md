# Obj_104E1D4C

### `0x10124700` Obj_104E1D4C::Cursor_SetPosition

- **Verified C++** (`tree/src/Obj_104E1D4C.cpp`): `void Obj_104E1D4C::Cursor_SetPosition(_DWORD *a2, float a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10124703 test ecx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SetCursorPos`, `sub_10311C2C` ×2
- **Calls imports:** `GetWindowRect`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 3, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pApp`, `g_pCDx`, `g_windowMode`, `g_cfgHardwareMouse`, `g_screenRectTopLeft`, `0x106218B6`, `g_screenRectBottomRight`, `0x106218BA`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Stores a new cursor position (and optional value a3 at +72). In windowed or mouse mode it converts the virtual-screen position to desktop coordinates using the window rect and frame metrics, then warps the OS mouse.

### `0x10124EB0` Obj_104E1D4C::Cursor_Draw

- **Verified C++** (`tree/src/Obj_104E1D4C.cpp`): `void Obj_104E1D4C::Cursor_Draw()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 99, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10124EB5 mov ebp, ecx` (ecx_use.json); entry EDX read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CDx_ShowCursor` ×2, `CDx::SetCursorShape`, `??0Iostream_init@@QAE@XZ_0`, `nullsub_1`, `Mat4_SetIdentity`, `Mat4_PostScale`, `Mat4_PostRotateZ`, `Shape_DrawScaled`, `Shape_DrawTransformed`
- **Reads globals:** `g_pCDx`, `g_cfgHardwareMouse`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): When visible, advances the cursor's animation frame. With a hardware cursor it sets and shows the OS cursor through CDx. Otherwise it hides it and draws the cursor shape transformed (scale matrix) at +12/+16; state 6 also draws the scroll-anchor shape.
