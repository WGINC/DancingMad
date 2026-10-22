# unit_10019A50_MotionQueue

### `0x10019A50` MotionQueue_ApplyPolicy

- **Verified C++** (`tree/src/unit_10019A50_MotionQueue.cpp`): `XI_API void __thiscall MotionQueue_ApplyPolicy(void * self_, undefined4 param_1, undefined4 param_2, float param_3, undefined4 param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 74 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10019A5E mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SampleAnimationTrack_ToBuffer`, `SampleAnimationTrack_Live`
- **Reads constants** (.rdata): 1
- **Reads globals:** `g_pBoneMotionMask`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `MotionQueue_ApplyPolicy` (not stated)
- **DancingMad note:** Iterates a motion queue array; for each slot, checks a global compatibility table (g_motionCompatibilityTable) for a 'locked' bit and a category value to decide between an immediate-override path and a queue-if-allowed path. Not traced into either sub-function.

### `0x10019B30` SampleAnimationTrack_ToBuffer

- **Verified C++** (`tree/src/unit_10019A50_MotionQueue.cpp`): `XI_API undefined4 __thiscall SampleAnimationTrack_ToBuffer(void * self_, int param_1, int * param_2, int param_3, float param_4, int param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 99 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x10019B3B mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10032A40` ×2, `fn_10032A70` ×4, `Quat_NLerp`, `sub_10311C2C`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `SampleAnimationTrack_ToBuffer` (confirmed)
- **DancingMad note:** Confirmed by full read (was a placeholder): near-identical keyframe-sampling shape to SampleAnimationTrack_Live (same frame/fraction split, same track stride, same Quat_NLerp calls), but writes its result into a caller-supplied staging buffer rather than the live pose, and returns a success/failure bool -- consistent with 'sample the new motion into a buffer to validate before committing it,' as opposed to the Live variant's direct application. Called by MotionQueue_ApplyPolicy when a queue slot's category value is 1; on success, sets a bit back into g_motionCompatibilityTable.

### `0x10019EE0` SampleAnimationTrack_Live

- **Verified C++** (`tree/src/unit_10019A50_MotionQueue.cpp`): `XI_API undefined4 __thiscall SampleAnimationTrack_Live(void * self_, int param_1, int * param_2, int param_3, float param_4, float param_5, int param_6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 91 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x10019EEB mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `fn_10032A40` ×2, `fn_10032A70` ×7, `Quat_NLerp` ×3, `sub_10311C2C`
- **Reads constants** (.rdata): 2
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `SampleAnimationTrack_Live` (confirmed)
- **DancingMad note:** Confirmed by full read (was a placeholder): splits the input time into an integer frame index and fractional blend weight, walks a per-slot keyframe track (stride 21 dwords, offset +0x3E), and calls Quat_NLerp four times to interpolate a rotation quaternion between the two surrounding keyframes -- plus a separate linear blend of a position/scale channel using the recurring 0x1032961C/0x103295D8 constants. Writes directly into the live per-bone fields. Called by MotionQueue_ApplyPolicy when a queue slot's category value is 0.

### `0x1001A3E0` fn_1001A3E0

- **Verified C++** (`tree/src/unit_10019A50_MotionQueue.cpp`): `XI_API void __thiscall fn_1001A3E0(void * self_, undefined4 param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1001A3EC lea edi, [ecx + 0x78]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1001AC40`, `fn_1001B1F0`, `fn_1001B2E0`
- **Run by a frame** (frame_set.json): self, stack

### `0x1001A420` MotionQueue_UpdateAllChannels

- **Verified C++** (`tree/src/unit_10019A50_MotionQueue.cpp`): `XI_API undefined4 __thiscall MotionQueue_UpdateAllChannels(void * self_, undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 34 trials, 19 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1001A42A mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CYyMotionQue::SampleInto` ×2, `CYyMotionQue_IsActive`, `Vec3_Copy` ×2, `Vec3_Lerp` ×2, `fn_10032A40`, `fn_10032A70`, `Quat_NLerp`, `_atexit`
- **Reads globals:** `0x10456D28`, `0x10456D2C`, `0x10456D30`, `0x10456D34`, `0x10456D38`, `g_pBoneMotionMask`, `g_poseScratchBoneCount`
- **Writes globals:** `0x10456D28`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `MotionQueue_UpdateAllChannels` (not stated)
- **DancingMad note:** Per-frame animation sampling for one actor: (1) reset every bone in g_poseScratch to default rotation/zero translation/unit scale; (2) sample the 5 base motion slots (this+0x00..+0x50, stride 0x14, applied 4 -> 0 so slot 0 wins) straight into g_poseScratch, marking touched bones in g_pBoneMotionMask (|0x40); (3) for the 2 blend slots (+0x64, +0x78), sample into g_poseBlendScratch and blend by the slot weight into bones whose mask has bit 7 and a nonzero category: Quat_NLerp for rotation, Vec3_Lerp for translation and scale. The call after NLerp (0x10032A70) is an empty ret, so blended quaternions are not renormalised.

### `0x1001A6E0` fn_1001A6E0

- **Verified C++** (`tree/src/unit_10019A50_MotionQueue.cpp`): `XI_API void __thiscall fn_1001A6E0(void * self_, int * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5, undefined4 param_6, undefined4 param_7, int param_8, undefined4 param_9, undefined4 param_10)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 42 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 40` (purges.json); entry ECX read: `0x1001A6E7 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_1001AD00`, `sub_10084620`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): stack
