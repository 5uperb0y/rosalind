def reverse_complement(dna):
    return dna[::-1].translate("".maketrans("ATCG", "TAGC"))
def dna2aa(dna):
    """Translates a DNA sequence into an amino acid sequence using the standard genetic code.

    Args:
        dna (str): A DNA sequence.

    Returns:
        str: The corresponding amino acid sequence.
    """
    code = {
        "TTT": "F", "TTC": "F",
        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATT": "I", "ATC": "I", "ATA": "I",
        "ATG": "M",
        "GTT": "V", "GTA": "V", "GTC": "V", "GTG": "V",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TAT": "Y", "TAC": "Y",
        "CAT": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "AAT": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "TGT": "C", "TGC": "C",
        "TGG": "W",
        "CGT": "R", "CGA": "R", "CGC": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "GGT": "G", "GGA": "G", "GGC": "G", "GGG": "G",
        "TGA": "", "TAG": "", "TAA": ""
    }
    return "".join([
        code.get(dna[pos: pos + 3], "")
        for pos in range(0, len(dna), 3)
    ])
def orf(dna):
    """
    Identifies all open reading frames (ORFs) from all read frames in a DNA sequence
    that start with 'ATG' and end with a stop codon ('TAA', 'TAG', 'TGA').

    Args:
        dna (str): A DNA sequence.

    Returns:
        list: A list of ORF sequences.
    """
    orf_locs = []
    start_locs = [[], [], []]
    for pos, _ in enumerate(dna):
        frame = pos % 3
        codon = dna[pos: pos + 3]
        if codon == "ATG":
            start_locs[frame].append(pos)
        elif codon in ["TGA", "TAG", "TAA"]:
            while start_locs[frame]:
                orf_locs.append((start_locs[frame].pop(), pos))
        else:
            pass
    return [ dna[i:j] for i, j in orf_locs ]
def read_fasta(fasta):
    """Reads a FASTA format file and stores sequences in a dictionary.

    Args:
        fasta (str): Path to the FASTA file.

    Returns:
        dict: A dictionary with sequence identifiers as keys and sequences as values.
    """
    seqs = {}
    seq_id = ""
    with open(fasta, "r") as file:
        for line in file:
            if line.startswith(">"):
                seq_id = line[1:].strip()
                seqs[seq_id] = ""
            else:
                seqs[seq_id] = seqs[seq_id] + line.strip()
    return seqs
def rosalind_orf(fasta):
    seqs = read_fasta(fasta)
    for _, seq in seqs.items():
        orf_seqs = orf(seq) + orf(reverse_complement(seq))
        dedup_orf_seqs = sorted(set(orf_seqs), key=orf_seqs.index)
        for orf_seq in dedup_orf_seqs:
            print(dna2aa(orf_seq))