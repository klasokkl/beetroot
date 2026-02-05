class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnsortedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def index(self, item):
        current = self.head
        pos = 0

        while current:
            if current.data == item:
                return pos
            current = current.next
            pos += 1

        raise ValueError("Item not in list")

    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("Pop from empty list")

        if pos is None:
            pos = 0
            current = self.head
            while current.next:
                current = current.next
                pos += 1

        if pos == 0:
            value = self.head.data
            self.head = self.head.next
            return value

        current = self.head
        index = 0

        while index < pos - 1 and current.next:
            current = current.next
            index += 1

        if current.next is None:
            raise IndexError("Index out of range")

        value = current.next.data
        current.next = current.next.next
        return value

    def insert(self, pos, item):
        new_node = Node(item)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while index < pos - 1 and current.next:
            current = current.next
            index += 1

        new_node.next = current.next
        current.next = new_node

    def slice(self, start, stop):
        result = UnsortedList()
        current = self.head
        index = 0

        while current and index < stop:
            if index >= start:
                result.append(current.data)
            current = current.next
            index += 1

        return result
