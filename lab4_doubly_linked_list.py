class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self): self.head = None

    def create(self, values):
        self.head = None
        for value in values: self.insert_end(value)

    def insert_beginning(self, value):
        node = Node(value)
        node.next = self.head
        if self.head: self.head.prev = node
        self.head = node

    def insert_end(self, value):
        node = Node(value)
        if not self.head: self.head = node; return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node; node.prev = cur

    def insert_index(self, index, value):
        if index < 0: print("Invalid index"); return
        if index == 0: self.insert_beginning(value); return
        cur = self.head
        for _ in range(index - 1):
            if cur is None: print("Index out of range"); return
            cur = cur.next
        if cur is None: print("Index out of range"); return
        node = Node(value); node.next = cur.next; node.prev = cur
        if cur.next: cur.next.prev = node
        cur.next = node

    def delete_value(self, value):
        cur = self.head
        while cur and cur.data != value: cur = cur.next
        if cur is None: return False
        if cur.prev: cur.prev.next = cur.next
        else: self.head = cur.next
        if cur.next: cur.next.prev = cur.prev
        return True

    def delete_beginning(self):
        if not self.head: return False
        self.head = self.head.next
        if self.head: self.head.prev = None
        return True

    def delete_end(self):
        if not self.head: return False
        cur = self.head
        while cur.next: cur = cur.next
        if cur.prev: cur.prev.next = None
        else: self.head = None
        return True

    def count(self):
        n, cur = 0, self.head
        while cur: n += 1; cur = cur.next
        return n

    def display(self):
        values, cur = [], self.head
        while cur: values.append(cur.data); cur = cur.next
        print(values if values else "List is empty")

    def search(self, value):
        cur, i = self.head, 0
        while cur:
            if cur.data == value: return i
            cur, i = cur.next, i + 1
        return -1

def main():
    ll = DoublyLinkedList()
    while True:
        print("\\n1.Create 2.Insert beginning 3.Insert end 4.Insert at index")
        print("5.Delete by value 6.Delete first 7.Delete last 8.Count 9.Display 10.Search 11.Exit")
        c = input("Choice: ")
        if c == "1": ll.create(list(map(int, input("Values separated by spaces: ").split())))
        elif c == "2": ll.insert_beginning(int(input("Value: ")))
        elif c == "3": ll.insert_end(int(input("Value: ")))
        elif c == "4": ll.insert_index(int(input("Index (0-based): ")), int(input("Value: ")))
        elif c == "5": print("Deleted" if ll.delete_value(int(input("Value: "))) else "Value not found")
        elif c == "6": print("Deleted" if ll.delete_beginning() else "List is empty")
        elif c == "7": print("Deleted" if ll.delete_end() else "List is empty")
        elif c == "8": print("Node count:", ll.count())
        elif c == "9": ll.display()
        elif c == "10":
            i = ll.search(int(input("Value to search: ")))
            print("Found at index", i if i >= 0 else "Not found")
        elif c == "11": break
        else: print("Invalid choice")

if __name__ == "__main__": main()
