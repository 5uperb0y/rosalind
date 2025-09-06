from ps import ps

def test_ps():
    assert ps([1,2,3,4,5], 1) == [1]
    assert ps([1,2,3,4,5], 3) == [1,2,3]
    assert ps([5,4,3,2,1], 3) == [1,2,3]
    assert ps([5,4,3,3,1], 3) == [1,3,3]
    assert ps([-5,-4,3,3,1], 3) == [-5,-4,1]