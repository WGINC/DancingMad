# XiModelActor

### `0x100C3FB0` fn_100C3FB0

- **Verified C++** (`tree/src/XiModelActor.cpp`): `XI_API int __thiscall fn_100C3FB0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C3FB0 lea eax, [ecx + 0x734]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self

### `0x100C3FC0` fn_100C3FC0

- **Verified C++** (`tree/src/XiModelActor.cpp`): `XI_API int __thiscall fn_100C3FC0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x100C3FC0 lea eax, [ecx + 0x744]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): self
