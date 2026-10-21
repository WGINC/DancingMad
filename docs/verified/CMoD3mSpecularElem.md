# CMoD3mSpecularElem

### `0x10041010` CMoD3mSpecularElem::GetRuntimeClass

- **Verified C++** (`tree/src/CMoD3mSpecularElem.cpp`): `char ** __cdecl CMoD3mSpecularElem::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoD3mSpecularElem_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x10041020` CMoD3mSpecularElem::Ctor

- **Verified C++** (`tree/src/CMoD3mSpecularElem.cpp`): `undefined8 __thiscall CMoD3mSpecularElem::Ctor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10041021 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoElem::Constructor`
- **Reads globals:** `g_pResourceMng`
- **Run by a frame** (frame_set.json): static

### `0x100410E0` CMoD3mSpecularElem::vf012

- **Verified C++** (`tree/src/CMoD3mSpecularElem.cpp`): `BOOL CMoD3mSpecularElem::vf012(int a1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100410F0` CMoD3mSpecularElem::ScalarDeletingDtor

- **Verified C++** (`tree/src/CMoD3mSpecularElem.cpp`): `_DWORD * CMoD3mSpecularElem::ScalarDeletingDtor(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x100410F1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `SharedDeleteHelper`, `CXi471011C8_VT_1032AD80_Dtor`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x100412B0` CMoD3mSpecularElem::vf18

- **Verified C++** (`tree/src/CMoD3mSpecularElem.cpp`): `void CMoD3mSpecularElem::vf18()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): NOT VERIFIED -- FAIL
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100412B5 mov ebp, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `CDx::SetTransform` ×2, `sub_10015230`, `fn_1003FCE0`, `fn_1003FCF0` ×5, `VertexBatch_BindAndDraw` ×3, `fn_1006AD90` ×4, `StateBlock_ApplyRSTSS` ×3, `StateBlock_ApplyTSS`, `MoProcessor_CallVSlot49`, `TextureHolder_BindWarped`, `_atexit` ×4
- **Direct3D 8 calls** (com_calls.json, proven device): `IDirect3DDevice8::SetRenderState` ×3, `IDirect3DDevice8::SetTextureStageState` ×15
- **Reads constants** (.rdata): 1
- **Indirect calls:** 30, of which 20 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `Fn100412B0_staticGuards`, `g_scratchValue`, `g_pResourceMng`, `g_pProcessor`
- **Writes globals:** `Fn100412B0_staticGuards`
- **Run by a frame** (frame_set.json): stack
