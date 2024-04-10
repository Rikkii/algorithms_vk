def merge_sorted_arrays(arr1, arr2):

    merged_array = []
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i = i + 1
        else:
            merged_array.append(arr2[j])
            j = j + 1
    if len(arr1[i:])!=0:
        merged_array.extend(arr1[i:])
    if len(arr2[j:])!=0:
        merged_array.extend(arr2[j:])

    return merged_array

a = [1, 5, 6, 8]
b = [2, 5, 10, 11,15]
print(merge_sorted_arrays(a, b))

# Недостаток: занимаем память