# CMoResource

### `0x10036B70` CMoResource::GetRuntimeClass_variant0

- **Verified C++** (`tree/src/CMoResource.cpp`): `char ** __cdecl CMoResource::GetRuntimeClass_variant0()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoResource_GetRuntimeClass_variant0` (not stated)
- **DancingMad note:** SHARED accessor (x4) -- do not assume this specific stub identifies a specific subclass instance

### `0x10047FC0` CMoResource::CMoCamera_SetLinkedObject

- **Verified C++** (`tree/src/CMoResource.cpp`): `int CMoResource::CMoCamera_SetLinkedObject(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10047FC0 mov ecx, dword ptr [ecx + 0x14]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoCamera_SetLinkedObject` (not stated)
- **DancingMad note:** Set half of a get/set pair for the +0x14 field.

### `0x10047FD0` CMoResource::vf005

- **Verified C++** (`tree/src/CMoResource.cpp`): `void CMoResource::vf005(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10056250` CMoResource::GetRuntimeClass_variant1

- **Verified C++** (`tree/src/CMoResource.cpp`): `char ** __cdecl CMoResource::GetRuntimeClass_variant1()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoResource_GetRuntimeClass_variant1` (not stated)
- **DancingMad note:** SHARED accessor (x4) -- do not assume this specific stub identifies a specific subclass instance

### `0x10056290` CMoResource::GetRuntimeClass_variant2

- **Verified C++** (`tree/src/CMoResource.cpp`): `char ** __cdecl CMoResource::GetRuntimeClass_variant2()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoResource_GetRuntimeClass_variant2` (not stated)
- **DancingMad note:** SHARED accessor (x4) -- do not assume this specific stub identifies a specific subclass instance

### `0x10071D70` CMoResource::GetRuntimeClass_variant3

- **Verified C++** (`tree/src/CMoResource.cpp`): `char ** __cdecl CMoResource::GetRuntimeClass_variant3()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoResource_GetRuntimeClass_variant3` (not stated)
- **DancingMad note:** SHARED accessor (x4) -- do not assume this specific stub identifies a specific subclass instance

### `0x10071DB0` CMoResource::vf008

- **Verified C++** (`tree/src/CMoResource.cpp`): `void CMoResource::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071DC0` CMoResource::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoResource.cpp`): `unsigned int ** CMoResource::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10071DC1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoResource::Destructor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071DE0` CMoResource::Destructor

- **Verified C++** (`tree/src/CMoResource.cpp`): `void __thiscall CMoResource::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10071DE1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoResource_Destroy`, `NodePool_ReleaseNode`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Base destructor of CMoResource: destroys/unlinks the resource and frees its handle slot in the mesh resource manager.

### `0x10071EC0` CMoResource::ReleaseChain

- **Verified C++** (`tree/src/CMoResource.cpp`): `undefined4 __thiscall CMoResource::ReleaseChain(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10071EC2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_100741E0` ×2
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): static, self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Decrements the 15-bit reference count of a resource and its parents up to the root, clearing bit 15 at the root when it reaches zero.

### `0x10072030` CMoResource::RegisterInTypeList

- **Verified C++** (`tree/src/CMoResource.cpp`): `void __thiscall CMoResource::RegisterInTypeList(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 88 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10072032 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10071200`, `MeshResourceMng_AllocHandle`
- **Reads globals:** `0x1047D124`, `g_pMeshResourceMng`
- **Writes globals:** `0x1047D124`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Registers a resource once: allocates its handle and links it at the head of its per-type list and the global resource list.

### `0x10072270` CMoResource::GetParent

- **Verified C++** (`tree/src/CMoResource.cpp`): `void * __thiscall CMoResource::GetParent(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10072270 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns the parent resource from the parent handle at +0x28, or this if the resource is its own root.

### `0x10072290` CMoResource::FindByTypeAndId

- **Verified C++** (`tree/src/CMoResource.cpp`): `undefined8 __thiscall CMoResource::FindByTypeAndId(void * self, undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100722C0`
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Looks up a resource of a given type and FourCC id under this resource with a fresh search serial; returns the handle via out param.

### `0x10072430` CMoResource::FindInScope

- **Verified C++** (`tree/src/CMoResource.cpp`): `undefined4 __stdcall CMoResource::FindInScope(undefined4 * param_1, int param_2, uint32_t param_3, int param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Walks the sibling chain from a resource, respecting nested open(type 1)/close(type 0) blocks, to find one matching type and/or id; returns its handle.
