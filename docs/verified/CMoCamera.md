# CMoCamera

### `0x1003C880` CMoCamera::GetRuntimeClass

- **Verified C++** (`tree/src/CMoCamera.cpp`): `char ** __cdecl CMoCamera::GetRuntimeClass()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoCamera_GetRuntimeClass` (not stated)
- **DancingMad note:** unique accessor

### `0x1003C890` CMoCamera::vf008

- **Verified C++** (`tree/src/CMoCamera.cpp`): `void CMoCamera::vf008()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x1003CB30` CMoCamera::SetPathData

- **Verified C++** (`tree/src/CMoCamera.cpp`): `int CMoCamera::SetPathData(_DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x1003CB35 mov eax, ecx` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `CMoAttachments_Reset`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoCamera_SetPathData` (not stated)
- **DancingMad note:** Copies a fixed position/direction pair plus a variable-length waypoint array (packed count field, same format as CMoGeneratorClone_InitCloneFromSource).

### `0x10071980` CMoCamera::GetSharedInstance

- **Verified C++** (`tree/src/CMoCamera.cpp`): `void * __cdecl CMoCamera::GetSharedInstance()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry EDX not established (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `_atexit`
- **Reads globals:** `CMoCamera_GetSharedInstance_staticGuard`
- **Writes globals:** `CMoCamera_GetSharedInstance_staticGuard`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoCamera_GetSharedInstance` (not stated)
- **DancingMad note:** Lazy-init singleton accessor.

### `0x100719F0` CMoCamera::vf009

- **Verified C++** (`tree/src/CMoCamera.cpp`): `void CMoCamera::vf009()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); leaves EAX, ECX, EDX untouched (reg_keeps.json)
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)

### `0x10071E30` CMoCamera::GetLinkedObject

- **Verified C++** (`tree/src/CMoCamera.cpp`): `__int16 CMoCamera::GetLinkedObject(_DWORD *a2)`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build); gates: fuzz PASS 100, town PASS 100, town2 PASS 100, combat PASS 100, zonetoinn PASS 100
- **Convention facts:** `ret 4` (purges.json); entry ECX read: `0x10071E39 mov ecx, dword ptr [ecx + 0x14]` (ecx_use.json); entry EDX never read (edx_use.json)
- **Calls directly:** `ResHandle_FreeIfUnreferenced`
- **Run by a frame** (frame_set.json): not shown (static reach from the main loop and the sampler did not find it)
- **DancingMad name:** `CMoCamera_GetLinkedObject` (not stated)
- **DancingMad note:** Get half of a get/set pair for the +0x14 field.
