class BinaryTreeArray:
    def __init__(self, size):
        self.tree = [None] * size

    def set_root(self, value):
        if not self.tree: print("Tree has zero capacity")
        else: self.tree[0] = value

    def set_left(self, parent_index, value):
        child=2*parent_index+1
        if parent_index < 0 or parent_index >= len(self.tree) or self.tree[parent_index] is None:
            print("Parent index is empty or invalid")
        elif child >= len(self.tree): print("Index out of range")
        else: self.tree[child]=value

    def set_right(self, parent_index, value):
        child=2*parent_index+2
        if parent_index < 0 or parent_index >= len(self.tree) or self.tree[parent_index] is None:
            print("Parent index is empty or invalid")
        elif child >= len(self.tree): print("Index out of range")
        else: self.tree[child]=value

    def traverse(self, order, i=0, out=None):
        if out is None: out=[]
        if i >= len(self.tree) or self.tree[i] is None: return out
        if order=="pre": out.append(self.tree[i])
        self.traverse(order, 2*i+1, out)
        if order=="in": out.append(self.tree[i])
        self.traverse(order, 2*i+2, out)
        if order=="post": out.append(self.tree[i])
        return out

    def levelorder(self):
        return [x for x in self.tree if x is not None]

    def display(self):
        for i, value in enumerate(self.tree): print(f"Index {i}: {value}")

def main():
    t=BinaryTreeArray(int(input("Array capacity: ")))
    while True:
        print("\n1.Set root 2.Set left child 3.Set right child 4.Preorder 5.Inorder 6.Postorder 7.Level order 8.Display 9.Exit")
        c=input("Choice: ")
        if c=="1": t.set_root(input("Root value: "))
        elif c=="2": t.set_left(int(input("Parent index: ")), input("Child value: "))
        elif c=="3": t.set_right(int(input("Parent index: ")), input("Child value: "))
        elif c in ("4","5","6"): print(t.traverse({"4":"pre","5":"in","6":"post"}[c]))
        elif c=="7": print(t.levelorder())
        elif c=="8": t.display()
        elif c=="9": break
        else: print("Invalid choice")

if __name__ == "__main__": main()
