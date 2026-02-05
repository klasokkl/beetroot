class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


s = input("Enter characters: ")

stack = Stack()

for ch in s:
    stack.push(ch)

while not stack.is_empty():
    print(stack.pop(), end="")
