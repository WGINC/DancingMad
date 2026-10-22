# StTrigger

### `0x10252CC0` StTrigger_ProcessOpcodesUpToTime

- **Verified C++** (`tree/src/StTrigger.cpp`): `XI_API int __cdecl StTrigger_ProcessOpcodesUpToTime(uint32_t * param_1, uint32_t param_2, int param_3, undefined4 * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 97 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10036F00`, `fn_10037020`, `CMoResource::FindByTypeAndId`, `sqopOpcodeGet` ×2, `sqopTrackAdvance`, `_sprintf`
- **Reads globals:** `g_pAppInputState`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StTrigger_ProcessOpcodesUpToTime` (confirmed)
- **DancingMad note:** MAJOR FINDING, directly relevant to this project's VFX-restoration goal: the real opcode dispatch/execute function. Confirms opcodes are TIME-KEYED -- processes every opcode whose time has passed since the last call in one 'catch up' pass, matching a cue-track/timeline metaphor exactly. Confirmed type dispatch: type 0 resolves a named/numbered resource via the same resource ID (61) and resolve call already confirmed for SetMusicTrackVolume_A/B/C, then calls the identical function used there on success -- strongly suggests type 0 triggers a sound effect/music cue by numbered ID, with a spatial-parameter fallback path on a name mismatch. Types 1 and 2 write into offsets of dword_10455C20 (45 xrefs across nearly the whole .text section) and set a dirty flag. CORRECTED, not left standing: checking this object directly found it's allocated/freed at the CApp (top-level application) level and one of its own nearby fields (byte_10455C34, +20) controls gamepad input config, not camera/effects -- revises the earlier 'plausibly camera-shake/screen-flash' guess downward. It's better understood as a broad, generic app-settings singleton, not a dedicated effects structure. What actually happens at +3508/+3516 remains genuinely unconfirmed. Only types 0/1/2 were confirmed; other opcode type values may exist unchecked.

### `0x10252EA0` fn_10252EA0

- **Verified C++** (`tree/src/StTrigger.cpp`): `XI_API int __cdecl fn_10252EA0(uint32_t * param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x10252F00` StTrigger_RegisterCallbacks

- **Verified C++** (`tree/src/StTrigger.cpp`): `XI_API undefined4 __cdecl StTrigger_RegisterCallbacks(int param_1, uint32_t param_2, uint32_t param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10017D20`, `fn_101C4820` ×2
- **Reads globals:** `g_pFileMng`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StTrigger_RegisterCallbacks` (not stated)
- **DancingMad note:** DEFINITIVE CONFIRMATION: explicitly registers StTriggerItemResolve and StTrigger_BuildFromFXT as a resolve/build callback pair in FFXI's generic resource-callback system (the same dword_10662DCC table used elsewhere), for the trigger/FXT resource type. Own error string confirms the term directly: 'Trigger file not found'.
