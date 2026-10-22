# sqopOpcode

### `0x10289EA0` sqopOpcodeGet

- **Verified C++** (`tree/src/sqopOpcode.cpp`): `XI_API int __cdecl sqopOpcodeGet(int * param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 78 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 2 argument slot(s) (cdecl_args.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqopOpcodeGet` (not stated)
- **DancingMad note:** Reads the opcode at the current playback index, extracting its type tag and two parameters.
