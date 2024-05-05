from lexv import lexv
def test_lexv():
    expected = [
        "D", "DD", "DDD", "DDN", "DDA", "DN", "DND", "DNN", "DNA", "DA", "DAD", "DAN", "DAA",
        "N", "ND", "NDD", "NDN", "NDA", "NN", "NND", "NNN", "NNA", "NA", "NAD", "NAN", "NAA",
        "A", "AD", "ADD", "ADN", "ADA", "AN", "AND", "ANN", "ANA", "AA", "AAD", "AAN", "AAA"
    ]
    actual = lexv(["D", "N", "A"], 3)
    assert expected == actual