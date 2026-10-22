# XiDoorActor

### `0x100AC380` fn_100AC380

- **Verified C++** (`tree/src/XiDoorActor.cpp`): `XI_API void __cdecl fn_100AC380(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100AC390` fn_100AC390

- **Verified C++** (`tree/src/XiDoorActor.cpp`): `XI_API char __thiscall fn_100AC390(XiDoorActor *self_, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100AC390 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx::SetTransform` ×4, `CDx::GetTransformCached` ×2, `Camera_GetViewMatrixPtr`, `Vec4_Set`, `Vec4_Copy`, `Gfx_ProjectWorldToClip`, `Gfx_NdcToScreen`, `fn_10027990` ×3, `fn_100279A0` ×6, `Mat4_SetIdentity`, `Mat4_SetTranslation`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100AC4E0` fn_100AC4E0

- **Verified C++** (`tree/src/XiDoorActor.cpp`): `XI_API char __thiscall fn_100AC4E0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100AC4E2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetFrameScale`, `sub_100A57F0`, `sub_10311C2C`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack

### `0x100AC5A0` fn_100AC5A0

- **Verified C++** (`tree/src/XiDoorActor.cpp`): `XI_API void __thiscall fn_100AC5A0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100AC5A8 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetViewMatrixPtr`, `Camera_GetMatrix154Ptr`, `Camera_GetViewportWidth`, `Camera_GetViewportHeight`, `Vec4_Copy`, `Gfx_NdcToScreen` ×2, `fn_10027990` ×3, `fn_100279A0` ×6, `Mat4_SetIdentity`, `Mat4_Copy` ×2, `Mat4_SetTranslation`, `Mat4_PostMultiply` ×2, `fn_10028230`, `sub_10028370` ×2, `Occlusion_QueryScreenRect`, `fn_1018B8F0`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `pTexture`, `g_translucentTarget`, `g_pXiZone`
- **Run by a frame** (frame_set.json): stack
