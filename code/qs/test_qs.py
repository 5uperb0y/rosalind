from qs import qs

def test_qs():
    assert qs([1,2,3,4]) == [1,2,3,4]
    assert qs([4,3,2,1]) == [1,2,3,4]
    assert qs([4,3,2,3,1]) == [1,2,3,3,4]