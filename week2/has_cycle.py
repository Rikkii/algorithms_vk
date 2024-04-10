from LinkedList import LinkedList

def has_cycle(head):
    if head==None or head.next == None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Создание экземпляра LinkedList
my_list = LinkedList()


# # Добавление элементов в список
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.make_cyclic()

print(has_cycle(my_list.head))