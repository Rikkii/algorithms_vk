def evenFirst(arr):

    evenIndex = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenIndex] = arr[evenIndex], arr[i]
            evenIndex += 1

    return arr

a=[3,2,4,1,11,8,9]
print(evenFirst(a))