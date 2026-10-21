# CMoProcessor

### `0x1006CE70` CMoProcessor::InitRotationMatrices

- **Verified C++** (`tree/src/CMoProcessor.cpp`): `_DWORD * CMoProcessor::InitRotationMatrices()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1006CE71 mov ebx, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `_atexit`
- **Reads globals:** `CMoProcessor_InitRotationMatrices_staticGuard`
- **Writes globals:** `g_identityMatrix_1047CC80_m00`, `g_identityMatrix_1047CC80_m01`, `g_identityMatrix_1047CC80_m02`, `g_identityMatrix_1047CC80_m03`, `g_identityMatrix_1047CC80_m10`, `g_identityMatrix_1047CC80_m11`, `g_identityMatrix_1047CC80_m12`, `g_identityMatrix_1047CC80_m13`, `g_identityMatrix_1047CC80_m20`, `g_identityMatrix_1047CC80_m21`, `g_identityMatrix_1047CC80_m22`, `g_identityMatrix_1047CC80_m23`, `g_identityMatrix_1047CC80_m30`, `g_identityMatrix_1047CC80_m31`, `g_identityMatrix_1047CC80_m32`, `g_identityMatrix_1047CC80_m33`, `CMoProcessor_InitRotationMatrices_staticGuard`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CMoProcessor_InitRotationMatrices` (not stated)
- **DancingMad note:** Part of the tiered-factory constructor chain: builds a global 4x4 identity matrix (lazy-init, own flag/buffer per call site) and copies it into the four RotationMatrix[0..3] slots, then tail-jumps into Pool_InitSlots.

### `0x1006E6B0` CMoProcessor::ScratchMatrixOp

- **Verified C++** (`tree/src/CMoProcessor.cpp`): `int CMoProcessor::ScratchMatrixOp(int a2, int a3, int a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 200 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 50, town2 PASS 50, combat PASS 50, zonetoinn PASS 50
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1006E6B6 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pProcessor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoProcessor_ScratchMatrixOp` (confirmed)
- **DancingMad note:** CORRECTED from an earlier name (Pool_AllocSlot) that undersold what this does. Full decompilation shows a self-contained operation, not a standalone allocator: borrows a scratch slot from the 32-slot pool (+0xA90 counter, +0xA10 array), calls a setup virtual method (offset 0x5C), calls Mat4x4_Multiply (offset 0x24) with the borrowed slot, then returns the slot to the pool before returning. STRUCTURAL RACE CONDITION: the counter/array read-modify-write is plain mov/inc/dec, zero synchronization (no lock prefix, no mutex). Reachability from multiple threads not confirmed either way -- this codebase is confirmed NOT naively single-threaded elsewhere (sqmoChannelBuildSQO uses a real mutex, see the dancer middleware document), so this is a genuine open question, not purely theoretical.

### `0x1006E970` CMoProcessor::CalcScreenBounds

- **Verified C++** (`tree/src/CMoProcessor.cpp`): `CMoProcessor * __stdcall CMoProcessor::CalcScreenBounds(float *a1, float *a2, int a3, int a4, const void *a5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 56 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 56, town PASS 55, town2 PASS 55, combat PASS 54, zonetoinn PASS 55
- **Convention facts:** `ret 20` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads constants** (.rdata): 3
- **Reads globals:** `g_pResourceMng`, `g_pProcessor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Computes the screen-space bounding rectangle of a strided point array under a matrix and the current view-projection.
