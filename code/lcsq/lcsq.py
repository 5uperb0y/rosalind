def lcsq(S, T):
    """Calculate and return the longest common subsequence (LCS) of two strings S and T.

    Args:
        S, T (str): The two input DNA strings.

    Return:
        str: A longest common subsequence of s1 and t.
    """
    # lcs denotes the longest subsequence of all s1's and s2's substring
    lcs = [
        [""] * (len(T) + 1)
        for _ in range(len(S) + 1)
        ]
    for s in range(len(S)):
        for t in range(len(T)):
            if S[s] == T[t]:
                lcs[s + 1][t + 1] = lcs[s][t] + S[s]
            else:
                lcs[s + 1][t + 1] = max(lcs[s + 1][t], lcs[s][t + 1], key=len)
    return lcs[-1][-1]
def rosalind_lcsq(path):
    with open(path, "r") as f:
        reads = []
        for line in f:
            if line.startswith(">"):
                reads.append("")
            else:
                reads[-1] = reads[-1] + line.strip()
    print(lcsq(reads[0], reads[1]))