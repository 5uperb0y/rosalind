from revp import revp_bf, revp_me, revp_manacher
import timeit
dna = "TCAATGCATGCGGGTCTATATGCAT" * 100
print(f"Using DNA sequnce TCAATGCATGCGGGTCTATATGCAT * 100")
print("Timing revp_bf:")
print(timeit.timeit('revp_bf(dna)', globals=globals(), number=1))
print("Timing revp_me:")
print(timeit.timeit('revp_me(dna)', globals=globals(), number=1))
print("Timing revp_manacher:")
print(timeit.timeit('revp_manacher(dna)', globals=globals(), number=1))
dna = "ATAT" * 100
print(f"Using DNA sequnce ATAT * 100")
print("Timing revp_bf:")
print(timeit.timeit('revp_bf(dna)', globals=globals(), number=1))
print("Timing revp_me:")
print(timeit.timeit('revp_me(dna)', globals=globals(), number=1))
print("Timing revp_manacher:")
print(timeit.timeit('revp_manacher(dna)', globals=globals(), number=1))