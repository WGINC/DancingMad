# mdl

### `0x1026E900` mdl_1026E900

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl mdl_1026E900(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 34 trials, 8 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); thin evidence: few trials returned
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10270690`, `sqFree` ×2, `fn_10277AB0`, `fn_1027DB80`, `fn_1027E0D0`
- **Reads globals:** `0x1099AECC`, `0x1099AED0`, `0x1099AED8`, `0x1099AEDC`
- **Writes globals:** `0x1099AEC8`, `0x1099AECC`, `0x1099AED0`, `0x1099AED8`, `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026EBF0` fn_1026EBF0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API int __cdecl fn_1026EBF0(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 96 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_102703C0`, `fn_102736E0`, `sub_10273810`, `sqDebugPrintf`
- **Reads globals:** `0x103B19C0`, `0x103B19C4`, `0x103B19C8`, `0x103B19CC`, `0x1099AEC8`, `0x1099AECC`, `0x1099AED0`
- **Writes globals:** `0x1099AECC`
- **Run by a frame** (frame_set.json): static

### `0x1026EE00` fn_1026EE00

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026EE00(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 35 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AECC`, `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x1026EF00` fn_1026EF00

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API int __cdecl fn_1026EF00(int param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 97 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1027DAE0`, `fn_1027DCC0`, `sqDebugPrintf` ×2
- **Reads globals:** `0x1099AED4`, `0x1099AED8`, `0x1099AEDC`
- **Writes globals:** `0x1099AED8`
- **Run by a frame** (frame_set.json): static

### `0x1026F160` fn_1026F160

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API undefined4 __cdecl fn_1026F160(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 58 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX not established (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10279870`
- **Run by a frame** (frame_set.json): static

### `0x1026F1B0` fn_1026F1B0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API undefined4 __cdecl fn_1026F1B0(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 34 trials, 14 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `fn_1027DB80`
- **Reads globals:** `0x1099AED8`, `0x1099AEDC`
- **Writes globals:** `0x1099AED8`
- **Run by a frame** (frame_set.json): static

### `0x1026F4F0` fn_1026F4F0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API undefined4 __cdecl fn_1026F4F0(int * param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json); leaves EDX untouched (reg_keeps.json)
- **Reads globals:** `0x1099AED8`, `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026F580` fn_1026F580

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026F580(int param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 83 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10285000`
- **Reads globals:** `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026F7B0` fn_1026F7B0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026F7B0(int param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 84 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026F900` fn_1026F900

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026F900(int param_1, uint32_t param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 76 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275090` ×2, `fn_102857E0`
- **Reads globals:** `0x1099AED8`, `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026F9A0` fn_1026F9A0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026F9A0(int param_1, uint32_t param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 80 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026F9E0` fn_1026F9E0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026F9E0(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 80 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_1026F580`, `fn_1026F9A0` ×3, `fn_10284FD0` ×3
- **Reads globals:** `0x1099AEDC`
- **Run by a frame** (frame_set.json): static

### `0x1026FE60` fn_1026FE60

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026FE60(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 70 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AECC`, `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x1026FEA0` fn_1026FEA0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026FEA0(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 86 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AECC`, `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x1026FEF0` fn_1026FEF0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026FEF0(int * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 70 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AECC`, `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x1026FF30` fn_1026FF30

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_1026FF30(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 86 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AECC`, `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x1026FF80` fn_1026FF80

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API undefined4 __cdecl fn_1026FF80(int param_1, float * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 67 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `M4fTransform` ×2, `fn_1028D9A0`
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x102700C0` fn_102700C0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_102700C0(int param_1, int param_2, undefined4 param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 70 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10279530`, `fn_10279870` ×2, `fn_1027A220`, `fn_1028DE10`
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x102701B0` fn_102701B0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_102701B0(int param_1, uint32_t param_2, undefined4 * param_3, uint32_t param_4, int param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 76 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 5 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10274640`, `fn_10274650`
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x10270240` fn_10270240

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_10270240(int param_1, undefined4 * param_2, int * param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x10270290` fn_10270290

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_10270290(int param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x102703C0` fn_102703C0

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_102703C0(int param_1, uint32_t param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 80 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 3 argument slot(s) (cdecl_args.json)
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x10270410` fn_10270410

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_10270410(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 75 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_102703C0` ×4, `sub_10273810` ×4
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static

### `0x10270690` fn_10270690

- **Verified C++** (`tree/src/mdl.cpp`): `XI_API void __cdecl fn_10270690(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqFree`
- **Reads globals:** `0x1099AED0`
- **Run by a frame** (frame_set.json): static
