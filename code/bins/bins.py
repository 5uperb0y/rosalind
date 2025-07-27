
def bins(l, key):
    """Binary search for the index of key in a sorted list.

    Args:
        l (list): A sorted list of elements.
        key: The element to search for in the list.
    
    Returns:
        int: The index of key in the list if found, otherwise -1.
    """
    left, right = 0, len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bins_rc(l, key):
    """Binary search (recursion) for the index of key in a sorted list.

    Args:
        l (list): A sorted list of elements.
        key: The element to search for in the list.
    
    Returns:
        int: The index of key in the list if found, otherwise -1.
    """
    def helper(l, key, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            return helper(l, key, mid + 1, right)
        else:
            return helper(l, key, left, mid - 1)
    return helper(l, key, 0, len(l) - 1)

def rosalind_bins(path):
    with open(path, "r") as f:
        lines = f.readlines()
        keys = [int(s) for s in lines[3].strip().split()]
        l = [int(s) for s in lines[2].strip().split()]
    out = []
    for key in keys:
        key_idx = bins(l, key)
        if key_idx != -1:
            out.append(key_idx + 1)
        else:
            out.append(-1)
    print(" ".join(map(str, out)))