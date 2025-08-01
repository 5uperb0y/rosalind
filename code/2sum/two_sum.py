def two_sum(l, target):
    """Find the first indice (i, j) where l[i] + l[j] == target, i < j.

    Args:
        l (list): A list of integers.
        target (int): The target sum to find.
    
    Returns:
        tuple: A tuple of indices (i, j) if a pair is found, otherwise -1.
    """
    diffs = {}
    for i, num in enumerate(l):
        diff = target - num
        if  diff in diffs.keys():
            return (diffs[diff], i) 
        diffs[num] = i
    return -1
def rosalind_2sum(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            l = list(map(int, line.strip().split()))
            out = two_sum(l, 0)
            if out == -1:
                print("-1")
            else:
                print(f"{out[0] + 1} {out[1] + 1}")