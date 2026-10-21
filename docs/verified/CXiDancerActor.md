# CXiDancerActor

### `0x100AB700` fn_100AB700

- **Verified C++** (`tree/src/CXiDancerActor.cpp`): `XI_API undefined4 __thiscall fn_100AB700(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, uint32_t param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100AB703 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_1008A120`, `fn_100AB750`, `CXiSkeletonActor::Constructor_1Arg`, `CXiSkeletonActor::LoadSkeletonResource`
- **Run by a frame** (frame_set.json): static

### `0x100AB750` fn_100AB750

- **Verified C++** (`tree/src/CXiDancerActor.cpp`): `XI_API void __thiscall fn_100AB750(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, uint32_t param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100AB7C4 mov dword ptr [ecx + 0x70], esi` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_100AB9A0`
- **Reads globals:** `0x10487FB4`
- **Writes globals:** `0x10487FB4`
- **Run by a frame** (frame_set.json): static

### `0x100AB830` fn_100AB830

- **Verified C++** (`tree/src/CXiDancerActor.cpp`): `XI_API void __thiscall fn_100AB830(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100AB831 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec4_Copy`, `fn_100929A0`
- **Run by a frame** (frame_set.json): static

### `0x100AB880` fn_100AB880

- **Verified C++** (`tree/src/CXiDancerActor.cpp`): `XI_API void __thiscall fn_100AB880(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100AB886 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec4_Copy`, `fn_100929A0`
- **Reads constants** (.rdata): 3
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x100AB9A0` fn_100AB9A0

- **Verified C++** (`tree/src/CXiDancerActor.cpp`): `XI_API void __thiscall fn_100AB9A0(void * self_, void * param_1, undefined4 param_2, undefined4 param_3, undefined4 * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x100AB9AF mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10093430`, `fn_100AB830`, `fn_100AB880`, `fn_100ABC70` ×2
- **Run by a frame** (frame_set.json): static
