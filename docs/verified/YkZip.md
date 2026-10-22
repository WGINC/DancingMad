# YkZip

### `0x10244DF0` fn_10244DF0

- **Verified C++** (`tree/src/YkZip.cpp`): `XI_API void * __thiscall fn_10244DF0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10244DF1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10126320`, `fn_10244F20`
- **Run by a frame** (frame_set.json): static
