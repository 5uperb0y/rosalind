from subs import subs
def test_subs():
	expected = [2, 4, 10]
	actual = subs("GATATATGCATATACTT", "ATAT")
	assert expected == actual