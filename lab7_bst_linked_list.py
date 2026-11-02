class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None

class BST:
    def __init__(self): self.root = None

    def insert(self, value):
        def add(node):
            if node is None: return Node(value)
            if value < node.data: node.left = add(node.left)
            elif value > node.data: node.right = add(node.right)
            else: print("Duplicate value ignored")
            return node
        self.root = add(self.root)

    def search(self, value):
        node = self.root
        while node:
            if value == node.data: return True
            node = node.left if value < node.data else node.right
        return False

    def delete(self, value):
        def remove(node, value):
            if node is None: return None
            if value < node.data: node.left = remove(node.left, value)
            elif value > node.data: node.right = remove(node.right, value)
            else:
                if node.left is None: return node.right
                if node.right is None: return node.left
                successor = node.right
                while successor.left: successor = successor.left
                node.data = successor.data
                node.right = remove(node.right, successor.data)
            return node
        existed = self.search(value)
        self.root = remove(self.root, value)
        return existed

    def traverse(self, order):
        result=[]
        def visit(n):
            if not n: return
            if order=="pre": result.append(n.data)
            visit(n.left)
            if order=="in": result.append(n.data)
            visit(n.right)
            if order=="post": result.append(n.data)
        visit(self.root); print(result)

    def count(self, n=None):
        if n is None:
            if self.root is None: return 0
            n=self.root
        return 1+self.count(n.left)+self.count(n.right) if n else 0

    def height(self, n=None):
        if n is None:
            if self.root is None: return 0
            n=self.root
        return 1+max(self.height(n.left), self.height(n.right)) if n else 0

    def minimum(self):
        n=self.root
        if not n: return None
        while n.left: n=n.left
        return n.data

    def maximum(self):
        n=self.root
        if not n: return None
        while n.right: n=n.right
        return n.data

def main():
    t=BST()
    while True:
        print("\n1.Insert 2.Delete 3.Search 4.Inorder 5.Preorder 6.Postorder 7.Count/Height 8.Min/Max 9.Exit")
        c=input("Choice: ")
        if c=="1": t.insert(int(input("Value: ")))
        elif c=="2": print("Deleted" if t.delete(int(input("Value: "))) else "Not found")
        elif c=="3": print("Found" if t.search(int(input("Value: "))) else "Not found")
        elif c in ("4","5","6"): t.traverse({"4":"in","5":"pre","6":"post"}[c])
        elif c=="7": print("Count:",t.count(),"Height:",t.height())
        elif c=="8": print("Minimum:",t.minimum(),"Maximum:",t.maximum())
        elif c=="9": break
        else: print("Invalid choice")

if __name__ == "__main__": main()
