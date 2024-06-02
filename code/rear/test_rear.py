from rear import rosalind_rear
def test_rosalind_rear():
	expected = "9 4 5 7 0"
	actual = rosalind_rear("rear.input")
	assert expected == actual