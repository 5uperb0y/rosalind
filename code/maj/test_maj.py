import pytest
from maj import maj_freq, maj_bm, maj_rc

# Define the parameterized inputs once
test_data = [
    ([3, 3, 4, 2, 3, 3, 3], 3),  # Majority element exists
    ([1, 2, 3, 4, 5], -1),       # No majority element
    ([7], 7),                    # Single element
    ([], -1),                    # Empty list
    ([9, 9, 9, 9, 9], 9),        # All elements same
    ([1, 1, 1, 2, 2], 1),        # Majority element at boundary
    ([5] * 100 + [6] * 49, 5),   # Large list with majority
    ([5] * 50 + [6] * 50, -1)    # Large list without majority
]

@pytest.mark.parametrize("input_list, expected", test_data)
def test_maj_freq(input_list, expected):
    assert maj_freq(input_list) == expected

@pytest.mark.parametrize("input_list, expected", test_data)
def test_maj_bm(input_list, expected):
    assert maj_bm(input_list) == expected

@pytest.mark.parametrize("input_list, expected", test_data)
def test_maj_rc(input_list, expected):
    assert maj_rc(input_list) == expected