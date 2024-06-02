def swap(l):
    """
    Generate all possible sequences of a tuple by reversing segments.

    Args:
        l (tuple): Input tuple, e.g., (1, 2).

    Returns:
        set: Set of tuples with reversed segments, e.g., {(1, 2), (2, 1)}.
    """
    return {
        l[:i] + l[i:j][::-1] + l[j:]
        for j in range(len(l) + 1)
        for i in range(j)
    }
def get_next_steps(curr, visited):
    """Generates next steps by swapping elements in `curr`, excluding those in `visited`.

    Args:
        curr (set): Current states.
        visited (set): States to exclude.

    Returns:
        set: Next possible states.
    """
    next_steps = set()
    for e in curr:
        next_steps.update(swap(e).difference(visited))
    return next_steps
def rev_dist(s1, s2):
    """Calculate the minimum number of reversals required to transform tuple s1 to tuple s2
    using bidirectional broad-first search.

    Args:
        s1 (tuple): Starting tuple.
        s2 (tuple): Target tuple.

    Returns:
        int: Minimum number of reversals required, or -1 if transformation is not possible.
    """
    f_curr, f_visited, b_curr, b_visited = {s1}, {s1}, {s2}, {s2}
    dist = 0
    while f_curr and b_curr:
        if f_curr.intersection(b_curr):
            return dist
        else:
            dist = dist + 1
            f_curr = get_next_steps(f_curr, f_visited)
            f_visited.update(f_curr)
        if b_curr.intersection(f_curr):
            return dist
        else:
            dist = dist + 1
            b_curr = get_next_steps(b_curr, b_visited)
            b_visited.update(b_curr)
    return -1
def rosalind_rear(path):
    with open(path, "r") as f:
        lines = [
            tuple(int(n) for n in line.strip().split())
            for line in f if line.strip()
            if not line.startswith("\n")
            ]
    return " ".join([
        str(rev_dist(lines[i], lines[i+1]))
        for i in range(0, len(lines), 2)
    ])