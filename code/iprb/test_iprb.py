import pytest
from iprb import iprb

def test_iprb():
    assert iprb(2, 2, 2) == pytest.approx(0.78333, rel=1e-5)


