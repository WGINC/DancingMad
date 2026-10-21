# CXiActorDraw

### `0x100817E0` CXiActorDraw::Update

- **Verified C++** (`tree/src/CXiActorDraw.cpp`): `undefined1 __cdecl CXiActorDraw::Update()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 100 returned normally, 0 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json); returns AL = 0 or 1, the rest left over (ret_kinds.json)
- **Calls directly:** `CXiActorDraw::UpdateDrawList`
- **Run by a frame** (frame_set.json): stack
- **DancingMad name:** `CXiActorDraw_Update` (not stated)
- **DancingMad note:** Thin delegate into CXiActorDraw_UpdateDrawList.

### `0x10082D70` CXiActorDraw::UpdateDrawList

- **Verified C++** (`tree/src/CXiActorDraw.cpp`): `void __cdecl CXiActorDraw::UpdateDrawList()`
- **Gate** (verification/gate_clean_final.jsonl, the live dumps): PASS -- 100 trials, 95 returned normally, 174 D3D calls compared (diffemu_gfx, clean build)
- **Convention facts:** `ret 0` (purges.json); entry ECX never read (ecx_use.json); entry EDX never read (edx_use.json); reads 0 argument slot(s) (cdecl_args.json)
- **Calls directly:** `Settings_GetValue`
- **Reads constants** (.rdata): 1
- **Indirect calls:** 3, of which 3 have a pop count from a definitive source (vcalls, com_calls, sp_solved, real_sp, game_sp)
- **Reads globals:** `g_pActorDrawListHead`
- **Writes globals:** `g_pActorDrawListHead`, `0x1048A324`, `g_actorUpdateCounter`, `g_actorUpdateInterval`
- **Run by a frame** (frame_set.json): self, stack
- **DancingMad name:** `CXiActorDraw_UpdateDrawList` (not stated)
- **DancingMad note:** Walks a global linked list of drawable actors (g_pActorDrawListHead, next-pointer at +0x54), comparing a depth-shaped float field (+0x8C) between adjacent nodes -- the classic shape of maintaining a depth-sorted list for back-to-front transparency ordering. Conditionally calls a per-actor virtual method (vtable offset 0x288) and sets dirty-flag-shaped bytes (+0xB0/+0xB2). Not traced past the list-walk setup.
