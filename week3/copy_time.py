def copy_time(n,x,y):
    # верхняя и нижняя границы
    l=0
    r=(n-1) * max(x,y)

    while l+1<r:
        mid = (r+l)//2
        # 4/2+4/1 = 6 < 4
        if mid//x+mid//y < n-1:
            l=mid
        else:
            r=mid

    return r+min(x,y)

print(copy_time(11,1,2))