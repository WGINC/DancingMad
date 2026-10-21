# unit_1005FFD0_AfterimageTask

### `0x10061110` fn_10061110

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API char __thiscall fn_10061110(float *self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 42 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006111B fsubr dword ptr [ecx + 0x74]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10062770` fn_10062770

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API undefined8 __thiscall fn_10062770(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10062772 lea edi, [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyObject_IsKindOf` ×2, `sub_1003B6D0` ×2
- **Run by a frame** (frame_set.json): static

### `0x100627D0` fn_100627D0

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API undefined8 __thiscall fn_100627D0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100627D2 lea edi, [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyObject_IsKindOf` ×2, `sub_1003B6D0`, `sub_1003B700`
- **Run by a frame** (frame_set.json): static

### `0x10062830` fn_10062830

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API void __thiscall fn_10062830(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 135 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10062831 lea esi, [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1003B6D0` ×4, `CMoAttachments::SetCaster`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x10062880` fn_10062880

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API void __thiscall fn_10062880(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 135 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10062881 lea esi, [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1003B700` ×4, `CMoAttachments::SetTarget`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x10062E20` fn_10062E20

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API undefined8 __cdecl fn_10062E20(undefined4 * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 5 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Scheduler_Execute`, `CMoResource::FindByTypeAndId`, `sub_100731B0`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): static

### `0x10062E80` fn_10062E80

- **Verified C++** (`tree/src/unit_1005FFD0_AfterimageTask.cpp`): `XI_API undefined8 __cdecl fn_10062E80(undefined4 param_1, undefined4 param_2, int param_3, int param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Scheduler_Kill`, `CMoResource::FindByTypeAndId`, `sub_10073D80`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): static
