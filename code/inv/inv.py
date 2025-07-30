def merge(S, T):
    s, t, inv = 0, 0, 0
    out = []
    while s < len(S) and t < len(T):
        if S[s] <= T[t]:
            out.append(S[s])
            s = s + 1
        else:
            out.append(T[t])
            t = t + 1
            inv = inv + len(S) - s
    out.extend(S[s:])
    out.extend(T[t:])
    return out, inv
def inv(l):
    if len(l) <= 1:
        return l, 0
    mid = len(l) // 2
    left, left_inv = inv(l[:mid])
    right, right_inv = inv(l[mid:])
    merged, merge_inv = merge(left, right)
    return merged, left_inv + right_inv + merge_inv
def rosalind_inv(path):
    with open(path, "r") as f:
        lines = f.readlines()
        l = list(map(int, lines[1].strip().split()))
    print(inv(l)[1])