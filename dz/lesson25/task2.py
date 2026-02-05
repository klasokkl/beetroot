class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(sequence):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in sequence:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


s = input("Enter a sequence: ")

if is_balanced(s):
    print("Balanced")
else:
    print("Not balanced")
