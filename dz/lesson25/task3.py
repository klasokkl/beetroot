class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, e):
        temp_stack = Stack()
        found = False

        # Ищем элемент
        while not self.is_empty():
            top = self.pop()
            if top == e and not found:
                found = True
                break
            temp_stack.push(top)

        # Возвращаем остальные элементы обратно
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Element {e} not found in stack")

        return e
