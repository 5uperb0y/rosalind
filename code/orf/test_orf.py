from orf import orf, rosalind_orf
def test_orf():
	test_data = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
	expected = ["ATG", "ATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA", "ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA"]
	actual = orf(test_data)
	assert expected == actual
def test_rosalind_orf(capsys):
	expected ="M\nMTPRLGLESLLE\nMGMTPRLGLESLLE\nMLLGSFRLIPKETLIQVAGSSPCNLS\n"
	rosalind_orf("orf.input")
	captured = capsys.readouterr()
	assert captured.out == expected
