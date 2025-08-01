import pytest
from two_sum import two_sum

@pytest.mark.parametrize("l, target, expected", [
    ([2, 7, 11, 15], 9, (0, 1)),  # Basic test case
    ([3, 2, 4], 6, (1, 2)),       # Pair in the middle
    ([3, 3], 6, (0, 1)),          # Pair with duplicate numbers
    ([1, 2, 3, 4, 5], 10, -1),    # No pair found
    ([0, -1, 2, -3, 1], -2, (3, 4)), # Negative numbers
    ([1], 2, -1),                 # Single element list
    ([], 0, -1),                  # Empty list
    ([1, 2, 3, 4, 5], 3, (0, 1)), # Pair at the start
    ([1, 2, 3, 4, 5], 9, (3, 4)), # Pair at the end
    ([1, 2, 3, 4, 5], 7, (2, 3)), # Pair in the middle
])
def test_two_sum(l, target, expected):
    assert two_sum(l, target) == expected