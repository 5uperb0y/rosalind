def slperm(l):
    """permutations of a numberic list, including -/+ of each number.
    """
    if len(l) == 1:
        return [[l[0]], [-l[0]]]
    else:
        return [
            p + [sign_e]
            for i, e in enumerate(l)
            for p in slperm(l[:i] + l[i+1:])
            for sign_e in [e, -e]
        ]
def print_permutations(n):
    num_perms = slperm(list(range(1, n+1)))
    print(len(num_perms))
    for p in num_perms:
        print(" ".join(map(str, p)))