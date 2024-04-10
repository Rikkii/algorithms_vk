def zerosBack(arr):

    zeroIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[i], arr[zeroIndex] = arr[zeroIndex], arr[i]
            zeroIndex += 1

    return arr

a=[0,0,1,0,3,12]
print(zerosBack(a))

b=[0,33,57,88,60,0,0,80,99]
print(zerosBack(b))