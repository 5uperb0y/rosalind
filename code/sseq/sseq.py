def sseq(dna, motif):
    """Finding the first position of a spliced motif in a DNA string.

    Args:
        dna (str): A DNA string.
        motif (str): A DNA motif to be found in the dna string. 
    
    Return:
        list: A list of 1-based positions where the motif is found as
              a subsequence in the DNA string.
    """
    motif_pos = []
    for pos, nt in enumerate(dna):
        if motif:
            if nt == motif[0]:
                motif_pos.append(pos + 1) 
                motif = motif[1:]
            else:
                pass
        else:
            break
    return motif_pos
def rosalind_sseq(path):
    with open(path, "r") as f:
        reads = []
        for line in f:
            if line.startswith(">"):
                reads.append("")
            else:
                reads[-1] = reads[-1] + line.strip()
    dna, motif = reads[0], reads[1]
    print(" ".join(map(str, sseq(dna, motif))))
def find_spliced_motifs_dp(dna, motif):
    """Finding all positions of a spliced motif in a DNA string using
    dynamic programming.
    
    Args:
        dna (str): A DNA string.
        motif (str): A DNA motif to be found in the dna string. 
    
    Return:
        set: A set of 1-based positions where the motif is found as
              a subsequence in the DNA string.
    """
    dp = [set() for _ in range(len(motif) + 1)]
    dp[0].add(())
    for i in range(len(dna)):
        for j in reversed(range(len(motif))):
            if dna[i] == motif[j]:
                for prev in dp[j]:
                    dp[j + 1].add(prev + (i + 1, ) )
            else:
                pass
    return dp[-1]
def find_spliced_motifs_rc(dna, motif):
    """Finding all positions of a spliced motif in a DNA string using
    recursion.
    
    Args:
        dna (str): A DNA string.
        motif (str): A DNA motif to be found in the dna string. 
    
    Return:
        list: A list of 1-based positions where the motif is found as
              a subsequence in the DNA string.
    """
    def search(start, path, index):
        if index == len(motif):
            return {path}
        else:
            pass
        results = set()
        for i in range(start, len(dna)):
            if dna[i] == motif[index]:
                results.update(search(i + 1, path + (i + 1, ), index + 1))
            else:
                pass
        return results
    return search(0, (), 0)