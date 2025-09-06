import random
def partition(arr: list[int], pivot_index: int, L: int, R: int) -> tuple[int, int]:
    """3-way partition: elements < pivot | = pivot | > pivot.
    
    Args:
        arr: list of integer sequence to partition in-place
        pivot_index: Index of pivot element
        L: Left boundary (inclusive)
        R: Right boundary (inclusive)
    
    Returns:
        (left_bound, right_bound) of equal elements
    """
    pivot = arr[pivot_index]
    l, i, r = L, L, R
    while i <= r:
        if arr[i] < pivot:
            arr[i], arr[l] = arr[l], arr[i]
            l = l + 1
            i = i + 1
        elif arr[i] > pivot:
            arr[i], arr[r] = arr[r], arr[i]
            r = r - 1
        else:
            i = i + 1
    return l, r

def qs(arr: list[int]) -> list[int]:
    """Sort an integer sequence in-place using randomized quicksort.
    
    Args:
        arr: an list of integer sequence to sort
    
    Returns:
        The same list, sorted in ascending order
    """
    def quick_sort(arr, L, R):
        if L >= R:
            return arr
        pivot_index = random.randint(L, R)
        l, r = partition(arr, pivot_index, L, R)
        quick_sort(arr, L, l - 1)
        quick_sort(arr, r + 1, R)
    quick_sort(arr, 0, len(arr) - 1)
    return arr

def rosalind_qs(path):
    with open(path, "r") as f:
        lines = f.readlines()
        seq = list(map(int, lines[1].strip().split()))
        output = " ".join(map(str, qs(seq)))
        print(output)
