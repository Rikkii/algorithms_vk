class Node:

    def __init__(self, data=None):
        self.data = data  # Узел содержит данные
        self.next = None  # Указатель на следующий узел

    def __str__(self):
        return str(self.data)

    def print_list(self):
        current = self
        while current:
            print(current.data, end=' ')
            current = current.next

class LinkedList(Node):
    def __init__(self):
        self.head = None  # Инициализация списка с пустой головой

    def append(self, data):
        new_node = Node(data)  # Создание нового узла

        if not self.head:
            self.head = new_node  # Если список пуст, новый узел становится головой
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # Добавление нового узла в конец списка

    def make_cyclic(self):
        if not self.head:
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head

    def display(self):
        current = self.head
        while current:
            print(current.data, id(current), id(current.next), end=' -> ')  # Печать данных текущего узла
            current = current.next
        print("None")  # Конец списка


# Создание экземпляра LinkedList
my_list = LinkedList()

# # Добавление элементов в список
my_list.append(1)
my_list.append(2)
my_list.append(3)


# # Вывод списка
# my_list.display()



