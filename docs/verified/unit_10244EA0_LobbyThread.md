# unit_10244EA0_LobbyThread

### `0x1024CF50` fn_1024CF50

- **Verified C++** (`tree/src/unit_10244EA0_LobbyThread.cpp`): `XI_API int __cdecl fn_1024CF50(_DWORD *a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 66 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_1024D130`, `sub_10250D80` ×3, `sub_102524B0` ×2, `sub_10252C80`, `sub_1026E400`, `sub_1026E460`, `sub_10270B60`, `scnFini`, `sub_10271C60`, `sub_10271C80`, `sub_102738D0`, `PackVec4` ×2, `sub_10275090`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_stateBlock_914C`
- **Run by a frame** (frame_set.json): static
