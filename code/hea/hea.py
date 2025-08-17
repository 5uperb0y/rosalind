def hea_williams(l: list[int]) -> list:
    """
    Constructs a max-heap from a list of integers using Williams' method.

    Args:
        l: The input list of integers.

    Returns:
        list: A list representing the max-heap.
    """
    heap = []
    for i, num in enumerate(l):
        heap.append(num)
        parent = (i - 1) // 2
        while i > 0 and heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
            parent = (i - 1)
    return heap
def sift_down(l: list[int], i: int) -> list:
    """Performs the sift-down operation on a binary heap to maintain the heap property.

    Args:
        l: The list representing the binary heap.
        i: The index of the element to sift down.

    Returns:
        list: The modified list after the sift-down operation.
    """
    n = len(l)
    candidates = [idx for idx in [i, 2 * i + 1, 2 * i + 2] if idx < n]
    largest = max(candidates, key=lambda idx: l[idx])
    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        return sift_down(l, largest)
    return l
def hea_floyd(l: list[int]) -> list:
    """Constructs a max-heap from a list of integers using the Floyd's method.

    Args:
        l: The input list of integers to be transformed into a max-heap.

    Returns:
        list: The list transformed into a max-heap.
    """
    for i in range(len(l) // 2, -1, -1):
        l = sift_down(l, i)
    return l
def rosalind_hea(path: str):
    with open(path, "r") as f:
        l = list(map(int, f.readlines()[1].strip().split()))
    print(" ".join(map(str, hea_floyd(l))))