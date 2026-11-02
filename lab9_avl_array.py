class AVLArray:
    def __init__(self, capacity=100):
        self.capacity=capacity
        self.data=[None]*capacity
        self.left=[-1]*capacity
        self.right=[-1]*capacity
        self.height=[0]*capacity
        self.count=0
        self.root=-1

    def new_node(self,key):
        if self.count>=self.capacity:
            print("Tree is full"); return -1
        i=self.count; self.count+=1
        self.data[i]=key; self.height[i]=1
        return i

    def h(self,i): return self.height[i] if i!=-1 else 0
    def balance(self,i): return self.h(self.left[i])-self.h(self.right[i]) if i!=-1 else 0
    def update(self,i):
        self.height[i]=1+max(self.h(self.left[i]),self.h(self.right[i]))

    def rotate_right(self,y):
        x=self.left[y]; t=self.right[x]
        self.right[x]=y; self.left[y]=t
        self.update(y); self.update(x)
        return x

    def rotate_left(self,x):
        y=self.right[x]; t=self.left[y]
        self.left[y]=x; self.right[x]=t
        self.update(x); self.update(y)
        return y

    def insert_node(self,i,key):
        if i==-1: return self.new_node(key)
        if key<self.data[i]: self.left[i]=self.insert_node(self.left[i],key)
        elif key>self.data[i]: self.right[i]=self.insert_node(self.right[i],key)
        else: return i
        self.update(i); b=self.balance(i)
        if b>1 and key<self.data[self.left[i]]: return self.rotate_right(i)
        if b<-1 and key>self.data[self.right[i]]: return self.rotate_left(i)
        if b>1 and key>self.data[self.left[i]]:
            self.left[i]=self.rotate_left(self.left[i]); return self.rotate_right(i)
        if b<-1 and key<self.data[self.right[i]]:
            self.right[i]=self.rotate_right(self.right[i]); return self.rotate_left(i)
        return i

    def insert(self,key):
        old=self.count; self.root=self.insert_node(self.root,key)
        if self.count>old: print("Element inserted")

    def min_node(self,i):
        while self.left[i]!=-1: i=self.left[i]
        return i

    def delete_node(self,i,key):
        if i==-1: return -1
        if key<self.data[i]: self.left[i]=self.delete_node(self.left[i],key)
        elif key>self.data[i]: self.right[i]=self.delete_node(self.right[i],key)
        else:
            if self.left[i]==-1: return self.right[i]
            if self.right[i]==-1: return self.left[i]
            t=self.min_node(self.right[i]); self.data[i]=self.data[t]
            self.right[i]=self.delete_node(self.right[i],self.data[t])
        self.update(i); b=self.balance(i)
        if b>1 and self.balance(self.left[i])>=0: return self.rotate_right(i)
        if b>1 and self.balance(self.left[i])<0:
            self.left[i]=self.rotate_left(self.left[i]); return self.rotate_right(i)
        if b<-1 and self.balance(self.right[i])<=0: return self.rotate_left(i)
        if b<-1 and self.balance(self.right[i])>0:
            self.right[i]=self.rotate_right(self.right[i]); return self.rotate_left(i)
        return i

    def delete(self,key):
        if not self.search(key): print("Element not found"); return
        self.root=self.delete_node(self.root,key); print("Element deleted")

    def search_node(self,i,key):
        if i==-1: return False
        if self.data[i]==key: return True
        return self.search_node(self.left[i],key) if key<self.data[i] else self.search_node(self.right[i],key)
    def search(self,key): return self.search_node(self.root,key)

    def traverse(self,i,order,out):
        if i==-1: return
        if order=="pre": out.append(self.data[i])
        self.traverse(self.left[i],order,out)
        if order=="in": out.append(self.data[i])
        self.traverse(self.right[i],order,out)
        if order=="post": out.append(self.data[i])

    def display(self):
        print("Index  Data  Left  Right  Height")
        for i in range(self.count):
            print(i, self.data[i], self.left[i], self.right[i], self.height[i])

def main():
    t=AVLArray(int(input("Array capacity (e.g. 100): ")))
    while True:
        print("\n1.Insert 2.Delete 3.Search 4.Inorder 5.Preorder 6.Postorder 7.Display 8.Exit")
        c=input("Choice: ")
        if c=="1": t.insert(int(input("Value: ")))
        elif c=="2": t.delete(int(input("Value: ")))
        elif c=="3": print("Found" if t.search(int(input("Value: "))) else "Not found")
        elif c in ("4","5","6"):
            order={"4":"in","5":"pre","6":"post"}[c]; out=[]
            t.traverse(t.root,order,out); print(out)
        elif c=="7": t.display()
        elif c=="8": break
        else: print("Invalid choice")

if __name__=="__main__": main()
