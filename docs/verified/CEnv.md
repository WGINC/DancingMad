# CEnv

### `0x1000D3F0` j_CEnv_UpdateDualTargetMode

- **Verified C++** (`tree/src/CEnv.cpp`): `XI_API void __thiscall j_CEnv_UpdateDualTargetMode(void * self_, undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** pops 4 through its tail jump to 0x1000D630 (tail_purges.json); entry ECX read: `through a callee` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1000D620` fn_1000D620

- **Verified C++** (`tree/src/CEnv.cpp`): `XI_API void __cdecl fn_1000D620(void)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static

### `0x1000D630` CEnv::UpdateStereoMode

- **Verified C++** (`tree/src/CEnv.cpp`): `void __thiscall CEnv::UpdateStereoMode(void * self, undefined4 xi_s1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1000D636 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Calls directly:** `CEnv::IsStereoMode`
- **Reads globals:** `g_cfgStereoMode`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `CEnv_UpdateStereoMode` (not stated)
- **DancingMad note:** Each frame: CEnv+0x18 = g_cfgStereoMode (registry 0030); while on, cycles the 0..3 counter at CEnv+0x1C. (Renamed from CEnv_UpdateDualTargetMode once the mode was identified as stereoscopic 3D.)

### `0x1000D660` CEnv::IsStereoMode

- **Verified C++** (`tree/src/CEnv.cpp`): `undefined4 __thiscall CEnv::IsStereoMode(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1000D660 mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): static, self
- **DancingMad name:** `CEnv_IsStereoMode` (not stated)
- **DancingMad note:** Returns CEnv+0x18 != 0. (Was CEnv_IsDualTargetMode.)
