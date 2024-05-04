from sign import slperm
def test_slperm():
    expected = { 
		(1, 2),
		(1, -2),
		(-1, 2),
		(-1, -2),
		(2, 1),
		(2, -1),
        (-2, 1),
        (-2, -1)
	}
    actual = { tuple(p) for p in slperm([1, 2]) }
    assert expected == actual