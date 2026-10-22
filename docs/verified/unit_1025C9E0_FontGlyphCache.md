# unit_1025C9E0_FontGlyphCache

### `0x1025D750` FontGlyphCache_GetDevice

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API IDirect3DDevice8 * __cdecl FontGlyphCache_GetDevice(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Returns the renderer's IDirect3DDevice8.

### `0x1025D760` FontGlyphCache_CreateTexture

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API int __cdecl FontGlyphCache_CreateTexture(unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, D3DFORMAT a5, D3DPOOL a6)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 6 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Wraps IDirect3DDevice8::CreateTexture, returning the texture or NULL on failure.

### `0x1025D7B0` FontGlyphCache_CreateVertexBuffer

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API int __cdecl FontGlyphCache_CreateVertexBuffer(unsigned int a1, unsigned int a2, unsigned int a3, D3DPOOL a4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 100 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 4 argument slot(s) (cdecl_args.json)
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pCDx`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **Summary** (inferred from reading the code, high confidence; docs/NAMES.md in ffximain-gfx): Wraps IDirect3DDevice8::CreateVertexBuffer, returning the buffer or NULL on failure.

### `0x1025E050` fn_1025E050

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1025E050(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `0x1066276C`
- **Run by a frame** (frame_set.json): static

### `0x1025E0B0` fn_1025E0B0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined * __cdecl fn_1025E0B0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1025E0C0` fn_1025E0C0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1025E0C0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x1025E230 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1025E0E0` fn_1025E0E0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1025E0E0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x1025E240 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1025E0F0` fn_1025E0F0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1025E0F0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x1025E020 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); sets only AL of EAX before it returns (ret_width.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1025E210` fn_1025E210

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1025E210(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1067A298`
- **Writes globals:** `0x1067A298`
- **Run by a frame** (frame_set.json): static

### `0x1025E230` fn_1025E230

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1025E230(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Writes globals:** `0x1067A298`
- **Run by a frame** (frame_set.json): static

### `0x1025E240` fn_1025E240

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1025E240(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Reads globals:** `0x1067A298`
- **Writes globals:** `0x1067A298`
- **Run by a frame** (frame_set.json): static

### `0x1025F2F0` fn_1025F2F0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __thiscall fn_1025F2F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 58 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1025F307 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls imports:** `EnterCriticalSection`, `LeaveCriticalSection` ×2
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x1025FD50` fn_1025FD50

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void * __thiscall fn_1025FD50(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x1025FD6F mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1025E260`, `fn_1025FE40`
- **Run by a frame** (frame_set.json): static

### `0x1025FE40` fn_1025FE40

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __thiscall fn_1025FE40(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1025FE41 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls imports:** `timeGetTime`
- **Run by a frame** (frame_set.json): static

### `0x1025FF10` fn_1025FF10

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __thiscall fn_1025FF10(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1025FF11 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls imports:** `timeGetTime`
- **Run by a frame** (frame_set.json): static

### `0x10260360` fn_10260360

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_10260360(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x10261210` fn_10261210

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void * __thiscall fn_10261210(void * self_, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 * param_4)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 16` (purges.json); entry ECX read: `0x10261215 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `fn_102659B0`
- **Run by a frame** (frame_set.json): static

### `0x102612D0` fn_102612D0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __thiscall fn_102612D0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 80 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x102612E7 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10265960`, `operator_delete`
- **Indirect calls:** 1, of which 1 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Run by a frame** (frame_set.json): static

### `0x102659B0` fn_102659B0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void * __thiscall fn_102659B0(void * self_, undefined4 param_1, void * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x102659B5 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json)
- **Calls directly:** `sub_10265940`
- **Run by a frame** (frame_set.json): static

### `0x1026CCA5` fn_1026CCA5

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026CCA5(void * param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10316D6B`, `sub_10316D90`
- **Run by a frame** (frame_set.json): static

### `0x1026CFA0` fn_1026CFA0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026CFA0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D0CA`, `fn_1026D1B4`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026D015` fn_1026D015

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026D015(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D0CA` ×2, `fn_1026D1B4` ×2, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026D0CA` fn_1026D0CA

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026D0CA(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_103169A0`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026D179` fn_1026D179

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026D179(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x1026D1B4` fn_1026D1B4

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026D1B4(int param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_103169A0`, `sub_10316D6B` ×2
- **Calls imports:** `OutputDebugStringA`
- **Run by a frame** (frame_set.json): static

### `0x1026D70C` fn_1026D70C

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026D70C(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_1026D634`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026D866` fn_1026D866

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026D866(int param_1, undefined4 * param_2, undefined1 * param_3, int param_4, undefined1 * param_5, int param_6, int param_7)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 50 trials, 30 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 7 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026CCA5`, `sub_1026CDF4`, `fn_1026D1B4` ×2, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026D9B1` fn_1026D9B1

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026D9B1(LPVOID param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 16 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10316D6B` ×3
- **Calls imports:** `CreateThread`, `OutputDebugStringA`
- **Run by a frame** (frame_set.json): static

### `0x1026DAC6` fn_1026DAC6

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026DAC6(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 93 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10316D6B` ×3
- **Calls imports:** `OutputDebugStringA`, `WaitForSingleObject`
- **Run by a frame** (frame_set.json): static

### `0x1026DB24` fn_1026DB24

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API unsigned char __cdecl fn_1026DB24(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1026DB6D` fn_1026DB6D

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026DB6D(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D0CA`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026DB8F` fn_1026DB8F

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026DB8F(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D179`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026DBAC` fn_1026DBAC

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026DBAC(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D1B4`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026DBCE` fn_1026DBCE

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026DBCE(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D0CA`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026DBF0` fn_1026DBF0

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API undefined4 __cdecl fn_1026DBF0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D179`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static

### `0x1026DC0D` fn_1026DC0D

- **Verified C++** (`tree/src/unit_1025C9E0_FontGlyphCache.cpp`): `XI_API void __cdecl fn_1026DC0D(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026D1B4`, `sub_10316D6B`
- **Run by a frame** (frame_set.json): static
