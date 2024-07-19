def edit(S, T):
    """Calculate the edit distance between two protein strings.

    Args:
        S (str): First protein string.
        T (str): Second protein string.

    Returns:
        int: Edit distance between S and T
    """
    # The edit distance between S's and T's substrings
    dist = [
        [0] * (len(T) + 1)
        for _ in range(len(S) + 1)
        ]
    for s in range(1, len(S) + 1):
        dist[s][0] = s
    for t in range(1, len(T) + 1):
        dist[0][t] = t
    for s in range(len(S)):
        for t in range(len(T)):
            if S[s] == T[t]:
                dist[s + 1][t + 1] = dist[s][t]
            else:
                dist[s + 1][t + 1] = min(dist[s][t], dist[s + 1][t], dist[s][t + 1]) + 1
    return dist[-1][-1]
def rosalind_edit(path):
    with open(path, "r") as f:
        reads = []
        for line in f:
            if line.startswith(">"):
                reads.append("")
            else:
                reads[-1] = reads[-1] + line.strip()
    print(edit(reads[0], reads[1]))