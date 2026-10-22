# sqsdAniso

### `0x102993B0` fn_102993B0

- **Verified C++** (`tree/src/sqsdAniso.cpp`): `XI_API void __cdecl fn_102993B0(int * param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 93 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxTextureSet` ×2, `sqgxTextureDecal` ×2, `sqgxTextureClut` ×2, `sqgxAlphaTest` ×2, `fn_102827D0`, `sqgxBlendTrsp`, `sqgxBlendOff`, `sqgxShader` ×3, `sqDrawableDraw`, `fn_102912F0`, `fn_10298E10`, `fn_1029C460`, `fn_102A1FA0`, `fn_102A34D0`, `fn_102A3770`
- **Run by a frame** (frame_set.json): static

### `0x10299610` sqsdAniso_BakeOntoShape

- **Verified C++** (`tree/src/sqsdAniso.cpp`): `XI_API int * __cdecl sqsdAniso_BakeOntoShape(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxShader`, `sub_10285740`, `sqDrawableDraw`, `fn_1028D9C0`, `fn_102912F0`, `fn_1029B5C0`, `sqgxDlistEnd`, `fn_102A2000`, `fn_102A3760`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqsdAniso_BakeOntoShape` (not stated)
- **DancingMad note:** Real, working bake function. Same 655369 cache tag as Glow/Generic. Selects between stored tangent-basis vectors (v4[22]/[25]/[26]) for anisotropic lighting based on a mode parameter, then sets a shading mode via sqgxContext_SelectShaderMode.
