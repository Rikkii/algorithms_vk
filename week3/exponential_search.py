from binary_search_iteratives import binary_search_iteratives

def binary_search_exponential(arr, target):
    border=1
    last_element = len(arr)-1
    while border < last_element and arr[border]<target:
        border = border*2
        if arr[border]==target:
            return border
        if border>last_element:
            border=last_element

    return binary_search_iteratives(arr, target, border/2, border)

arr = [1,2,3,6,8,9,15,26,70]
target=15
print(binary_search_exponential(arr, target))