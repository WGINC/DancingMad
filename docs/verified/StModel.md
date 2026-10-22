# StModel

### `0x102524E0` StModelItemClear

- **Verified C++** (`tree/src/StModel.cpp`): `XI_API undefined4 __cdecl StModelItemClear(uint32_t * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `fn_10017D20` ×2, `sqFree` ×5, `fn_10277AB0`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `StModelItemClear` (not stated)
- **DancingMad note:** Real function name from its own embedded (dead/no-op) debug-print strings: 'StModelItemClear(A): called with non-NULL dmbPtr/dmpPtr [%p]'. Releases dmbPtr/dmpPtr (Dynamic Model Buffer/Pack pointers) via sqFree with file+line tags from StModel.cpp.
