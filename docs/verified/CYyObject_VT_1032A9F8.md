# CYyObject_VT_1032A9F8

### `0x100394D0` ThreadPool_StartThread

- **Verified C++** (`tree/src/CYyObject_VT_1032A9F8.cpp`): `XI_API void __thiscall ThreadPool_StartThread(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100394D2 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10017D20` ×2, `fn_100395D0`, `sub_10039670`, `Allocator_Generic`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `ThreadPool_StartThread` (not stated)
- **DancingMad note:** Thread-pool start wrapper (capacity 9: 'Thread Num Over!!' / 'Thread Create Error!!'). Exactly one caller: LobbyThread_Start.

### `0x10039550` fn_10039550

- **Verified C++** (`tree/src/CYyObject_VT_1032A9F8.cpp`): `XI_API void __thiscall fn_10039550(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10039551 lea esi, [ecx + 0xc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100396A0`
- **Run by a frame** (frame_set.json): static

### `0x100395D0` fn_100395D0

- **Verified C++** (`tree/src/CYyObject_VT_1032A9F8.cpp`): `XI_API undefined4 __thiscall fn_100395D0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100395D0 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
