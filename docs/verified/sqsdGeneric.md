# sqsdGeneric

### `0x10290910` fn_10290910

- **Verified C++** (`tree/src/sqsdGeneric.cpp`): `XI_API void __cdecl fn_10290910(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 0 through its tail jump to 0x102A3390 (tail_purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static

### `0x10290FC0` sqsdGeneric_BakeOntoShape

- **Verified C++** (`tree/src/sqsdGeneric.cpp`): `XI_API int * __cdecl sqsdGeneric_BakeOntoShape(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxShader`, `sub_10285740`, `sqDrawableDraw`, `sqDebugPrintf` ×4, `fn_1028D9C0`, `fn_1029B5C0`, `sqgxDlistEnd`, `fn_102A2000`, `fn_102A3760`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqsdGeneric_BakeOntoShape` (confirmed)
- **DancingMad note:** Confirmed: uses the SAME 655369 magic-number cache tag as sqsdGlow_BakeOntoShape -- all shader types that cache, cache via one unified convention. Builds a real feature bitmask (bump=1, env=4, phong=2) from what the model actually has, logging real 'Model is missing...' errors if a requested feature lacks its data. Passes the combined bitmask to sqgxContext_SelectShaderMode -- a real shader-permutation system. Also references a real 'Spherigon' warning (curved-surface normal interpolation, a known period rendering technique).
