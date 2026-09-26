/*
 * Dancing Mad -- FFXI PC client struct definitions.
 *
 * Extracted from tools/ffxi_symbols_ida.py's STRUCT_DECLS block, with one deliberate change:
 * `unsigned __int8` (an IDA/MSVC-specific type extension, not standard C) is replaced with the
 * portable `unsigned char` -- identical 1-byte unsigned semantics, but this substitution was
 * necessary rather than assumed, since Ghidra's C parser is not guaranteed to recognize IDA's
 * compiler-extension typedefs. Every field offset, size, and comment is otherwise unchanged.
 *
 * Usage in Ghidra: Data Type Manager -> right-click your program's archive -> "Parse C Source..."
 * -> add this file. Do this BEFORE running ffxi_symbols_ghidra.py so g_pProcessor (0x1047CF7C)
 * can be typed as CMoProcessor* -- the naming script does not depend on this step, but is more
 * useful with it done first.
 *
 * See docs/FINDINGS.md for what each field means and how it was confirmed -- the inline comments
 * below are a summary, not the full evidence.
 */

struct CMoProcessor
{
  void *vftable;
  float ScratchMatrices[512];        /* +0x004: 32 scratch 4x4 matrices (pool storage) */
  unsigned char pad_0804[12];
  float RotationMatrix[64];          /* +0x810: 4 identity-initialized 4x4 matrices */
  unsigned char pad_0910[256];
  float *ScratchMatrixFreeList[32];  /* +0xA10: pool slot pointers -> ScratchMatrices */
  int ScratchMatrixStackTop;         /* +0xA90: slots in use; acquire = list[top++] */
  unsigned char pad_0A94[12];
  float TransposeScratch[16];        /* +0xAA0: absent in the lowest tier (0xAA0-byte alloc) */
  float TransposeScratchTemp[16];    /* +0xAE0 */
  unsigned char pad_0B20[144];     /* to 0xBB0, the two larger tiers' allocation size */
};
struct CXiSkeletonActorRes
{
  unsigned char CMoTask_base[52];  /* CMoTask is exactly 0x34 bytes */
  void *pLinkedActor;                /* +0x34 */
  void *pfnOnLoaded;                 /* +0x38 */
  int loadState;                     /* +0x3C */
  int field_40;                      /* +0x40, zeroed in the constructor */
  int resourceId;                    /* +0x44 */
};
