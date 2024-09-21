import sys, gc

genSeq = (x for x in range(1000000))
listSeq = [x for x in range(1000000)]

print(f"Size of genSeq: {sys.getsizeof(genSeq)}")
print(f"Size of listSeq: {sys.getsizeof(listSeq)}")

del listSeq
gc.collect()