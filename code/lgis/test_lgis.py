from lgis import lgis
from lgis import rosalind_lgis
def test_lgis():
    expected = [1, 2, 3]
    actual = lgis([5, 1, 4, 2, 3])
    assert expected == actual
def test_rosalind_lgis(capsys):
    rosalind_lgis("lgis.input")
    captured = capsys.readouterr()
    assert captured.out == "5 6 7\n5 3 2 1\n"
