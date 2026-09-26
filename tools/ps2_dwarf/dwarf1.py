"""DWARF version 1 parser (Metrowerks MIPS output) for SCUS_972.66.

DWARF 1 has no standard Python reader (pyelftools starts at v2). Format:
each entry = u32 length (including itself) + u16 tag + attributes until the
entry's end. An attribute is a u16 whose low nibble is the data form. Entries
shorter than 8 bytes are null/padding. The tree is implied by AT_sibling:
entries between a node and its sibling are its children.
"""

from __future__ import annotations

import pickle
import struct
import sys

TAGS = {
    0x01: "array_type", 0x02: "class_type", 0x03: "entry_point", 0x04: "enumeration_type",
    0x05: "formal_parameter", 0x06: "global_subroutine", 0x07: "global_variable", 0x0A: "label",
    0x0B: "lexical_block", 0x0C: "local_variable", 0x0D: "member", 0x0F: "pointer_type",
    0x10: "reference_type", 0x11: "compile_unit", 0x12: "string_type", 0x13: "structure_type",
    0x14: "subroutine", 0x15: "subroutine_type", 0x16: "typedef", 0x17: "union_type",
    0x18: "unspecified_parameters", 0x19: "variant", 0x1A: "common_block",
    0x1B: "common_inclusion", 0x1C: "inheritance", 0x1D: "inlined_subroutine", 0x1E: "module",
    0x1F: "ptr_to_member_type", 0x20: "set_type", 0x21: "subrange_type", 0x22: "with_stmt",
}
FUND = {
    0x1: "char", 0x2: "signed char", 0x3: "unsigned char", 0x4: "short", 0x5: "signed short",
    0x6: "unsigned short", 0x7: "int", 0x8: "signed int", 0x9: "unsigned int", 0xA: "long",
    0xB: "signed long", 0xC: "unsigned long", 0xD: "void*", 0xE: "float", 0xF: "double",
    0x10: "long double", 0x14: "void", 0x15: "bool",
}
MODS = {1: "*", 2: "&", 3: "const ", 4: "volatile "}

# attribute names (value >> 4)
AT_SIBLING, AT_LOCATION, AT_NAME = 0x001, 0x002, 0x003
AT_FUND_TYPE, AT_MOD_FUND_TYPE, AT_USER_DEF_TYPE, AT_MOD_U_D_TYPE = 0x005, 0x006, 0x007, 0x008
AT_BYTE_SIZE, AT_LOW_PC, AT_HIGH_PC, AT_VIRTUAL = 0x00B, 0x011, 0x012, 0x030


def parse(debug: bytes) -> list[tuple]:
    """Return a list of (offset, tag, attrs_dict, parent_offset)."""
    out = []
    stack: list[tuple[int, int]] = []  # (die offset, sibling offset)
    off, end = 0, len(debug)
    while off + 4 <= end:
        length = struct.unpack_from("<I", debug, off)[0]
        if length < 8:
            off += max(length, 4)
            continue
        tag = struct.unpack_from("<H", debug, off + 4)[0]
        attrs = {}
        p, stop = off + 6, off + length
        while p + 2 <= stop:
            at = struct.unpack_from("<H", debug, p)[0]
            p += 2
            form, name = at & 0xF, at >> 4
            if form in (1, 2):  # addr, ref
                val = struct.unpack_from("<I", debug, p)[0]; p += 4
            elif form == 3:  # block2
                n = struct.unpack_from("<H", debug, p)[0]; val = debug[p + 2 : p + 2 + n]; p += 2 + n
            elif form == 4:  # block4
                n = struct.unpack_from("<I", debug, p)[0]; val = debug[p + 4 : p + 4 + n]; p += 4 + n
            elif form == 5:  # data2
                val = struct.unpack_from("<H", debug, p)[0]; p += 2
            elif form == 6:  # data4
                val = struct.unpack_from("<I", debug, p)[0]; p += 4
            elif form == 7:  # data8
                val = struct.unpack_from("<Q", debug, p)[0]; p += 8
            elif form == 8:  # string
                z = debug.index(b"\0", p); val = debug[p:z].decode("latin1"); p = z + 1
            else:
                break  # unknown form: stop decoding this entry's attributes
            attrs[name] = val
        while stack and stack[-1][1] <= off:
            stack.pop()
        parent = stack[-1][0] if stack else None
        out.append((off, tag, attrs, parent))
        sib = attrs.get(AT_SIBLING)
        if sib is not None and sib > off + length:
            stack.append((off, sib))
        off += length
    return out


def location_offset(block: bytes) -> int | None:
    """Decode a member location: typically OP_CONST n ; OP_ADD -> n."""
    p, stack = 0, []
    while p < len(block):
        op = block[p]; p += 1
        if op in (1, 2, 3, 4):
            v = struct.unpack_from("<I", block, p)[0]; p += 4
            if op == 4:
                stack.append(v)
        elif op == 7:  # OP_ADD
            continue
        elif op in (5, 6):
            continue
        else:
            return None
    return stack[-1] if stack else None


def main(elf_path: str, out_path: str) -> None:
    d = open(elf_path, "rb").read()
    shoff = struct.unpack_from("<I", d, 0x20)[0]
    shentsize, shnum, shstrndx = struct.unpack_from("<HHH", d, 0x2E)
    sh = [struct.unpack_from("<IIIIIIIIII", d, shoff + i * shentsize) for i in range(shnum)]
    stroff = sh[shstrndx][4]
    sec = {d[stroff + s[0] : d.index(b"\0", stroff + s[0])].decode(): s for s in sh}
    dbg = sec[".debug"]
    debug = d[dbg[4] : dbg[4] + dbg[5]]
    dies = parse(debug)
    with open(out_path, "wb") as f:
        pickle.dump(dies, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"{len(dies)} entries parsed from {len(debug):#x} bytes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
