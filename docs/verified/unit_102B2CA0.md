# unit_102B2CA0

### `0x102B2CA0` fn_102B2CA0

- **Verified C++** (`tree/src/unit_102B2CA0.cpp`): `XI_API void __cdecl fn_102B2CA0(int param_1, int * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 63 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sqgxTextureDecal` ×2, `sqgxTextureUpdate`, `sqgxBlendAdd`, `sqgxBlendOff`, `sqgxColor`, `sqgxAmbient`, `fn_102833A0`, `fn_102833C0`, `sqgxPass` ×2, `sqgxShader` ×3, `sqDrawableDraw` ×2, `fn_10298C50`, `fn_102A1FA0`, `fn_102A34D0`
- **Reads globals:** `g_pSqgxContext`
- **Run by a frame** (frame_set.json): static
