# unit_10073750_ResourceIter

### `0x10073A60` fn_10073A60

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __stdcall fn_10073A60(int * param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 31 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoResource::RegisterInTypeList`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack

### `0x10073B20` MoRes_FreeIfUnreferenced

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined4 __stdcall MoRes_FreeIfUnreferenced(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 81 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoResource_Destroy` ×2, `fn_10072240`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Destroys a resource (and, if its root is not locked, the root's children) when its reference count is zero.

### `0x10073B80` fn_10073B80

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined4 __stdcall fn_10073B80(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_100720B0`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack

### `0x10073BA0` fn_10073BA0

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined4 __stdcall fn_10073BA0(undefined4 * param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads globals:** `0x1047D124`
- **Run by a frame** (frame_set.json): static

### `0x100740C0` MeshResourceMng_Evict

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined4 __thiscall MeshResourceMng_Evict(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 21 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100740C8 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10072240`, `MoRes_FreeIfUnreferenced`
- **Reads globals:** `0x1047CF84`
- **Run by a frame** (frame_set.json): static

### `0x10074110` fn_10074110

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined8 __thiscall fn_10074110(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10074110 mov edx, dword ptr [ecx + 4]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10074140` MeshResourceMng_AllocHandle

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __thiscall MeshResourceMng_AllocHandle(void * self_, int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1007414B mov edx, dword ptr [ecx + 4]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the resource's handle, allocating one from the manager's free list if it has none.

### `0x10074180` NodePool_ReleaseNode

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __thiscall NodePool_ReleaseNode(void * self_, uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1007418F lea esi, [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Pushes a node onto the pool's free list at this+4 and decrements the live count at this+0x4000C (clamped at 0), guarded by a range check against the 65536-dword inline pool.

### `0x100741E0` fn_100741E0

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined4 __thiscall fn_100741E0(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100741E4 lea edx, [ecx + 8]` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Run by a frame** (frame_set.json): static

### `0x10074280` fn_10074280

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __cdecl fn_10074280(undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x1047D114`
- **Run by a frame** (frame_set.json): static

### `0x100742B0` ResourceIter_FindFirst

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __thiscall ResourceIter_FindFirst(void * self_, int param_1, int param_2, uint32_t param_3, uint32_t param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100742BA mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10074380`, `fn_100743D0`
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `ResourceIter_FindFirst` (not stated)
- **DancingMad note:** Resource search iterator: first match of (type, id) under a resource file.

### `0x10074310` fn_10074310

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __thiscall fn_10074310(void * self_, undefined4 param_1, int param_2, uint32_t param_3, uint32_t param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1007431B mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10074380`, `fn_100743D0`
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): static

### `0x10074380` fn_10074380

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API uint32_t __thiscall fn_10074380(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10074380 mov eax, dword ptr [ecx + 0x14]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100743D0` fn_100743D0

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API void __thiscall fn_100743D0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 89 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100743D0 mov edx, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoResource::GetParent` ×2
- **Reads globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): static, self, stack

### `0x100745C0` ResourceIter_FindNext

- **Verified C++** (`tree/src/unit_10073750_ResourceIter.cpp`): `XI_API undefined4 __thiscall ResourceIter_FindNext(void * self_, undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100745C1 mov esi, dword ptr [ecx + 0x14]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100743D0`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `ResourceIter_FindNext` (not stated)
- **DancingMad note:** Resource search iterator: next match.
