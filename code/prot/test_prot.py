from prot import translate
def test_translate():
	expected = "MAMAPRTEINSTRING"
	actual = translate("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
	assert expected == actual