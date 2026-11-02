class Node:
    def __init__(self, key):
        self.key=key
        self.left=self.right=None
        self.height=1

class AVLTree:
    def height(self, node): return node.height if node else 0
    def balance(self, node): return self.height(node.left)-self.height(node.right) if node else 0
    def update(self, node): node.height=1+max(self.height(node.left),self.height(node.right))

    def rotate_right(self, y):
        x=y.left; t=x.right
        x.right=y; y.left=t
        self.update(y); self.update(x)
        return x

    def rotate_left(self, x):
        y=x.right; t=y.left
        y.left=x; x.right=t
        self.update(x); self.update(y)
        return y

    def insert(self, node, key):
        if not node: return Node(key)
        if key < node.key: node.left=self.insert(node.left,key)
        elif key > node.key: node.right=self.insert(node.right,key)
        else: return node
        self.update(node); b=self.balance(node)
        if b>1 and key<node.left.key: return self.rotate_right(node)       # LL
        if b<-1 and key>node.right.key: return self.rotate_left(node)      # RR
        if b>1 and key>node.left.key:                                     # LR
            node.left=self.rotate_left(node.left); return self.rotate_right(node)
        if b<-1 and key<node.right.key:                                    # RL
            node.right=self.rotate_right(node.right); return self.rotate_left(node)
        return node

    def min_node(self,node):
        while node.left: node=node.left
        return node

    def delete(self,node,key):
        if not node: return None
        if key<node.key: node.left=self.delete(node.left,key)
        elif key>node.key: node.right=self.delete(node.right,key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp=self.min_node(node.right); node.key=temp.key
            node.right=self.delete(node.right,temp.key)
        self.update(node); b=self.balance(node)
        if b>1 and self.balance(node.left)>=0: return self.rotate_right(node)
        if b>1 and self.balance(node.left)<0:
            node.left=self.rotate_left(node.left); return self.rotate_right(node)
        if b<-1 and self.balance(node.right)<=0: return self.rotate_left(node)
        if b<-1 and self.balance(node.right)>0:
            node.right=self.rotate_right(node.right); return self.rotate_left(node)
        return node

    def search(self,node,key):
        if not node: return False
        if node.key==key: return True
        return self.search(node.left,key) if key<node.key else self.search(node.right,key)

    def traversal(self,node,order,out):
        if not node: return
        if order=="pre": out.append(node.key)
        self.traversal(node.left,order,out)
        if order=="in": out.append(node.key)
        self.traversal(node.right,order,out)
        if order=="post": out.append(node.key)

    def display(self,node,level=0):
        if node:
            self.display(node.right,level+1)
            print("   "*level+str(node.key))
            self.display(node.left,level+1)

def main():
    avl=AVLTree(); root=None
    while True:
        print("\n1.Insert 2.Delete 3.Search 4.Inorder 5.Preorder 6.Postorder 7.Display 8.Exit")
        c=input("Choice: ")
        if c=="1": root=avl.insert(root,int(input("Value: ")))
        elif c=="2": root=avl.delete(root,int(input("Value: ")))
        elif c=="3": print("Found" if avl.search(root,int(input("Value: "))) else "Not found")
        elif c in ("4","5","6"):
            order={"4":"in","5":"pre","6":"post"}[c]; result=[]
            avl.traversal(root,order,result); print(result)
        elif c=="7": avl.display(root)
        elif c=="8": break
        else: print("Invalid choice")

if __name__=="__main__": main()
