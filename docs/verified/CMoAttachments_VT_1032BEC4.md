# CMoAttachments_VT_1032BEC4

### `0x10063120` CMoAttachments_VT_1032BEC4::vf001

- **Verified C++** (`tree/src/CMoAttachments_VT_1032BEC4.cpp`): `_DWORD * CMoAttachments_VT_1032BEC4::vf001(char a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** pops 4 through its tail jump to 0x10061EA0 (tail_purges.json); entry ECX read: `0x10063120 sub ecx, 0x34` (ecx_use.json); entry EDX never read (edx_use.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
