def lexf(elements, k):
    """Generate all permutations of a specified length from a given set of elements.
    
    Args:
    elements (list): A list of characters or items from which permutations are to be generated.
    length (int): The length of each permutation sequence.

    Returns:
    list: A list of all permutations as strings.
    """
    if k == 1:
        return elements
    else:
        return [
            f"{e}{k_str}"
            for e in elements
            for k_str in lexf(elements, k - 1)
        ]
def print_results(elements, k):
    for k_str in lexf(elements, k):
        print(k_str)