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
def mer_rc(S, T):
    """Merges two sorted lists S and T into a single sorted list recursively.

    Args:
        S (list): A sorted list of integers.
        T (list): Another sorted list of integers.

    Returns:
        list: A merged sorted list containing all integers from S and T.
    """
    if not S:
        return T
    if not T:
        return S
    if S[0] <= T[0]:
        return [S[0]] + mer_rc(S[1:], T)
    else:
        return [T[0]] + mer_rc(S, T[1:])
def rosalind_mer(path):
    with open(path, "r") as f:
        lines = f.readlines()
        S = [int(x) for x in lines[1].strip().split()]
        T = [int(x) for x in lines[3].strip().split()]
    print(" ".join(map(str, mer(S, T))))