# CAtelIdleTask

### `0x100142B0` fn_100142B0

- **Verified C++** (`tree/src/CAtelIdleTask.cpp`): `XI_API undefined4 __cdecl fn_100142B0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `App_AdvanceSeqStep`, `Mem_AllocFromArea`, `CMoTask_Constructor`, `CMoTask::ResetFields`, `CMoTask_RegisterWithMng`, `fn_1015E910`, `fn_101AB730`
- **Reads globals:** `g_pCamera`, `g_pSceneState`
- **Writes globals:** `0x1045690C`, `g_resourcesDirty`
- **Run by a frame** (frame_set.json): static
