# XiFurnitureActor

### `0x100C3E70` fn_100C3E70

- **Verified C++** (`tree/src/XiFurnitureActor.cpp`): `XI_API void __cdecl fn_100C3E70(void * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `sub_10085240`, `sub_10085270`, `fn_1008A7B0`
- **Run by a frame** (frame_set.json): static
