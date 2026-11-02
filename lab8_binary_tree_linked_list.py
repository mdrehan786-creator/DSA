from collections import deque

class Node:
    def __init__(self, data):
        self.data, self.left, self.right = data, None, None

class BinaryTree:
    def __init__(self): self.root=None

    def create_sample(self):
        # Same example structure as the lab manual: A with children B,C; B has D,E.
        self.root=Node("A")
        self.root.left=Node("B")
        self.root.right=Node("C")
        self.root.left.left=Node("D")
        self.root.left.right=Node("E")

    def traverse(self, order):
        result=[]
        def visit(n):
            if not n: return
            if order=="pre": result.append(n.data)
            visit(n.left)
            if order=="in": result.append(n.data)
            visit(n.right)
            if order=="post": result.append(n.data)
        visit(self.root)
        return result

    def levelorder(self):
        if not self.root: return []
        q=deque([self.root]); result=[]
        while q:
            n=q.popleft(); result.append(n.data)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        return result

def main():
    t=BinaryTree()
    t.create_sample()
    print("Sample tree created (A root, B/C children, D/E under B).")
    print("Preorder:",t.traverse("pre"))
    print("Inorder:",t.traverse("in"))
    print("Postorder:",t.traverse("post"))
    print("Level order:",t.levelorder())

if __name__ == "__main__": main()
