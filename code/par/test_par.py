import pytest
from par import par_index, par_list
def test_par_list():
    assert par_list([4, 5, 3, 7, 2]) == [3, 2, 4, 5, 7]
    assert par_list([10, 1, 2, 3, 4]) == [1, 2, 3, 4, 10]
    assert par_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert par_list([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 5]

def test_par_index():
    assert par_index([4, 5, 3, 7, 2]) == [2, 3, 4, 7, 5]
    assert par_index([10, 1, 2, 3, 4]) == [4, 1, 2, 3, 10]
    assert par_index([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert par_index([5, 4, 3, 2, 1]) == [1, 4, 3, 2, 5]

