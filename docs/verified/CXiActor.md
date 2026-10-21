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
