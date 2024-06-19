from splc import rm_introns, rm_introns_with_regex, rosalind_splc
def test_rm_introns():
    dna = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
    introns = ["ATCGGTCGAA", "ATCGGTCGAGCGTGT"]
    expected = "ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG"
    assert expected == rm_introns(dna, introns)
def test_rm_introns_with_regex():
    dna = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
    introns = ["ATCGGTCGAA", "ATCGGTCGAGCGTGT"]
    expected = "ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG"
    assert expected == rm_introns_with_regex(dna, introns)
def test_rosalind_splc(capsys):
    rosalind_splc("splc.input")
    captured = capsys.readouterr()
    assert captured.out == "MVYIADKQHVASREAYGHMFKVCA\n"