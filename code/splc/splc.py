import re
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
def rm_introns(dna, introns):
    """Remove intron strings from a DNA string using replace().

    Args:
        dna (str): A DNA sequence that starts with ATG and ends with TGA, TAG, or TAA.
        introns (list): Intron strings to be removed from the DNA string.

    Return:
        str: A modified DNA string with all specified introns removed.
    """
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna
def rm_introns_with_regex(dna, introns):
    """Remove intron strings from a DNA string using regular expression substitution.

    Args:
        dna (str): A DNA sequence that starts with ATG and ends with TGA, TAG, or TAA.
        introns (list): Intron strings to be removed from the DNA string.

    Return:
        str: A modified DNA string with all specified introns removed.
    """
    return re.sub(r"|".join(introns), "", dna)
def rosalind_splc(path):
    reads = []
    with open(path, "r") as file:
        for line in file:
            if line.startswith(">"):
                reads.append("")
            else:
                reads[-1] = reads[-1] + line.strip()
    dna, introns = reads[0], reads[1:]
    print(dna2aa(rm_introns(dna, introns)))