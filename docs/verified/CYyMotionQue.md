# CYyMotionQue

### `0x1001A660` CYyMotionQue::SetSlotMotion

- **Verified C++** (`tree/src/CYyMotionQue.cpp`): `void __thiscall CYyMotionQue::SetSlotMotion(void * self, int * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6, undefined4 param_7, int param_8, undefined4 param_9, undefined4 param_10)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 42 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 40` (purges.json); entry ECX read: `0x1001A667 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_1001ACB0`, `sub_10084620`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, medium confidence; docs/NAMES.md in ffximain-gfx): Sets motion slot a9 (0-6, 5 dwords each) of a motion queue for an actor, skipping it when the actor rejects motion, and notifies the actor for slot 0.

### `0x1001A850` CYyMotionQue_GetResource

- **Verified C++** (`tree/src/CYyMotionQue.cpp`): `XI_API void __thiscall CYyMotionQue_GetResource(void * self_, undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1001A854 mov ecx, dword ptr [ecx + 0x34]` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
- **DancingMad name:** `CYyMotionQue_GetResource` (not stated)
- **DancingMad note:** Getter (via out-param) for +0x34.

### `0x1001A8E0` CYyMotionQue::ComputeFrameAdvance

- **Verified C++** (`tree/src/CYyMotionQue.cpp`): `void __thiscall CYyMotionQue::ComputeFrameAdvance(void * self, int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 86 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1001A8E4 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Camera_GetFrameScale`, `sub_1001B590` ×2, `ResourceHandle_IsResident`, `ResourceHandle_Deref` ×3
- **Reads constants** (.rdata): 4
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CYyMotionQue_ComputeFrameAdvance` (not stated)
- **DancingMad note:** Resolves the motion resource via g_pMeshResourceMng, reads a signed 16-bit frame count, clamps current time against it (NaN-safe compare vs g_timeThresholdConstant2 at 0x103295D8 -- note this is the SAME recurring constant as CTsZoneMap and CMoLfdElem use elsewhere), scales by the +0x28 speed field.

### `0x1001AB60` CYyMotionQue::StartMotion

- **Verified C++** (`tree/src/CYyMotionQue.cpp`): `void __thiscall CYyMotionQue::StartMotion(void * self, int param_1, undefined4 param_2, undefined4 param_3, int param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1001AB63 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `MotionQueue_ApplyPolicy`, `ResourceHandle_IsResident`, `ResourceHandle_Deref`
- **Reads globals:** `g_pMeshResourceMng`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CYyMotionQue_StartMotion` (not stated)
- **DancingMad note:** Defaults a blend weight to 1.0 under specific conditions, resolves the motion resource, calls MotionQueue_ApplyPolicy -- the actual 'begin a new motion transition' entry point.

### `0x1001B230` CYyMotionQue::SampleInto

- **Verified C++** (`tree/src/CYyMotionQue.cpp`): `undefined4 __thiscall CYyMotionQue::SampleInto(void * self, int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 87 returned normally, 268 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1001B232 mov edi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Reads constants** (.rdata): 1
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CYyMotionQue_SampleInto` (not stated)
- **DancingMad note:** Samples one motion-queue slot into a 52-byte-per-bone pose buffer (args: layer index, buffer). Medium.

### `0x1001B2E0` fn_1001B2E0

- **Verified C++** (`tree/src/CYyMotionQue.cpp`): `XI_API void __thiscall fn_1001B2E0(void * self_, int * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 96 returned normally, 157 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x1001B2E1 mov ebp, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1001B0F0`, `fn_1001B5D0`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
