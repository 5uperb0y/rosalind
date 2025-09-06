def sift_down(l: list[int], i: int, n: int):
    candidates = [idx for idx in (i, 2 * i + 1, 2 * i + 2) if idx < n]
    largest = max(candidates, key=lambda x: l[x])
    if largest != i:
        l[largest], l[i] = l[i], l[largest]
        sift_down(l, largest ,n)

def heapify(l: list[int], k: int) -> list[int]:
    """Builds a max-heap of size k from a list of integer.

    Args:
        l: Input list of numbers.
        k: Number of elements to keep in the heap.

    Returns:
        The modified list where the first k elements form a max-heap.
    """
    # 先取出前 k 個數字建立 heap，此時還不是最終型態
    for idx in range(k // 2 - 1, -1, -1):
        sift_down(l, idx, k)
    # 如果根節點大於剩餘的數字，表示 heap 的總和還有縮小的空間
    for idx in range(k, len(l)):
        if l[0] > l[idx]:
            l[0] = l[idx]
            sift_down(l, 0, k)
    return l

def ps(l: list[int], k: int) -> list[int]:
    """Finds the k smallest integers using heap sort.

    Args:
        l: Input list of integers.
        k: Number of smallest integers to extract.

    Returns:
        A list containing the k smallest integers in ascending order.
    """
    hp = heapify(l, k)
    for end in range(k - 1, 0, -1):
        hp[0], hp[end] = hp[end], hp[0]
        sift_down(hp, 0, end)
    return(hp[:k])

def rosalind_ps(path):
    with open(path, "r") as f:
        lines = f.readlines()
        k = int(lines[2].strip())
        l = list(map(int, lines[1].strip().split()))
        print(" ".join(map(str, ps(l, k))))