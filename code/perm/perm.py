def lperm(l):
    """Permutations of a list
    """
    if len(l) == 1:
        return [l]
    else:
        return [
            p + [e]
            for i, e in enumerate(l)
            for p in lperm(l[:i] + l[i+1:])
        ]
def print_permutations(n):
    num_perms = lperm(list(range(1, n+1)))
    print(len(num_perms))
    for p in num_perms:
        print(" ".join(map(str, p)))