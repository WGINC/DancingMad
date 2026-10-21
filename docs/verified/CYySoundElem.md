# CYySoundElem

### `0x100369F0` fn_100369F0

- **Verified C++** (`tree/src/CYySoundElem.cpp`): `XI_API undefined4 __thiscall fn_100369F0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100369F2 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10036980`, `CMoElem::Constructor`, `fn_10044AA0`
- **Run by a frame** (frame_set.json): static
