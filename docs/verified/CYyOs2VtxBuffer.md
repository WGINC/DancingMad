# CYyOs2VtxBuffer

### `0x1002CCB0` CYyOs2VtxBuffer::CreateBuffersStep

- **Verified C++** (`tree/src/CYyOs2VtxBuffer.cpp`): `char CYyOs2VtxBuffer::CreateBuffersStep(int a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 90 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 90, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1002CCB2 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_AllocObject`, `Mem_FreeObject`, `CYyVbMng::AcquireVertexBuffer`, `CYyVbMng_ReleaseVertexBuffer`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pVbMng`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Incremental state machine (state at this+60) that allocates a 0xFFFF-filled index shadow, creates a D3D INDEX16 index buffer, then acquires a pooled vertex buffer; on failure frees everything. Returns 1 when finished.

### `0x1002D680` CYyOs2VtxBuffer::Constructor

- **Verified C++** (`tree/src/CYyOs2VtxBuffer.cpp`): `int CYyOs2VtxBuffer::Constructor(_DWORD **a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1002D682 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_10071F50`, `CMoTask_Constructor`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Calls base ctor, stores CYyOs2VtxBuffer_vtbl, zeroes buffer fields and creates the vertex shader from g_vsDecl_1628.

### `0x1002D700` CYyOs2VtxBuffer::CYyOs2VtxBuffer_Destructor

- **Verified C++** (`tree/src/CYyOs2VtxBuffer.cpp`): `char CYyOs2VtxBuffer::CYyOs2VtxBuffer_Destructor()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 158 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 99, town2 PASS 99, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 0 through its tail jump to 0x100747C0 (tail_purges.json); entry ECX read: `0x1002D702 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `Mem_FreeObject` ×4, `CYyVbMng_ReleaseVertexBuffer`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pVbMng`
- **Run by a frame** (frame_set.json): stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Restores the vtable, frees the index shadow, releases the index buffer and pooled VB, deletes the vertex shader, frees other heap blocks, removes itself from a 16-slot global table and calls the base dtor.
