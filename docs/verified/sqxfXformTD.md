# sqxfXformTD

### `0x1026DF00` sqxfXformTD_Init

- **Verified C++** (`tree/src/sqxfXformTD.cpp`): `XI_API void __cdecl sqxfXformTD_Init(undefined4 * param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10274640`, `fn_1027A6F0`, `fn_10289F50`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqxfXformTD_Init` (not stated)
- **DancingMad note:** Writes the sqObject header / manual vtable: type 0xC0003 (SQXF_XFORMTD_TYPE), +0x08 Validate, +0x0C Destroy, +0x10 Print, +0x14 active=0xFF, +0x18 Update. Zeroes position +0x5C, identity quaternion +0x68, scalar +0x78 = 1.0. Layout matches the PS2 sqObject/sqUpdater debug types exactly.

### `0x1026E1F0` sqxfXformTD_Update

- **Verified C++** (`tree/src/sqxfXformTD.cpp`): `XI_API void __cdecl sqxfXformTD_Update(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); returns EAX = 0 or 1 (ret_kinds.json)
- **Calls directly:** `fn_1027A9D0`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `sqxfXformTD_Update` (confirmed)
- **DancingMad note:** FULLY DECODED by disassembling the raw, previously-unanalyzed bytes directly (this address was never auto-analyzed as a function by IDA). Takes only 'this' -- no time argument, so 'TD' is not 'time-driven'; the math matches 'target/distance' better, though that expansion is a reading, not a confirmed name. Converts the object's quaternion to a 3x3 rotation and writes a 4x4 matrix (+0x1C-+0x58) whose translation is position + scalar x (rotation's third column): a boom/orbit placement, 'scalar' units along the object's own forward axis from a pivot. Used for both lights and cameras via a real code-generation template.
