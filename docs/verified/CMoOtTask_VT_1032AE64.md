# CMoOtTask_VT_1032AE64

### `0x10042020` CMoOtTask_VT_1032AE64::vf8

- **Verified C++** (`tree/src/CMoOtTask_VT_1032AE64.cpp`): `char CMoOtTask_VT_1032AE64::vf8()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 56 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 56, town PASS 68, town2 PASS 68, combat PASS 68, zonetoinn PASS 68
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1004202F mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx::GetTransformCached`, `sub_100555B0`
- **Reads constants** (.rdata): 4
- **Indirect calls:** 3, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`, `g_pProcessor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
