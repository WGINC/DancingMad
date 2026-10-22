# YkJpgBit

### `0x101D08E0` fn_101D08E0

- **Verified C++** (`tree/src/YkJpgBit.cpp`): `XI_API undefined4 __thiscall fn_101D08E0(void * self_, undefined4 param_1, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x101D08E4 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): static
