import pytest
from hs import hs

tests = [
    ([1], [1]),
    ([1, 1], [1, 1]),
    ([1, 0 , -1], [-1, 0, 1]),
    ([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
]
@pytest.mark.parametrize("input_list, expected_output", tests)
def test_hs(input_list, expected_output):
    assert hs(input_list) == expected_output