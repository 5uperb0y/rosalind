
import pytest
from ins import ins

@pytest.mark.parametrize("l, expected", [
    ([1], ([1], 0)),
    ([2, 1], ([1, 2], 1)),
    ([-1, -2, -3], ([-3, -2, -1], 3)),
    ([6, 10, 4, 5, 1, 2], ([1, 2, 4, 5, 6, 10], 12)),
])
def test_ins(l, expected):
    assert ins(l) == expected