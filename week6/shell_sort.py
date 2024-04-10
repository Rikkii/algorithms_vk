def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap>0:
        i = gap
        for i in range(n):
            m_gap=i
            while m_gap >= gap and arr[m_gap]<arr[m_gap-gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap = m_gap - gap
        gap = gap//2
    return arr

arr=[1,6,3,8,4,9,10,3]
print(shell_sort(arr))
