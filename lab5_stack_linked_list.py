class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        print(value, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        value = self.top.data
        self.top = self.top.next
        print(value, "popped")

    def peek(self):
        print("Stack is empty" if self.top is None else f"Top element: {self.top.data}")

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        current = self.top
        values = []
        while current:
            values.append(current.data)
            current = current.next
        print("Top to bottom:", values)

def main():
    stack = Stack()
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
