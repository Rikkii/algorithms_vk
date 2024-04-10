from LinkedList import LinkedList



def reverse_linked_list(head):
    prev = None
    current = head

    while current!=None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head = prev
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

# Создание экземпляра LinkedList
my_list = LinkedList()


# Добавление элементов в список
my_list.append(1)
my_list.append(2)
my_list.append(3)

head = reverse_linked_list(my_list.head)
print_list(head)