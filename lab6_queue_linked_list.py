class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        print(value, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(value, "removed")

    def peek(self):
        print("Queue is empty" if self.front is None else f"Front element: {self.front.data}")

    def display(self):
        current, values = self.front, []
        while current:
            values.append(current.data)
            current = current.next
        print(values if values else "Queue is empty")

def main():
    q = Queue()
    while True:
        print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
        c = input("Choice: ")
        if c == "1": q.enqueue(int(input("Value: ")))
        elif c == "2": q.dequeue()
        elif c == "3": q.peek()
        elif c == "4": q.display()
        elif c == "5": break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()
