# sqsdCartoon

### `0x102997A0` fn_102997A0

- **Verified C++** (`tree/src/sqsdCartoon.cpp`): `XI_API void __cdecl fn_102997A0(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxBlendSub`, `sqgxPassAdd` ×2, `sqgxShader` ×2, `sqDrawableDraw` ×2, `fn_10298C50` ×2, `fn_102A1FA0`, `fn_102A34D0`
- **Run by a frame** (frame_set.json): static

### `0x10299840` sqsdCartoon_BakeOntoShape_Stub

- **Verified C++** (`tree/src/sqsdCartoon.cpp`): `XI_API undefined4 __cdecl sqsdCartoon_BakeOntoShape_Stub(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `sqDebugPrintf`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqsdCartoon_BakeOntoShape_Stub` (confirmed)
- **DancingMad note:** CONFIRMED unimplemented stub (prints 'not implemented', does nothing). Matches the same pattern as BRDF and AmbientMap. Cel-shading is fully DEFINED in the script system (real parameters confirmed) but its bake/application path is inert in this shipped build.
