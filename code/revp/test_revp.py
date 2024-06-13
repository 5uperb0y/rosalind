import pytest
from revp import revp_bf, revp_me, revp_manacher
@pytest.mark.parametrize("func", [revp_bf, revp_me, revp_manacher])
def test_revp_functions_on_rosalind_case(func):
    dna = "TCAATGCATGCGGGTCTATATGCAT"
    expected = {
        (22, 2), (5, 4), (4, 6), (11, 2), (24, 2), (7, 4), (6, 2), (18, 4), 
        (4, 2), (17, 2), (19, 2), (8, 2), (10, 2), (20, 6), (17, 4), (18, 2), 
        (6, 6), (21, 4), (20, 2)
    }
    assert expected == set(func(dna))
@pytest.mark.parametrize("func, dna, expected", [
    (revp_manacher, "", set()),
    (revp_manacher, "A", set()),
    (revp_manacher, "AT", {(1, 2)}),
    (revp_manacher, "ATAT", {(1, 2), (2, 2), (1, 4), (3, 2)}),
    (revp_manacher, "ABC", set()),
])
def test_revp_manacher_edge_cases(func, dna, expected):
    assert expected == set(func(dna))
