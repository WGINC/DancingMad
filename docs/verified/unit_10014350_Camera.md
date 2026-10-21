# unit_10014350_Camera

### `0x10014350` fn_10014350

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __thiscall fn_10014350(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 62 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `sub_10014390`, `sub_101AB7D0`
- **Indirect calls:** 1, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x1045690C`
- **Writes globals:** `0x1045690C`, `0x104570E0`
- **Run by a frame** (frame_set.json): static, stack

### `0x100149B0` fn_100149B0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined1 __thiscall fn_100149B0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100149B2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10014C90`, `GameMode_PollPendingState`, `fn_102463C0`
- **Reads globals:** `g_pGameMode`, `0x1046393C`
- **Run by a frame** (frame_set.json): static

### `0x10014A20` fn_10014A20

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __thiscall fn_10014A20(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10014C90`
- **Run by a frame** (frame_set.json): static

### `0x10014C10` fn_10014C10

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined1 __thiscall fn_10014C10(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10014C11 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10014C60`, `fn_10029B60`, `fn_10093B70`, `fn_10152FA0`, `fn_1019C4F0`, `fn_10251620`
- **Reads globals:** `g_pStDancer`
- **Run by a frame** (frame_set.json): static

### `0x10014C60` fn_10014C60

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10014C60(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10029390`
- **Reads globals:** `0x104570B0`
- **Run by a frame** (frame_set.json): static

### `0x10014C90` fn_10014C90

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __thiscall fn_10014C90(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10014C91 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10014CB0`, `fn_10093B70`
- **Run by a frame** (frame_set.json): static

### `0x10014CB0` fn_10014CB0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10014CB0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10029390`
- **Reads globals:** `0x104570B0`
- **Run by a frame** (frame_set.json): static

### `0x10014CE0` fn_10014CE0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10014CE0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

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

### `0x10014D60` fn_10014D60

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10014D60(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self

### `0x10014D70` Camera_GetFloat2DC

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API long double __cdecl Camera_GetFloat2DC(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the float at g_pCamera+0x2DC.

### `0x10014D80` Camera_GetFloat2E0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API long double __cdecl Camera_GetFloat2E0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the float at g_pCamera+0x2E0.

### `0x10014D90` Camera_SetClearColorRGB

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl Camera_SetClearColorRGB(undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10014DB0`
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Sets g_pCamera's background clear colour (+0x308) from r,g,b bytes with alpha 0x80.

### `0x10014DB0` fn_10014DB0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall fn_10014DB0(void * self_, uint32_t param_1, uint32_t param_2, uint32_t param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10014DDC mov dword ptr [ecx + 0x308], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10014E00` fn_10014E00

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10014E00(undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10014E20`
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self

### `0x10014E20` fn_10014E20

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall fn_10014E20(void * self_, undefined4 param_1, undefined4 param_2, uint32_t param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10014E39 mov dword ptr [ecx + 0x304], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10014E60` fn_10014E60

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10014E60(float param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10014E80` fn_10014E80

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10014E80(float param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self

### `0x10014EB0` fn_10014EB0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10014EB0(float param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self

### `0x10014ED0` fn_10014ED0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10014ED0(float param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015100` fn_10015100

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10015100(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_100151A0`
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015120` fn_10015120

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __thiscall fn_10015120(void * self_, undefined4 xi_s1, undefined4 xi_s2, undefined4 xi_s3, undefined4 xi_s4, undefined4 xi_s5, undefined4 xi_s6, undefined4 xi_s7, undefined4 xi_s8, undefined4 xi_s9, undefined4 xi_s10, undefined4 xi_s11, undefined4 xi_s12, undefined4 xi_s13, undefined4 xi_s14, undefined4 xi_s15, undefined4 xi_s16)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 64` (purges.json); entry ECX read: `0x10015121 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100279A0`, `Mat4_SetIdentity`, `Mat4_Copy` ×4, `Mat4_InvertOrthonormal`
- **Run by a frame** (frame_set.json): static

### `0x100151D0` fn_100151D0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall fn_100151D0(void * self_, undefined4 xi_s1, undefined4 xi_s2, undefined4 xi_s3, undefined4 xi_s4, undefined4 xi_s5, undefined4 xi_s6, undefined4 xi_s7, undefined4 xi_s8, undefined4 xi_s9, undefined4 xi_s10, undefined4 xi_s11, undefined4 xi_s12, undefined4 xi_s13, undefined4 xi_s14, undefined4 xi_s15, undefined4 xi_s16)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 64` (purges.json); entry ECX read: `0x100151D4 add ecx, 0x154` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100279A0`, `Mat4_Copy`
- **Run by a frame** (frame_set.json): static

### `0x10015220` Camera_GetViewMatrixPtr

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API int __cdecl Camera_GetViewMatrixPtr(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns a pointer to the matrix at g_pCamera+0x94.

### `0x10015250` Camera_GetField50

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl Camera_GetField50(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the dword at g_pCamera+0x50.

### `0x10015270` Camera_GetMatrix154Ptr

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API int __cdecl Camera_GetMatrix154Ptr(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns a pointer to the matrix at g_pCamera+0x154.

### `0x10015290` fn_10015290

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10015290(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_100152B0`
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x100152B0` fn_100152B0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall fn_100152B0(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100152B4 mov dword ptr [ecx + 0x2f8], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100152C0` fn_100152C0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API long double __cdecl fn_100152C0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015360` fn_10015360

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10015360(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10015490`, `Mat4_Copy`
- **Reads constants** (.rdata): 2
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x100153A0` fn_100153A0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_100153A0(float param_1, float param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 2
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015480` Camera_BuildProjection

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl Camera_BuildProjection(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10015490 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Camera_BuildProjection` (not stated)
- **DancingMad note:** FOV = 2*atan(192 / cam+0x2F4); near/far cam+0x2DC/+0x2E0; output cam+0x154 via D3DX.

### `0x10015490` fn_10015490

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall fn_10015490(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10015491 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Mat4_Copy`, `D3DXMatrixPerspectiveFovLH_static`
- **Reads constants** (.rdata): 2
- **Run by a frame** (frame_set.json): static

### `0x10015510` Camera_ApplyViewProjection

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl Camera_ApplyViewProjection(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 54 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 54, town PASS 59, town2 PASS 59, combat PASS 59, zonetoinn PASS 59
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×2, `Camera_SetViewMatrix`, `Camera_GetField50` ×6, `Camera_GetMatrix154Ptr`, `Camera_BuildProjection`, `Camera_UpdateController`, `fn_10021AE0`, `fn_10021B70`, `CameraCache_CacheViewProjection`, `fn_10044540`, `fn_10069F90`, `fn_1006A180`
- **Reads globals:** `g_pCDx`, `g_pCamera`, `g_pMoCamera`, `g_pResourceMng`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `Camera_ApplyViewProjection` (not stated)
- **DancingMad note:** Builds and sets D3DTS_VIEW then D3DTS_PROJECTION from the camera object at 0x104568FC.

### `0x100155D0` fn_100155D0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_100155D0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015600` fn_10015600

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10015600(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015610` fn_10015610

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10015610(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015640` fn_10015640

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10015640(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015650` fn_10015650

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10015650(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static

### `0x10015680` Camera_GetViewportWidth

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl Camera_GetViewportWidth(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `Camera_GetViewportWidth` (not stated)
- **DancingMad note:** Returns word g_pCamera+0x18.

### `0x10015690` Camera_GetViewportHeight

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl Camera_GetViewportHeight(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCamera`
- **Run by a frame** (frame_set.json): static, self
- **DancingMad name:** `Camera_GetViewportHeight` (not stated)
- **DancingMad note:** Returns word g_pCamera+0x1A.

### `0x100156A0` fn_100156A0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API int __cdecl fn_100156A0(int param_1, int param_2, undefined4 * param_3, undefined4 * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x10015740` fn_10015740

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10015740(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100157B0` fn_100157B0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __stdcall fn_100157B0(undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `App_WinMain`
- **Writes globals:** `g_pFileMng`
- **Run by a frame** (frame_set.json): stack

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
- **Calls directly:** `CApp_Constructor`, `CDx_Constructor`, `CDx::SetDefaultRenderTargets`, `App_BeginTimerPeriod`, `fn_100191D0`, `Mem_AllocDefault` ×2, `ShapeMng_Init`, `MenuMng_Init`
- **Indirect calls:** 4, of which 0 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pD3DHolder`, `g_pCDx`, `hWnd`, `hmod`, `g_installDir`, `g_sceneStateStorage_38`, `g_sceneStateStorage_3C`, `xRight`, `yBottom`
- **Writes globals:** `g_pApp`, `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Creates CDx (2640 bytes) from the D3DHolder device, stores the back-buffer size and default back-buffer/depth surfaces, constructs CApp (dword_103D3C64), begins the timer period and creates helper objects.

### `0x10016300` fn_10016300

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10016300(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CApp::RunMainLoop`, `fn_10016410`
- **Reads globals:** `g_pApp`
- **Writes globals:** `0x104569CC`
- **Run by a frame** (frame_set.json): stack

### `0x10016320` fn_10016320

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API _DWORD * __cdecl fn_10016320(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): NOT VERIFIED -- INCONCLUSIVE
- **Convention facts:** pops 0 through its tail jump to 0x1015D9E0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_100191B0`, `sub_10120200`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pApp`, `g_pCDx`
- **Writes globals:** `g_pApp`, `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100163C0` fn_100163C0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_100163C0(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x104569C5`
- **Run by a frame** (frame_set.json): static

### `0x100163E0` fn_100163E0

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_100163E0(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x104569C6`
- **Run by a frame** (frame_set.json): static

### `0x10016400` App_SetGlobal_104569C8

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl App_SetGlobal_104569C8(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x104569C8`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Stores its argument in dword_104569C8.

### `0x10016410` fn_10016410

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10016410(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `0x104569C8`
- **Run by a frame** (frame_set.json): static

### `0x100164C0` App_SetErrorCode

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl App_SetErrorCode(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x104569F8`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Stores a startup error code in dword_104569F8.

### `0x10016560` fn_10016560

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10016560(undefined4 * param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Reads globals:** `g_cfgBackgroundResX`, `g_cfgBackgroundResY`
- **Run by a frame** (frame_set.json): static

### `0x100170A0` GammaRamp_SetRGB

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall GammaRamp_SetRGB(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100170A8 mov dword ptr [ecx + 0x604], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Stores the three requested gamma values (+1540/+1544/+1548).

### `0x100170D0` GammaRamp_GetRGB

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall GammaRamp_GetRGB(void * self_, undefined4 * param_1, undefined4 * param_2, undefined4 * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100170D4 mov eax, dword ptr [ecx + 0x604]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Reads the three requested gamma values into out-pointers.

### `0x10017100` GammaRamp_GetChannelSamples

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __thiscall GammaRamp_GetChannelSamples(void * self_, float * param_1, float * param_2, float * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10017107 mov ax, word ptr [ecx + 0xf4]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns one sample from each of the R, G and B ramp tables, scaled to floats by 1/28494.

### `0x10017160` GammaRamp_BuildRamps

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __thiscall GammaRamp_BuildRamps(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10017161 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_100171B0` ×3
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Builds the R, G and B 256-entry gamma tables from the applied gamma values.

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

### `0x10017630` fn_10017630

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API void __cdecl fn_10017630(undefined4 param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_1031111E`
- **Reads globals:** `0x10456A50`
- **Writes globals:** `0x10456A50`, `0x10456A51`
- **Run by a frame** (frame_set.json): static

### `0x10017670` fn_10017670

- **Verified C++** (`tree/src/unit_10014350_Camera.cpp`): `XI_API undefined4 __cdecl fn_10017670(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10014CE0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10010520`, `App_SetGlobal_104569C8`
- **Run by a frame** (frame_set.json): static
