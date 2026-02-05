class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:  
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        value = self.front.data
        self.front = self.front.next

        if self.front is None: 
            self.rear = None

        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data


if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front element:", q.peek())  

    while not q.is_empty():
        print("Dequeued:", q.dequeue())
