def lgis(l):
    """Longest Increasing Subsequence
    """
    lis_len = [1] * len(l)
    prev = [-1] * len(l)
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] > l[j] and lis_len[j] + 1 > lis_len[i]:
                lis_len[i] = lis_len[j] + 1
                prev[i] = j
            else:
                pass
    final_pos = max(range(len(l)), key=lambda x: lis_len[x]) 
    output = []
    while final_pos != -1:
        output.append(l[final_pos])
        final_pos = prev[final_pos]
    return output[::-1]
def rosalind_lgis(path):
    with open(path, "r") as f:
        nums = [ int(n) for n in f.readlines()[1].strip().split() ]
        print(" ".join([ str(n) for n in lgis(nums) ]))
        print(" ".join([ str(n) for n in lgis(nums[::-1])[::-1] ]))