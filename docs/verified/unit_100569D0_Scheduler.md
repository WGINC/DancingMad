# unit_100569D0_Scheduler

### `0x10056AA0` fn_10056AA0

- **Verified C++** (`tree/src/unit_100569D0_Scheduler.cpp`): `XI_API void __thiscall fn_10056AA0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x100720B0 (tail_purges.json); entry ECX read: `0x10056AA1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10074CF0`
- **Reads globals:** `dword_1047D140`
- **Run by a frame** (frame_set.json): stack

### `0x10056CE0` fn_10056CE0

- **Verified C++** (`tree/src/unit_100569D0_Scheduler.cpp`): `XI_API int __thiscall fn_10056CE0(void * self_, int param_1, int param_2, undefined4 param_3, undefined4 param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10056CEB mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocFromArea`, `fn_10057270`, `fn_10062830`, `fn_10062880`, `CMoTask::ResetFields`
- **Writes globals:** `g_resourcesDirty`
- **Run by a frame** (frame_set.json): static, stack

### `0x10056EB0` fn_10056EB0

- **Verified C++** (`tree/src/unit_100569D0_Scheduler.cpp`): `XI_API void __thiscall fn_10056EB0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10056EB2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10074AB0`
- **Reads globals:** `dword_1047D140`
- **Run by a frame** (frame_set.json): static
