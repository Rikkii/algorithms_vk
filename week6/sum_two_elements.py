def sum_two_elements(arr, target):
    cache = {}
    n = len(arr)
    for i in range(n):
        cache[arr[i]] = i

    for i in range(n):
        diff = target - arr[i]
        if diff in cache:
            return i, cache[diff]

    return None

arr = [1,2,3,4,5]
target = 3
print(sum_two_elements(arr, target))