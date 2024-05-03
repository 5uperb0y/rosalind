def reverse_complement(dna):
    """complementing a strand of dna
    """
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(comp[nt] for nt in dna[::-1])