import pytest
from ms import ms

@pytest.mark.parametrize("input_list, expected", [
    ([], []),  # Test empty list
    ([1], [1]),  # Test single element
    ([2, 1], [1, 2]),  # Test two elements
    ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),  # Test unsorted list
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Test already sorted list
    ([10, -1, 2, 5, 0], [-1, 0, 2, 5, 10]),  # Test list with negative numbers
    ([3, 3, 3, 3], [3, 3, 3, 3]),  # Test list with duplicate elements
    ([100, 50, 25, 75, 0], [0, 25, 50, 75, 100]),  # Test larger numbers
])
def test_ms(input_list, expected):
    assert ms(input_list) == expected