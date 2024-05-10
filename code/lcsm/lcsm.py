def read_fasta(path):
    """Read a fasta file into a dictionary
    """
    with open(path, "r") as f:
        reads = {}
        for line in f:
            if line.startswith(">"):
                key = line[1:].strip()
                reads[key] = ""
            else:
                reads[key] = reads[key] + line.strip()
        return reads
def lcs(strs):
    """Finding the longest common substring from multiple strings
    """
    min_s = min(strs, key = len)
    kmer = [
        min_s[i:i+k+1]
        for k in range(len(min_s) + 1)
        for i in range(len(min_s) - k)
    ]
    for mer in kmer[::-1]:
        if all(mer in s for s in strs):
            return mer
        else:
            pass
    return ""
def lcsm(fasta):
    """Finding the longest common nucleotide sequence from multiple sequences in a fasta file
    """
    seqs = list(read_fasta(fasta).values())
    return(lcs(seqs))