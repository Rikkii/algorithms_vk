def binary_search_ternary(data, target):
    l=0
    r=len(data)-1
    while r>=l:
        m1=l+(r-l)//3
        m2=r-(r-l)//3

        if data[m1]==target:
            return m1
        if data[m2]==target:
            return m2

        if target<data[m1]:
            r=m1-1
        elif target>data[m2]:
            l=m2+1
        else:
            l=m1+1
            r=m2-1

    return -1



arr=[1,3,3,4,5,6,7,7,7,7,7,8,9,9]
target=7
print(binary_search_ternary(arr,target))
