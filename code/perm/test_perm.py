from perm import lperm
def test_lperm():
	expected = { 
		(1, 2, 3),
		(1, 3, 2),
		(2, 1, 3),
		(2, 3, 1),
		(3, 1, 2),
		(3, 2, 1)
	}	
	actual = { tuple(p) for p in lperm([1, 2, 3]) }
	assert expected == actual