# sqinCluster

### `0x102AF540` sqinCluster_Create

- **Verified C++** (`tree/src/sqinCluster.cpp`): `XI_API undefined4 * __cdecl sqinCluster_Create(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `sqinCluster_Init`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqinCluster_Create` (confirmed)
- **DancingMad note:** Allocates 160 bytes (sqinCluster's confirmed object size), calls sqinCluster_Init.

### `0x102AF570` sqinCluster_Init

- **Verified C++** (`tree/src/sqinCluster.cpp`): `XI_API void __cdecl sqinCluster_Init(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `sub_1027EBD0`, `fn_102AF170`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqinCluster_Init` (not stated)
- **DancingMad note:** Sets up sqinCluster's manual C-style function-pointer table (not real C++ vtable dispatch -- portable-middleware style), including sqinCluster_Dump.
