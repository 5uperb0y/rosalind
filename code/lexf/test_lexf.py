from lexf import lexf
def test_lexf():
   expected = [
      "AA",
      "AC",
      "AG",
      "AT",
      "CA",
      "CC",
      "CG",
      "CT",
      "GA",
      "GC",
      "GG",
      "GT",
      "TA",
      "TC",
      "TG",
      "TT"
      ]
   actual = lexf(["A", "C", "G", "T"], 2)
   assert expected == actual