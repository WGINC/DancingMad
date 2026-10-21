# CMoResource_VT_1032C55C

### `0x10063C50` CMoResource_VT_1032C55C::vf008

- **Verified C++** (`tree/src/CMoResource_VT_1032C55C.cpp`): `void CMoResource_VT_1032C55C::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10063C50 mov dword ptr [ecx + 0x34], 0` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
