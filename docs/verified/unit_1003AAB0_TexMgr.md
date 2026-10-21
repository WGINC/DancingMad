# unit_1003AAB0_TexMgr

### `0x1003AAB0` fn_1003AAB0

- **Verified C++** (`tree/src/unit_1003AAB0_TexMgr.cpp`): `XI_API int __thiscall fn_1003AAB0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003AAB0 lea eax, [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1003AAF0` fn_1003AAF0

- **Verified C++** (`tree/src/unit_1003AAB0_TexMgr.cpp`): `XI_API int * __thiscall fn_1003AAF0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_1003AAB0`
- **Run by a frame** (frame_set.json): static

### `0x1003AB70` TexMgr_UploadPumpEntry

- **Verified C++** (`tree/src/unit_1003AAB0_TexMgr.cpp`): `XI_API undefined1 __thiscall TexMgr_UploadPumpEntry(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `TexMgr_UploadPump`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `TexMgr_UploadPumpEntry` (not stated)
- **DancingMad note:** Called from Frame_Render right after BeginScene; forwards to TexMgr_UploadPump.

### `0x1003AB80` TexMgr_Enqueue

- **Verified C++** (`tree/src/unit_1003AAB0_TexMgr.cpp`): `XI_API void __thiscall TexMgr_Enqueue(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_1003AAF0`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `TexMgr_Enqueue` (not stated)
- **DancingMad note:** Sets a texture object's state to 1 (pending) and links it into the manager.

### `0x1003ABB0` TexMgr_UploadPump

- **Verified C++** (`tree/src/unit_1003AAB0_TexMgr.cpp`): `XI_API undefined4 __thiscall TexMgr_UploadPump(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 2 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1003ABB2 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `TexObj_CreateAndUpload`, `TexObj_Reupload`, `fn_1003AAB0`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pSceneState`
- **Run by a frame** (frame_set.json): static, self, stack
- **DancingMad name:** `TexMgr_UploadPump` (not stated)
- **DancingMad note:** Per-frame upload pump over the texture list: state 1 -> create+upload, state 2 -> release+reupload. In-game (scene state 0x60) and not in immediate mode (mgr+0x10 == 0) it stops after 20 uploads per frame.

### `0x1003AEA0` TexMgr_FindByName

- **Verified C++** (`tree/src/unit_1003AAB0_TexMgr.cpp`): `XI_API int __thiscall TexMgr_FindByName(void * self_, int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 65 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003AAB0`
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `TexMgr_FindByName` (not stated)
- **DancingMad note:** Looks up an already-loaded texture by its 16-byte name key (dedupe; caller bumps the refcount).
