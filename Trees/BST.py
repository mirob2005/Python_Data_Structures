from ADTs.Queue_head import Queue
from ADTs.Stack import Stack

class Node:
    def __init__(self,key,left,right):
        self.key = key
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
        
    def __str__(self):
        string = ("BFS: %s\n" % self.printBFS())
        string += ("DFS (Preorder): %s\n" % self.printDFSpreorder())
        string += ("DFS (Inorder): %s\n" % self.printDFSinorder())
        string += ("DFS (Postorder): %s\n" % self.printDFSpostorder())
        return string
    
    def printBFS(self):
        return str(self.traverseBFS())
    
    def printDFSpreorder(self):
        return str(self.traverseDFSpreorder())
    
    def printDFSinorder(self):
        return str(self.traverseDFSinorder())
    
    def printDFSpostorder(self):
        return str(self.traverseDFSpostorder())
    
    def insert(self, key):
        if(self.root == None):
            self.root = Node(key,None,None)
        else:
            ptr = self.root
            while ptr:
                if(key < ptr.key):
                    if(ptr.left == None):
                        ptr.left = Node(key, None, None)
                        return
                    else:
                        ptr = ptr.left
                elif(key > ptr.key):
                    if(ptr.right == None):
                        ptr.right = Node(key, None, None)
                        return
                    else:
                        ptr = ptr.right
                else:
                    print("Key %s already exists in BST!"% key)
                    return
                
    def find(self, key):
        pass
    
    def delete(self, key):
        pass
    
    def traverseBFS(self):
        keys = []
        bfsQ = Queue()
        bfsQ.enQueue(self.root)
        cur = bfsQ.deQueue()
        while cur:
            #print("cur.key = %s"%cur.key)
            keys.append(cur.key)
            #print("%s added to keys" % str(cur.key))
            if(cur.left):
                bfsQ.enQueue(cur.left)
                #print('cur.left.key = %s' % cur.left.key)
            if(cur.right):
                bfsQ.enQueue(cur.right)
                #print("cur.right.key = %s"%cur.right.key)
            cur = bfsQ.deQueue()
            #print("--------------------------------")
        return keys
    
    def traverseDFSpreorder(self):
        #root, left subtree, right subtree
        keys = []
        dfsS = Stack()
        dfsS.push(self.root)
        cur = dfsS.pop()
        while cur:
            #print("cur.key = %s"%cur.key)
            keys.append(cur.key)
            #print("%s added to keys" % str(cur.key))
            if(cur.right):
                dfsS.push(cur.right)
                #print("cur.right.key = %s"%cur.right.key)
            if(cur.left):
                dfsS.push(cur.left)
                #print('cur.left.key = %s' % cur.left.key)
            cur = dfsS.pop()
            #print("--------------------------------")
        return keys
        
    def traverseDFSinorder(self):
        #left subtree, root, right subtree
        keys = []
        dfsS = Stack()
        dfsS.push(self.root)
        cur = dfsS.pop()
        while cur:
            #print("cur.key = %s"%cur.key)
            if((not cur.left) or (cur.left.key in keys)):
                keys.append(cur.key)
                #print("%s added to keys" % str(cur.key))
                if(cur.right):
                    dfsS.push(cur.right)
                    #print("cur.right.key = %s"%cur.right.key)
            else:
                dfsS.push(cur)
                if(cur.left and cur.left.key not in keys):
                    dfsS.push(cur.left)
                    #print('cur.left.key = %s' % cur.left.key)
            cur = dfsS.pop()
            #print("--------------------------------")
        return keys
    
    def traverseDFSpostorder(self):
        #left subtree, right subtree, root
        keys = []
        dfsS = Stack()
        dfsS.push(self.root)
        cur = dfsS.pop()
        while cur:
            #print("cur.key = %s"%cur.key)
            if(((not cur.left) or (cur.left.key in keys)) and ((not cur.right) or (cur.right.key in keys))):
                keys.append(cur.key)
                #print("%s added to keys" % str(cur.key))
            else:
                dfsS.push(cur)
                if(cur.right):
                    dfsS.push(cur.right)
                    #print("cur.right.key = %s"%cur.right.key)
                if(cur.left):
                    dfsS.push(cur.left)
                    #print('cur.left.key = %s' % cur.left.key)
            cur = dfsS.pop()
            #print("--------------------------------")
        return keys
        
    def copyTree(self):
        pass
    
if __name__ == '__main__':
    myT = BST()
        
    for data in [5,2,3,1,0,4,7,6,9,8,10]:
        myT.insert(data)

    if(myT.find(1)):
        print("1 is in BST")
    else:
        print("1 is not in BST")

    print(myT)
