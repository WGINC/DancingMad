# PS2 debug-data tools

The PS2 build of Final Fantasy XI (disc executable `SCUS_972.66`) carries genuine, complete debug
data — a 12,227-entry function symbol table and a 14.8 MB DWARF **version 1** `.debug` section
(Metrowerks CodeWarrior for MIPS): 321,865 entries describing 2,758 distinct named types, with
every member's name, type, and offset, plus inheritance. No standard Python library reads DWARF
v1 — it's old enough to predate the versions modern tooling targets — so this project wrote its
own parser rather than go without it. This debug data is where a large share of this whole
project's confidence comes from: PC-side structures could be checked against a real, named PS2
layout instead of inferred from shape alone.

This is also where the PS2-side disassembly throughout `docs/FINDINGS.md` came from — `ee_disasm.py`
exists because standard MIPS disassemblers (including Capstone) misdecode two PS2-specific
opcodes: `LQ` (0x1E) and `SQ` (0x1F) collide with a MIPS32R2 encoding, so a standard decoder prints
a plausible-looking but flatly wrong instruction (`ext $s0, $sp, 0, 1`) for what the PS2's actual
R5900 CPU executes as `sq $s0, 0($sp)`. Confirmed by hand-checking the raw opcode/register/immediate
fields against the real R5900 instruction set (PCSX2's own opcode tables), not by assuming a
plausible-looking decode was correct.

## What's here

- **`dwarf1.py`** — parses the raw `.debug` section of a DWARF v1 binary into a flat list of DIEs
  (debug information entries). This is the one genuinely hard part; DWARF v1's encoding is a real
  departure from later versions.
- **`index.py`** — walks the parsed DIEs and builds a clean class/struct/union database: name,
  size, base classes, and every member's name/type/offset. Where a type has duplicate definitions
  (common in DWARF), keeps the most complete one.
- **`show.py`** — a tiny CLI to print a type's layout: `python3 show.py XiSkeletonActor KzSKD`.
- **`ee_disasm.py`** — the R5900 disassembler described above. Self-contained, no dependencies
  beyond the standard library.
- **`ps2_types.json`** — a ready-made export of `index.py`'s output: all 2,758 types, ready to use
  without re-running the parser yourself.
- **`ps2_symbols.json`** — the function symbol table (name → address, size), 19,944 entries,
  converted from this project's own working pickle into portable JSON for the same reason the
  findings' symbol scripts are plain text rather than a binary format: something anyone can open,
  diff, and trust without executing arbitrary pickle data.

## What's deliberately *not* here

The raw parsed DWARF (`dies.pkl` in this project's own working environment, ~20 MB) isn't included.
It's a large intermediate cache, fully superseded by `ps2_types.json` for any practical use, and
regenerating it requires `dwarf1.py` plus your own copy of `SCUS_972.66` — which, like every other
game file, isn't included in this repository either.

## Reproducing this yourself

1. `python3 dwarf1.py SCUS_972.66 dies.pkl` — parse `.debug` from your own copy of the disc image.
2. `python3 index.py` — builds `classes.pkl` next to itself (same directory as this script,
   resolved automatically regardless of your current working directory).
3. `python3 show.py XiSkeletonActor` — print a layout, to spot-check the result.

You only need steps 1–2 if you want to regenerate `ps2_types.json` yourself, or need a type that
didn't make it into that export for some reason. For everyday use, `ps2_types.json` and
`ps2_symbols.json` are the ready-to-use artifacts.

## Validation

Cross-checked against `atom0s`'s independently-produced `XiEvents` project: its PS2 names for
`REQSTACK` and `XiEvent` — including the `Priorty` typo, preserved faithfully rather than "corrected"
— come out at exactly the offsets this project's own parser produces. Two independent parses of the
same debug data agreeing down to a real typo is about as strong a validation as this kind of tooling
gets.

## Notes on the data itself

Member types are rendered best-effort from the DWARF encoding — arrays show as `"array"` rather
than a fully resolved element type/count, since that detail wasn't always recoverable cleanly.
Vtables appear as data symbols named `__vt__<length><ClassName>`, whose first two words are a
header before the actual function pointer slots begin.
