class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.top = -1
        self.size = size

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.items[self.top] = value
        print(value, "pushed")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        print(value, "popped")

    def peek(self):
        print("Stack is empty" if self.top == -1 else f"Top element: {self.items[self.top]}")

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top to bottom:", self.items[self.top::-1])

def main():
    size = int(input("Enter stack size: "))
    stack = Stack(size)
    while True:
        print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
        choice = input("Choice: ")
        if choice == "1":
            stack.push(int(input("Value: ")))
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.peek()
        elif choice == "4":
            stack.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
