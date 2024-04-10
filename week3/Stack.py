class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Пример использования стека
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())  # Вывод: 3
print(s.pop())  # Вывод: 2
