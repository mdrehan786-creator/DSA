class CircularQueue:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Queue size must be positive")
        self.items = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value
        print(value, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return
        value = self.items[self.front]
        self.items[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(value, "removed")

    def peek(self):
        print("Queue is empty" if self.front == -1 else f"Front element: {self.items[self.front]}")

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        result, i = [], self.front
        while True:
            result.append(self.items[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(result)

def main():
    q = CircularQueue(int(input("Queue capacity: ")))
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
