def translate(rna):
    """Translate a RNA string into a proten string

    Args:
        rna (str): A RNA string composed of nucleotides ('U', 'C', 'A', 'G'), length must be a multiple of three.

    Returns:
        str: Amino acid sequence derived from the RNA
    """
    code = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",
    "GUU": "V", "GUA": "V", "GUC": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "CGU": "R", "CGA": "R", "CGC": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGA": "G", "GGC": "G", "GGG": "G",
    "UGA": "", "UAG": "", "UAA": ""
    }
    pos = 0
    protein = ""
    while code.get(rna[pos: pos + 3], ""):
        protein = protein + code.get(rna[pos: pos + 3], "")
        pos = pos + 3
    return protein