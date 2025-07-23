from fib import fib
# copilot is amazing for writing tests :)
def test_fib_small_values():
    assert fib(1, 1) == 1
    assert fib(2, 1) == 1
    assert fib(3, 1) == 2
    assert fib(4, 1) == 3

def test_fib_larger_values():
    assert fib(5, 1) == 5
    assert fib(6, 1) == 8
    assert fib(5, 3) == 19
    assert fib(6, 3) == 40

def test_fib_edge_cases():
    assert fib(1, 5) == 1
    assert fib(2, 5) == 1
