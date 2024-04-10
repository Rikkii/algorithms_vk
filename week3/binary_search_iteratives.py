
def binary_search_iteratives(data, target, l, r):

    l=0
    r=len(data)-1

    if target<data[l] or target>data[r]:
        return -1

    while l <= r:
        middle = (l+r)//2
        if target == data[middle]:
            return middle

        if target<data[middle]:
            r = middle-1
        else:
            l = middle+1

    return -1

a = [1,2,3,4,5]
target=2
print(binary_search_iteratives(a, target, 0, len(a)))
