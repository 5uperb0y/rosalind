from sort import rev_dist, rosalind_sort
def test_rev_dist():
	expected = (2, [(4, 9), (2, 5)])
	actual = rev_dist((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 8, 9, 3, 2, 7, 6, 5, 4, 10))
	assert expected == actual
def test_rosalind_sort(capsys):
    rosalind_sort("sort.input")
    captured = capsys.readouterr()
    assert captured.out == "2\n4 9\n2 5\n"