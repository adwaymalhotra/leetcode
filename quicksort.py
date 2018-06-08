def quickSort(ns, lo , hi):
    if lo < hi:
        p = partition(ns, lo, hi)
        quickSort(ns, lo, p)
        quickSort(ns, p+1, hi)
        
def swap(ns, i, j):
    t = ns[i]
    ns[i] = ns[j]
    ns[j] = t

def partition(ns, lo, hi):
    if hi<=lo: return lo
    N = len(ns)
    p = (ns[hi] + ns[lo])/2
    i = lo
    j = hi
    
    while i<=j:
        while i<=hi and ns[i]<=p:
            i+=1
        while j>-1 and ns[j]>p:
            j-=1
        if i>j:
            if i == hi+1:
                j = j-1
            return j
        elif i==j:
            return i
        else: swap(ns, i, j)