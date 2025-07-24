def iprb(k, m, n):
        """
        Calculate the probability of producing an individual with a dominant phenotype.

        Args:
            k (int): Homozygous dominant count.
            m (int): Heterozygous count.
            n (int): Homozygous recessive count.

        Returns:
            float: Probability of dominant phenotype.
        """
        N = float(k + m + n)
        return 1 - ( n*(n-1) + n*m + 0.25*m*(m-1) )/( N*(N-1) )
def rosalind_iprb(path):
    with open(path, "r") as f:
        k, m, n = [int(s) for s in f.readline().strip().split()]
        print(iprb(k, m, n))