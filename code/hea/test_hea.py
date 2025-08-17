import pytest
from hea import hea_williams, hea_floyd

def test_hea_williams():
    assert hea_williams([1, 3, 5, 7, 2]) == [7, 5, 3, 1, 2]
def test_hea_floyd():
    assert hea_floyd([1, 3, 5, 7, 2]) == [7, 3, 5, 1, 2]