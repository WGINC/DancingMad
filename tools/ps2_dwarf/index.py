"""Index classes/structs from parsed DWARF 1 entries (see dwarf1.py)."""

from __future__ import annotations

import pickle
import struct

from dwarf1 import (AT_BYTE_SIZE, AT_FUND_TYPE, AT_LOCATION, AT_MOD_FUND_TYPE, AT_MOD_U_D_TYPE,
                    AT_NAME, AT_USER_DEF_TYPE, FUND, MODS, location_offset)

import os
_here = os.path.dirname(os.path.abspath(__file__))
dies = pickle.load(open(os.path.join(_here, "dies.pkl"), "rb"))
by_off = {d[0]: d for d in dies}
children: dict[int, list] = {}
for d in dies:
    if d[3] is not None:
        children.setdefault(d[3], []).append(d)


def type_name(attrs: dict, depth: int = 0) -> str:
    if AT_FUND_TYPE in attrs:
        return FUND.get(attrs[AT_FUND_TYPE], f"fund{attrs[AT_FUND_TYPE]:#x}")
    if AT_USER_DEF_TYPE in attrs:
        return ref_name(attrs[AT_USER_DEF_TYPE], depth)
    for key, is_ref in ((AT_MOD_FUND_TYPE, False), (AT_MOD_U_D_TYPE, True)):
        if key in attrs:
            blk = attrs[key]
            tail = 4 if is_ref else 2
            mods, raw = blk[:-tail], blk[-tail:]
            base = (ref_name(struct.unpack("<I", raw)[0], depth) if is_ref
                    else FUND.get(struct.unpack("<H", raw)[0], "?"))
            s = base
            for m in reversed(mods):
                s = f"{MODS.get(m, '?')}{s}" if m in (3, 4) else f"{s}{MODS.get(m, '?')}"
            return s
    return "?"


def ref_name(ref: int, depth: int = 0) -> str:
    d = by_off.get(ref)
    if d is None:
        return f"<ref {ref:#x}>"
    tag, attrs = d[1], d[2]
    if AT_NAME in attrs:
        return attrs[AT_NAME]
    if tag == 0x01 and depth < 4:  # array: element type from children/attrs
        return "array"
    if tag == 0x15:
        return "func_type"
    return f"<anon {tag:#x}>"


def class_record(d) -> dict:
    off, tag, attrs, _ = d
    members, bases, methods = [], [], []
    for c in children.get(off, []):
        ct, ca = c[1], c[2]
        if ct == 0x0D:
            loc = location_offset(ca[AT_LOCATION]) if AT_LOCATION in ca else None
            members.append((ca.get(AT_NAME, "?"), loc, type_name(ca)))
        elif ct == 0x1C:
            loc = location_offset(ca[AT_LOCATION]) if AT_LOCATION in ca else None
            bases.append((type_name(ca), loc))
        elif ct in (0x14, 0x06):
            methods.append(ca.get(AT_NAME, "?"))
    return {"name": attrs.get(AT_NAME), "size": attrs.get(AT_BYTE_SIZE), "tag": tag,
            "members": members, "bases": bases, "methods": methods, "die": off}


classes: dict[str, dict] = {}
for d in dies:
    if d[1] in (0x02, 0x13, 0x17) and AT_NAME in d[2]:
        rec = class_record(d)
        best = classes.get(rec["name"])
        # keep the most complete definition (declarations have no size/members)
        if best is None or (len(rec["members"]), rec["size"] or 0) > (len(best["members"]), best["size"] or 0):
            classes[rec["name"]] = rec

pickle.dump(classes, open(os.path.join(_here, "classes.pkl"), "wb"))
print(len(classes), "distinct named classes/structs/unions")
