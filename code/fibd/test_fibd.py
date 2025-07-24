import pytest
from fibd import fibd

@pytest.mark.parametrize("n, m, expected", [
    (6, 3, 4),
    (98, 17, 133903587288445821265),
    (89, 18, 1769967188277700563),
])
def test_fibd(n, m, expected):
    assert fibd(n, m) == expected