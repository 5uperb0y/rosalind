from lcsm import lcsm
from lcsm import read_fasta
from lcsm import lcs
def test_read_fasta():
	expected = {
		"Rosalind_1":"GATTACA",
		"Rosalind_2":"TAGACCA",
		"Rosalind_3":"ATACA",
	}
	actual = read_fasta("lcsm.input")
	assert expected == actual
def test_lcsm():
	expected = ["TA", "CA", "AC"]
	actual = lcsm("lcsm.input")
	assert actual in expected