# Dancing Mad

**Independent reverse-engineering research into the PC client of Final Fantasy XI** - its
graphics pipeline, animation and skinning systems, actor/collision model, and the `dancer`
middleware underneath it - cross-referenced against the PS2 client's debug symbols where they
still exist.

Maintained by **Dellingr**.

## What this actually is

This project reconstructs, from the shipped PC client binary (`FFXiMain.dll`) and PS2 debug data,
how the game's rendering and animation systems really work - real addresses, real function
behavior confirmed by disassembly, and honest notes on what's still inferred versus verified.
Every claim in the documentation is tagged by how it was established: matched against real PS2
symbols, confirmed by direct disassembly, or observed in a live, running session. Static claims
were re-checked against actual bytes rather than accepted on the strength of a plausible guess,
and several early guesses that turned out wrong are documented as corrections rather than quietly
edited away - including exactly what was assumed and why it was wrong, where that happened.

**Status:** the graphics pipeline map is complete - device creation, the frame loop, `CDx`'s
submission and render-state layer, global scene state, camera, textures, the full animation and
bone-pose pipeline, actors and effects, post-processing, stereoscopic 3D, and the weather/time-of-day
environment system. A small number of items remain genuinely open and are marked as such in
[`docs/ROADMAP.md`](docs/ROADMAP.md) - they need a live logging session under a specific scenario
(a crowded zone, a fresh client launch before the first zone load), not more static analysis.

## Repository layout

```
docs/
  FINDINGS.md          The master findings document -- the full, detailed research record.
                        21 top-level sections: class hierarchies, vertex skinning, animation
                        blending, the dancer middleware's 16-module census, lighting, the
                        FFXI-bootstrap seam, the complete graphics pipeline (§18), and an
                        open-questions section that's honest about what isn't settled yet.
  GRAPHICS_PIPELINE.md  A standalone, consolidated map of the rendering pipeline specifically --
                        device creation through frame submission through post-processing --
                        pulled out of FINDINGS.md for readers who want the pipeline itself
                        without the full research trail behind it.
  ROADMAP.md            Phase-by-phase project status and what's still open.

tools/
  ffxi_symbols_ida.py    Applies every confirmed name and struct definition from this research
                         directly into an IDA Pro database. 1,288 named addresses.
  ffxi_symbols_ghidra.py Same 1,288 names and comments, for Ghidra instead -- a mechanical,
                         verified conversion from the IDA script (same addresses, same names,
                         same confidence-tagged comments), not a separately-maintained copy.
  ffxi_structs.h         The struct definitions as a standalone C header, for Ghidra's own
                         "Parse C Source" -- one deliberate type substitution documented in the
                         file's own header (an IDA/MSVC-specific type has no place in portable C).
  dynamic_analysis_hooks/
                         A logging-only instrumentation DLL for runtime verification -- confirms
                         static findings against the actual running client without needing a
                         debugger attached. Includes its own build instructions and a full,
                         honest build-verification log (what was actually compiled, disassembled,
                         and run, versus what's untested). See its own README for details.
  ps2_dwarf/             The custom DWARF v1 parser and R5900 disassembler this project wrote to
                         read the PS2 build's own debug data, plus ready-to-use JSON exports of
                         its output (2,758 PS2 types, 19,944 symbols) -- this is where most of
                         this project's cross-platform confidence actually comes from. See its
                         own README for what's here, what isn't, and why.
```

## Using the tools

**`tools/ffxi_symbols_ida.py`** (IDA Pro) - open the unpacked client DLL, then run this script
(File → Script file...) to apply every confirmed name and structure from this research directly
into your own database.

**`tools/ffxi_symbols_ghidra.py`** + **`tools/ffxi_structs.h`** (Ghidra) - the same 1,288 names,
mechanically converted to Ghidra's own scripting API rather than hand-copied, so nothing drifted
between the two. Import `ffxi_structs.h` via the Data Type Manager's "Parse C Source..." first if
you want `g_pProcessor` correctly typed, then run the script from Script Manager. Both scripts'
own headers have full usage instructions.

Either way, every entry states its own confidence level in its comment - PS2-confirmed matches,
self-authored names backed by observed behavior, or explicit placeholders for functions whose
purpose wasn't determinable from static analysis alone. Treat those differently; the scripts
themselves are honest about which is which.

## What this project does *not* include

No game files. No `FFXiMain.dll`, no `.DAT` files, no other copyrighted game assets of any kind -
none of that is included here, and none of it is required to read the documentation. The tools
operate on a copy of the client you already own; this repository only contains original research,
analysis, and tooling. This project is not affiliated with, endorsed by, or sponsored by Square
Enix. Final Fantasy XI and all related assets are the property of their respective owners.

## Credits

**Dellingr** - project lead and primary researcher. Every session's direction, every dynamic
capture, every real-world DAT file and log this project's static findings were checked against
came from this end.

**Claude (Anthropic)** - collaborative research partner throughout: static disassembly, the
dynamic-analysis tooling, and this documentation itself. Full transparency on that relationship
below.

**Hokuten** (four
repositories, `ffximain-main` plus three companions, with its own automated `ClassExtract`
vtable/constructor/destructor tool) - cross-referenced extensively in this project's own work.
Several of its claims were independently verified and confirmed correct; at least one was checked
and found to repeat an error class the same project had already identified and fixed elsewhere.

**atom0s**, for the `XiEvents` project - independently named several of the same classes and
structures this project arrived at separately (`CYyObject`, `CXiSkeletonActor`, and others),
providing real, independent confirmation at points where this project's own naming could otherwise
only be checked against itself.

**Square Enix's original PS2 development team**, whose build process left real, complete DWARF
debug data on the PS2 disc - 2,758 named types with full member layouts, and a 12,227-entry
function symbol table. An enormous share of this project's confidence, rather than plausible
guesswork, comes directly from debug information nobody involved in this project produced, that
simply happened to still be there to find.

**Hex-Rays' Lumina service**, credited honestly rather than favorably: it supplied a large number
of function name matches in the working IDA database, and on this specific binary the overwhelming
majority turned out to be false positives on small, generic function bodies (matching unrelated
Microsoft, PopCap, and DXUT code to this 2002-era engine). Named here for transparency about a
real tool this project had to actively guard against, not to overstate its contribution.

## A note on methodology

Static claims were re-checked against real disassembled bytes rather than accepted on plausibility,
runtime behavior was confirmed with live logging rather than assumed from static reading alone, and
cross-checks against independent research were verified point by point rather than trusted on
reputation. Where an earlier finding in this project turned out to be wrong, the correction is
documented in place - including a few genuine mistakes in the tooling itself (a stack-argument
mix-up, a wrong patch length, an MSVC/GCC syntax incompatibility) that were caught during testing
before being shipped. The goal throughout was to make every claim checkable, not just plausible.

## License

See [`LICENSE`](LICENSE). The documentation and tooling in this repository are original work and
are provided under the MIT License. This license covers this project's own analysis, documentation,
and code only - it does not and cannot grant any rights to Final Fantasy XI itself or any of its
assets.
