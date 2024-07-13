from lcsq import lcsq
def test_lcsq():
	expected = "ACCTGG"
	assert expected == lcsq("AACCTTGG", "ACACTGTGA")