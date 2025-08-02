import pytest
from three_sum import three_sum

@pytest.mark.parametrize("l, target, expected", [
    ([2, 7, 0, 15], 9, (0, 1, 2)),
    ([3, 3, 3], 9, (0, 1, 2)),
    ([1, 1, 1], 0, None),
    ([2, -3, 4, 10, 5], 0, None),
    ([], 0, None),
    ([5, 3, -1, 0, 2, 6], 8, (0, 1, 3)),
])
def test_three_sum(l, target, expected):
    assert three_sum(l, target) == expected