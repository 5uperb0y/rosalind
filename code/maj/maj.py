def maj_freq(l):
    """ Specify the majority element in a list by counting occurrences.

    Args:
        l (list): A list of positive integers.

    Returns:
        int: The majority element if it exists, otherwise -1.
    """
    freqs = {}
    for e in l:
        if e in freqs:
            freqs[e] = freqs[e] + 1
        else:
            freqs[e] = 1
    for e, freq in freqs.items():
        if freq > len(l) // 2:
            return e
    return -1

def maj_bm(l):
    """Specify the majority element in a list using Boyer-Moore voting algorithm.

    Args:
        l (list): A list of positive integers.
    Returns:
        int: The majority element if it exists, otherwise -1.
    """
    candidate = None
    freq = 0
    for e in l:
        if freq == 0:
            candidate = e
            freq = 1
        if e == candidate:
            freq = freq + 1
        else:
            freq = freq - 1
    if l.count(candidate) > len(l) // 2:
        return candidate
    return -1

def maj_rc(l):
    """Specify the majority element in a list using recursion.

    Args:
        l (list): A list of positive integers.
    
    Returns:
        int: The majority element if it exists, otherwise -1.
    """
    if not l:
        return -1
    
    if len(l) == 1:
        return l[0]

    mid = len(l) // 2
    left = maj_rc(l[:mid])
    right = maj_rc(l[mid:])

    if left == right:
        return left

    else:
        if l.count(left) > len(l) // 2:
            return left
        elif l.count(right) > len(l) // 2:
            return right
        else:
            return -1

def rosalind_maj(path):
    with open(path, "r") as f:
        lines = f.readlines()
        series = [
            [int(s) for s in line.strip().split()]
            for line in lines[1:]
        ]
    out = " ".join(str(maj_freq(s)) for s in series)
    print(out)