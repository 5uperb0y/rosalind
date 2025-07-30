import pytest
from inv import inv

@pytest.mark.parametrize("test_case, expected", [
    ([], 0),
    ([1], 0),
    ([1, 2, 3, 4, 5], 0),
    ([5, 4, 3, 2, 1], 10),
    ([3, 2, 1], 3),
    ([1, 3, 2, 4, 5], 1),
    ([10, 20, 30, 5, 15], 5),
    ([1, 5, 3, 2, 4], 4),
])
def test_inv(test_case, expected):
    assert inv(test_case)[1] == expected