# CMoSchedularTask

### `0x10057090` CMoSchedularTask::GetRuntimeClass

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `char ** __cdecl CMoSchedularTask::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoSchedularTask_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10057250` CMoSchedularTask::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `void * CMoSchedularTask::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10057251 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CMoSchedularTask::Destructor`
- **Run by a frame** (frame_set.json): stack

### `0x10057270` fn_10057270

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `XI_API void * __thiscall fn_10057270(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x10057272 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1003B540`, `fn_10055640`, `fn_100573B0`, `fn_100573E0`, `CMoTask_Constructor`, `sub_10074A00`
- **Run by a frame** (frame_set.json): static

### `0x100573B0` fn_100573B0

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `XI_API void __thiscall fn_100573B0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100573B2 mov byte ptr [ecx + 0x141], al` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100573E0` fn_100573E0

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `XI_API void __thiscall fn_100573E0(void * self_, int param_1, uint32_t param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 67 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100573E9 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10057CC0`
- **Run by a frame** (frame_set.json): static, stack

### `0x100574A0` CMoSchedularTask::Destructor

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `void __thiscall CMoSchedularTask::Destructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 28 returned normally, 154 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x100747C0 (tail_purges.json); entry ECX read: `0x100574A3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `ReleaseSubObjectIfPresent`, `fn_1003B690`, `sub_1003B6D0` ×2, `sub_1003B700` ×2, `sub_10055650`, `sub_100683D0`, `CMoResource::ReleaseChain`, `sub_10074A50`, `sub_1018CEA0`
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `dword_1047D140`
- **Run by a frame** (frame_set.json): self
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Destructor of CMoSchedularTask: notifies attached objects, clears back-references in other 'Ms' tasks, frees owned data, invokes an end callback and destroys 16 sub-entries.

### `0x10057CC0` fn_10057CC0

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `XI_API void __thiscall fn_10057CC0(void * self_, short * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10057CC8 mov dword ptr [ecx + 0x90], eax` (ecx_use.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x10057E10` CMoSchedularTask::vf8

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `undefined4 __thiscall CMoSchedularTask::vf8(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 55 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10057E14 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `sub_10057C20`, `CMoSchedularTask::Interpret`, `sub_10062DE0`, `ResourceHandle_IsResident`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pResourceMng`, `dword_1065CB0C`
- **Writes globals:** `Fn10057E10_static_BEF8`
- **Run by a frame** (frame_set.json): self, stack

### `0x10057FB0` CMoSchedularTask::Interpret

- **Verified C++** (`tree/src/CMoSchedularTask.cpp`): `int CMoSchedularTask::Interpret()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 90 returned normally, 8 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 90, town PASS 89, town2 PASS 76, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10057FB9 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::CreateTexture` ×2, `Camera_GetField50` ×3, `fn_10015290`, `Camera_GetViewportWidth` ×2, `Camera_GetViewportHeight` ×2, `fn_10017D30` ×2, `fn_1001E760`, `fn_1001E780`, `sub_10021280`, `Vec4_Copy` ×6, `Mem_AllocFromArea` ×14, `CYyObject_IsKindOf` ×14, `sub_10035E30`, `sub_10036B90`, `fn_10036F00` ×2, `fn_10037020`, `sub_100370D0`, `fn_1003B540`, `sub_1003B6D0` ×12, `sub_1003B700` ×6, `CMoAttachments::SetCaster`, `CMoAttachments::SetTarget`, `fn_1003B8B0` ×12, `fn_1003B900` ×7, `sub_1003B950` ×4, `sub_1003C8A0`, `sub_1003CBB0`, `sub_1003DE40` ×3, `sub_100439C0`, `sub_10043BB0`, `sub_10049560` ×2, `CMoGeneratorClone::ResolveTarget` ×4, `sub_100496F0` ×2, `fn_1004E3B0` ×24, `sub_1004E3C0` ×24, `fn_100527F0`, `fn_10052870` ×36, `fn_10052880` ×3, `fn_10052890` ×5, `fn_100528A0` ×2, `SharedConditionalStateReset`, `CMoGeneratorClone::CreateInstance` ×2, `sub_10053890`, `YmGenerater_Stop` ×2, `fn_100539E0` ×6, `fn_10053A00` ×3, `sub_10053E60`, `CMoGeneratorClone_Kill`, `sub_10056BB0` ×10, `Scheduler_Execute` ×3, `fn_10056EB0`, `Scheduler_Kill`, `sub_10057BE0` ×15, `sub_10057BF0` ×14, `CMoSchedularTask::Interpret` ×2, `sub_1005DFF0`, `sub_1005E000`, `sub_1005E020`, `sub_1005E040` ×37, `sub_1005E070`, `sub_1005E090` ×2, `sub_1005E0B0` ×6, `sub_1005E0E0`, `sub_1005E0F0` ×2, `??0Iostream_init@@QAE@XZ_6`, `fn_1005E110` ×11, `sub_1005E120` ×8, `sub_1005E130` ×6, `sub_1005E140` ×2, `sub_1005E150` ×2, `sub_1005E160` ×2, `sub_1005E170`, `sub_1005E180`, `sub_1005E190` ×2, `sub_1005E1A0`, `sub_1005E1C0` ×2, `sub_1005E1D0` ×13, `sub_1005E1F0` ×14, `sub_1005E200` ×2, `sub_1005E210` ×4, `sub_1005E230` ×4, `sub_1005E240` ×2, `sub_1005E250` ×5, `sub_1005E260`, `sub_1005E270`, `sub_1005E280`, `sub_1005E290`, `sub_1005E2A0` ×2, `sub_1005E2B0`, `sub_1005E2C0`, `sub_1005E2D0`, `sub_1005E2E0` ×8, `sub_1005E2F0` ×3, `unknown_libname_57`, `sub_1005E310`, `sub_1005E320` ×4, `sub_1005E330`, `sub_1005E350`, `sub_1005E360` ×2, `sub_1005E380`, `sub_1005E3A0`, `sub_1005E3E0`, `sub_1005E420`, `sub_1005E460`, `sub_1005E4A0` ×13, `sub_1005E4B0` ×4, `sub_1005E4C0` ×14, `sub_1005E4D0`, `sub_1005E4E0` ×2, `sub_1005E4F0` ×18, `sub_1005E500` ×4, `sub_1005E510` ×23, `sub_1005E520` ×5, `sub_1005E530` ×2, `sub_1005E540`, `sub_1005E550` ×3, `sub_1005E570`, `sub_1005E590` ×39, `sub_1005E5B0`, `sub_1005E5D0` ×3, `sub_1005E5E0`, `sub_1005E5F0`, `sub_1005E600` ×2, `sub_1005E610` ×2, `sub_1005E620` ×2, `sub_1005E630`, `sub_1005E640`, `sub_1005E650` ×2, `sub_1005E660` ×3, `sub_1005E680`, `sub_1005E690`, `sub_1005E6A0`, `sub_1005E6B0`, `sub_1005E6C0`, `sub_1005E6D0`, `sub_1005E6E0`, `sub_1005E6F0`, `sub_1005E700`, `sub_1005E710`, `sub_1005E720`, `sub_1005E740`, `sub_1005E750`, `sub_1005E760`, `sub_1005E770`, `sub_1005E780`, `sub_1005E790`, `sub_1005E7A0` ×5, `sub_1005E7B0`, `sub_1005E7C0`, `sub_1005E7D0`, `sub_1005E7E0`, `sub_1005E800`, `sub_1005E880`, `sub_1005E890`, `sub_1005F320`, `sub_1005F450`, `sub_1005F6C0` ×4, `sub_1005FA20`, `sub_100601F0` ×3, `sub_100607E0` ×2, `sub_10060910` ×2, `sub_10060920`, `sub_10060930`, `sub_10060940`, `sub_10060950`, `sub_10060990`, `sub_10060B30`, `sub_10060DA0`, `sub_10060F80`, `sub_10061240`, `sub_100613D0`, `sub_100615B0`, `sub_100617B0`, `sub_100618A0` ×2, `sub_10061960`, `sub_10061AF0`, `sub_10061C70`, `sub_10061E00`, `sub_10061FD0`, `sub_10062180`, `sub_10062310`, `sub_100624B0`, `sub_10062650`, `fn_10062770` ×118, `fn_100627D0` ×54, `fn_10062830` ×3, `fn_10062880` ×4, `sub_100628D0` ×4, `sub_10062900` ×5, `sub_10062D50` ×4, `sub_10062DE0` ×7, `sub_100683D0` ×13, `sub_100683F0` ×3, `fn_100684F0`, `sub_10068500`, `sub_10068510` ×2, `sub_100685C0` ×9, `sub_100685F0`, `sub_10068890`, `sub_10068AE0`, `sub_10068CE0`, `sub_10068EF0`, `sub_10068F80`, `sub_10069010`, `sub_100690A0`, `sub_10069130`, `sub_100691C0`, `sub_10069D30` ×3, `fn_1006BF60`, `ResourceHandle_IsResident`, `CMoResource::FindByTypeAndId` ×25, `YmResourceFile_FindResourceUnder`, `sub_100725C0`, `ResourceHandle_Deref` ×5, `sub_10072FD0`, `CMoTask_Constructor` ×4, `sub_10074790` ×4, `sub_100747D0`, `CMoTask::ResetFields` ×14, `fn_10074920` ×4, `sub_10074A30`, `sub_10083220`, `sub_10083230`, `sub_10084160`, `sub_100841A0` ×3, `CXiActor::GetModelField170` ×3, `CXiActor::GetModelByteEE` ×2, `sub_10085E40`, `fn_100A57C0`, `sub_100A8E30`, `sub_100AA380` ×2, `sub_100AA3B0` ×2, `sub_100AA8E0`, `sub_100AA940`, `sub_100AAD40`, `sub_100ABEA0` ×4, `sub_100AC290` ×2, `sub_100ADEE0`, `sub_100C3BC0`, `sub_100C3BD0`, `sub_100C3CE0`, `fn_100C51C0`, `sub_100C8BB0`, `fn_100CD4E0` ×2, `sub_100CD920` ×3, `sub_100CDD60`, `sub_100CDE70` ×2, `sub_100CDF00`, `sub_100CE180` ×5, `sub_100CE250`, `CXiSkeletonActor::ReverseFindRes` ×7, `fn_100D5430`, `sub_100D5490`, `sub_100D5F10` ×2, `sub_100D60E0`, `sub_100D6850` ×2, `ntGameTimeGet`, `fn_10186FE0` ×3, `fn_10186FF0` ×3, `fn_10187000` ×3, `sub_10187010` ×3, `sub_101874F0` ×2, `sub_101880B0`, `sub_1018B010`, `sub_1018B3A0`, `fn_1018BAE0`, `sub_1018BB10`, `sub_1018BB20`, `unknown_libname_158` ×8, `fn_1018BBC0` ×8, `sub_1018BBE0` ×2, `Time_Normalize` ×14, `sub_1018C210`, `sub_1018C810`, `sub_1018C870`, `sub_1018C980` ×4, `Sch_GetStatusEntry`, `sub_1018CE10`, `sub_1018CEF0`, `Settings_GetValue`, `fn_10193890`, `sub_10311C2C` ×45
- **Reads constants** (.rdata): 14
- **Indirect calls:** 76, of which 57 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pEnv`, `g_pCamera`, `g_afterimageTex`, `g_pSceneState`, `CMoSchedularTask_Interpret_static_BCE4`, `CMoSchedularTask_Interpret_static_BCE8`, `CMoSchedularTask_Interpret_static_BCEC`, `CMoSchedularTask_Interpret_static_BCF0`, `byte_1047BF18`, `g_pAfterimageTask`, `dword_1047BF20`, `dword_1047BF24`, `dword_1047BF28`, `dword_1047BF2C`, `dword_1047BF30`, `g_pProcessor`, `g_pMeshResourceMng`, `XiControlActor_isFirstPersonView`, `g_pXiZone`, `dword_1065CB18`
- **Writes globals:** `g_afterimageStrength`, `g_afterimageTex`, `g_afterimageHalfTex`, `g_afterimageDepth`, `dword_1045691C`, `g_afterimageState`, `g_feedbackBufferIndex`, `CMoSchedularTask_Interpret_static_BCE4`, `CMoSchedularTask_Interpret_static_BCE8`, `CMoSchedularTask_Interpret_static_BCEC`, `CMoSchedularTask_Interpret_static_BCF0`, `byte_1047BF18`, `g_pAfterimageTask`, `dword_1047BF20`, `dword_1047BF24`, `dword_1047BF28`, `dword_1047BF2C`, `dword_1047BF30`, `g_resourcesDirty`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CMoSchedularTask_Interpret` (not stated)
- **DancingMad note:** 23.6 KB scheduler opcode interpreter (jump table 0x1005DC1C), reached from CMoSchedularTask vtable slot 8 via 0x10057E10. Talks to the D3D device directly (render/texture-stage state, vertex shader, DP/DIP/DPUP) and creates the afterimage textures.
