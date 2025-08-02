
def two_sum(l, target, skip_index=None):
    """2sum with skip_index to avoid using the same element twice."""
    diffs = {}
    for i, num in enumerate(l):
        if i == skip_index:
            continue
        diff = target - num
        if diff in diffs:
            return (diffs[diff], i)
        diffs[num] = i
    return None
def three_sum(l, target):
    """Find the first three indices in `l` that add up to `target`.

    Args:
        l (list): List of integers.
        target (int): Target sum.

    Returns:
        tuple: A tuple of indices if a solution is found, otherwise None.
    """
    for i, num in enumerate(l):
        residual = target - num
        out = two_sum(l, residual, skip_index=i)
        if out is not None:
            return (i, out[0], out[1])
    return None
def rosalind_3sum(path):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            l = list(map(int, line.strip().split()))
            out = three_sum(l, 0)
            if out:
                print(f"{out[0] + 1} {out[1] + 1} {out[2] + 1}")
            else:
                print("-1")