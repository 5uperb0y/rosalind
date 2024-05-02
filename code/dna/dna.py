def nt_freq(dna):
    """Counting DNA nucleotide
    """
    return " ".join(str(dna.count(nt)) for nt in "ACGT")