# YkMyroom

### `0x101D2F00` fn_101D2F00

- **Verified C++** (`tree/src/YkMyroom.cpp`): `XI_API void __thiscall fn_101D2F00(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 297 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101D2F01 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1013A320`, `fn_10150CC0`, `fn_101594D0`, `fn_1015E8A0` ×3, `fn_101D30B0`, `fn_101D31B0`, `fn_101D3DC0`, `operator_delete`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pTkHelp`, `g_pTkTitle`, `g_pTargetMng`, `0x106631DC`, `0x106631E0`, `0x106631E4`
- **Writes globals:** `0x106631DC`, `0x106631E0`, `0x106631E4`
- **Run by a frame** (frame_set.json): static
