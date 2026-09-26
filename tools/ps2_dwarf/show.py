import pickle, sys
import os
_here = os.path.dirname(os.path.abspath(__file__))
C = pickle.load(open(os.path.join(_here, "classes.pkl"), "rb"))
def show(n, limit=60):
    r = C.get(n)
    if not r: print("MISSING", n); return
    sz = f"{r['size']:#x}" if r['size'] else "?"
    print(f"== {n} size={sz} bases={r['bases']} members={len(r['members'])} methods={len(r['methods'])}")
    for m in r["members"][:limit]:
        o = f"+{m[1]:#06x}" if m[1] is not None else "   ?   "
        print(f"   {o} {m[0]:26} {m[2]}")
    if len(r["members"]) > limit: print(f"   ... {len(r['members'])-limit} more")
for n in sys.argv[1:]: show(n)
