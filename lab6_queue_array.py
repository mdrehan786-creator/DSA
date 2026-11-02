class Queue:
    def __init__(self, size=5):
        self.items = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.items[self.rear] = value
        print(value, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return
        value = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        print(value, "removed")

    def peek(self):
        print("Queue is empty" if self.front == -1 else f"Front element: {self.items[self.front]}")

    def display(self):
        print("Queue is empty" if self.front == -1 else self.items[self.front:self.rear + 1])

def main():
    q = Queue(int(input("Queue capacity: ")))
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
