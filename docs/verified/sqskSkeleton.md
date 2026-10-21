# sqskSkeleton

### `0x1027B580` fn_1027B580

- **Verified C++** (`tree/src/sqskSkeleton.cpp`): `XI_API undefined4 * __cdecl fn_1027B580(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sub_10275D80`, `fn_1027B5A0`
- **Run by a frame** (frame_set.json): static

### `0x1027B5A0` fn_1027B5A0

- **Verified C++** (`tree/src/sqskSkeleton.cpp`): `XI_API void __cdecl fn_1027B5A0(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1027C4C0` fn_1027C4C0

- **Verified C++** (`tree/src/sqskSkeleton.cpp`): `XI_API void __cdecl fn_1027C4C0(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 26 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10275D40` ×2, `sqFree` ×2, `fn_10291390`, `fn_10291460`, `fn_10291BA0`, `fn_10291C50`
- **Run by a frame** (frame_set.json): static

### `0x1027C980` fn_1027C980

- **Verified C++** (`tree/src/sqskSkeleton.cpp`): `XI_API int __cdecl fn_1027C980(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Calls directly:** `sqDebugPrintf` ×2
- **Run by a frame** (frame_set.json): static

### `0x1027C9D0` fn_1027C9D0

- **Verified C++** (`tree/src/sqskSkeleton.cpp`): `XI_API void __cdecl fn_1027C9D0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 28 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json)
- **Run by a frame** (frame_set.json): static

### `0x1029A420` sqskSkeleton_GetNodeByIndex

- **Verified C++** (`tree/src/sqskSkeleton.cpp`): `XI_API int __cdecl sqskSkeleton_GetNodeByIndex(int param_1, int param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqskSkeleton_GetNodeByIndex` (confirmed)
- **DancingMad note:** CORRECTED from an initial name (sqskSkeleton_GetJointByIndex) that was wrong -- caught by cross-checking against sqskSkeleton_Dump's own confirmed code immediately after naming. Resolves into the NODE array, not the joint array: sqskSkeleton_Dump confirms the joint array lives at field offset 36 (156-byte stride) while the node array lives at offset 32; this function reads its base from offset 32. Its 248-byte stride is consistent with a node being a larger structure that likely wraps a joint plus hierarchy/parent-child linkage, though that composition isn't confirmed, only consistent with the offset/stride evidence. Called from sqinSkinBuildBinary while resolving a cluster's bone reference -- meaning a skin cluster's bone reference resolves to a scene NODE, not a raw joint directly.
