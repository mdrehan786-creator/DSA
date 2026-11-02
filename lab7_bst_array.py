class BSTArray:
    def __init__(self, capacity=100):
        self.tree = [None] * capacity

    def insert(self, value):
        i = 0
        while i < len(self.tree):
            if self.tree[i] is None:
                self.tree[i] = value
                return
            if value == self.tree[i]:
                print("Duplicate value ignored")
                return
            i = 2 * i + (1 if value < self.tree[i] else 2)
        print("Array capacity exceeded; try a larger capacity")

    def search(self, value):
        i = 0
        while i < len(self.tree) and self.tree[i] is not None:
            if self.tree[i] == value: return True
            i = 2 * i + (1 if value < self.tree[i] else 2)
        return False

    def _minimum_index(self, i):
        while 2*i+1 < len(self.tree) and self.tree[2*i+1] is not None:
            i = 2*i+1
        return i

    def delete(self, value, i=0):
        if i >= len(self.tree) or self.tree[i] is None: return False
        if value < self.tree[i]: return self.delete(value, 2*i+1)
        if value > self.tree[i]: return self.delete(value, 2*i+2)
        left, right = 2*i+1, 2*i+2
        has_left = left < len(self.tree) and self.tree[left] is not None
        has_right = right < len(self.tree) and self.tree[right] is not None
        if not has_left and not has_right:
            self.tree[i] = None
        elif has_left and not has_right:
            self._move_subtree(left, i)
        elif has_right and not has_left:
            self._move_subtree(right, i)
        else:
            j = self._minimum_index(right)
            successor = self.tree[j]
            self.tree[i] = successor
            self.delete(successor, right)
        return True

    def _move_subtree(self, src, dst):
        # Copy subtree values into a temporary structure, clear it, then reinsert.
        vals = []
        def collect(i):
            if i >= len(self.tree) or self.tree[i] is None: return
            vals.append(self.tree[i])
            collect(2*i+1); collect(2*i+2)
        collect(src)
        def clear(i):
            if i >= len(self.tree) or self.tree[i] is None: return
            self.tree[i] = None
            clear(2*i+1); clear(2*i+2)
        clear(src)
        self.tree[dst] = vals[0]
        for v in vals[1:]:
            self.insert(v)

    def _traverse(self, i, order, out):
        if i >= len(self.tree) or self.tree[i] is None: return
        if order == "pre": out.append(self.tree[i])
        self._traverse(2*i+1, order, out)
        if order == "in": out.append(self.tree[i])
        self._traverse(2*i+2, order, out)
        if order == "post": out.append(self.tree[i])

    def traversal(self, order):
        out=[]; self._traverse(0, order, out); print(out)

    def count(self):
        return sum(x is not None for x in self.tree)

    def height(self, i=0):
        if i >= len(self.tree) or self.tree[i] is None: return 0
        return 1 + max(self.height(2*i+1), self.height(2*i+2))

    def display(self):
        print([(i, v) for i, v in enumerate(self.tree) if v is not None])

def main():
    t = BSTArray()
    while True:
        print("\n1.Insert 2.Delete 3.Search 4.Inorder 5.Preorder 6.Postorder 7.Count/Height 8.Display 9.Exit")
        c=input("Choice: ")
        if c=="1": t.insert(int(input("Value: ")))
        elif c=="2": print("Deleted" if t.delete(int(input("Value: "))) else "Not found")
        elif c=="3": print("Found" if t.search(int(input("Value: "))) else "Not found")
        elif c=="4": t.traversal("in")
        elif c=="5": t.traversal("pre")
        elif c=="6": t.traversal("post")
        elif c=="7": print("Count:",t.count(),"Height:",t.height())
        elif c=="8": t.display()
        elif c=="9": break
        else: print("Invalid choice")

if __name__ == "__main__": main()
