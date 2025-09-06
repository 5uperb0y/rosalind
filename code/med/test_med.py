from med import med_hp, med_qs, med_sort

def test_med_sort():
    assert med_sort([2,36,5,21,8,13,11,20,5,4,1], 8) == 13
def test_med_hp():
    assert med_hp([2,36,5,21,8,13,11,20,5,4,1], 8) == 13
def test_med_qs():
    assert med_qs([2,36,5,21,8,13,11,20,5,4,1], 8) == 13
