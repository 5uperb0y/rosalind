
def par3_build(arr: list[int]) -> list[int]:
    """Reorders integers into < pivot, = pivot, and > pivot partitions.

    Args:
        arr: List of integers, where the first integer is the pivot.

    Returns:
        A new list with integers partitioned around the pivot.
    """
    L, mid, R = [], [arr[0]], []  # 新增了 mid 來儲存與基準值相等的數字
    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            R.append(arr[i])
        elif arr[i] < arr[0]:
            L.append(arr[i])
        else:
            mid.append(arr[i])
    return L + mid + R

def par3_nested(arr: list[int]) -> list[int]:
    """Reorders integers into < pivot, = pivot, and > pivot partitions.

    Args:
        arr: List of integers, where the first integer is the pivot.

    Returns:
        A new list with integers partitioned around the pivot.
    """
    # 等於基準值的數字範圍
    L, R = 1, 1
    for i in range(1, len(arr)):
        # 第一輪比較，區分 <= 和 > 基準值的數字
        # 把小於等於基準值的數字放到 R 的左邊
        if arr[i] <= arr[0]: 
            arr[i], arr[R] = arr[R], arr[i]
            # 第二輪比較，區分 < 和 = 基準值的數字
            # 把小於基準值的數字放到 L 的左邊
            if arr[R] < arr[0]:
                arr[L], arr[R] = arr[R], arr[L]
                L = L + 1
            R = R + 1
    arr[0], arr[L-1] = arr[L-1], arr[0]
    return arr

def par3_dnf(arr: list[int]) -> list[int]:
    """
    Partitions `arr` around the first element (pivot) using the Dutch National Flag algorithm.
    
    Args:
        arr: List of elements to partition, with the first element as the pivot.
    
    Returns:
        Partitioned list with elements < pivot, = pivot, and > pivot.
    """ 
    L, R = 1, len(arr) - 1
    i = 1
    while i <= R:
        if arr[i] < arr[0]:
            arr[i], arr[L] = arr[L], arr[i]
            L = L + 1
            i = i + 1
        elif arr[i] > arr[0]:
            arr[i], arr[R] = arr[R], arr[i]
            R = R - 1
        else:
            i = i + 1
    arr[0], arr[L - 1] = arr[L - 1], arr[0]
    return arr

def rosalind_par3(path):
    with open(path, "r") as f:
        lines = f.readlines()
        arr = list(map(int, lines[1].strip().split()))
        print(" ".join(map(str, par3_dnf(arr))))

rosalind_par3("rosalind_par3.txt")