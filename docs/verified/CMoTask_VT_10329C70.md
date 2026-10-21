# CMoTask_VT_10329C70

### `0x100119A0` CMoTask_VT_10329C70::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoTask_VT_10329C70.cpp`): `_DWORD * CMoTask_VT_10329C70::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100119A1 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoTask_VT_10329C70_Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1006B480` CMoTask_VT_10329C70::vf8

- **Verified C++** (`tree/src/CMoTask_VT_10329C70.cpp`): `char CMoTask_VT_10329C70::vf8()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006B480 mov eax, dword ptr [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CameraCache_CacheViewProjection`, `sub_10069EE0`, `sub_1006A180`
- **Reads globals:** `g_pMoCamera`, `g_pResourceMng`
- **Run by a frame** (frame_set.json): stack

### `0x1006B4C0` CMoTask_VT_10329C70::vf1

- **Verified C++** (`tree/src/CMoTask_VT_10329C70.cpp`): `_DWORD * __stdcall CMoTask_VT_10329C70::vf1(_DWORD *a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `nullsub_43`
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
