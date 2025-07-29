def mer(S, T):
    """Merges two sorted lists S and T into a single sorted list.

    Args:
        S (list): A sorted list of integers.
        T (list): Another sorted list of integers.

    Returns:
        list: A merged sorted list containing all integers from S and T.
    """
    merged = []
    s, t = 0, 0
    while s < len(S) and t < len(T):
        if S[s] <= T[t]:
            merged.append(S[s])
            s = s + 1
        else:
            merged.append(T[t])
            t = t + 1
    merged.extend(S[s:])
    merged.extend(T[t:])
    return merged
def ms(l):
    """Sorts a list of integers using the merge sort algorithm.

    Args:
        l (list): A list of integers to be sorted.

    Returns:
        list: A sorted list of integers.
    """
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = ms(l[:mid])
    right = ms(l[mid:])
    return mer(left, right)
def rosalind_ms(path):
    with open(path, "r") as f:
        lines = f.readlines()
        l = [int(x) for x in lines[1].strip().split()]
        out = ms(l)
        print(" ".join(map(str, out)))