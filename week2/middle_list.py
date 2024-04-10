from LinkedList import LinkedList
def middle_list(head):
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow

# Создание экземпляра LinkedList
my_list = LinkedList()


# Добавление элементов в список
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(middle_list(my_list.head))