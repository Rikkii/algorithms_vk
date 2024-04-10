def binary_search_sqrt(target):

    l=0
    r=target
    while l<=r:
        middle = (l+r)//2
        if middle**2 > target:
            r = middle-1
            continue
        if middle**2 < target:
            l = middle+1
            continue
        return middle
    return r

print(binary_search_sqrt(120))