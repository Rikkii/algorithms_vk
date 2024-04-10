#  Ищем последнее вхождение числа

def binary_search_right_side(data, target):
    l=0
    r=len(data)-1

    while l+1<r:
        middle=(l+r)//2
        if data[middle]<=target:
            l=middle
        else:
            r=middle

    if data[r]==target:
        return r
    if data[l]:
        return l
    return -1

arr=[1,3,3,4,5,6,7,7,7,7,7,8,9,9]
target=7
print(right_binary_search(arr,target))
