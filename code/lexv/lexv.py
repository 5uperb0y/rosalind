def lexv(elements, k):
    """Ordering Strings of Varying Length Lexicographically
    """
    if k == 1:
        return elements
    else:
        output = []
        for e in elements:
            output.append(e)
            output.extend([f"{e}{k_str}" for k_str in lexv(elements, k - 1) ])
        return output
def print_results(elements, k):
    for s in lexv(elements, k):
        print(s)