# unit_1005DFF0

### `0x1005E110` fn_1005E110

- **Verified C++** (`tree/src/unit_1005DFF0.cpp`): `XI_API void __thiscall fn_1005E110(void * self_, undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1005E110 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
