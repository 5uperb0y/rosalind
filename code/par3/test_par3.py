from par3 import par3_build, par3_dnf, par3_nested

def test_par3_build():
    assert par3_build([5, 2, 8, 5, 1, 7]) == [2, 1, 5, 5, 8, 7]
    assert par3_build([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert par3_build([10, 20, 5, 15, 10]) == [5, 10, 10, 20, 15]
    assert par3_build([1]) == [1]
    assert par3_build([4, 2, 6, 4, 4, 8]) == [2, 4, 4, 4, 6, 8]

def check_partition(arr: list[int], p: int) -> bool:
    prev = -1
    for x in arr:
        diff = (x > p) - (x < p) # left, mid, right = -1, 0, 1
        if diff < prev:
            return False
        prev = diff
    return True

def test_par3_nested():
    assert check_partition(par3_nested([5, 2, 8, 5, 1, 7]), 5)
    assert check_partition(par3_nested([3, 3, 3, 3]), 3)
    assert check_partition(par3_nested([10, 20, 5, 15, 10]), 10)
    assert check_partition(par3_nested([1]), 1)
    assert check_partition(par3_nested([4, 2, 6, 4, 4, 8]), 4)

def test_par3_():
    assert check_partition(par3_dnf([5, 2, 8, 5, 1, 7]), 5)
    assert check_partition(par3_dnf([3, 3, 3, 3]), 3)
    assert check_partition(par3_dnf([10, 20, 5, 15, 10]), 10)
    assert check_partition(par3_dnf([1]), 1)
    assert check_partition(par3_dnf([4, 2, 6, 4, 4, 8]), 4)

