def par_list(arr: list[int]) -> list[int]:
    """
    Partitions the integer sequence around the first element (pivot).

    Args:
        arr: integer sequence to partition.

    Returns:
        Partitioned integer sequence with pivot in place.
    """
    L, R= [], []
    for i in range(1, len(arr)):
        if arr[i] <= arr[0]:
            L.append(arr[i])
        else:
            R.append(arr[i])
    return L + [arr[0]] + R

def par_index(arr: list[int]) -> list[int]:
    """
    Partitions the integer sequence around the first element (pivot).

    Args:
        arr: integer sequence to partition.

    Returns:
        Partitioned integer sequence with pivot in place.
    """
    i = 1
    for curr in range(1, len(arr)):
        if arr[curr] <= arr[0]:
            arr[i], arr[curr] = arr[curr], arr[i]
            i = i + 1
    arr[i-1], arr[0] = arr[0], arr[i-1]
    return arr

def rosalind_par(path):
    with open(path, "r") as f:
        lines = f.readlines()
        arr = list(map(int, lines[1].strip().split()))
        print(" ".join(map(str, par_index(arr))))
        