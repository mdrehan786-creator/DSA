class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self): self.head = None

    def create(self, values):
        self.head = None
        for value in values: self.insert_end(value)

    def insert_beginning(self, value):
        node = Node(value)
        if not self.head:
            node.next = node; self.head = node; return
        tail = self.head
        while tail.next != self.head: tail = tail.next
        node.next = self.head; tail.next = node; self.head = node

    def insert_end(self, value):
        node = Node(value)
        if not self.head:
            node.next = node; self.head = node; return
        tail = self.head
        while tail.next != self.head: tail = tail.next
        tail.next = node; node.next = self.head

    def insert_index(self, index, value):
        if index < 0: print("Invalid index"); return
        if index == 0: self.insert_beginning(value); return
        cur = self.head
        if cur is None: print("Index out of range"); return
        for _ in range(index - 1):
            cur = cur.next
            if cur == self.head: print("Index out of range"); return
        node = Node(value); node.next = cur.next; cur.next = node

    def delete_value(self, value):
        if not self.head: return False
        cur, prev = self.head, None
        while True:
            if cur.data == value:
                if prev is None:
                    if cur.next == self.head: self.head = None
                    else:
                        tail = self.head
                        while tail.next != self.head: tail = tail.next
                        self.head = cur.next; tail.next = self.head
                else:
                    prev.next = cur.next
                return True
            prev, cur = cur, cur.next
            if cur == self.head: break
        return False

    def delete_beginning(self):
        if not self.head: return False
        if self.head.next == self.head: self.head = None; return True
        tail = self.head
        while tail.next != self.head: tail = tail.next
        self.head = self.head.next; tail.next = self.head
        return True

    def delete_end(self):
        if not self.head: return False
        if self.head.next == self.head: self.head = None; return True
        prev, cur = None, self.head
        while cur.next != self.head: prev, cur = cur, cur.next
        prev.next = self.head
        return True

    def count(self):
        if not self.head: return 0
        n, cur = 0, self.head
        while True:
            n += 1; cur = cur.next
            if cur == self.head: return n

    def display(self):
        if not self.head: print("List is empty"); return
        values, cur = [], self.head
        while True:
            values.append(cur.data); cur = cur.next
            if cur == self.head: break
        print(values)

    def search(self, value):
        if not self.head: return -1
        cur, i = self.head, 0
        while True:
            if cur.data == value: return i
            cur, i = cur.next, i + 1
            if cur == self.head: return -1

def main():
    ll = CircularLinkedList()
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
