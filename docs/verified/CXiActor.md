# CXiActor

### `0x10082070` CXiActor::CXiSkeletonActor_GetMoveSpeed

- **Verified C++** (`tree/src/CXiActor.cpp`): `double CXiActor::CXiSkeletonActor_GetMoveSpeed()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10082070 fld dword ptr [ecx + 0x98]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetMoveSpeed` (not stated)
- **DancingMad note:** PS2 slot 51 -> PC slot 104. Part of a fully-verified 9-slot band (104-112); reads +0x98.

### `0x10082080` CXiActor::CXiSkeletonActor_SetMoveSpeed

- **Verified C++** (`tree/src/CXiActor.cpp`): `void CXiActor::CXiSkeletonActor_SetMoveSpeed(float speed)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10082084 mov dword ptr [ecx + 0x98], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiSkeletonActor_SetMoveSpeed` (not stated)
- **DancingMad note:** PS2 slot 52 -> PC slot 105. Writes +0x98, the same field slot 104 reads.

### `0x10082090` CXiActor::CXiSkeletonActor_GetMoveSpeedBase

- **Verified C++** (`tree/src/CXiActor.cpp`): `float CXiActor::CXiSkeletonActor_GetMoveSpeedBase()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10082090 fld dword ptr [ecx + 0x94]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetMoveSpeedBase` (not stated)
- **DancingMad note:** PS2 slot 53 -> PC slot 106. Reads +0x94, distinct from MoveSpeed's own field.

### `0x100820A0` CXiActor::CXiSkeletonActor_SetMoveSpeedBase

- **Verified C++** (`tree/src/CXiActor.cpp`): `void CXiActor::CXiSkeletonActor_SetMoveSpeedBase(float speed)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100820A4 mov dword ptr [ecx + 0x94], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiSkeletonActor_SetMoveSpeedBase` (not stated)
- **DancingMad note:** PS2 slot 54 -> PC slot 107. Writes +0x94.

### `0x100820B0` CXiActor::CXiSkeletonActor_GetWalkSpeed

- **Verified C++** (`tree/src/CXiActor.cpp`): `double CXiActor::CXiSkeletonActor_GetWalkSpeed()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100820B0 fld dword ptr [ecx + 0x98]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetWalkSpeed` (confirmed)
- **DancingMad note:** PS2 slot 55 -> PC slot 108. Confirmed derived, not stored: reads GetMoveSpeed's own field (+0x98) and scales by a constant, exactly matching the real PS2 body -- WalkSpeed has no field of its own.

### `0x100820C0` CXiActor::CXiSkeletonActor_SetWalkSpeed

- **Verified C++** (`tree/src/CXiActor.cpp`): `void CXiActor::CXiSkeletonActor_SetWalkSpeed(float speed)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100820C4 mov dword ptr [ecx + 0x9c], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiSkeletonActor_SetWalkSpeed` (confirmed)
- **DancingMad note:** PS2 slot 56 -> PC slot 109. Writes +0x9C -- a field GetWalkSpeed never reads back from, matching a confirmed real asymmetry in the PS2 body (SetWalkSpeed writes a field its own getter ignores).

### `0x100820D0` CXiActor::CXiSkeletonActor_GetEquip

- **Verified C++** (`tree/src/CXiActor.cpp`): `int CXiActor::CXiSkeletonActor_GetEquip(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_GetEquip` (not stated)
- **DancingMad note:** PS2 slot 57 -> PC slot 110. As certain a match as this project has produced: both platforms' real bodies are just lui/ori-equivalent loads of the literal constant 0x74657374 (ASCII "test") returned unconditionally -- an identical hardcoded placeholder on both platforms.

### `0x100820E0` GetEmbeddedMember_0x34

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API int __thiscall GetEmbeddedMember_0x34(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100820E0 lea eax, [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `GetEmbeddedMember_0x34` (confirmed)
- **DancingMad note:** lea eax,[ecx+0x34]; ret. One of a family of six confirmed trivial accessors at consecutive small offsets (4, 8, 0x10, 0x14, 0x34, 0x44), most plausibly used by the large XiActor-family classes to expose several internal sub-components individually.

### `0x100820F0` GetEmbeddedMember_0x44

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API int __thiscall GetEmbeddedMember_0x44(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100820F0 lea eax, [ecx + 0x44]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `GetEmbeddedMember_0x44` (not stated)
- **DancingMad note:** lea eax,[ecx+0x44]; ret. Sibling of GetEmbeddedMember_0x34, same family.

### `0x10082200` CXiActor_GetModel

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API void __thiscall CXiActor_GetModel(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10082204 mov ecx, dword ptr [ecx + 0xb4]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiActor_GetModel` (not stated)
- **DancingMad note:** PS2 slot 65 -> PC 119. Returns the model handle at +0xB4 (= PS2 +0x8C + 0x28 XiActor shift). IsReadComplete calls this slot as the model.

### `0x10082380` CXiActor_GetFieldA8

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __thiscall CXiActor_GetFieldA8(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10082380 mov eax, dword ptr [ecx + 0xa8]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiActor_GetFieldA8` (not stated)
- **DancingMad note:** RENAMED 2026-09-26 (was IsFishingRod, wrong). Reads +0xA8.

### `0x10082790` CXiActor_SetSubActorStatus

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API void __thiscall CXiActor_SetSubActorStatus(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10082794 mov dword ptr [ecx + 0xa4], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CXiActor_SetSubActorStatus` (not stated)
- **DancingMad note:** PS2 IsChocobo(SUBACTOR_STATUS) -- despite the name, a setter of +0x80 on PS2 -> PC 212, setter of +0xA4. HIGH.

### `0x100827A0` CXiActor::IsChocobo

- **Verified C++** (`tree/src/CXiActor.cpp`): `undefined4 __thiscall CXiActor::IsChocobo(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100827A0 mov eax, dword ptr [ecx + 0xa4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiActor_IsChocobo` (not stated)
- **DancingMad note:** PS2 XiActor::IsChocobo() -> PC 211. HIGH: +0xA4 in [1,4], PS2 +0x80 > 0 && < 5.

### `0x100827F0` fn_100827F0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __thiscall fn_100827F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100827F0 mov eax, dword ptr [ecx + 0xa4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x10082860` fn_10082860

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __thiscall fn_10082860(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10082860 mov eax, dword ptr [ecx + 0xa4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100828B0` fn_100828B0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __thiscall fn_100828B0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100828B0 mov eax, dword ptr [ecx + 0xa4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x10082900` fn_10082900

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __thiscall fn_10082900(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10082900 mov eax, dword ptr [ecx + 0xa4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100832D0` CXiActor::CXiSkeletonActor_AddRef

- **Verified C++** (`tree/src/CXiActor.cpp`): `void CXiActor::CXiSkeletonActor_AddRef()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100832D0 inc dword ptr [ecx + 0x80]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_AddRef` (candidate)
- **DancingMad note:** PS2 slot 38 -> PC slot 88. Confirmed by elimination against every other simple inc/dec-shaped PS2 candidate.

### `0x10083390` CXiActor::CXiSkeletonActor_AddSchRef

- **Verified C++** (`tree/src/CXiActor.cpp`): `void CXiActor::CXiSkeletonActor_AddSchRef()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10083390 inc dword ptr [ecx + 0x84]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_AddSchRef` (not stated)
- **DancingMad note:** PS2 slot 42 -> PC slot 90. Exact shape match: both platforms unconditional, no guard, same field-touch pattern.

### `0x100833A0` CXiActor::CXiSkeletonActor_SubSchRef

- **Verified C++** (`tree/src/CXiActor.cpp`): `void CXiActor::CXiSkeletonActor_SubSchRef()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100833A0 dec dword ptr [ecx + 0x84]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CXiSkeletonActor_SubSchRef` (not stated)
- **DancingMad note:** PS2 slot 43 -> PC slot 91. Exact shape match, same basis as AddSchRef.

### `0x10083750` fn_10083750

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API int * __cdecl fn_10083750(float * param_1, uint32_t param_2, uint32_t param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 98 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetViewMatrixPtr`, `Camera_GetField50` ×2, `Camera_GetMatrix154Ptr`, `Vec3_Copy`, `fn_10027990`, `fn_100279A0`, `Mat4_Copy`, `Mat4_PostMultiply`, `fn_10083430`, `sub_10085240`, `sub_10085270`, `fn_101CC510`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self, stack

### `0x10083B40` fn_10083B40

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API int * __cdecl fn_10083B40(int * param_1, uint32_t param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 97 returned normally, 192 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetViewMatrixPtr`, `fn_100152C0` ×2, `sub_10027600`, `fn_10027990`, `fn_100279A0`, `Mat4_Copy`, `fn_10028230` ×2, `fn_10083430`, `sub_10085240`, `sub_10085270`, `fn_101CC510`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x10083D00` fn_10083D00

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API int * __cdecl fn_10083D00(int * param_1, uint32_t param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 97 returned normally, 192 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetViewMatrixPtr`, `fn_100152C0` ×2, `sub_10027600`, `fn_10027990`, `fn_100279A0`, `Mat4_Copy`, `fn_10028230` ×2, `fn_10083430`, `sub_10085240`, `sub_10085270`, `fn_101CC510`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x10083EC0` fn_10083EC0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __cdecl fn_10083EC0(undefined4 param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10083F20`
- **Run by a frame** (frame_set.json): static

### `0x10083EE0` fn_10083EE0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __cdecl fn_10083EE0(uint32_t param_1, uint32_t param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10083F20`
- **Run by a frame** (frame_set.json): static

### `0x10083F00` fn_10083F00

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __cdecl fn_10083F00(uint32_t param_1, uint32_t param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10083F20`
- **Run by a frame** (frame_set.json): static

### `0x10083F20` fn_10083F20

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API int * __cdecl fn_10083F20(uint32_t param_1, uint32_t param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 27 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10027530`, `fn_10027990`, `fn_100279A0`, `Mat4_SetIdentity`, `Mat4_PostRotateY`, `Mat4_SetRow3`, `fn_10028230`, `Mat4_InvertOrthonormal`, `ActorHandle_Resolve`, `fn_10082FA0` ×2, `fn_10083430`, `sub_10085240`, `sub_10085270`, `sub_1008E8D0`, `sub_101CC220`, `fn_101CC510`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 3, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x10084100` fn_10084100

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __cdecl fn_10084100(int param_1, int param_2, float param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `sub_100275D0`
- **Run by a frame** (frame_set.json): static, stack

### `0x10084140` CXiActor::IsModelMissingOrFlag2000

- **Verified C++** (`tree/src/CXiActor.cpp`): `uint32_t __thiscall CXiActor::IsModelMissingOrFlag2000(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084140 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns true when the actor has no model data at +0x70, or when that data's flags at +0x120 have bit 0x2000 set.

### `0x10084390` CXiActor::GetModelField170

- **Verified C++** (`tree/src/CXiActor.cpp`): `undefined4 __thiscall CXiActor::GetModelField170(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084390 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `0x1047D60C`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the dword at model+0x170, or the default dword_1047D60C when there is no model.

### `0x100843B0` CXiActor::HasNonzeroField150or158

- **Verified C++** (`tree/src/CXiActor.cpp`): `undefined4 __thiscall CXiActor::HasNonzeroField150or158(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100843B0 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns true when model(+0x70)->+0xD4->+0x260 has a nonzero float at +0x150 or +0x158.

### `0x10084400` CXiActor::GetModelByteEE

- **Verified C++** (`tree/src/CXiActor.cpp`): `int __thiscall CXiActor::GetModelByteEE(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084400 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1047D610`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the signed byte at model+0xEE, or the default dword_1047D610 when there is no model.

### `0x10084420` CXiActor::GetModelByteEF

- **Verified C++** (`tree/src/CXiActor.cpp`): `int __thiscall CXiActor::GetModelByteEF(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084421 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `0x1047D614`
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns a byte that comes from virtual +956 when virtual +948 says so, otherwise from model+0xEF, otherwise the default dword_1047D614.

### `0x10084480` CXiActor::GetModelPartWord

- **Verified C++** (`tree/src/CXiActor.cpp`): `uint32_t __thiscall CXiActor::GetModelPartWord(void * self, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10084481 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns the u16 part id for slot a2: from virtual +964 when virtual +948 says so, otherwise model+0xFC[a2], otherwise the default (a2<<12)\|table[a2].

### `0x10084500` CXiActor::GetModelFlags120Top2

- **Verified C++** (`tree/src/CXiActor.cpp`): `uint32_t __thiscall CXiActor::GetModelFlags120Top2(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084500 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns bits 30-31 of model+0x120, or 1 when there is no model.

### `0x10084520` CXiActor::GetModelFlags130Top2

- **Verified C++** (`tree/src/CXiActor.cpp`): `uint32_t __thiscall CXiActor::GetModelFlags130Top2(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084520 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns bits 30-31 of model+0x130, or 0 when there is no model.

### `0x10084540` CXiActor::GetModelFloat9AEC0

- **Verified C++** (`tree/src/CXiActor.cpp`): `long double __thiscall CXiActor::GetModelFloat9AEC0(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084540 mov ecx, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns sub_1009AEC0(model) as a double, or 0.0 when there is no model.

### `0x10084580` CXiActor::IsModelMissingOrSuppressed

- **Verified C++** (`tree/src/CXiActor.cpp`): `uint32_t __thiscall CXiActor::IsModelMissingOrSuppressed(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084580 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns true when there is no model, when actor byte +0x88 has bit 8 set, or when model+0x128 has bit 0x10 set.

### `0x10084640` CXiActor::TestModelFlags100000_200000_4000

- **Verified C++** (`tree/src/CXiActor.cpp`): `uint32_t __thiscall CXiActor::TestModelFlags100000_200000_4000(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084640 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Run by a frame** (frame_set.json): self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns true when model data exists and has flag 0x100000 or 0x200000 at +0x120, or flag 0x4000 at +0x128.

### `0x10084720` CXiActor::GetModelByte1DB

- **Verified C++** (`tree/src/CXiActor.cpp`): `undefined4 __thiscall CXiActor::GetModelByte1DB(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084720 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the unsigned byte at model+0x1DB, or 0 when there is no model.

### `0x100849A0` fn_100849A0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API long double __thiscall fn_100849A0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100849A0 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): self

### `0x10084BA0` fn_10084BA0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API uint32_t __thiscall fn_10084BA0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084BA0 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1047D631`
- **Run by a frame** (frame_set.json): self

### `0x10084BC0` fn_10084BC0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API undefined4 __thiscall fn_10084BC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10084BC0 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x10085010` fn_10085010

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API void __thiscall fn_10085010(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10085014 mov dword ptr [ecx + 0xb4], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10085060` CXiActor::SpawnResourceGenerators

- **Verified C++** (`tree/src/CXiActor.cpp`): `void __thiscall CXiActor::SpawnResourceGenerators(void * self, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 97 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10085067 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_10017D20`, `CMoGeneratorClone::CreateInstance`, `fn_10053A00`, `ResourceIter_FindFirst` ×2, `ResourceIter_FindNext` ×4
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static, stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Unless the actor is suppressed (vfunc+292 or flag +178&2), it walks the actor's type-5 resources. For each one of the listed kinds with flag 0x1000 at +216 it calls sub_10053A00, then collects up to 128 of them and creates a CMoGeneratorClone instance for each.

### `0x10085490` CXiActor::IsInModelSlotTable

- **Verified C++** (`tree/src/CXiActor.cpp`): `int __thiscall CXiActor::IsInModelSlotTable(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10085490 mov eax, dword ptr [ecx + 0x70]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Returns true when this actor pointer appears in any of the 12 actor slots at model+0xA4..+0xD0.

### `0x10085500` fn_10085500

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API uint32_t __thiscall fn_10085500(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10085500 mov eax, dword ptr [ecx + 0x88]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10085BF0` fn_10085BF0

- **Verified C++** (`tree/src/CXiActor.cpp`): `XI_API void __thiscall fn_10085BF0(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10085BF4 mov dword ptr [ecx + 0xbc], eax` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
