import pytest
from bins import bins, bins_rc

@pytest.mark.parametrize("l, key, expected", [
    ([1, 2, 3, 4, 5], 3, 2),  # Key is in the middle
    ([1, 2, 3, 4, 5], 1, 0),  # Key is the first element
    ([1, 2, 3, 4, 5], 5, 4),  # Key is the last element
    ([1, 2, 3, 4, 5], 6, -1), # Key is not in the list
    ([1, 2, 3, 4, 5], 0, -1), # Key is less than the smallest element
    ([], 3, -1),              # Empty list
    ([1], 1, 0),              # Single element list, key matches
    ([1], 2, -1),             # Single element list, key does not match
])
def test_bins(l, key, expected):
    assert bins(l, key) == expected

@pytest.mark.parametrize("l, key, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 1, 0),
    ([1, 2, 3, 4, 5], 5, 4),
    ([1, 2, 3, 4, 5], 6, -1),
    ([1, 2, 3, 4, 5], 0, -1),
    ([], 3, -1),
    ([1], 1, 0),
    ([1], 2, -1),
])
def test_bins_rc(l, key, expected):
    assert bins_rc(l, key) == expected