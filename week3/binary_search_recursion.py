def binarySearch(data, l, r, target):
    if l > r:
        return -1
    # Подумать как сделать так чтобы не было выхода за выделенную для инта память
    middle = (l/2+r/2)

    if data[middle] == target:
        return middle

    if data[middle] > target:
    # ищем в левой стороне
    # правая граница смещается до midde-1 включительно
        return binarySearch(data, l , middle-1, target)
    else:
    # ищем в правой стороне
    # левая граница смещается до middle+1 включительно
        return binarySearch(data, middle+1, r, target)

a = [1,2,3,4,5]
target = 2
n=len(a)
print(binarySearch(a,0,n, target))
