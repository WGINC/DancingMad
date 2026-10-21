# CXiCollisionActor

### `0x100A46D0` CXiCollisionActor_IsTouchDown

- **Verified C++** (`tree/src/CXiCollisionActor.cpp`): `XI_API undefined1 __thiscall CXiCollisionActor_IsTouchDown(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A46D0 mov al, byte ptr [ecx + 0x5e0]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiCollisionActor_IsTouchDown` (not stated)
- **DancingMad note:** PS2 slot 47 -> PC 102. Reads IsTouch (+0x5E0), exactly as PS2's override reads +0x1C0. High.

### `0x100A46F0` CXiCollisionActor_IsOnLift

- **Verified C++** (`tree/src/CXiCollisionActor.cpp`): `XI_API undefined1 __thiscall CXiCollisionActor_IsOnLift(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A46F0 mov al, byte ptr [ecx + 0x5e2]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiCollisionActor_IsOnLift` (not stated)
- **DancingMad note:** PS2 slot 48 -> PC 103. Reads +0x5E2, the OnMove-computed lift state -- the role PS2's is_on_lift plays (PS2 OnMove writes it, IsOnLift reads it). PC inserted a separate input byte at +0x5E1. High.

### `0x100A4710` CXiCollisionActor_GetCurrentAreaId

- **Verified C++** (`tree/src/CXiCollisionActor.cpp`): `XI_API undefined4 __thiscall CXiCollisionActor_GetCurrentAreaId(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4710 mov eax, dword ptr [ecx + 0x5e4]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CXiCollisionActor_GetCurrentAreaId` (not stated)
- **DancingMad note:** PC-only virtual getter for current_area_id (+0x5E4). 12 virtual call sites.

### `0x100A4C20` CXiCollisionActor::Constructor

- **Verified C++** (`tree/src/CXiCollisionActor.cpp`): `void * __thiscall CXiCollisionActor::Constructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100A4C22 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Vec4_Set`, `fn_100A89E0`, `sub_103149A0` ×2
- **Run by a frame** (frame_set.json): static
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Builds the CXiControlActor base, stores the CXiCollisionActor vtable and initializes collision fields, including two random 0..119 timers and an orientation (0,-1,0,1) at +0x160.
