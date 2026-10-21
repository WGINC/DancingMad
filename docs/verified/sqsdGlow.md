# sqsdGlow

### `0x102999A0` fn_102999A0

- **Verified C++** (`tree/src/sqsdGlow.cpp`): `XI_API undefined4 __cdecl fn_102999A0(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10283970`, `sqgxShader`, `fn_102A1FA0`
- **Run by a frame** (frame_set.json): static

### `0x10299AB0` sqsdGlow_BakeOntoShape

- **Verified C++** (`tree/src/sqsdGlow.cpp`): `XI_API int * __cdecl sqsdGlow_BakeOntoShape(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10285740`, `sqDrawableDraw`, `fn_1028D9C0`, `fn_102999A0`, `fn_1029B5C0`, `sqgxDlistEnd`, `fn_102A2000`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqsdGlow_BakeOntoShape` (confirmed)
- **DancingMad note:** CONFIRMED ANSWER to how Glow actually applies to geometry: not a simple render-state change. Checks a magic-number cache tag (655369) on the shape first -- if already glow-processed, skips entirely (a real, confirmed caching optimization, same spirit as sqgxContext's state cache). Otherwise creates a new processed-shape wrapper combining the base geometry with glow-specific baked data. Called from sqmdDMBBuildShapes for shader type 0xF0003.
