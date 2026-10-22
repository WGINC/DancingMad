# CAcc

### `0x1000CFB0` CAcc::Constructor

- **Verified C++** (`tree/src/CAcc.cpp`): `undefined4 __thiscall CAcc::Constructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1000CFB0 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CAcc_Constructor` (not stated)
- **DancingMad note:** Sets the CAcc vtable (0x10329A3C) and zeroes the three COM pointers at +4/+8/+0xC. Constructed by CDx_Constructor (x4), CMoOcclusionMng (sub_1006C140), sub_10044270 and sub_100755A0. CAcc has no methods beyond the shared base slots and a destructor, so the pointers are filled by owner code (not yet identified).
