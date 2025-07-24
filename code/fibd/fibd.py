def fibd (n, m):
    def fibd(n, m):
        """        Calculate the number of rabbits alive after n months with a lifespan of m months.

        Args:
            n (int): The number of months to simulate.
            m (int): The lifespan of rabbits in months.

        Returns:
            int: The total number of rabbits alive after n months.
        """
    fn = [1, 1]
    for i in range(2, n):
        if i < m:
            tmp = 0
        elif i == m:
            tmp = 1
        else:
            tmp = fn[i - m - 1]
        fn.append(fn[i - 1] + fn[i - 2] - tmp)
    return fn[-1]
def rosalind_fibd(path):
    with open(path, "r") as f:
        n, m = [int(s) for s in f.readline().strip().split()]
        print(fibd(n, m))