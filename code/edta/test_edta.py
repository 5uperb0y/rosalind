from edta import edta
def test_edta():
    expected = ["4", "PRET-TY", "PRTTEIN"]
    assert expected == edta("PRETTY", "PRTTEIN")