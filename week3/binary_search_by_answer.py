def binary_search_by_answer(w,h,n):
    l=max(w,h)

    r=l*n

    while l+1<r:
        middle = (r+l)//2

        res = (middle//w) * (middle//h)
        if res<n:
            l=middle
        else:
            r=middle

    return r

print(binary_search_by_answer(3,4,9))