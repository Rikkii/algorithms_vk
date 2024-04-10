from shell_sort import shell_sort

def feed_animals(animals, food):
    animals= shell_sort(animals)
    food = shell_sort(food)

    count=0
    for f in food:
        if f>=animals[count]:
            count = count+1

        if count == len(animals):
            break
    return count

food=[1,4,3,8]
animals=[8,2,3,2]

print(feed_animals(animals, food))