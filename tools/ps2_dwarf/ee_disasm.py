"""
Minimal but CORRECT R5900 (PS2 Emotion Engine) disassembler.

Built because capstone's standard MIPS32 decoder silently misinterprets PS2-specific
opcodes: LQ (0x1E) and SQ (0x1F) collide with MIPS32R2's SPECIAL3/EXT encoding, so
capstone prints a plausible-looking but WRONG "ext $s0, $sp, 0, 1" for what is actually
"sq $s0, 0($sp)". Confirmed by hand-decoding the raw opcode/rs/rt/immediate fields
against the real R5900 ISA (PCSX2's R5900OpcodeTables.cpp) rather than trusting output
that merely looks reasonable.

Only implements what the seven disintegration functions actually contain: standard
MIPS-III integer ops, branches, LQ/SQ, and the couple of MMI opcodes observed (PADDUB
via the MMI1 sub-table). This is not a general-purpose EE disassembler.
"""

import struct

REGS = ["zero","at","v0","v1","a0","a1","a2","a3","t0","t1","t2","t3","t4","t5","t6","t7",
        "s0","s1","s2","s3","s4","s5","s6","s7","t8","t9","k0","k1","gp","sp","fp","ra"]

def r(n): return f"${REGS[n]}"

def signed16(v):
    return v - 0x10000 if v & 0x8000 else v

def decode(word, addr):
    op = (word >> 26) & 0x3F
    rs = (word >> 21) & 0x1F
    rt = (word >> 16) & 0x1F
    rd = (word >> 11) & 0x1F
    sa = (word >> 6) & 0x1F
    funct = word & 0x3F
    imm = word & 0xFFFF
    simm = signed16(imm)
    target = (word & 0x3FFFFFF)

    if word == 0:
        return "nop"

    if op == 0x00:  # SPECIAL
        if funct == 0x00: return f"sll {r(rd)}, {r(rt)}, {sa}" if word else "nop"
        if funct == 0x02: return f"srl {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x03: return f"sra {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x04: return f"sllv {r(rd)}, {r(rt)}, {r(rs)}"
        if funct == 0x06: return f"srlv {r(rd)}, {r(rt)}, {r(rs)}"
        if funct == 0x07: return f"srav {r(rd)}, {r(rt)}, {r(rs)}"
        if funct == 0x08: return f"jr {r(rs)}"
        if funct == 0x09: return f"jalr {r(rd)}, {r(rs)}"
        if funct == 0x0A: return f"movz {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x0B: return f"movn {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x10: return f"mfhi {r(rd)}"
        if funct == 0x12: return f"mflo {r(rd)}"
        if funct == 0x18: return f"mult {r(rs)}, {r(rt)}"
        if funct == 0x19: return f"multu {r(rs)}, {r(rt)}"
        if funct == 0x1A: return f"div {r(rs)}, {r(rt)}"
        if funct == 0x1B: return f"divu {r(rs)}, {r(rt)}"
        if funct == 0x20: return f"add {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x21: return f"addu {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x22: return f"sub {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x23: return f"subu {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x24: return f"and {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x25: return f"or {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x26: return f"xor {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x27: return f"nor {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x2A: return f"slt {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x2B: return f"sltu {r(rd)}, {r(rs)}, {r(rt)}"
        if funct == 0x3C: return f"dsll32 {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x38: return f"dsll {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x3A: return f"dsrl {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x3B: return f"dsra {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x3E: return f"dsrl32 {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x3F: return f"dsra32 {r(rd)}, {r(rt)}, {sa}"
        if funct == 0x0C: return "syscall"
        if funct == 0x0D: return f"break {sa}"
        if funct == 0x0F: return "sync"
        return f".special funct={funct:#x} ({word:08x})"

    if op == 0x01:  # REGIMM
        names = {0:"bltz",1:"bgez",2:"bltzl",3:"bgezl",16:"bltzal",17:"bgezal"}
        nm = names.get(rt, f"regimm_{rt}")
        return f"{nm} {r(rs)}, {addr+4+simm*4:#x}"

    if op == 0x02: return f"j {(addr & 0xF0000000) | (target << 2):#x}"
    if op == 0x03: return f"jal {(addr & 0xF0000000) | (target << 2):#x}"
    if op == 0x04: return f"beq {r(rs)}, {r(rt)}, {addr+4+simm*4:#x}"
    if op == 0x05: return f"bne {r(rs)}, {r(rt)}, {addr+4+simm*4:#x}"
    if op == 0x06: return f"blez {r(rs)}, {addr+4+simm*4:#x}"
    if op == 0x07: return f"bgtz {r(rs)}, {addr+4+simm*4:#x}"
    if op == 0x08: return f"addi {r(rt)}, {r(rs)}, {simm}"
    if op == 0x09: return f"addiu {r(rt)}, {r(rs)}, {simm}"
    if op == 0x0A: return f"slti {r(rt)}, {r(rs)}, {simm}"
    if op == 0x0B: return f"sltiu {r(rt)}, {r(rs)}, {simm}"
    if op == 0x0C: return f"andi {r(rt)}, {r(rs)}, {imm:#x}"
    if op == 0x0D: return f"ori {r(rt)}, {r(rs)}, {imm:#x}"
    if op == 0x0E: return f"xori {r(rt)}, {r(rs)}, {imm:#x}"
    if op == 0x0F: return f"lui {r(rt)}, {imm:#x}"
    if op == 0x14: return f"beql {r(rs)}, {r(rt)}, {addr+4+simm*4:#x}"
    if op == 0x15: return f"bnel {r(rs)}, {r(rt)}, {addr+4+simm*4:#x}"
    if op == 0x16: return f"blezl {r(rs)}, {addr+4+simm*4:#x}"
    if op == 0x17: return f"bgtzl {r(rs)}, {addr+4+simm*4:#x}"

    if op == 0x1C:  # MMI
        # funct 0x08 -> MMI0 class, sub-dispatched by sa (tbl_MMI0)
        if funct == 0x08:
            mmi0 = {0:"paddw",1:"psubw",2:"pcgtw",3:"pmaxw",4:"paddh",5:"psubh",6:"pcgth",
                    7:"pmaxh",8:"paddb",9:"psubb",10:"pcgtb",16:"paddsw",17:"psubsw",
                    18:"pextlw",19:"ppacw",20:"paddsh",21:"psubsh",22:"pextlh",23:"ppach",
                    24:"paddsb",25:"psubsb",26:"pextlb",27:"ppacb",30:"pext5",31:"ppac5"}
            nm = mmi0.get(sa, f"mmi0_sa{sa}")
            return f"{nm} {r(rd)}, {r(rs)}, {r(rt)}"
        # only decoding what's actually observed: funct 0x28 -> MMI1 class,
        # sub-dispatched by sa; sa=24 -> PADDUB per tbl_MMI1
        if funct == 0x28:
            mmi1 = {1:"pabsw",2:"pceqw",3:"pminw",4:"padsbh",5:"pabsh",6:"pceqh",7:"pminh",
                    10:"pceqb",16:"padduw",17:"psubuw",18:"pextuw",20:"padduh",21:"psubuh",
                    22:"pextuh",24:"paddub",25:"psubub",26:"pextub",27:"qfsrv"}
            nm = mmi1.get(sa, f"mmi1_sa{sa}")
            return f"{nm} {r(rd)}, {r(rs)}, {r(rt)}"
        return f".mmi funct={funct:#x} sa={sa} ({word:08x})"

    if op == 0x1E:  # LQ (128-bit load quadword) -- collides with std MIPS EXT
        return f"lq {r(rt)}, {simm}({r(rs)})"
    if op == 0x1F:  # SQ (128-bit store quadword) -- collides with std MIPS EXT
        return f"sq {r(rt)}, {simm}({r(rs)})"
    if op == 0x36:  # LQC2 -- load quadword to a VU0 vector register
        return f"lqc2 $vf{rt}, {simm}({r(rs)})"
    if op == 0x3E:  # SQC2
        return f"sqc2 $vf{rt}, {simm}({r(rs)})"

    if op == 0x20: return f"lb {r(rt)}, {simm}({r(rs)})"
    if op == 0x21: return f"lh {r(rt)}, {simm}({r(rs)})"
    if op == 0x23: return f"lw {r(rt)}, {simm}({r(rs)})"
    if op == 0x24: return f"lbu {r(rt)}, {simm}({r(rs)})"
    if op == 0x25: return f"lhu {r(rt)}, {simm}({r(rs)})"
    if op == 0x28: return f"sb {r(rt)}, {simm}({r(rs)})"
    if op == 0x29: return f"sh {r(rt)}, {simm}({r(rs)})"
    if op == 0x2B: return f"sw {r(rt)}, {simm}({r(rs)})"
    if op == 0x37: return f"ld {r(rt)}, {simm}({r(rs)})"
    if op == 0x3F: return f"sd {r(rt)}, {simm}({r(rs)})"
    if op == 0x31: return f"lwc1 $f{rt}, {simm}({r(rs)})"
    if op == 0x39: return f"swc1 $f{rt}, {simm}({r(rs)})"

    if op == 0x11:  # COP1 (FPU)
        fmt = rs
        if fmt == 0x10:  # single-precision
            f_funct = word & 0x3F
            fd = (word >> 6) & 0x1F
            fs = (word >> 11) & 0x1F
            ft = (word >> 16) & 0x1F
            names = {0:"add.s",1:"sub.s",2:"mul.s",3:"div.s",4:"sqrt.s",5:"abs.s",
                     6:"mov.s",7:"neg.s",36:"cvt.w.s",40:"max.s",41:"min.s",
                     48:"c.f.s",50:"c.eq.s",52:"c.lt.s",54:"c.le.s"}
            if f_funct in names:
                return f"{names[f_funct]} $f{fd}, $f{fs}, $f{ft}"
            return f".cop1.s funct={f_funct:#x}"
        if fmt == 0x14:  # W format (integer) -- only CVT.S.W observed
            fd = (word >> 6) & 0x1F
            fs = (word >> 11) & 0x1F
            f_funct = word & 0x3F
            if f_funct == 0x20:
                return f"cvt.s.w $f{fd}, $f{fs}"
            return f".cop1.w funct={f_funct:#x}"
        if fmt == 4: return f"mtc1 {r(rt)}, $f{(word>>11)&0x1F}"
        if fmt == 0: return f"mfc1 {r(rt)}, $f{(word>>11)&0x1F}"
        if fmt == 8:
            cc = (word >> 18) & 7
            branch_kind = "bc1t" if (word >> 16) & 1 else "bc1f"
            return f"{branch_kind} {addr+4+simm*4:#x}"
        return f".cop1 fmt={fmt:#x}"

    return f".unknown op={op:#x} ({word:08x})"


def disasm_range(data, va, size, main_va=0x100000, main_off=0x100):
    off = va - main_va + main_off
    out = []
    for i in range(0, size, 4):
        word = struct.unpack_from("<I", data, off + i)[0]
        out.append((va + i, word, decode(word, va + i)))
    return out


if __name__ == "__main__":
    import sys
    d = open(sys.argv[1], "rb").read()
    va = int(sys.argv[2], 16)
    size = int(sys.argv[3])
    for a, w, txt in disasm_range(d, va, size):
        print(f"  {a:#08x}: [{w:08x}] {txt}")
