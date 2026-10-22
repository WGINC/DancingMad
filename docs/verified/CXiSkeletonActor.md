# CXiSkeletonActor

### `0x1002B6E0` CXiSkeletonActor::DrawModel

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::DrawModel(_DWORD *a2, __int16 *a3, int a4, _DWORD *a5, int a6, int a7, unsigned int a8)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 1248 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 28` (purges.json); entry ECX read: `0x1002B6ED mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CDx::SetDefaultRenderState`, `CDx::SetTransform`, `CDx::GetTransformCached` ×3, `fn_1000BE10`, `sub_10015240` ×2, `Model_BeginTranslucentPass`, `Model_TranslucentUnbindTexture`, `fn_1001D390`, `Model_CompositeTranslucentPass`, `ProjTex_CaptureToTarget`, `sub_10026210`, `Vec4_Copy`, `sub_10026F50`, `fn_10027990` ×2, `fn_100279A0` ×2, `Mat4_SetIdentity` ×5, `Mat4_Copy` ×2, `Mat4_SetScale` ×2, `Mat4_SetTranslation` ×3, `Mat4_PostMultiply` ×2, `sub_10027F60` ×3, `Mat4_TransformPointInPlace`, `CXiSkeletonActor::AnimateModels` ×2, `CXiSkeletonActor::PrepareModelsOnce`, `fn_10033DA0`, `sub_10038A70`, `Post_CaptureSceneToTarget`, `Post_DrawRotatingGhostLayers`, `sub_10039410`
- **Reads constants** (.rdata): 2
- **Indirect calls:** 73, of which 72 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_modelsDrawnThisFrame`, `g_cfg0000`, `dword_104570F8`, `g_envMapEnabled`, `dword_10457100`, `dword_10457268`, `dword_1045726C`, `g_projTexEnabled`, `g_lightTable_End`, `g_skinningCapabilityFlag`, `g_modelPrimitiveCount`, `g_modelColor`, `dword_104574B0`, `dword_104574B4`
- **Writes globals:** `g_modelsDrawnThisFrame`, `dword_10457130`, `dword_10457140`, `dword_104571AC`, `dword_104571C0`, `0x104571F0`, `0x104571F4`, `0x104571F8`, `0x104571FC`, `g_modelPrimitiveCount`, `g_modelColor`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_DrawModel` (not stated)
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Per-actor model draw: caches transforms, sets material colour, optional env-map and projected-screen-texture setup, default render states and fog, then animates and draws the model. (pseudocode truncated)

### `0x1002C2D0` CXiSkeletonActor::AnimateModels

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `uint32_t __thiscall CXiSkeletonActor::AnimateModels(void * self, int * param_1, int param_2, uint32_t param_3, undefined4 xi_s4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1002C2D3 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Model_AnimateAndPose`, `CYyModel::GetField44Addr`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `Model_AnimateEntry` (not stated) — differs from this repository's `CXiSkeletonActor_AnimateModels`
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Walks the actor's model list (sub_1002B5A0) calling Model_AnimateAndPose on each; if all succeed sets flags(+0x30)\|=0x12 and returns 1, else 0.

### `0x1002C360` CXiSkeletonActor::PrepareModelsOnce

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::PrepareModelsOnce(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 94 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1002C362 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelBase::DrawLit`, `CYyModel::GetField44Addr`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Once per update (guarded by flag 4 at this+48) calls sub_1002A3B0 on every model in the actor's list, then resets texture stage 1 TEXTURETRANSFORMFLAGS/TEXCOORDINDEX to 0.

### `0x1002C3E0` CXiSkeletonActor::GetElemThunk

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `undefined4 __thiscall CXiSkeletonActor::GetElemThunk(void * self, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 xi_s5, undefined4 xi_s6, undefined4 xi_s7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 28` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1002C400`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Forwards (this,a3,a4,a5) to sub_1002C400, dropping the other arguments.

### `0x1002C5C0` CXiSkeletonActor::GetModelElem

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int __thiscall CXiSkeletonActor::GetModelElem(void * self, uint32_t param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1002A9B0`, `CYyModel::GetField44Addr`
- **Run by a frame** (frame_set.json): self, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Finds the a3-th model in the actor's model list and returns sub_1002A9B0(model, idx, a2) (an element pointer).

### `0x100343C0` CXiSkeletonActor::PoseCompose

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `_BYTE * CXiSkeletonActor::PoseCompose(int a2, int a3, int a4, int a5, _BYTE *a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 81 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 81, town PASS 75, town2 PASS 75, combat PASS 75, zonetoinn PASS 75
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x100343C1 mov eax, dword ptr [ecx + 4]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec3_MulInPlace`, `Mat4_Copy`, `Mat4_SetScale` ×3, `Mat4_SetTranslation` ×3, `Mat4_PostMultiply` ×3, `BoneXform_PostMultiplyInto` ×3
- **Reads globals:** `g_boneWeightMatrixTable`, `g_pSharedSkeleton`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_PoseCompose` (confirmed)
- **DancingMad note:** The real pose composer -- previously only partially traced. Confirmed as one continuous 100-instruction function: reads only the parent-index byte from each 30-byte CYySkl record (the other 29 bytes are never read at all), then composes each bone's transform from a separate 64-byte-stride array via 4 real helper calls per bone, one of which (0x10027D10) is a confirmed real 4x4-matrix-shaped multiply-accumulate. Also contains a confirmed override/exception mechanism: a lookup table at 0x1045EC28 marks specific bone indices as already-handled, skipping the normal composition step for them.

### `0x10082F20` CXiSkeletonActor::GetEnglishName

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char * CXiSkeletonActor::GetEnglishName()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10082F21 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CXiActor::IsInModelSlotTable`, `Entity_BuildDisplayName`
- **Writes globals:** `g_actorNameBuffer`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_GetEnglishName` (not stated)
- **DancingMad note:** PS2 slot 37 -> PC slot 51. Every branch verified against the real PS2 body: field check, IsSubActor-equivalent boolean call, static-buffer string-copy, null-field fallback.

### `0x100832E0` CXiSkeletonActor::SubRef

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::SubRef()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100832E0 mov eax, dword ptr [ecx + 0x80]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SubRef` (confirmed)
- **DancingMad note:** PS2 slot 39 -> PC slot 89. Confirmed by elimination; PC adds an underflow guard PS2's real body does not have.

### `0x100A4740` CXiSkeletonActor::GetPos

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char * CXiSkeletonActor::GetPos()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4740 lea eax, [ecx + 0x5fc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetPos` (not stated)
- **DancingMad note:** PS2 slot 58 -> PC slot 111. Trivial address-computation getter, matches PS2's addiu v0,a0,640 shape and sequence position.

### `0x100A4750` CXiSkeletonActor::GetDir

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char * CXiSkeletonActor::GetDir()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4750 lea eax, [ecx + 0x61c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetDir` (not stated)
- **DancingMad note:** PS2 slot 59 -> PC slot 112. Same basis as GetPos, immediately following it on both platforms.

### `0x100A4760` CXiSkeletonActor::IsMotionLock

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `BOOL CXiSkeletonActor::IsMotionLock()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4760 mov eax, dword ptr [ecx + 0x840]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsMotionLock` (not stated)
- **DancingMad note:** PS2 IsMotionLock() -> PC 149: returns bit 6 of +0x840. Medium.

### `0x100A4770` CXiSkeletonActor::IsMotionLock_Set

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::IsMotionLock_Set(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4774 mov eax, dword ptr [ecx + 0x840]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsMotionLock_Set` (not stated)
- **DancingMad note:** PS2 IsMotionLock(char) (plain store of a bool) -> PC 148: stores the arg into bit 6 of +0x840. Medium (PC packed the bool into a flag word).

### `0x100A4790` CXiSkeletonActor::EnableFlag8AC

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::EnableFlag8AC()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4790 or byte ptr [ecx + 0x8ac], 1` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_EnableFlag8AC` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. or byte [ecx+0x8AC],1 -- clean, unambiguous set-bit.

### `0x100A47A0` CXiSkeletonActor::DisableFlag8AC

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::DisableFlag8AC()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A47A0 and byte ptr [ecx + 0x8ac], 0xfe` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_DisableFlag8AC` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. and byte [ecx+0x8AC],0xFE -- clean, unambiguous clear-bit.

### `0x100A47B0` CXiSkeletonActor::IsFlag8ACSet

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::IsFlag8ACSet()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A47B0 mov al, byte ptr [ecx + 0x8ac]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsFlag8ACSet` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Reads bit 0 of +0x8AC -- completes the triplet with Enable/DisableFlag8AC.

### `0x100A47C0` CXiSkeletonActor::GetField79C

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetField79C()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A47C0 mov al, byte ptr [ecx + 0x79c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetField79C` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Reads byte +0x79C, pairs with SetField79C.

### `0x100A47D0` CXiSkeletonActor::SetField79C

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::SetField79C(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A47D4 mov byte ptr [ecx + 0x79c], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetField79C` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Writes byte +0x79C.

### `0x100A47E0` CXiSkeletonActor::IsReadComplete

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `bool CXiSkeletonActor::IsReadComplete()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100D12D0 (tail_purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsReadComplete` (not stated)
- **DancingMad note:** PS2 slot 70 -> PC 121. Tail-jumps to CXiSkeletonActor_IsReadCompleteBody.

### `0x100A47F0` CXiSkeletonActor::vf256

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `_DWORD * CXiSkeletonActor::vf256(_DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A47F4 mov ecx, dword ptr [ecx + 0x864]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100A4800` CXiSkeletonActor::SetField670

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `__int16 CXiSkeletonActor::SetField670(__int16 a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4805 mov word ptr [ecx + 0x670], ax` (ecx_use.json); entry EDX never read (edx_use.json); sets only AX of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetField670` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Writes word +0x670.

### `0x100A4810` CXiSkeletonActor::GetField670

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `__int16 CXiSkeletonActor::GetField670()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4810 mov ax, word ptr [ecx + 0x670]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AX of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetField670` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Reads word +0x670, pairs with SetField670.

### `0x100A4820` CXiSkeletonActor::vf257

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf257()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100A4830` CXiSkeletonActor::SetColor

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetColor(unsigned int color)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4834 mov dword ptr [ecx + 0x660], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_SetColor` (not stated)
- **DancingMad note:** PS2 slot 8 -> PC slot 12. Writes +0x660.

### `0x100A4840` CXiSkeletonActor::GetColor

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `unsigned int CXiSkeletonActor::GetColor()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4840 mov eax, dword ptr [ecx + 0x660]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetColor` (not stated)
- **DancingMad note:** PS2 slot 7 -> PC slot 11. Reads +0x660 (init 0x80808080).

### `0x100A4850` CXiSkeletonActor::vf017

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::vf017()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4852 mov al, byte ptr [ecx + 0x663]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4860` CXiSkeletonActor::SetMultiTexAlpha

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetMultiTexAlpha(int alpha)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4864 mov dword ptr [ecx + 0x668], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetMultiTexAlpha` (not stated)
- **DancingMad note:** PS2 slot 9 -> PC slot 13. Writes +0x668 (init 128).

### `0x100A4870` CXiSkeletonActor::GetMultiTexAlpha

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetMultiTexAlpha()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4870 mov eax, dword ptr [ecx + 0x668]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetMultiTexAlpha` (not stated)
- **DancingMad note:** PS2 slot 10 -> PC slot 14. Reads +0x668.

### `0x100A4880` CXiSkeletonActor::SetSahdowAlpha

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetSahdowAlpha(int alpha)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4884 mov dword ptr [ecx + 0x66c], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetSahdowAlpha` (not stated)
- **DancingMad note:** PS2 slot 11 -> PC slot 15. Writes +0x66C (init 128). PS2's own spelling, kept as-is.

### `0x100A4890` CXiSkeletonActor::GetShadowAlpha

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetShadowAlpha()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4890 mov eax, dword ptr [ecx + 0x66c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetShadowAlpha` (not stated)
- **DancingMad note:** PS2 slot 12 -> PC slot 16. Reads +0x66C.

### `0x100A48A0` CXiSkeletonActor::EnableEffect

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::EnableEffect(unsigned int flagBit)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A48A4 mov edx, dword ptr [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_EnableEffect` (not stated)
- **DancingMad note:** PS2 slot 14 -> PC slot 19. ORs a bit into +0x734.

### `0x100A48C0` CXiSkeletonActor::DisableEffect

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::DisableEffect(unsigned int flagBit)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A48C4 mov edx, dword ptr [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_DisableEffect` (not stated)
- **DancingMad note:** PS2 slot 15 -> PC slot 20. AND-NOTs a bit out of +0x734.

### `0x100A48E0` CXiSkeletonActor::DisableEffectAll

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::DisableEffectAll()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A48E0 mov dword ptr [ecx + 0x734], 0` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_DisableEffectAll` (not stated)
- **DancingMad note:** PS2 slot 16 -> PC slot 21. Clears +0x734.

### `0x100A48F0` CXiSkeletonActor::SetUVOffset

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::SetUVOffset(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100A48F8 mov dword ptr [ecx + 0x73c], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetUVOffset` (not stated)
- **DancingMad note:** PS2 slot 17 -> PC slot 22. Two-float (u,v) store.

### `0x100A4910` CXiSkeletonActor::SetDistAmount

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetDistAmount(float amount)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4914 mov dword ptr [ecx + 0x744], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetDistAmount` (not stated)
- **DancingMad note:** PS2 slot 18 -> PC slot 23. Writes +0x744.

### `0x100A4920` CXiSkeletonActor::SetEmapColor

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetEmapColor(unsigned int color)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4924 mov dword ptr [ecx + 0x74c], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetEmapColor` (not stated)
- **DancingMad note:** PS2 slot 19 -> PC slot 24. Writes +0x74C.

### `0x100A4930` CXiSkeletonActor::SetEmapTexture

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetEmapTexture(void *texture)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4934 mov dword ptr [ecx + 0x750], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetEmapTexture` (not stated)
- **DancingMad note:** PS2 slot 20 -> PC slot 25. Writes +0x750.

### `0x100A4940` CXiSkeletonActor::SetSeparateValue

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetSeparateValue(float value)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4944 mov dword ptr [ecx + 0x748], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetSeparateValue` (not stated)
- **DancingMad note:** PS2 slot 21 -> PC slot 26. Writes +0x748.

### `0x100A4950` CXiSkeletonActor::SetEmapAlphaMode

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::SetEmapAlphaMode(int mode)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4954 mov dword ptr [ecx + 0x730], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetEmapAlphaMode` (not stated)
- **DancingMad note:** PS2 slot 25 -> PC slot 31. Writes +0x730.

### `0x100A4960` CXiSkeletonActor::GetEmapAlphaMode

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::GetEmapAlphaMode()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4960 mov eax, dword ptr [ecx + 0x730]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetEmapAlphaMode` (not stated)
- **DancingMad note:** PS2 slot 26 -> PC slot 32. Reads +0x730.

### `0x100A4970` CXiSkeletonActor::vf258

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `_DWORD * CXiSkeletonActor::vf258(_DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4974 mov ecx, dword ptr [ecx + 0x750]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4980` CXiSkeletonActor::get_field_74C

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::get_field_74C()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4980 mov eax, dword ptr [ecx + 0x74c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4990` CXiSkeletonActor::set_field_73C

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::set_field_73C(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4994 mov dword ptr [ecx + 0x73c], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A49A0` CXiSkeletonActor::get_field_73C

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `double CXiSkeletonActor::get_field_73C()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A49A0 fld dword ptr [ecx + 0x73c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A49B0` CXiSkeletonActor::set_field_740

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::set_field_740(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A49B4 mov dword ptr [ecx + 0x740], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A49C0` CXiSkeletonActor::get_field_740

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `double CXiSkeletonActor::get_field_740()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A49C0 fld dword ptr [ecx + 0x740]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A49D0` CXiSkeletonActor::IsEnvmap

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::IsEnvmap()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A49D0 mov eax, dword ptr [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsEnvmap` (not stated)
- **DancingMad note:** PS2 slot 22 -> PC slot 27. Tests bit 0 of +0x734.

### `0x100A49E0` CXiSkeletonActor::IsDistortion

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `BOOL CXiSkeletonActor::IsDistortion()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A49E0 mov eax, dword ptr [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsDistortion` (not stated)
- **DancingMad note:** PS2 slot 23 -> PC slot 28. Tests bit 1 of +0x734.

### `0x100A49F0` CXiSkeletonActor::IsMasking

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `BOOL CXiSkeletonActor::IsMasking()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A49F0 mov eax, dword ptr [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsMasking` (not stated)
- **DancingMad note:** PS2 slot 24 -> PC slot 29. Tests bit 2 of +0x734.

### `0x100A4A00` CXiSkeletonActor::vf030

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `BOOL CXiSkeletonActor::vf030()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4A00 mov eax, dword ptr [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100A4A10` CXiSkeletonActor::IsDirectionLock

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::IsDirectionLock()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4A10 mov eax, dword ptr [ecx + 0x838]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsDirectionLock` (not stated)
- **DancingMad note:** PS2 IsDirectionLock() -> PC 198: returns +0x838. Previously GetField838.

### `0x100A4A20` CXiSkeletonActor::IsConstrain

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `__int16 CXiSkeletonActor::IsConstrain()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4A20 mov ax, word ptr [ecx + 0x83c]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AX of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_IsConstrain` (not stated)
- **DancingMad note:** PS2 IsConstrain() -> PC 200: reads both elements at once (word +0x83C), as PS2 reads the word at +0x3D8. Previously GetField83C.

### `0x100A4A30` CXiSkeletonActor::IsConstrain_Set

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `bool CXiSkeletonActor::IsConstrain_Set(char a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100A4A3D mov byte ptr [edx + ecx + 0x83c], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsConstrain_Set` (not stated)
- **DancingMad note:** PS2 IsConstrain(char, int) -> PC 199. HIGH: stores (c==1) at index i (sete + indexed store), as PS2 stores (c==1) into halfword +0x3D8+2i. PC shrank the elements to bytes at +0x83C.

### `0x100A4A50` CXiSkeletonActor::IsConstrain2

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `__int16 CXiSkeletonActor::IsConstrain2()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4A50 mov ax, word ptr [ecx + 0x83e]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AX of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsConstrain2` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, PC-only: word read of +0x83E. Previously GetField83E.

### `0x100A4A60` CXiSkeletonActor::IsConstrain2_Get

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::IsConstrain2_Get(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4A64 mov al, byte ptr [eax + ecx + 0x83e]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsConstrain2_Get` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, PC-only: indexed byte read of the +0x83E family. Previously GetIndexedByte83E.

### `0x100A4A70` CXiSkeletonActor::IsConstrain2_Set

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `bool CXiSkeletonActor::IsConstrain2_Set(char a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100A4A7D mov byte ptr [edx + ecx + 0x83e], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsConstrain2_Set` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, PC-only: a second two-element constrain family at +0x83E, identical shape to IsConstrain_Set.

### `0x100A4A90` CXiSkeletonActor::vf041

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf041()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4A90 mov al, byte ptr [ecx + 0x8a5]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4AA0` CXiSkeletonActor::vf042

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf042(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4AA4 mov byte ptr [ecx + 0x8a5], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4AB0` CXiSkeletonActor::vf043

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf043()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4AB0 mov al, byte ptr [ecx + 0x8a6]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4AC0` CXiSkeletonActor::vf044

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf044(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4AC4 mov byte ptr [ecx + 0x8a6], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4AD0` CXiSkeletonActor::vf045

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf045()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4AD0 mov al, byte ptr [ecx + 0x8a7]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100A4AE0` CXiSkeletonActor::vf046

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf046(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4AE4 mov byte ptr [ecx + 0x8a7], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4AF0` CXiSkeletonActor::vf047

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf047()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4AF0 mov al, byte ptr [ecx + 0x8a8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4B00` CXiSkeletonActor::ActivateFlag9F8

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::ActivateFlag9F8(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4B04 mov byte ptr [ecx + 0x8a8], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_ActivateFlag9F8` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Unconditionally writes 1 to byte +0x9F8.

### `0x100A4B10` CXiSkeletonActor::ActivateFlagA04

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::ActivateFlagA04()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4B10 mov al, byte ptr [ecx + 0x8a9]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_ActivateFlagA04` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. Unconditionally writes 1 to byte +0xA04.

### `0x100A4B20` CXiSkeletonActor::vf050

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::vf050(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A4B24 mov byte ptr [ecx + 0x8a9], al` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4B30` CXiSkeletonActor::vf099

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf099()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4B30 mov byte ptr [ecx + 0x9f8], 1` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100A4B40` CXiSkeletonActor::vf100

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf100()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4B40 mov byte ptr [ecx + 0xa04], 1` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100AB070` CXiSkeletonActor::GetRuntimeClass_variant0

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char ** __cdecl CXiSkeletonActor::GetRuntimeClass_variant0()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetRuntimeClass_variant0` (not stated)
- **DancingMad note:** SHARED accessor (x3) -- do not assume this specific stub identifies a specific subclass instance

### `0x100C5190` CXiSkeletonActor::GetRuntimeClass_variant1

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char ** __cdecl CXiSkeletonActor::GetRuntimeClass_variant1()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiSkeletonActor_GetRuntimeClass_variant1` (not stated)
- **DancingMad note:** SHARED accessor (x3) -- do not assume this specific stub identifies a specific subclass instance

### `0x100C52A0` CXiSkeletonActor::Constructor_1Arg

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::Constructor_1Arg(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100C52A4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Camera_GetField50`, `Actor_InitIndexTable`, `Vec4_Copy` ×3, `fn_10027990`, `CYyModel::Constructor`, `LinkNode_Init`, `OcclusionQuery_Init`, `CMoTask_RegisterWithMng`, `ActorHandle_Constructor`, `CXiActor::IsModelMissingOrFlag2000`, `CXiActor::GetModelField170`, `CXiActor::GetModelByteEE` ×4, `Net_SendPacket00COnce`, `CXiCollisionActor::Constructor`, `CXiSkeletonActor::Init`, `Actor_SetSlotTableEntry` ×3
- **Run by a frame** (frame_set.json): static

### `0x100C5540` CXiSkeletonActor::ScalarDeletingDtor

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::ScalarDeletingDtor(char a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100C5541 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CXiSkeletonActor::DestructorBody`
- **Run by a frame** (frame_set.json): stack

### `0x100C5560` CXiSkeletonActor::Constructor_2Arg

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::Constructor_2Arg(_DWORD *a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100C5564 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Actor_InitIndexTable`, `Vec4_Copy` ×3, `fn_10027990`, `CYyModel::Constructor`, `LinkNode_Init`, `OcclusionQuery_Init`, `CMoTask_RegisterWithMng`, `ActorHandle_Constructor`, `CXiActor::IsModelMissingOrFlag2000`, `CXiActor::GetModelField170`, `CXiActor::GetModelByteEE` ×4, `Net_SendPacket00COnce`, `CXiCollisionActor::Constructor`, `CXiSkeletonActor::Init`, `CXiSkeletonActor::LoadSkeletonResource`, `Actor_SetSlotTableEntry` ×3
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100C56E0` CXiSkeletonActor::Constructor_3Arg

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::Constructor_3Arg(_DWORD *a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100C56E4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Actor_InitIndexTable`, `Vec4_Copy` ×3, `fn_10027990`, `CYyModel::Constructor`, `LinkNode_Init`, `OcclusionQuery_Init`, `CMoTask_RegisterWithMng`, `ActorHandle_Constructor`, `CXiActor::IsModelMissingOrFlag2000`, `CXiActor::GetModelField170`, `CXiActor::GetModelByteEE` ×4, `Net_SendPacket00COnce`, `CXiCollisionActor::Constructor`, `CXiSkeletonActor::Init`, `CXiSkeletonActor::LoadSkeletonResource`, `Actor_SetSlotTableEntry` ×3
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100C5880` CXiSkeletonActor::Constructor_4Arg

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::Constructor_4Arg(_DWORD *a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100C5884 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Actor_InitIndexTable`, `Vec4_Copy` ×3, `fn_10027990`, `CYyModel::Constructor`, `LinkNode_Init`, `OcclusionQuery_Init`, `CMoTask_RegisterWithMng`, `ActorHandle_Constructor`, `Net_SendPacket00COnce`, `CXiCollisionActor::Constructor`, `CXiSkeletonActor::Init`, `CXiSkeletonActor::LoadSkeletonResource`, `Actor_SetSlotTableEntry` ×3
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100C59B0` CXiSkeletonActor::Constructor_Factory

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::Constructor_Factory(_DWORD *a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 82 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 82, town PASS 77, town2 PASS 77, combat PASS 77, zonetoinn PASS 77
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100C59B3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10017D30` ×7, `Actor_InitIndexTable`, `Vec4_Copy` ×3, `fn_10027990`, `CYyModel::Constructor`, `LinkNode_Init`, `OcclusionQuery_Init`, `CMoTaskMng::Forward10075120`, `ActorHandle_Constructor`, `Net_SendPacket00COnce`, `CXiCollisionActor::Constructor`, `CXiSkeletonActor::Init`, `CXiSkeletonActor::LoadSkeletonResource`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100C5C00` CXiSkeletonActor::DestructorBody

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::DestructorBody()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 77 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100A8CA0 (tail_purges.json); entry ECX read: `0x100C5C01 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_100279A0`, `CYyModel::Destructor`, `CMoGeneratorClone_Kill` ×2, `LinkNode_Unlink`, `OcclusionQuery_Release`, `ResHandle_FreeIfUnreferenced`, `CMoResource::ReleaseChain` ×3, `ActorHandle_Destructor`, `ActorHandle_Resolve`, `Actor_UnlinkAllAttachLists`, `CXiSkeletonActor_DeleteOwnedList`, `fn_10157660`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pTargetMng`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_DestructorBody` (not stated)
- **DancingMad note:** Releases resources and destroys the owned async skeleton-load task at +0xA08 (calls its vtable slot 6, scalar-deleting destructor, then clears the field) -- the actor owns the task. Decrements the actor's two update-bucket counters.

### `0x100C5D60` CXiSkeletonActor::Init

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::Init()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C5D63 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Vec4_Copy` ×2, `Vec3_Copy`, `sub_100814F0`, `fn_100D5430`, `fn_100D6240`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 11, of which 11 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_skelActorInit_848`, `c_skelActorInit_84C`, `c_skelActorInit_850`, `c_skelActorInit_61C`, `c_skelActorInit_620`, `c_skelActorInit_624`, `c_skelActorInit_628`, `c_skelActorInit_5FC`, `c_skelActorInit_600`, `c_skelActorInit_604`, `c_skelActorInit_608`, `c_skelActorInit_9D8`, `c_skelActorInit_9DC`, `c_skelActorInit_9E0`, `c_skelActorInit_9E4`, `c_skelActorInit_60C`, `c_skelActorInit_610`, `c_skelActorInit_614`, `c_skelActorInit_618`, `c_skelActorInit_62C`, `c_skelActorInit_630`, `c_skelActorInit_634`, `c_skelActorInit_638`, `c_skelActorInit_7B4`, `c_skelActorInit_7B8`, `c_skelActorInit_7BC`, `c_skelActorInit_7C0`, `g_actorSerialCounter`
- **Writes globals:** `g_actorSerialCounter`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiSkeletonActor_Init` (not stated)
- **DancingMad note:** Init/reset. Sets opacity (+0x59C, likely XiControlActor::alpha_base) to 0 so actors fade in; color +0x660 = 0x80808080 and mtex_alpha/shadow_alpha (+0x668/+0x66C) = 128 (PS2 '0x80 = 1.0' convention); animation-name table 'idl?wlk?run?btl?' at +0x7C8; +0xA08 = 0; assigns the actor to the least-loaded of four buckets in g_actorUpdateBucketCountA/B (indices at +0x9F0/+0x9FC; used by sub_100CBDE0 to run work every fourth frame).

### `0x100C63D0` CXiSkeletonActor::OnMove

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::OnMove()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 86 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 86, town PASS 96, town2 PASS 96, combat PASS 96, zonetoinn PASS 96
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C63D8 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `CDx::GetTransformCached` ×3, `Camera_GetFrameScale` ×6, `Camera_GetFloat2DC`, `Camera_GetFloat2E0`, `Camera_GetMatrix154Ptr` ×2, `fn_10026E00` ×2, `Vec4_Set` ×2, `Vec4_Copy` ×6, `Vec3_Copy` ×9, `Vec3_AddInPlace` ×5, `Vec3_Add_10026FA0` ×2, `Vec3_Sub` ×4, `fn_100272B0` ×2, `sub_100274B0` ×2, `sub_10027530` ×3, `Gfx_ProjectWorldToClip`, `Gfx_NdcToScreen`, `fn_10027990` ×5, `fn_100279A0` ×7, `Mat4_SetIdentity`, `Mat4_SetScale`, `Mat4_PostRotateY` ×2, `Mat4_SetTranslation`, `fn_10028170`, `Mat4_TransformPointInPlace`, `fn_10028230` ×2, `sub_10028370`, `CYyModel::GetField44Addr`, `fn_1002C270`, `fn_1002C2A0`, `Skel_OffsetAllTranslations`, `sub_10039410`, `sub_1003BA20`, `sub_100553C0`, `fn_1006CA20`, `ResourceHandle_IsResident` ×2, `ActorHandle_Resolve` ×3, `CXiActor_ModelTest95790`, `CXiActor_ModelTest95680` ×7, `CXiActor_ModelTest956A0` ×7, `CXiActor::GetModelField170` ×33, `fn_10084670`, `sub_100846D0`, `sub_100846F0`, `sub_10085000` ×2, `CXiActor::IsInModelSlotTable`, `fn_10085BF0` ×2, `fn_10087060` ×2, `sub_1008E130`, `Entity_GetIndexedPtr`, `sub_100A4ED0`, `fn_100A5E10`, `fn_100C8280`, `sub_100C83C0` ×2, `sub_100C8ED0` ×2, `sub_100C9330` ×2, `sub_100C9810`, `sub_100C9C10`, `sub_100CA310`, `sub_100CA730`, `sub_100CA8C0` ×2, `sub_100CAA60`, `sub_100CAF90`, `sub_100CB390`, `sub_100CB400`, `sub_100CD040`, `fn_100CDF90`, `sub_100D1070`, `sub_100D4BC0`, `fn_1018B8F0`
- **Reads constants** (.rdata): 13
- **Indirect calls:** 91, of which 88 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `c_skelActorOnMove_init0`, `c_skelActorOnMove_init1`, `c_skelActorOnMove_init2`, `c_skelActorOnMove_init3`, `g_pCDx`, `g_pCamera`, `dword_1047BC94`, `XiControlActor_isFirstPersonView`, `g_pXiZone`
- **Writes globals:** `CXiSkeletonActor_OnMove_static_A344`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_OnMove` (not stated)
- **DancingMad note:** PS2 vtable slot 5 (OnMove) -> PC slot 8. The per-frame actor update.

### `0x100CBD60` CXiSkeletonActor::RunStaggeredUpdates

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::RunStaggeredUpdates()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100CBD61 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CXiSkeletonActor::PerActor_FourBucketStaggeredUpdate`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_RunStaggeredUpdates` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, PC slot 162: two guarded calls into PerActor_FourBucketStaggeredUpdate (+0x8D4/+0x8E8).

### `0x100CBDE0` CXiSkeletonActor::PerActor_FourBucketStaggeredUpdate

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::PerActor_FourBucketStaggeredUpdate()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 30 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 30, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100CBDE9 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform`, `GetFrameCounter` ×4, `Camera_GetField50`, `Camera_GetViewportWidth`, `Camera_GetViewportHeight`, `Vec4_Set` ×2, `Vec4_Copy` ×2, `Vec3_Copy` ×5, `Vec3_AddInPlace`, `Vec3_Add_10026FA0` ×4, `Vec3_Sub` ×3, `Vec3_Scale`, `fn_10027990`, `fn_100279A0`, `Mat4_Copy` ×3, `Mat4_BuildScale` ×2, `Mat4_PostRotateX` ×3, `Mat4_PostRotateY` ×3, `Mat4_PostRotateZ` ×3, `Mat4_SetRow3` ×2, `Mat4_TransformNormal` ×2, `CYyModel::GetField44Addr`, `CXiSkeletonActor::DrawModel` ×2, `CXiSkeletonActor::AnimateModels`, `Shadow_SmoothLightDirection`, `Occlusion_QueryScreenRect`, `CXiActor_ModelTest956A0`, `CXiActor::GetModelField170` ×5, `CXiActor::HasNonzeroField150or158`, `CXiActor::IsModelMissingOrSuppressed`, `CXiActor_TestModelFlag128_8`, `CXiActor::TestModelFlags100000_200000_4000` ×2, `CXiActor::IsInModelSlotTable`, `Actor_SelectNearestLights`, `Actor_SetCameraFromModelPoints` ×3, `CXiSkeletonActor_CalcGroundTiltMatrix` ×2, `CXiSkeletonActor_UpdateHeadLook`, `Actor_PrepareDrawGlobals`, `_D3DXMatrixLookAtRH@16` ×2, `sub_10311C2C`, `_atexit` ×4
- **Reads constants** (.rdata): 13
- **Indirect calls:** 61, of which 46 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pAppSettings`, `g_pCDx`, `g_shadowSetting`, `g_cfg0020`, `pTexture`, `g_translucentTarget`, `g_actorShadowMode`, `g_shadowCasterDistance`, `dword_1045B810`, `g_nearestLight`, `PerActor_FourBucketStaggeredUpdate_staticGuards`, `g_actorUpdateCounter`, `g_actorUpdateInterval`, `g_pXiZone`
- **Writes globals:** `byte_104570F0`, `g_envMapEnabled`, `g_projTexEnabled`, `g_skinningCapabilityFlag`, `byte_10457538`, `g_actorShadowMode`, `g_shadowCasterDistance`, `dword_1045B810`, `word_1045B814`, `g_lightLookAtTarget`, `PerActor_FourBucketStaggeredUpdate_static_A310`, `PerActor_FourBucketStaggeredUpdate_static_A314`, `g_lightLookAtEye`, `PerActor_FourBucketStaggeredUpdate_static_A31C`, `PerActor_FourBucketStaggeredUpdate_static_A320`, `PerActor_FourBucketStaggeredUpdate_staticGuards`, `PerActor_FourBucketStaggeredUpdate_static_A32C`, `PerActor_FourBucketStaggeredUpdate_static_A330`, `PerActor_FourBucketStaggeredUpdate_static_A334`, `g_lightLookAtUp`, `PerActor_FourBucketStaggeredUpdate_static_A33C`, `PerActor_FourBucketStaggeredUpdate_static_A340`, `g_actorUpdateCounter`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `PerActor_FourBucketStaggeredUpdate` (not stated)
- **DancingMad note:** Runs two blocks of per-actor work only when a per-actor bucket index (+0x9F0, +0x9FC) matches a global frame counter mod 4 (via GetFrameCounter) -- spreads per-actor cost evenly across four frames rather than doing it all every frame.

### `0x100CCF50` CXiSkeletonActor::OcclusionClip

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::OcclusionClip()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100CCF54 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetViewportWidth`, `Camera_GetViewportHeight`, `CYyModel::GetField44Addr`, `fn_1002C270`, `Occlusion_QueryScreenRect`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `pTexture`, `g_translucentTarget`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_OcclusionClip` (not stated)
- **DancingMad note:** PS2 slot 95 -> PC 191 (0 args). Projects a screen rect from +0x8F0..+0x90C using the camera viewport, runs Occlusion_QueryScreenRect; on fail sets +0xB0 and +0xB2 bit0. PS2 OcclusionClip is a real 524-B KO_OcclusionCulling call (not a stub, correcting the older doc).

### `0x100CD490` CXiSkeletonActor::SetMotion

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char * CXiSkeletonActor::SetMotion(int *a2, float a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100CD491 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyMotionQue::SetSlotMotion`, `CYyModel::GetField44Addr` ×2
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetMotion` (not stated)
- **DancingMad note:** PS2 slot 84 -> PC 165 (SetMotion(YmResource*, float), ret 8). PS2 base body is empty; PC implements it on the model sub-object at +0x674. Medium.

### `0x100CD4E0` fn_100CD4E0

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API void __thiscall fn_100CD4E0(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6, int param_7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 28` (purges.json); entry ECX read: `0x100CD4E1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyMotionQue::SetSlotMotion`, `CYyModel::GetField44Addr` ×2
- **Run by a frame** (frame_set.json): self, stack

### `0x100CD540` fn_100CD540

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API undefined4 __thiscall fn_100CD540(void * self_, int * param_1, uint32_t param_2, undefined4 param_3, float param_4, undefined4 param_5, undefined4 param_6, undefined4 param_7, int param_8, int param_9, undefined4 param_10, undefined4 param_11)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 30 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 44` (purges.json); entry ECX read: `0x100CD560 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10017D20` ×2, `CYyMotionQue::SetSlotMotion` ×2, `fn_1001A6E0` ×2, `CYyModel::GetField44Addr` ×8, `CMoResource::GetParent` ×2, `ResourceIter_FindFirst` ×2, `ResourceIter_FindNext` ×2, `CXiActor::GetModelByteEE` ×6, `sub_10312872` ×2
- **Reads constants** (.rdata): 1
- **Reads globals:** `g_resourceFindDepth`, `0x1048A38C`
- **Writes globals:** `g_resourceFindDepth`, `0x1048A38C`
- **Run by a frame** (frame_set.json): stack

### `0x100CDF90` fn_100CDF90

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API void __thiscall fn_100CDF90(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 25 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100CDF94 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetFrameScale`, `ResourceHandle_IsResident`, `CMoResource::FindInScope`, `fn_100CD4E0`, `CXiSkeletonActor::IsReadCompleteBody`, `sub_103149A0`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Writes globals:** `0x1048A38C`
- **Run by a frame** (frame_set.json): stack

### `0x100CE160` fn_100CE160

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API void __thiscall fn_100CE160(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100CE160 add ecx, 0x674` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1001B170`, `CYyModel::GetField44Addr`
- **Run by a frame** (frame_set.json): static

### `0x100CE480` CXiSkeletonActor::ReverseFindRes

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `_DWORD * CXiSkeletonActor::ReverseFindRes(_DWORD *a2, int a3, int a4, int a5, int a6, char a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 30 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 30, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x100CE484 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `List_GetTail`, `ResourceHandle_IsResident` ×3, `CMoResource::GetParent` ×3, `ResourceIter_FindFirst` ×3, `ResourceIter_FindNext` ×3
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_ReverseFindRes` (not stated)
- **DancingMad note:** PS2 XiSkeletonActor::ReverseFindRes(RES_TYPE, uint, uint, int) (0x1CF770). Called with (7, id, -1, ...) by SetAction/KillAction/IsMovingAction.

### `0x100CE9B0` CXiSkeletonActor::ActorFindResource

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `_DWORD * CXiSkeletonActor::ActorFindResource(_DWORD *a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 28 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 28, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100CE9B6 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelBase::GetPartList`, `CYyModel::GetField44Addr`, `ResourceHandle_IsResident`, `CMoResource::GetParent`, `YmResourceFile_FindResourceUnder`, `ResourceIter_FindFirst`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_ActorFindResource` (not stated)
- **DancingMad note:** PS2 ActorFindResource(RES_TYPE, uint) (slot 66 -> PC 123). FindFirst only; fallback to GetModelFile.

### `0x100CEB00` CXiSkeletonActor::ActorFindResourceNth

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `_DWORD * CXiSkeletonActor::ActorFindResourceNth(_DWORD *a2, int a3, int a4, int a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 28 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 28, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100CEB07 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelBase::GetPartList`, `CYyModel::GetField44Addr`, `ResourceHandle_IsResident`, `CMoResource::GetParent`, `ResourceIter_FindFirst` ×2, `ResourceIter_FindNext` ×2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_ActorFindResourceNth` (not stated)
- **DancingMad note:** PS2 ActorFindResource(RES_TYPE, uint, int) (slot 67 -> PC 122; MSVC reverses overload order). FindFirst/FindNext over the actor resource list, fallback to GetModelFile.

### `0x100CEC90` CXiSkeletonActor::ActorGetResourceCount

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::ActorGetResourceCount(int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 26 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 26, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100CEC96 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelBase::GetPartList`, `CYyModel::GetField44Addr`, `ResourceHandle_IsResident`, `CMoResource::GetParent`, `ResourceIter_FindFirst` ×2, `ResourceIter_FindNext` ×2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_resourceFindDepth`
- **Writes globals:** `g_resourceFindDepth`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_ActorGetResourceCount` (not stated)
- **DancingMad note:** PS2 slot 68 -> PC 124. Counts FindFirst/FindNext hits.

### `0x100CEDF0` CXiSkeletonActor::ReplaceAttack

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::ReplaceAttack(int a1, int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_ReplaceAttack` (not stated)
- **DancingMad note:** PS2 ReplaceAttack -> PC 175. Empty on both (PS2 16 B); ret 0x10 matches PC SetAttack arity.

### `0x100CEE00` CXiSkeletonActor::SetAttack

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::SetAttack(int a2, int a3, int a4, char *Source)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100CEE04 mov eax, dword ptr [ecx]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `ChatLog_AddMessage`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pTkMsgWinData`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetAttack` (not stated)
- **DancingMad note:** PS2 SetAttack(uint, XiActor*, char*, int, DAMAGE_KIND) -> PC 174 (ret 0x10 -- PC signature has one fewer stack arg). Calls SetAction through vslot 166.

### `0x100CEE40` CXiSkeletonActor::SetAction

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::SetAction(int a2, _DWORD *a3, void *a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100CEE55 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Scheduler_Execute` ×2, `YmResourceFile_FindResourceUnder`, `ResourceHandle_Deref` ×2, `CXiSkeletonActor::ReverseFindRes`, `CXiSchStatus_Destructor`, `operator_delete`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_SetAction` (not stated)
- **DancingMad note:** PS2 XiSkeletonActor::SetAction(uint, XiActor*, CXiSchStatus*), slot 85 -> PC 166. HIGH: identical callee sequence to the real PS2 body -- ReverseFindRes(7,id,-1) -> Scheduler_Execute; else YmResourceFile::FindResourceUnder(7,id) -> Scheduler_Execute; else destroy the CXiSchStatus. ret 0xC = 3 args.

### `0x100CF030` CXiSkeletonActor::SetAttack_SchStatus

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `int CXiSkeletonActor::SetAttack_SchStatus(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100CF032 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Sch_GetStatusEntry`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetAttack_SchStatus` (not stated)
- **DancingMad note:** PS2 SetAttack(CXiSchStatus*) -> PC 173. HIGH: calls SetAction through vslot 166 (+0x298), as PS2 calls it through vtbl+0x154. MSVC grouped/reversed the overloads.

### `0x100CF100` fn_100CF100

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API undefined8 __thiscall fn_100CF100(void * self_, undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100CF102 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CXiActor::GetModelField170`, `sub_100D5FE0`, `sub_100D6180`, `fn_100D6240`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack

### `0x100CF200` CXiSkeletonActor::vf172

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf172(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100CF200 add ecx, 0x674` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CYyModelBase_ForwardToField24`, `CYyModel::GetField44Addr`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100CF210` CXiSkeletonActor::SetModel

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::SetModel(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100CF21A mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10017D30`, `Actor_GetPercentScaleByIndex` ×6, `Actor_LookupPercentScaleA`, `Actor_LookupPercentScaleB`, `Actor_SetPair14`, `Actor_SetPair1C`, `CYyModelBase::SetResourceAndRebuild`, `CYyModelBase::AddPartFromResource`, `CYyModel::CreateModelBase`, `CMoGeneratorClone::CreateInstance`, `ResourceHandle_IsResident`, `CMoResource_AddRefChain` ×3, `CMoResource::FindInScope`, `ResourceHandle_Deref`, `ResourceIter_FindFirst` ×2, `ResourceIter_FindNext` ×2, `CXiActor::GetModelByteEF` ×2, `CXiActor::GetModelFlags120Top2` ×4, `CXiActor::GetModelFlags130Top2`, `CXiActor::GetModelFloat9AEC0`, `CXiActor::SpawnResourceGenerators`
- **Indirect calls:** 10, of which 10 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SetModel` (candidate)
- **DancingMad note:** PS2 XiSkeletonActor::SetModel(YmResource*) slot 83 -> PC 164. Upgraded from _Candidate: now inside the confirmed positional run (163 OnChangeEquip, 166-168 action cluster).

### `0x100CFA50` fn_100CFA50

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API void __thiscall fn_100CFA50(void * self_, int * param_1, void * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100CFA59 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelBase::AddPartFromResource`, `CMoResource_AddRefChain`, `ResourceIter_FindFirst`, `ResourceIter_FindNext`, `CXiActor::SpawnResourceGenerators`
- **Run by a frame** (frame_set.json): static, stack

### `0x100CFAD0` fn_100CFAD0

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API undefined * __thiscall fn_100CFAD0(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_100CFB40`
- **Run by a frame** (frame_set.json): stack

### `0x100CFC10` CXiSkeletonActor::Slot244_Unknown

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::Slot244_Unknown(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100CFC17 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Vec4_Copy` ×2, `fn_10027990`, `fn_100279A0` ×2, `Mat4_SetIdentity`, `Mat4_PostRotateY`, `Mat4_SetTranslation`, `Mat4_PostMultiply`, `Mat4_TransformCoordInPlace`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_Slot244_Unknown` (candidate)
- **DancingMad note:** RETRACTED as SetAction candidate (2026-09-26): the real SetAction is 0x100CEE40, found by callee identity. This is PC slot 244 (ret 0xC, 814 B): identity/copy matrix helpers from the skinning code plus CDx-range indirect calls. Purpose not determined.

### `0x100D04B0` CXiSkeletonActor::GetField878Ptr_Candidate

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char * CXiSkeletonActor::GetField878Ptr_Candidate()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D04B0 lea eax, [ecx + 0x878]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetField878Ptr_Candidate` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, not PS2-confirmed. lea eax,[ecx+0x878]; ret. Unresolved candidate for GetGroundNormal/GetFocal.

### `0x100D04C0` CXiSkeletonActor::GetNamePos

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetNamePos(int a2, float *a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100D04C5 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CXiActor_NameCalc`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_GetNamePos` (not stated)
- **DancingMad note:** PS2 slot 80 -> PC 158. HIGH: GetElem (vslot 113) then CXiActor_NameCalc, as PS2 does. ret 0xC.

### `0x100D0510` CXiSkeletonActor::OnDrawName

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::OnDrawName()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 84 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 84, town PASS 82, town2 PASS 82, combat PASS 82, zonetoinn PASS 82
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D051E mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Quat_SetIdentity`, `ActorHandle_Resolve`, `CXiActor_TestModelFlag128_8`, `Entity_GetIndexedPtr`, `Entity_IsModelIdB22toB31`, `CXiSkeletonActor::DrawNameIfVisible`, `CXiSkeletonActor::DrawName2IfVisible`, `sub_101CC4F0`, `_sprintf` ×2
- **Indirect calls:** 7, of which 7 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `byte_1047D694`, `byte_1047D695`, `XiControlActor_isFirstPersonView`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_OnDrawName` (not stated)
- **DancingMad note:** PS2 slot 81 -> PC 161. HIGH: calls vslot 158 (GetNamePos) through its own vtable, as the PS2 body calls GetNamePos (vtbl+0x140).

### `0x100D06F0` CXiSkeletonActor::GetArrowPos

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetArrowPos(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100D06F2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_GetArrowPos` (not stated)
- **DancingMad note:** PS2 slot 100 -> PC 159 (order settled). GetElem then vslot 160 (screen projection) -- PS2 GetArrowPos = NameCalc + YmDB::Translate3Dto2D.

### `0x100D0740` CXiSkeletonActor::ProjectToScreen

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char __stdcall CXiSkeletonActor::ProjectToScreen(int a1, int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 12` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CDx::SetTransform` ×4, `CDx::GetTransformCached` ×2, `Camera_GetViewMatrixPtr`, `Vec4_Set`, `Gfx_ProjectWorldToClip`, `Gfx_NdcToScreen`, `fn_10027990` ×3, `fn_100279A0` ×6, `Mat4_SetIdentity`, `Mat4_SetTranslation`
- **Reads constants** (.rdata): 1
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_ProjectToScreen` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, PC-only virtual (slot 160, ret 0xC). Builds view/projection via CDx_GetTransformCached/SetTransform and projects a point -- the PC counterpart of PS2 YmDB::Translate3Dto2D, promoted to a vtable slot.

### `0x100D0880` CXiSkeletonActor::DrawNameIfVisible

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void __thiscall CXiSkeletonActor::DrawNameIfVisible(void * self, undefined4 * param_1, char * param_2, float param_3, uint32_t param_4, uint32_t param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x100D0880 cmp word ptr [ecx + 0xb2], 0` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Actor_DrawWorldText`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Calls Actor_DrawWorldText(a2..a6) unless the actor's u16 at +0xB2 is nonzero.

### `0x100D08B0` CXiSkeletonActor::DrawName2IfVisible

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void __thiscall CXiSkeletonActor::DrawName2IfVisible(void * self, undefined4 * param_1, char * param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x100D08B0 cmp word ptr [ecx + 0xb2], 0` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `DrawNameplateSecondString`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Calls sub_10086900(a2,a3,a4), the 3-argument text-draw variant, unless the actor's u16 at +0xB2 is nonzero.

### `0x100D08E0` CXiSkeletonActor::GetWidthScale

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `double CXiSkeletonActor::GetWidthScale()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); float result equal at its declared precision (the original returns ST0 unrounded); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D08E2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyModel::GetField44Addr`, `fn_10035250`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetWidthScale` (not stated)
- **DancingMad note:** PS2 slot 34 -> PC slot 38.

### `0x100D09B0` CXiSkeletonActor::GetHeightScale

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `double CXiSkeletonActor::GetHeightScale()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); float result equal at its declared precision (the original returns ST0 unrounded); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D09B2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyModel::GetField44Addr`, `fn_10035250`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_GetHeightScale` (not stated)
- **DancingMad note:** PS2 slot 35 -> PC slot 39.

### `0x100D0A80` CXiSkeletonActor::GetDepthScale

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `double CXiSkeletonActor::GetDepthScale()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); float result equal at its declared precision (the original returns ST0 unrounded); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D0A82 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyModel::GetField44Addr`, `fn_10035250`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 4, of which 4 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetDepthScale` (not stated)
- **DancingMad note:** PS2 slot 36 -> PC slot 40.

### `0x100D0D40` fn_100D0D40

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API undefined4 __thiscall fn_100D0D40(void * self_, int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100D0D45 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10085010`, `sub_100CF750`
- **Run by a frame** (frame_set.json): static, stack

### `0x100D12D0` CXiSkeletonActor::IsReadCompleteBody

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `bool CXiSkeletonActor::IsReadCompleteBody()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 91 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 91, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D12D5 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `List_GetTail`, `ResourceHandle_IsResident` ×3, `CXiActor::GetModelByteEE`, `CXiActor::GetModelPartWord`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_IsReadCompleteBody` (not stated)
- **DancingMad note:** IsReadComplete with PS2 IsReadCompleteResList inlined: false if +0x8A4 set; every handle in the resource list at +0x7E4, the model (vslot 119) and vslot 256 must be resident.

### `0x100D2F40` CXiSkeletonActor::OnSkeletonLoaded

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char __cdecl CXiSkeletonActor::OnSkeletonLoaded(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CXiSkeletonActor::LoadSkeletonSync`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiSkeletonActor_OnSkeletonLoaded` (not stated)
- **DancingMad note:** Completion callback passed to CXiSkeletonActorRes_Constructor by CXiSkeletonActor_LoadSkeletonResource (stored at task+0x38). Name from role; body not analyzed.

### `0x100D2F60` CXiSkeletonActor::LoadSkeletonSync

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::LoadSkeletonSync(int arg0)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 98 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 98, town PASS 93, town2 PASS 96, combat PASS 98, zonetoinn PASS 92
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D2F67 mov edi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10017D30` ×9, `ResourceHandle_IsResident` ×14, `fn_100710F0` ×8, `sub_10072FD0`, `fn_100730E0` ×13, `sub_100731B0`, `ActorHandle_Constructor` ×14, `sub_100814F0` ×14, `fn_10083340`, `CXiActor::GetModelByteEE`, `CXiActor::GetModelByteEF` ×6, `CXiActor::GetModelPartWord` ×8, `fn_10084670`, `fn_10084690`, `CXiActor::GetModelByte1DB` ×2, `fn_100C51C0` ×7, `sub_100D0B50` ×5, `fn_100D0D40` ×3, `sub_100D0D70` ×3, `sub_100D1190`, `fn_100D43E0`, `fn_100FD3A0`, `Allocator_Generic` ×14
- **Indirect calls:** 23, of which 20 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pMeshResourceMng`, `g_pXiZone`
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `CXiSkeletonActor_LoadSkeletonSync` (not stated)
- **DancingMad note:** Synchronous skeleton-load path taken by CXiSkeletonActor_LoadSkeletonResource for special-case actors (vtable slot 193 true, or +0x70 sub-object flag 0x80/0x100), and as the fallback if task allocation fails.

### `0x100D4330` CXiSkeletonActor::LoadSkeletonResource

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::LoadSkeletonResource(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D4332 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `Mem_AllocFromArea`, `CMoTask::ResetFields`, `CXiSkeletonActor::LoadSkeletonSync` ×2, `CXiSkeletonActorRes::Constructor`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Writes globals:** `g_resourcesDirty`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiSkeletonActor_LoadSkeletonResource` (not stated)
- **DancingMad note:** Decides synchronous vs. asynchronous skeleton load: if the actor is a special case (vtable slot 193 true, or its +0x70 sub-object has flag 0x80 or 0x100) loads synchronously; otherwise allocates a 72-byte task, constructs it via CXiSkeletonActorRes_Constructor with callback sub_100D2F40, and stores it at actor+0xA08.

### `0x100D43E0` fn_100D43E0

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API int __cdecl fn_100D43E0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10087830`
- **Run by a frame** (frame_set.json): static

### `0x100D4410` fn_100D4410

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API int __thiscall fn_100D4410(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100D4414 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_1001B710`, `sub_1002C7E0`, `Mem_AllocDefault`
- **Run by a frame** (frame_set.json): stack

### `0x100D4540` fn_100D4540

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API int __thiscall fn_100D4540(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D4540 mov eax, dword ptr [ecx + 0x7e4]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100D4560` CXiSkeletonActor::GetElem

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetElem(unsigned int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 95, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100D456A mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Actor_LookupByteField1C`, `Vec4_Set`, `Vec4_Copy`, `CXiSkeletonActor::GetElemThunk`, `CXiSkeletonActor::GetModelElem`, `CXiActor_ModelTest95790`, `CXiActor_ModelTest95680`, `CXiActor_ModelTest956A0`, `CXiActor::GetModelField170` ×3, `CXiActor::GetModelByteEF` ×3, `CXiActor::GetModelByte1DB`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 7, of which 7 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_GetElem` (high)
- **DancingMad note:** PS2 slot 60 -> PC 113 (EID_INDEX, float*). Position, arity and size order match; medium-high confidence.

### `0x100D4800` CXiSkeletonActor::GetElemLocal

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetElemLocal(unsigned int a2, int a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100D480A mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec4_Set`, `Vec4_Copy`, `fn_100270A0`, `CXiSkeletonActor::GetElemThunk`, `CXiSkeletonActor::GetModelElem` ×2, `CXiActor_ModelTest95790`, `CXiActor_ModelTest95680`, `CXiActor_ModelTest956A0`, `CXiActor::GetModelField170` ×3
- **Reads constants** (.rdata): 1
- **Indirect calls:** 7, of which 7 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiSkeletonActor_GetElemLocal` (high)
- **DancingMad note:** PS2 slot 61 -> PC 114 (EID_INDEX, float*). Medium-high confidence.

### `0x100D49B0` CXiSkeletonActor::GetEidMatrix

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::GetEidMatrix(int a2, _DWORD *a3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100D49BC add ecx, 0x674` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CXiSkeletonActor_GetModelEidMatrix`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetEidMatrix` (medium)
- **DancingMad note:** PS2 slot 62 -> PC 115 (EID_INDEX, matrix*); forwards to the model sub-object at +0x674. Medium confidence.

### `0x100D5430` fn_100D5430

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API void __thiscall fn_100D5430(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D5430 mov eax, dword ptr [ecx + 0x840]` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x100D5460` CXiSkeletonActor::IsDirectionLock_Set

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char CXiSkeletonActor::IsDirectionLock_Set(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D547C mov eax, dword ptr [ecx + 0x838]` (ecx_use.json); entry EDX never read (edx_use.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_IsDirectionLock_Set` (not stated)
- **DancingMad note:** PS2 IsDirectionLock(char) -> PC 197. HIGH: same inc/dec counter shape as PS2 (+0x3D0 -> PC +0x838). Previously GetCheckedField838.

### `0x100D6240` fn_100D6240

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `XI_API uint32_t __thiscall fn_100D6240(void * self_, int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 46 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100D6254 add ecx, 0x674` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CYyModelBase::GetPartList`, `CYyModel::GetField44Addr`, `fn_1002C710`, `fn_1002C750`
- **Run by a frame** (frame_set.json): static

### `0x100D62C0` CXiSkeletonActor::DrawResourceShadows

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char * CXiSkeletonActor::DrawResourceShadows()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 46 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 46, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D62C2 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CYyModelBase::GetPartList`, `CYyModel::GetField44Addr`, `ResourceHandle_IsResident` ×2, `CXiActor::SpawnResourceGenerators` ×2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_DrawResourceShadows` (author-inferred)
- **DancingMad note:** AUTHOR-INFERRED, PC slot 194: for each resident resource of the model sub-object (+0x674), draws it through the actor shadow/decal routine 0x10085060 (DrawIndexedPrimitiveUP).

### `0x100D6370` CXiSkeletonActor::KillAllGenerater

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::KillAllGenerater()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100D6371 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `CMoGeneratorClone_Kill` ×2, `CMoResource::ReleaseChain` ×2, `CXiActor_KillGeneratorClones`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_KillAllGenerater` (not stated)
- **DancingMad note:** PS2 slot 13 -> PC slot 18. Releases the two generator sub-objects. PS2's own spelling, kept as-is.

### `0x100D6F90` CXiSkeletonActor::vf033

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf033()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100D6FA0` CXiSkeletonActor::vf034

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf034()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100D6FB0` CXiSkeletonActor::vf035

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf035(int a1, int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 8` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100D6FC0` CXiSkeletonActor::vf036

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf036(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100D6FD0` CXiSkeletonActor::vf037

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `void CXiSkeletonActor::vf037()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100D7140` CXiSkeletonActor::GetRuntimeClass_variant2

- **Verified C++** (`tree/src/CXiSkeletonActor.cpp`): `char ** __cdecl CXiSkeletonActor::GetRuntimeClass_variant2()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetRuntimeClass_variant2` (not stated)
- **DancingMad note:** SHARED accessor (x3) -- do not assume this specific stub identifies a specific subclass instance
