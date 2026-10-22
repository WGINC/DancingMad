# unit_100231F0_SkinVerticesFinish

### `0x10025010` fn_10025010

- **Verified C++** (`tree/src/unit_100231F0_SkinVerticesFinish.cpp`): `XI_API void * __thiscall fn_10025010(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10025011 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10029C90`
- **Run by a frame** (frame_set.json): static
