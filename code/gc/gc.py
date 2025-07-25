def gc(seq):
    """
    Calculate the GC content of a DNA sequence.

    Args:
        seq (str): A string representing a DNA sequence.

    Returns:
        float: The GC content as a percentage of the sequence.
    """
    return (seq.count("G") + seq.count("C")) * 100 / len(seq)
def rosalind_gc(fa_path):
    with open(fa_path, "r") as f:
        seqs = {}
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                id = line[1:]
                seqs[id] = ""
            else:
                seqs[id] = seqs[id] + line
    gcs = {
        id: gc(seq) for id, seq in seqs.items()
    }
    max_gc = max(gcs.items(), key=lambda item: item[1])
    print(max_gc[0])
    print(max_gc[1])
rosalind_gc("rosalind_gc.txt")