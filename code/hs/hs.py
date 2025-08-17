def sift_down(l: list[int], i: int, n: int):
    """
    Performs the sift-down operation on a binary heap to maintain the heap property.

    Args:
        l: The list representing the binary heap.
        i: The index of the current node to sift down.
        n: The size of the heap (number of valid elements in the list).

    Returns:
        None. The list `l` is modified in place.
    """
    candidates = [idx for idx in (i, 2 * i + 1, 2 * i + 2) if idx < n]
    largest = max(candidates, key=lambda x: l[x])
    if largest != i:
        l[largest], l[i] = l[i], l[largest]
        sift_down(l, largest ,n)
def heapify(l: list[int]) -> list[int]:
    """ Converts a list into a max-heap in-place.

    Args:
        l: The list of integers to be heapified.

    Returns:
        list: The same list, rearranged to satisfy the max-heap property.
    """
    n = len(l)
    for idx in range(n // 2 - 1, -1, -1):
        sift_down(l, idx, n)
    return l
def hs(l: list[int]) -> list[int]:
    """Performs a heap sort on the given list of integers.

    Args:
        l: The list of integers to be sorted.

    Returns:
        list: The sorted list of integers in ascending order.
    """
    hp = heapify(l)
    for end in range(len(l) - 1, 0, -1):
        hp[end], hp[0] = hp[0], hp[end]
        sift_down(hp, 0, end)
    return hp
def rosalind_hs(path):
    with open(path, "r") as f:
        l = list(map(int, f.readlines()[1].strip().split()))
        print(" ".join(map(str, hs(l))))