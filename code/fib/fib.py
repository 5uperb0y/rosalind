def fib(n, k):
    """Compute rabbit pairs after n months with k offspring pairs per mature pair.

    Args:
        n (int): Months to simulate (n >= 1).
        k (int): Offspring pairs per mature pair.

    Returns:
        int: Total rabbit pairs after n months.
    """
    if n <= 2:
        return 1
    else:
        return fib(n - 1, k) + fib(n - 2, k) * k
def rosalind_fib(path):
    with open(path, "r") as f:
        n, k = ( int(s) for s in f.readline().strip().split(" "))
        print(fib(n, k))