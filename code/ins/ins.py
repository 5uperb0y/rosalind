def ins(l):
    """Sorts integers using insertion sort and counts swaps.
    
    Args:
        l (list): A list of integers to be sorted.
    Returns:
        tuple: A tuple containing the sorted list and the number of swaps made.
    """
    swap_num = 0
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            j = i
            while j > 0 and l[j-1] > l[i]:
                j = j - 1
                swap_num = swap_num + 1
            l.insert(j, l.pop(i))
    return l, swap_num
def rosalind_ins(path):
    with open(path, "r") as f:
        lines = f.readlines()
        l = list(map(int, lines[1].strip().split()))
        print(ins(l)[1])
rosalind_ins("rosalind_ins.txt")
