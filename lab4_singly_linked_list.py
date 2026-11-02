class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, values):
        self.head = None
        for value in values:
            self.insert_end(value)

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert_index(self, index, value):
        if index < 0:
            print("Invalid index"); return
        if index == 0:
            self.insert_beginning(value); return
        cur = self.head
        for _ in range(index - 1):
            if cur is None:
                print("Index out of range"); return
            cur = cur.next
        if cur is None:
            print("Index out of range"); return
        node = Node(value)
        node.next = cur.next
        cur.next = node

    def delete_value(self, value):
        cur, prev = self.head, None
        while cur:
            if cur.data == value:
                if prev is None: self.head = cur.next
                else: prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def delete_beginning(self):
        if self.head is None: return False
        self.head = self.head.next
        return True

    def delete_end(self):
        if self.head is None: return False
        if self.head.next is None:
            self.head = None; return True
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        return True

    def count(self):
        n, cur = 0, self.head
        while cur:
            n += 1; cur = cur.next
        return n

    def display(self):
        values, cur = [], self.head
        while cur:
            values.append(cur.data); cur = cur.next
        print(values if values else "List is empty")

    def search(self, value):
        cur, index = self.head, 0
        while cur:
            if cur.data == value: return index
            cur, index = cur.next, index + 1
        return -1

def main():
    ll = SinglyLinkedList()
    while True:
        print("\\n1.Create 2.Insert beginning 3.Insert end 4.Insert at index")
        print("5.Delete by value 6.Delete first 7.Delete last 8.Count 9.Display 10.Search 11.Exit")
        choice = input("Choice: ")
        if choice == "1":
            values = list(map(int, input("Enter values separated by spaces: ").split()))
            ll.create(values)
        elif choice == "2": ll.insert_beginning(int(input("Value: ")))
        elif choice == "3": ll.insert_end(int(input("Value: ")))
        elif choice == "4": ll.insert_index(int(input("Index (0-based): ")), int(input("Value: ")))
        elif choice == "5": print("Deleted" if ll.delete_value(int(input("Value: "))) else "Value not found")
        elif choice == "6": print("Deleted" if ll.delete_beginning() else "List is empty")
        elif choice == "7": print("Deleted" if ll.delete_end() else "List is empty")
        elif choice == "8": print("Node count:", ll.count())
        elif choice == "9": ll.display()
        elif choice == "10":
            i = ll.search(int(input("Value to search: ")))
            print("Found at index", i if i >= 0 else "Not found")
        elif choice == "11": break
        else: print("Invalid choice")

if __name__ == "__main__": main()
