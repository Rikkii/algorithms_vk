from LinkedList import LinkedList, Node


def merge_sorted_lists(head1, head2):
    dummy = Node()
    current = dummy

    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    else:
        current.next = head2

    return dummy.next


# Создание экземпляра LinkedList
my_list1 = LinkedList()
my_list2 = LinkedList()

# Добавление элементов в список
my_list1.append(1)
my_list1.append(5)
my_list1.append(10)


my_list2.append(2)
my_list2.append(3)
my_list2.append(15)

merge_sorted_lists(my_list1.head, my_list2.head).print_list()








