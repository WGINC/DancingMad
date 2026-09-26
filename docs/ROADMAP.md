# Roadmap to a complete PC graphics-pipeline map

Status 2026-09-26: **Phases 1 (active items), 2, 3, and 3b are done. Phase 4, the consolidated
pipeline map, is written** — see `GRAPHICS_PIPELINE.md`. Two dynamic-only
questions are parked in the Future box below; neither blocks the map.

---

## Phase 1 — Extended live session with `dynamic_analysis_hooks` — DONE (active items)

Session-2 log (85,848 lines):
1. **CreateDevice path** — hardware vertex processing (`behaviorFlags=0x40`). Closed.
2. **Ground/water/normal** — `GetWaterHeight`/`GetGroundHeight` ramp together at the water edge
   (623/623, 539/539, 495/495 at the transition); `GetGroundNormal` fires every frame. Closed.

(StartDisintegration and the race condition moved to the Future box.)

## Phase 2 — Small static follow-ups — DONE

5. Record byte `+0x01` = PS2 `flip`, unused by the PC pose path (§17, §18.7).
6. `CAcc` gap in `CDx` — original claim right; `+0x1AC`/`+0x1CC` never filled (§13 #1).
7. Texture upload path — loader → 20/frame pump → runtime DXT1/DXT3 via D3DX (§18.9).

## Phase 3 — Rendering completeness — DONE

8. Particle rendering — no separate renderer; four CPU-built submission paths; 73-function draw
   census (§18.11).
9. Post-processing — afterimage, flash, zoom-feedback, upscale composite, UI composite, fade; a
   depth blur is compiled in but dead (§18.10).
10. **Registry 0030 — stereoscopic 3D** (§18.14). Every `CDx` draw is repeated for a second eye
    with a ±0.006 projection X offset; left/right packed side by side at composite.

## Phase 3b — `CXiSkeletonActor`'s vtable — DONE

Closed by reading every PS2 body directly and matching PC by callee identity, arity, fields and a
positional run (PS2 75–99 → PC 153–193) (§18.13, §18.14):
- Action cluster: `SetAction` 166, `KillAction` 167, `IsMovingAction` 168 (High). Last round's
  `SetAction` candidate retracted.
- `GetFocal` 153 (High). `SetTarget`, the target stubs, `GetNamePos`/`GetArrowPos` (order settled),
  `OnDrawName`, `SetModel` (upgraded), `SetMotion`, `IsMovingTechnic`, `SetAttack` ×2,
  `ReplaceAttack`, `UseMagic` ×2, `OcclusionClip`, `AmIUserControlTarget`/`AmIControlActor`,
  `Append` ×2.
- The IsXxx cluster: all nine pairs (lock counters and bytes, not bit flags — which is why three
  earlier bit-mask searches missed them).
- `Unlink{Caster,Target}Attachments` (renamed from a misread Find pair; PS2 field `+0x40` confirmed).
- **Explained absence:** `ViewVolumeClip` has no PC vtable body — PC moved view culling out of it.

Several older doc claims were corrected along the way (ViewVolumeClip/OcclusionClip were not stubs;
IsMovingAction does not dispatch through its parameter; four slots named IsChocobo/IsFishingRod
were wrong).

What remains unnamed in the table is PC-only code with no PS2 counterpart (e.g. slots 244/245),
labeled as such — not a gap in the pipeline map.

## Phase 4 — Consolidation — DONE

The standalone pipeline map (`GRAPHICS_PIPELINE.md`, also published as a page):
device creation → per-frame state machine → frame order → `CDx` submission and render-state
layer → global scene state → camera → textures → animation → bone pose/skinning → actors and effects →
post-processing and composite → stereo mode → configuration. Built from §18, every address
re-checked against the symbol script.

---

## Future box — parked, not blocking the map

Both need a live session, and neither changes the pipeline structure.

- **Race condition (`ResolveTree`/`Evictor`).** Session 2 showed one thread ID across 85K lines and
  zero `Evictor` hits. Needs a session that is logging *before the very first zone-in* after launch,
  so a genuinely uncached zone load is captured. Watch for a second thread ID.
- **`StartDisintegration`.** Zero hits in session 2. The 7-slot repoint is already in the DLL; it
  needs a session that deliberately includes deaths / disintegration effects. Zero hits across such
  a session would itself be the answer.
- ~~**Animation rate.**~~ **Closed statically (§18.16), no hook needed.** Visible actors animate every
  frame. The 1-in-4 bucket staggers only the screen-rect occlusion re-test; culled actors skip
  animation until their next bucket frame finds them visible.

## Phase 5 — Animation and collision loose ends — DONE (§18.16)

- **Animation rate** — closed statically (see above).
- **Collision actor** — every `CXiCollisionActor` override now matched against the PS2
  `XiCollisionActor` overrides and DWARF layout: `ExecHitCheck` 101, `IsTouchDown` 102, `IsOnLift`
  103, `GetPos` 111, `IsBlendNormal` 255; PC-only `current_area_id` accessors 97/98 and a deferred
  hit-check request (96, 252, 253). The "one byte off" `IsOnLift` note and the "permanently
  unresolvable stubs" claim are both explained and corrected. One wrong script address
  (`0x100D6670`) removed.

## Phase 6 — Environment and weather — DONE (§18.17, §18.18)

- Resource type map: all 97 `RES_TYPE` names from PS2 DWARF, matched to the PC loader switch.
- Time of day: weather records are named `HHMM`; the zone interpolates between the two bracketing the
  game clock (`Env_BlendTimeOfDay`). Registry 0034 = time-of-day light tint.
- World environment render `0x1017B510` (projection, lighting, fog, draw); no separate sky pass.
- Water: no clip-plane reflection pass exists. Shadows: stencil only in `dancer` code.
- Settings object: ~60 indices mapped by usage; `0x3C` = actor draw budget.
- DATs: Z-sort periods not present in model DATs (negative result); mounts are standalone models.

A further logging session's results: weather-to-weather transition **confirmed active** (16+13 hits);
`dancer` stencil shadows **confirmed not exercised** in this session (real negative, four hooks, zero
hits, long session). Draw-budget gate did not fire at all this session (needs a crowded-actor
scenario) -- `+0x6A4 == 4` and the link-field identity remain open.

## Explicitly adjacent, not part of "pipeline complete"

- Z-sort period values in shipped model data. `.dmb` is the middleware's internal format name; on
  disk it's inside FFXI's numbered `.DAT` files under `ROM/`. Needs a few model DATs — low
  priority, characterizes real-world values only.
- The disintegrate-fix *implementation* — investigation done; building it consumes the map.
