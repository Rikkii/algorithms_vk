import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def reverseArray(arr, left, right):
     # left = 0
     # right = len(arr) - 1
     while left < right:
         logging.info(arr[left])
         logging.info(arr[right])
         arr[left], arr[right] = arr[right], arr[left]
         left = left + 1
         right = right - 1
     return arr


def solution(arr, k):
    """

    :type arr: list
    """
    n = len(arr)
    # reverseArray(arr, 0, n - 1)
    # reverseArray(arr, 0, k - 1)
    # reverseArray(arr, k, n - 1)

    reverseArray(arr, 0, k%n - 1)
    reverseArray(arr, k%n, n - 1)

    return arr

# arr = [1,2,3,4,5,6]
# print(reverseArray(arr))

arr = [1,2,3,4,5,6,7]
print(solution(arr, 10))
