def med_sort(l: list[int], k: int) -> int:
    """Get the kth (1-based) smallest integer within a list (sort method)"""
    return sorted(l)[k-1] # 因為是 1-based 所以要減 1

import heapq
def med_hp(l: list[int], k: int) -> int:
    """Get the kth (1-based) smallest integer within a list (heap method)"""
    smallest = heapq.nsmallest(k, l)
    return smallest[-1]

import random
def partition(l: list[int], pivot: int) -> list[int]:
    """3-way partition"""
    left, mid, right = [], [], []
    for x in l:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            mid.append(x)
    return left, mid, right

def med_qs(l: list[int], k: int) -> int:
    """Get the kth (1-based) smallest integer within a list (quick select method)"""
    if len(l) == 1:
        return l[0]
    pivot = random.choice(l)
    left, mid, right = partition(l, pivot)
    if k <= len(left): # k locate at left part
        return med_qs(left, k)
    elif k > len(left) + len(mid): # k locate at right part
        return med_qs(right, k - len(left) - len(mid)) # 1-based, do not need to minus 1
    else:
        return mid[0]

def rosalind_med(path):
    with open(path, "r") as f:
        lines = f.readlines()
        l = list(map(int, lines[1].strip().split()))
        k = int(lines[2])
        print(med_qs(l, k))
