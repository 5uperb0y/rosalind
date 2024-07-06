import pytest
from sseq import sseq, find_spliced_motifs_dp, find_spliced_motifs_rc
def test_sseq():
	expect = [3, 4, 5]
	assert expect == sseq("ACGTACGTGACG", "GTA")
def test_find_spliced_motifs_dp():
	expect = {(3, 4, 10), (3, 4, 5), (3, 8, 10), (7, 8, 10)}
	assert expect == find_spliced_motifs_dp("ACGTACGTGACG", "GTA")
def test_find_spliced_motifs_rc():
	expect = {(3, 4, 10), (3, 4, 5), (3, 8, 10), (7, 8, 10)}
	assert expect == find_spliced_motifs_dp("ACGTACGTGACG", "GTA")