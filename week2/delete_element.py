from LinkedList import LinkedList, Node

def delete_element(head, val):
    dummy = Node()
    dummy.next = head
    prev = dummy
    cur = head

    while cur!=None:
        if cur.data==val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next


# Создание экземпляра LinkedList
my_list = LinkedList()


# Добавление элементов в список
my_list.append(1)
my_list.append(2)
my_list.append(3)

# noda = Node()
dummy = delete_element(my_list.head, 1)
print(dummy.print_list())