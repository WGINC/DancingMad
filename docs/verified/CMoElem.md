# CMoElem

### `0x100353C0` CMoElem::GetRuntimeClass_variant0

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant0()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant0` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10036A80` CMoElem::vf013

- **Verified C++** (`tree/src/CMoElem.cpp`): `void CMoElem::vf013(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10036A90` CMoElem::vf014

- **Verified C++** (`tree/src/CMoElem.cpp`): `void CMoElem::vf014(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10036AA0` CMoElem::vf015

- **Verified C++** (`tree/src/CMoElem.cpp`): `int CMoElem::vf015()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10036AB0` CMoElem::vf019

- **Verified C++** (`tree/src/CMoElem.cpp`): `void CMoElem::vf019()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x1003E690` CMoElem::GetRuntimeClass_variant1

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant1()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant1` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10041000` CMoElem::GetRuntimeClass_variant2

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant2()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant2` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10041120` CMoElem::CMoElemFamily_IsKind0

- **Verified C++** (`tree/src/CMoElem.cpp`): `BOOL CMoElem::CMoElemFamily_IsKind0(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElemFamily_IsKind0` (confirmed)
- **DancingMad note:** True only when the queried kind == 0. Shared verbatim between 0x1032AD80 and 0x1032B3B8 -- not distinguishing between them, just confirmed identical code.

### `0x100426A0` CMoElem::GetRuntimeClass_variant3

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant3()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant3` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x100426D0` CMoElem::GetRuntimeClass_variant4

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant4()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant4` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10043190` CMoElem::GetRuntimeClass_variant5

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant5()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant5` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10043570` CMoElem::GetRuntimeClass_variant6

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant6()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant6` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10043700` CMoElem::GetRuntimeClass_variant7

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant7()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant7` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10044880` CMoElem::GetRuntimeClass_variant8

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant8()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant8` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10044890` CMoElem::Constructor

- **Verified C++** (`tree/src/CMoElem.cpp`): `undefined8 __thiscall CMoElem::Constructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10044891 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10055570`, `OcclusionQuery_Init`
- **Reads globals:** `g_countdown_1047BC6C`
- **Writes globals:** `g_countdown_1047BC6C`
- **Run by a frame** (frame_set.json): static, self, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Base constructor of CMoElem: calls parent ctor, inits occlusion query member, stores CMoElem vtable and zeroes/initializes fields.

### `0x10044950` CMoElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoElem.cpp`): `int * CMoElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10044951 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoElem::CMoElemFamily_SharedCleanup`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10044970` CMoElem::CMoElemFamily_SharedCleanup

- **Verified C++** (`tree/src/CMoElem.cpp`): `char CMoElem::CMoElemFamily_SharedCleanup()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100747C0 (tail_purges.json); entry ECX read: `0x10044973 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoGeneratorClone::UnlinkElemListA`, `CMoGeneratorClone_UnlinkElemListB`, `LinkNode_Unlink`, `Mem_FreeWithHeader12`, `OcclusionQuery_Release`, `CMoResource::ReleaseChain` ×2, `MoRes_FreeIfUnreferenced` ×2, `NodePool_ReleaseNode` ×2
- **Reads globals:** `g_countdown_1047BC6C`, `g_pMeshResourceMng`
- **Writes globals:** `g_countdown_1047BC6C`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CMoElemFamily_SharedCleanup` (not stated)
- **DancingMad note:** The common destructor-body cleanup call shared by most CMoElem-family siblings' destructors (CMoDisintegrateProgElem, CMoVuLineProgElem, and many more).

### `0x10044AA0` fn_10044AA0

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API void __thiscall fn_10044AA0(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10044AA0 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoResource_AddRefChain`
- **Run by a frame** (frame_set.json): static, self

### `0x10044AC0` fn_10044AC0

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API unsigned char __thiscall fn_10044AC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10044AC0 mov eax, dword ptr [ecx + 0xfc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): self

### `0x10044AE0` fn_10044AE0

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API undefined4 __thiscall fn_10044AE0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 74 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10044AE2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_100473F0`, `sub_1004A980`, `fn_1004E720`, `sub_10053DD0`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): self, stack

### `0x10044C20` fn_10044C20

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API void __thiscall fn_10044C20(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10044C20 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoResource_AddRefChain`
- **Run by a frame** (frame_set.json): static

### `0x10045800` fn_10045800

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API void __cdecl fn_10045800(float * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Reads constants** (.rdata): 2
- **Run by a frame** (frame_set.json): self

### `0x100458F0` fn_100458F0

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API undefined4 __thiscall fn_100458F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100458F0 fld dword ptr [ecx + 0x138]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_100555B0`
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): self, stack

### `0x10045920` fn_10045920

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API bool __thiscall fn_10045920(int self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 4 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10045924 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `RegisterWithProcessor` ×2, `_atexit`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `Fn10045920_staticGuards`, `g_pResourceMng`, `g_pProcessor`
- **Writes globals:** `Fn10045920_staticGuards`, `Fn10045920_static_BC10`, `Fn10045920_static_BC14`, `Fn10045920_static_BC18`
- **Run by a frame** (frame_set.json): stack

### `0x10045A40` fn_10045A40

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API undefined4 __thiscall fn_10045A40(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10045A45 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10044AE0`, `fn_10044D40`, `YmElem_ComputeViewDepthKey`, `sub_10045190`, `fn_100458F0`, `YmElem_BuildDrawMatrixAndTest`
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): stack

### `0x100467E0` fn_100467E0

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API int __thiscall fn_100467E0(void *self_, int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 78 returned normally, 1452 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 78, town PASS 76, town2 PASS 76, combat PASS 77, zonetoinn PASS 76
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100467F2 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetLight` ×3, `fn_10045800`, `fn_10045C50`, `RegisterWithProcessor`, `fn_100464D0`, `sub_10046550`, `fn_100473F0` ×2, `CMoDX::SetWorldMatrix`, `CMoDX::SetViewMatrix`, `fn_1006AD90`, `StateBlock_ApplyTSS`, `XiZone::GetDirLights`, `fn_1018B960`, `XiZone::GetDirLight`, `XiZone::GetAmbient`, `XiZone::GetFog`, `D3DXMatrixPerspectiveFovLH_static`, `_atexit`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::GetTransform`, `IDirect3DDevice8::LightEnable` ×10, `IDirect3DDevice8::SetRenderState` ×34, `IDirect3DDevice8::SetTransform`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 55, of which 49 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pCamera`, `Fn100467E0_staticGuards`, `g_pResourceMng`, `g_pProcessor`, `g_pZoneMap`, `g_zbiasPreset_C4D0`, `g_pXiZone`
- **Writes globals:** `Fn100467E0_staticGuards`, `0x1047BC0F`
- **Run by a frame** (frame_set.json): self, stack

### `0x100472E0` CMoElem::vf018

- **Verified C++** (`tree/src/CMoElem.cpp`): `void CMoElem::vf018()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100472F0` fn_100472F0

- **Verified C++** (`tree/src/CMoElem.cpp`): `XI_API int __thiscall fn_100472F0(_WORD *a1, __int16 a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 98, town2 PASS 98, combat PASS 98, zonetoinn PASS 98
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100472FD mov ax, word ptr [ecx + 0x16c]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10046550`, `CMoDX::SetViewMatrix`, `fn_1006AD90`, `StateBlockHolder_ApplyRenderStates`, `_atexit`
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState`, `IDirect3DDevice8::SetTransform`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `Fn100472F0_staticGuards`, `g_pResourceMng`, `g_pZoneMap`
- **Writes globals:** `Fn100472F0_staticGuards`
- **Run by a frame** (frame_set.json): self, stack

### `0x10047550` CMoElem::GetRuntimeClass_variant9

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant9()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant9` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10047570` CMoElem::GetRuntimeClass_variant10

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant10()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant10` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x100548A0` CMoElem::GetRuntimeClass_variant11

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant11()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant11` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x100562D0` CMoElem::GetRuntimeClass_variant12

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant12()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant12` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance

### `0x10064160` CMoElem::GetRuntimeClass_variant13

- **Verified C++** (`tree/src/CMoElem.cpp`): `char ** __cdecl CMoElem::GetRuntimeClass_variant13()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoElem_GetRuntimeClass_variant13` (not stated)
- **DancingMad note:** SHARED accessor (x14) -- do not assume this specific stub identifies a specific subclass instance
