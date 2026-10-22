# sqrdLight

### `0x1026E2F0` sqrdLight_Init

- **Verified C++** (`tree/src/sqrdLight.cpp`): `XI_API void __cdecl sqrdLight_Init(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqrdLight_Init` (confirmed)
- **DancingMad note:** Sets up a default white (1,1,1,1) color and the standard 3-slot manual vtable. Confirmed via a literal code-generation template embedded in the binary (static sqrdLight s_%s_light_%1d = {...}).
