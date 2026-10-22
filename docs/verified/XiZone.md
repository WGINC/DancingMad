# XiZone

### `0x101889C0` XiZone::FindSubArea

- **Verified C++** (`tree/src/XiZone.cpp`): `int __cdecl XiZone::FindSubArea(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 1 argument slot(s) (cdecl_args.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10188900`
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static, self
- **DancingMad name:** `XiZone_FindSubArea` (not stated)
- **DancingMad note:** Looks up a sub-area environment by ID; callers fall back to the zone itself.

### `0x101889E0` fn_101889E0

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API void __thiscall fn_101889E0(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 56 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x101889E1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_101889E0`, `fn_1018A320`
- **Run by a frame** (frame_set.json): static

### `0x10188A10` fn_10188A10

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API void __thiscall fn_10188A10(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 56 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10188A11 mov ebx, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `thunk_sub_10028AA0`, `fn_10188A10`, `fn_1018ABF0`
- **Run by a frame** (frame_set.json): static

### `0x10188A50` Env_RampWindStrength

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API uint32_t __thiscall Env_RampWindStrength(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 77 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10188A52 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Camera_GetFrameScale`, `sub_103149A0` ×2
- **Reads constants** (.rdata): 4
- **Run by a frame** (frame_set.json): static, stack
- **DancingMad name:** `Env_RampWindStrength` (not stated)
- **DancingMad note:** Ramps +0x134 (steps 0.0025/0.01, cap 1.2).

### `0x10188B10` fn_10188B10

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API uint32_t __thiscall fn_10188B10(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x10188B3C mov eax, dword ptr [ecx + 0x18]` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json); leaves ECX untouched (reg_keeps.json)
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static

### `0x10188B70` XiZone::GetDirLights

- **Verified C++** (`tree/src/XiZone.cpp`): `void __thiscall XiZone::GetDirLights(void * self, undefined4 * param_1, undefined4 * param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 8` (purges.json); entry ECX read: `0x10188B76 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `Vec3_Scale` ×2, `fn_10186FD0` ×2
- **Run by a frame** (frame_set.json): self, stack

### `0x1018B130` XiZone::GetInstance

- **Verified C++** (`tree/src/XiZone.cpp`): `void __cdecl XiZone::GetInstance()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Mem_AllocDefault`, `XiZone::Constructor`
- **Reads globals:** `g_pXiZone`
- **Writes globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `XiZone_GetInstance` (not stated)
- **DancingMad note:** Create-on-demand singleton accessor for g_pXiZone.

### `0x1018B170` XiZone::Constructor

- **Verified C++** (`tree/src/XiZone.cpp`): `void * __thiscall XiZone::Constructor(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1018B173 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10187380`, `fn_101880C0`, `fn_1018BAE0`, `unknown_libname_158`, `Time_Normalize`
- **Reads globals:** `0x1065CA58`
- **Writes globals:** `0x1065CA58`, `0x1065CA60`, `0x1065CA64`, `0x1065CA65`, `0x1065CA66`, `0x1065CA67`, `0x1065CA68`, `0x1065CA69`, `0x1065CA6A`, `0x1065CA6B`, `0x1065CA6C`, `0x1065CA6D`, `0x1065CA6E`, `0x1065CA6F`, `0x1065CA70`, `0x1065CA71`, `0x1065CA72`, `0x1065CA73`, `0x1065CA74`, `0x1065CA78`, `0x1065CA7C`, `0x1065CA84`, `0x1065CA85`, `0x1065CA86`, `0x1065CA87`, `0x1065CA88`, `0x1065CA89`, `0x1065CA8A`, `0x1065CA8B`, `0x1065CA8C`, `0x1065CA8D`, `0x1065CA8E`, `0x1065CA8F`, `0x1065CA90`, `0x1065CA91`, `0x1065CA92`, `0x1065CA93`, `0x1065CA94`, `0x1065CA98`, `0x1065CA9C`, `0x1065CAA4`, `0x1065CAA5`, `0x1065CAA6`, `0x1065CAA7`, `0x1065CAA8`, `0x1065CAAC`, `0x1065CAB0`, `0x1065CAB4`, `0x1065CAB5`, `0x1065CAB6`, `0x1065CAB8`, `0x1065CAB9`, `0x1065CABA`, `0x1065CABB`, `0x1065CABC`, `0x1065CB08`
- **Run by a frame** (frame_set.json): static
- **DancingMad name:** `XiZone_Constructor` (not stated)
- **DancingMad note:** Installs XiZone vtable 0x10336838; initializes +0x1D4 (fog distance multiplier).

### `0x1018B5E0` fn_1018B5E0

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API void __thiscall fn_1018B5E0(void * self_, int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1018B5E0 mov eax, dword ptr [ecx + 0x1bc]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_101875C0`, `fn_101875E0`, `fn_101889E0`
- **Run by a frame** (frame_set.json): static

### `0x1018B620` fn_1018B620

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API void __thiscall fn_1018B620(void * self_)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1018B621 mov esi, ecx` (ecx_use.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `fn_10081A30`, `fn_10178F70`, `fn_10186DB0`, `fn_10187030`, `fn_10188A10`, `Time_Normalize`
- **Reads globals:** `g_pCamera`, `g_pZoneMap`
- **Run by a frame** (frame_set.json): static

### `0x1018B860` XiZone::DrawScene

- **Verified C++** (`tree/src/XiZone.cpp`): `void __thiscall XiZone::DrawScene(void * self)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX read: `0x1018B868 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Sky_DrawDomeViewCentered`, `fn_101874A0`, `fn_1018B8B0` ×2
- **Reads globals:** `g_pXiZone`
- **Run by a frame** (frame_set.json): static, stack

### `0x1018B8B0` fn_1018B8B0

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API void __stdcall fn_1018B8B0(int param_1)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `fn_10036170`
- **Run by a frame** (frame_set.json): static

### `0x1018B8F0` fn_1018B8F0

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API long double __thiscall fn_1018B8F0(void * self_, undefined4 param_2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1018B8F7 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json); leaves EDX untouched (reg_keeps.json)
- **Calls directly:** `fn_10187020`, `sub_101892B0`
- **Reads constants** (.rdata): 1
- **Run by a frame** (frame_set.json): static, stack

### `0x1018B960` fn_1018B960

- **Verified C++** (`tree/src/XiZone.cpp`): `XI_API void __thiscall fn_1018B960(void * self_, undefined4 param_1, undefined4 param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1018B961 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `XiZone::FindSubArea`, `XiZone::GetDirLights`
- **Run by a frame** (frame_set.json): stack

### `0x1018B9A0` XiZone::GetDirLight

- **Verified C++** (`tree/src/XiZone.cpp`): `void __thiscall XiZone::GetDirLight(void * self, undefined4 param_1, undefined4 param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1018B9A1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `XiZone::FindSubArea`, `fn_10188CA0`
- **Run by a frame** (frame_set.json): stack

### `0x1018B9E0` XiZone::GetAmbient

- **Verified C++** (`tree/src/XiZone.cpp`): `void __thiscall XiZone::GetAmbient(void * self, uint32_t * param_1, int param_2, int param_3)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 12` (purges.json); entry ECX read: `0x1018B9E1 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `XiZone::FindSubArea`, `Env_ComputeAmbient`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `XiZone_GetAmbient` (not stated)
- **DancingMad note:** Output-pointer ambient query (optional sub-area ID) -> Env_ComputeAmbient.

### `0x1018BA20` XiZone::GetFog

- **Verified C++** (`tree/src/XiZone.cpp`): `void __thiscall XiZone::GetFog(void * self, undefined4 param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4, int param_5)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 20` (purges.json); entry ECX read: `0x1018BA21 mov esi, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `XiZone::FindSubArea`, `sub_10189120`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `XiZone_GetFog` (not stated)
- **DancingMad note:** Output-pointer fog color/end/start query (mode, optional sub-area ID) -> Env_ComputeFog.
