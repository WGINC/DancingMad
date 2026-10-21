# CXiTimerLow

### `0x10019490` fn_10019490

- **Verified C++** (`tree/src/CXiTimerLow.cpp`): `XI_API void * __thiscall fn_10019490(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10019491 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10019210`, `fn_100194F0`
- **Calls imports:** `timeGetTime`
- **Run by a frame** (frame_set.json): static
