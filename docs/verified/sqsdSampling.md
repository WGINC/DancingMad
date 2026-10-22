# sqsdSampling

### `0x10299090` fn_10299090

- **Verified C++** (`tree/src/sqsdSampling.cpp`): `XI_API void __cdecl fn_10299090(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxTextureSet` ×3, `sqgxTextureDecal`, `sqgxTextureClamp`, `sqgxTextureClut` ×2, `sqgxZMask` ×2, `sqgxBlendAdd`, `sqgxBlendTrsp`, `sqgxBlendAddDestAlpha`, `sqgxBlendOff`, `fn_10283F20`, `sqgxPassAdd` ×2, `sqgxShader` ×2, `sqDrawableDraw` ×2, `fn_1029BCD0`, `fn_1029BD40`, `fn_102A1FA0`, `fn_102A34D0`
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static

### `0x10299250` sqsdSampling_BakeOntoShape

- **Verified C++** (`tree/src/sqsdSampling.cpp`): `XI_API int __cdecl sqsdSampling_BakeOntoShape(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqgxShader`, `sub_10285740`, `sqDrawableDraw`, `fn_1028D9C0`, `fn_1029B5C0`, `sqgxDlistEnd`, `fn_102A2000`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqsdSampling_BakeOntoShape` (confirmed)
- **DancingMad note:** CONFIRMED REAL DIFFERENCE from the other 4 shader types: no 655369 cache-tag check at all -- always rebuilds on every call. Not confirmed whether intentional (cheap enough not to need caching) or a genuine inconsistency. Passes a simple 2-value mode constant to sqgxContext_SelectShaderMode, gated on the 'back' script parameter.
