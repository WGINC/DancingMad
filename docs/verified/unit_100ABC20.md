# unit_100ABC20

### `0x100ABC20` fn_100ABC20

- **Verified C++** (`tree/src/unit_100ABC20.cpp`): `XI_API void * __thiscall fn_100ABC20(void * self_, char * param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x100ABC26 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `_strncpy`
- **Run by a frame** (frame_set.json): static

### `0x100ABC70` fn_100ABC70

- **Verified C++** (`tree/src/unit_100ABC20.cpp`): `XI_API void __cdecl fn_100ABC70(undefined4 * param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
