# CXiControlActor

### `0x100A45D0` CXiControlActor_GetGroundMaterial

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API undefined4 __thiscall CXiControlActor_GetGroundMaterial(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A45D0 mov eax, dword ptr [ecx + 0x174]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiControlActor_GetGroundMaterial` (not stated)
- **DancingMad note:** PC slot 134, reads +0x174.

### `0x100A4640` CXiControlActor::AmIControlActor

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `unsigned char __thiscall CXiControlActor::AmIControlActor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4641 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `ActorHandle_Resolve`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiControlActor_AmIControlActor` (not stated)
- **DancingMad note:** PS2 slot 97 -> PC 193. Same shape against singleton 0x1047D600.

### `0x100A4670` CXiControlActor_IsFreeRun

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API undefined1 __thiscall CXiControlActor_IsFreeRun(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4670 mov al, byte ptr [ecx + 0xf9]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiControlActor_IsFreeRun` (not stated)
- **DancingMad note:** PS2 IsFreeRun() byte +0xD5 -> PC 204 byte +0xF9 (+0x24 shift, same as IsControlLock). HIGH.

### `0x100A4690` CXiControlActor_IsWalkLock

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API undefined1 __thiscall CXiControlActor_IsWalkLock(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4690 mov al, byte ptr [ecx + 0xfa]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiControlActor_IsWalkLock` (not stated)
- **DancingMad note:** PS2 IsWalkLock() byte +0xD6 -> PC 206 byte +0xFA. HIGH.

### `0x100A46B0` CXiControlActor_IsParallelMove

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API undefined1 __thiscall CXiControlActor_IsParallelMove(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A46B0 mov al, byte ptr [ecx + 0xfb]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiControlActor_IsParallelMove` (not stated)
- **DancingMad note:** PS2 IsParallelMove() byte +0xD7 -> PC 208 byte +0xFB. HIGH.

### `0x100A46C0` CXiControlActor_IsControlLock

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API undefined4 __thiscall CXiControlActor_IsControlLock(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A46C0 mov eax, dword ptr [ecx + 0xfc]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiControlActor_IsControlLock` (not stated)
- **DancingMad note:** PS2 IsControlLock() -> PC 196: returns counter +0xFC.

### `0x100A5770` fn_100A5770

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API void __thiscall fn_100A5770(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A5776 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec3_Copy`
- **Run by a frame** (frame_set.json): static

### `0x100A57C0` fn_100A57C0

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API undefined4 __thiscall fn_100A57C0(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100A57C6 mov dword ptr [ecx + 0xd4], edx` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self

### `0x100A89E0` fn_100A89E0

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API void * __thiscall fn_100A89E0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A89E3 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `ActorHandle_Constructor`, `sub_100814F0`, `ActorHandle_Resolve`, `fn_10081CF0`, `fn_100A5770`, `Actor_SetSlotTableEntry` ×2
- **Reads globals:** `0x1035BC0C`, `0x1035BC10`, `0x1035BC14`, `0x1035BC18`, `0x1035BC1C`, `0x1035BC20`, `0x1035BC24`, `0x1035BC28`, `0x1035BC2C`, `0x1035BC30`, `0x1035BC34`, `0x1035BC38`, `g_pTargetMng`
- **Run by a frame** (frame_set.json): static

### `0x100AAEF0` fn_100AAEF0

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `XI_API long double __stdcall fn_100AAEF0(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads constants** (.rdata): 1
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack

### `0x100AAF50` CXiControlActor::Slot137_Set388

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `void __thiscall CXiControlActor::Slot137_Set388(void * self, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100AAF54 lea edx, [ecx + 0x388]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_100AAFB0`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiControlActor_Slot137_Set388` (not stated)
- **DancingMad note:** RENAMED 2026-09-26: an earlier session named this SetIsChocobo; the real IsChocobo pair is 0x100827A0/0x10082790 (SUBACTOR_STATUS at +0xA4). This forwards its arg to 0x100AAFB0 with this+0x388. Purpose unknown.

### `0x100AAF70` CXiControlActor::Slot138_Scan3F0

- **Verified C++** (`tree/src/CXiControlActor.cpp`): `void __thiscall CXiControlActor::Slot138_Scan3F0(void * self, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100AAF72 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_100AAFB0`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiControlActor_Slot138_Scan3F0` (not stated)
- **DancingMad note:** RENAMED 2026-09-26 (was IsChocobo, wrong -- see 0x100827A0). Scans 4 entries at +0x3F0 against the arg. Purpose unknown.
