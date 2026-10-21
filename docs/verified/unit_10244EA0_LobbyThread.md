# unit_10244EA0_LobbyThread

### `0x10244F20` fn_10244F20

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __cdecl fn_10244F20(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10244F30` fn_10244F30

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void * __thiscall fn_10244F30(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10244F31 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10126320`, `fn_10245040`
- **Run by a frame** (frame_set.json): static

### `0x10245040` fn_10245040

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __thiscall fn_10245040(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10245040 mov dword ptr [ecx + 0x14], 2` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10245600` LobbyThread_Start

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined4 __cdecl LobbyThread_Start(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `Mem_AllocDefault`, `fn_10039440`, `ThreadPool_StartThread`
- **Writes globals:** `g_pLobbyThreadPool`, `0x106690A4`, `0x106690A8`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `LobbyThread_Start` (not stated)
- **DancingMad note:** Creates the thread pool (g_pLobbyThreadPool) and starts the game's only pooled worker, LobbyThread_Main.

### `0x10245B50` fn_10245B50

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined4 __cdecl fn_10245B50(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x106690AC`
- **Run by a frame** (frame_set.json): static

### `0x10245B60` Lobby_DestroyThreadPool

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API int __cdecl Lobby_DestroyThreadPool(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 94 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10039550`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pLobbyThreadPool`, `0x106690A4`
- **Writes globals:** `g_pLobbyThreadPool`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Shuts down the lobby thread pool and deletes it through its virtual deleting destructor when present.

### `0x10245BA0` thunk_sub_10245BB0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __cdecl thunk_sub_10245BB0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x10245BB0 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x10245BB0` fn_10245BB0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __cdecl fn_10245BB0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10014CB0`, `CYyCamMng2::CreateGlobal`, `XiZone::GetInstance`, `fn_1018B620`
- **Reads globals:** `g_pCamera`, `g_pXiZone`
- **Run by a frame** (frame_set.json): static

### `0x10245BE0` fn_10245BE0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined4 __cdecl fn_10245BE0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10039590`
- **Reads globals:** `g_pLobbyThreadPool`
- **Run by a frame** (frame_set.json): static

### `0x10245F30` fn_10245F30

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined4 __thiscall fn_10245F30(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10245F30 mov eax, dword ptr [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10246000` fn_10246000

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __stdcall fn_10246000(undefined4 param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x10246030` fn_10246030

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined8 __thiscall fn_10246030(void * self_, char * param_1, uint32_t param_2, uint32_t param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10245F30`, `fn_1024C060` ×2
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x10246160` fn_10246160

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined8 __stdcall fn_10246160(undefined4 param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry EDX not established (edx_use.json)
- **Reads globals:** `0x106690C8`
- **Run by a frame** (frame_set.json): static

### `0x102462F0` fn_102462F0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __stdcall fn_102462F0(undefined4 param_1, uint32_t param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x10246320` fn_10246320

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined4 __stdcall fn_10246320(undefined4 param_1, uint32_t param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x102463C0` fn_102463C0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __stdcall fn_102463C0(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x102463F0` fn_102463F0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined4 __stdcall fn_102463F0(undefined4 param_1, uint32_t param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1024C060`, `operator_delete`, `Allocator_Generic`, `sub_10311F30`, `sub_10311FDE`, `sub_1031217F`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x102465E0` fn_102465E0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API uint32_t __stdcall fn_102465E0(uint32_t param_1, uint32_t param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1024C060`, `operator_delete` ×2, `Allocator_Generic` ×2, `sub_10311F30`, `sub_10311FDE`, `_sprintf`
- **Reads globals:** `0x106690B0`, `0x10669108`
- **Run by a frame** (frame_set.json): static

### `0x10246770` fn_10246770

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __stdcall fn_10246770(undefined4 param_1, uint32_t param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x102467A0` fn_102467A0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __stdcall fn_102467A0(undefined4 param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x102467F0` fn_102467F0

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined8 __stdcall fn_102467F0(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1024C060`
- **Reads globals:** `0x106690B0`
- **Run by a frame** (frame_set.json): static

### `0x1024C060` fn_1024C060

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API undefined8 __stdcall fn_1024C060(int param_1, int * param_2, int param_3, int param_4, int param_5, int param_6, int param_7, int param_8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 32` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads globals:** `0x106690C4`, `0x106690E8`, `0x106690F0`
- **Writes globals:** `0x106690C4`
- **Run by a frame** (frame_set.json): static

### `0x1024C210` fn_1024C210

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void * __thiscall fn_1024C210(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1024C212 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10126320`, `fn_1024C930`, `Allocator_Generic`
- **Reads globals:** `0x10669144`
- **Writes globals:** `0x10669144`
- **Run by a frame** (frame_set.json): static

### `0x1024C930` fn_1024C930

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void * __thiscall fn_1024C930(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1024C931 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10126320`
- **Run by a frame** (frame_set.json): static

### `0x1024CF50` fn_1024CF50

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API int __cdecl fn_1024CF50(_DWORD *a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 66 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1024D130`, `fn_10250D80` ×3, `fn_102524B0` ×2, `fn_10252C80`, `fn_1026E400`, `fn_1026E460`, `fn_10270B60`, `scnFini`, `fn_10271C60`, `fn_10271C80`, `fn_102738D0`, `PackVec4` ×2, `sub_10275090`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_stateBlock_914C`
- **Run by a frame** (frame_set.json): static

### `0x1024D130` fn_1024D130

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API void __cdecl fn_1024D130(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10272630`, `fn_10272750`, `fn_10272880`, `fn_102729E0`
- **Reads globals:** `0x10389304`, `0x10389308`
- **Run by a frame** (frame_set.json): static
