# unit_10003890_DirectInput

### `0x10003890` fn_10003890

- **Verified C++** (`tree/src/unit_10003890_DirectInput.cpp`): `XI_API void __thiscall fn_10003890(_DWORD *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 3 returned normally, 8244 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned; gates: fuzz UNRESOLVED 0, town PASS 3, town2 PASS 3, combat PASS 3, zonetoinn PASS 3
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100038A2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×3, `CDx::GetTransformCached`, `CDx::DrawPrimitiveUP` ×2, `Vec4_Copy`, `Vec3_Sub`, `??0Iostream_init@@QAE@XZ_0` ×3, `nullsub_1` ×3, `Mat4_SetIdentity` ×2, `Mat4_PostRotateY`, `Mat4_SetTranslation` ×2
- **Indirect calls:** 13, of which 9 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Writes globals:** `g_debugLineVerts_v0_color`
- **Run by a frame** (frame_set.json): static

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
