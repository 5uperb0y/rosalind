def complement(dna):
    """Complementing a DNA sequence."""
    return dna.translate(str.maketrans("ATCG", "TAGC"))
def revp_bf(dna):
    """Find a list of all palindromes' positions and their length, in the DNA
    sequence using brute force.

    Args:
        dna (str): A DNA string composed of nucleotides ("A", "T", "C", "G").

    Returns:
        list: A list of tuple, recording the position and length of every
              reverse palindrome, like [(<position>, <length>)]
    """
    return [
        (i + 1, j - i)
        for j in range(len(dna) + 1)
        for i in range(j)
        if dna[i:j] == complement(dna[i:j])[::-1]
    ]
def revp_me(dna):
    """Find a list of all palindromes' positions and their length, in the DNA
    sequence using middle expansion approach.

    Args:
        dna (str): A DNA string composed of nucleotides ("A", "T", "C", "G").

    Returns:
        list: A list of tuple, recording the position and length of every
              reverse palindrome, like [(<position>, <length>)]
    """
    palindromes = []
    for mid in range(1, len(dna)):
        for span in range(1, min(mid, len(dna) - mid) + 1):
            left_nt = dna[mid - span]
            right_nt = dna[mid - 1 + span]
            if left_nt == complement(right_nt):
                palindromes.append((mid - span + 1, span * 2))
            else:
                break
    return palindromes
def extend(dna, mid, start_span=1):
    """Extend the palindrome from the middle point to the maximum span.

    Args:
        dna (str): A DNA string composed of nucleotides ("A", "T", "C", "G").
        mid (int): Index of the middle point from which to check symmetry.
        start_span (int): Initial distance from the middle to start checking.

    Returns:
        int: Maximum span where the sequence remains a palindrome.
    """
    max_span = start_span
    for span in range(start_span, min(mid, len(dna) - mid) + 1):
        left_nt = dna[mid - span]
        right_nt = dna[mid - 1 + span]
        if left_nt == complement(right_nt):
            max_span = span
        else:
            break
    return max_span
def revp_manacher(dna):
    """Find a list of all palindromes' positions and their length, in the DNA
    sequence using the Manacher's algorithm.
    
    Args:
        dna (str): A DNA string composed of nucleotides ("A", "T", "C", "G").

    Returns:
        list: A list of tuple, recording the position and length of every
              reverse palindrome, like [(<position>, <length>)]
    """
    max_spans = [-1] * len(dna)
    right = center = 0
    for mid in range(1, len(dna)):
        if mid < right:
            mirror = 2 * center - mid
            max_spans[mid] = min(max_spans[mirror], right - mid)
        else:
            max_spans[mid] = 0
        max_spans[mid] = extend(dna, mid, max_spans[mid])
        if max_spans[mid] + mid > right:
            right = max_spans[mid] + mid
            center = mid
        else:
            pass
    return [
        (idx - span + 1, span * 2)
        for idx, max_span in enumerate(max_spans)
        for span in range(1, max_span + 1)
    ]
def read_fasta(path):
    """Read FASTA into a dictionary, like {<read id>: <sequence>}"""
    with open(path, "r") as file:
        reads = {}
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                id = line[1:]
                reads[id] = ""
            else:
                reads[id] = reads[id] + line
    return reads
def rosalind_revp(path):
    reads = read_fasta(path)
    for seq in reads.values():
        palindromes = [x for x in revp_manacher(seq) if x[1] >= 4]
        for start, palindrome_length in palindromes:
            print(start, palindrome_length)