# CYyVbMng

### `0x1003B210` CYyVbMng::AcquireVertexBuffer

- **Verified C++** (`tree/src/CYyVbMng.cpp`): `int CYyVbMng::AcquireVertexBuffer(int a2, int a3, int a4, int a5, int *a6, char a7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 105 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 98, town2 PASS 99, combat PASS 99, zonetoinn PASS 99
- **Convention facts:** `ret 24` (purges.json); entry ECX read: `0x1003B218 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Mem_AllocDefault`, `CYyVb::Constructor`
- **Indirect calls:** 2, of which 2 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`, `g_pVertexBufferListHead`
- **Run by a frame** (frame_set.json): static, self, stack
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Rounds the size up to 2000 bytes and reuses a free pooled vertex buffer of matching FVF/usage/pool (aging and evicting unused ones when over 300), otherwise creates a new D3D vertex buffer and wraps it in a CYyVb.

### `0x1003B3C0` CYyVbMng::ReleaseVertexBuffer

- **Verified C++** (`tree/src/CYyVbMng.cpp`): `undefined4 __stdcall CYyVbMng::ReleaseVertexBuffer(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Reads globals:** `g_pVertexBufferListHead`
- **Run by a frame** (frame_set.json): static, self
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Finds the pooled entry in use (state 3) holding the given D3D vertex buffer and decrements its state, returning it to the pool.
