def edta(S, T):
    """Align two strings using dynamic programming

    Args:
        S (str): First protein string.
        T (str): Second protein string.
    
    Returns:
        list: [Edit distance (str), aligned S (str), aligned T (str)]
    """
    dists = [ [0] * (len(T) + 1) for _ in range(len(S) + 1) ]
    edits = [ [-1] * (len(T) + 1) for _ in range(len(S) + 1) ] # 0: match, 1: insertion, 2: deletion
    for s in range(1, len(S) + 1):
        dists[s][0] = s
        edits[s][0] = 2
    for t in range(1, len(T) + 1):
        dists[0][t] = t
        edits[0][t] = 1
    # Fill DP tables
    for s in range(len(S)):
        for t in range(len(T)):
            if S[s] == T[t]:
                dists[s + 1][t + 1] = dists[s][t]
                edits[s + 1][t + 1] = 0
            else:
                choices = [dists[s][t], dists[s + 1][t], dists[s][t + 1]]
                dists[s + 1][t + 1] = min(choices) + 1
                edits[s + 1][t + 1] = choices.index(min(choices))
    # Reconstruct aligned sequences
    aln_s, aln_t = "", ""
    x, y = len(S), len(T)
    moves = [(1, 1), (0, 1), (1, 0)] # [match, insertion, deletion]
    while edits[x][y] >= 0:
        move_x, move_y = moves[edits[x][y]]
        aln_s = (S[x - 1] if move_x else "-") + aln_s
        aln_t = (T[y - 1] if move_y else "-") + aln_t
        x, y = x - move_x, y - move_y
    return([str(dists[-1][-1]), aln_s, aln_t])
def rosalind_edta(path):
    with open(path, "r") as f:
        reads = []
        for line in f:
            if line.startswith(">"):
                reads.append("")
            else:
                reads[-1] = reads[-1] + line.strip()
    print("\n".join(edta(reads[0], reads[1])))