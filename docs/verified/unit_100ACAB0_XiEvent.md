# unit_100ACAB0_XiEvent

### `0x100AD6D0` fn_100AD6D0

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __cdecl fn_100AD6D0(undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6, undefined4 param_7, undefined4 param_8, undefined4 param_9)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 18 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 9 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100C2E20`, `fn_100C3190` ×2, `fn_100C3210`, `fn_100C3300`, `Allocator_Generic`
- **Reads globals:** `0x10482F40`, `0x104855AA`
- **Run by a frame** (frame_set.json): static

### `0x100AE350` fn_100AE350

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API int __cdecl fn_100AE350(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x104896E4`
- **Run by a frame** (frame_set.json): static

### `0x100AE3A0` fn_100AE3A0

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __cdecl fn_100AE3A0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10127EA0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1015EB60`
- **Reads globals:** `0x1047D3E8`, `0x1047D3EC`, `0x104886F4`, `g_pTkMsgWinData`
- **Writes globals:** `0x1047D3EC`, `0x104886F4`, `0x104897F4`, `0x104898F8`
- **Run by a frame** (frame_set.json): static

### `0x100BA080` fn_100BA080

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __cdecl fn_100BA080(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Reads globals:** `0x104882B0`, `0x10488978`, `0x104897EC`, `g_pXiZone`
- **Writes globals:** `0x10488978`
- **Run by a frame** (frame_set.json): static

### `0x100BD5F0` fn_100BD5F0

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __thiscall fn_100BD5F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100BD5F1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyObject_IsKindOf`, `fn_10087D40`, `fn_10087E40`, `sub_100D44B0`, `fn_100D5430`, `operator_delete`
- **Run by a frame** (frame_set.json): static

### `0x100BD760` fn_100BD760

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API undefined * __cdecl fn_100BD760(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_100BD820`, `_atexit`
- **Reads globals:** `0x1048A2E1`
- **Writes globals:** `0x1048A2E1`
- **Run by a frame** (frame_set.json): self

### `0x100C2E20` fn_100C2E20

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void * __thiscall fn_100C2E20(void * self_, undefined4 * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, char * param_5, undefined4 param_6, undefined4 param_7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 28` (purges.json); entry ECX read: `0x100C2E25 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10086FC0` ×2, `_strncpy`
- **Reads globals:** `0x104804CC`, `0x10482F1A`, `0x10485F7A`
- **Run by a frame** (frame_set.json): static

### `0x100C3050` fn_100C3050

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __thiscall fn_100C3050(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C3050 mov eax, dword ptr [ecx + 0x40]` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `operator_delete`
- **Run by a frame** (frame_set.json): static

### `0x100C3060` fn_100C3060

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void * __thiscall fn_100C3060(void * self_, undefined4 * param_1, undefined4 param_2, undefined2 * param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6, undefined4 param_7, undefined4 param_8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 32` (purges.json); entry ECX read: `0x100C3064 mov edx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x100C3190` fn_100C3190

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API undefined * __cdecl fn_100C3190(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_100C31F0`, `_atexit`
- **Reads globals:** `0x1048A2E0`
- **Writes globals:** `0x1048A2E0`
- **Run by a frame** (frame_set.json): static

### `0x100C3200` fn_100C3200

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __thiscall fn_100C3200(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C3200 mov dword ptr [ecx + 8], 1` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100C3210` fn_100C3210

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API undefined4 __thiscall fn_100C3210(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C3210 mov edx, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100C3220` fn_100C3220

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __thiscall fn_100C3220(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C3221 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100C3050`, `operator_delete`
- **Run by a frame** (frame_set.json): static

### `0x100C3260` fn_100C3260

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __thiscall fn_100C3260(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100C326D mov esi, dword ptr [ecx]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100C3300` fn_100C3300

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API void __thiscall fn_100C3300(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 52 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x100C3307 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_10086FC0` ×2, `sub_100C3020` ×2, `sub_100C3030` ×2, `fn_100C3060`, `fn_100C3260` ×2, `Allocator_Generic`
- **Reads globals:** `0x10485F7A`
- **Run by a frame** (frame_set.json): static

### `0x100C3480` fn_100C3480

- **Verified C++** (`tree/src/unit_100ACAB0_XiEvent.cpp`): `XI_API undefined4 __thiscall fn_100C3480(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 85 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C348F mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `Camera_GetFrameScale` ×2, `sub_10087DF0`, `sub_100C2D00` ×2, `sub_100C2FB0`, `sub_100C2FE0` ×2, `sub_100C30F0`, `sub_100C3100` ×2, `sub_100C3120`, `sub_100C3130` ×15, `sub_100C3140` ×2, `sub_100C3150`, `sub_100C3160`, `sub_100C3170`, `ChatLog_AddMessage`, `sub_10311C2C` ×2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pSceneState`, `0x104807FC`, `g_pTkMsgWinData`
- **Writes globals:** `0x104807FC`
- **Run by a frame** (frame_set.json): stack
