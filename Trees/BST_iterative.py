from ADTs.Queue_head import Queue
from ADTs.Stack import Stack

class Node:
    def __init__(self,key,left,right,parent):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        
class BST:
    def __init__(self):
        self.root = None
        #Use this to alternate between replacing nodes with inorder
        #successor and predecessor
        self.replaceWithSuccessor = False
        
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
            self.root = Node(key,None,None,None)
            return True
        else:
            ptr = self.root
            while ptr:
                if(key < ptr.key):
                    if(ptr.left == None):
                        ptr.left = Node(key, None, None, ptr)
                        return True
                    else:
                        ptr = ptr.left
                elif(key > ptr.key):
                    if(ptr.right == None):
                        ptr.right = Node(key, None, None, ptr)
                        return True
                    else:
                        ptr = ptr.right
                else:
                    return False
                
    def insertList(self, alist):
        boolResult = True
        for item in alist:
            boolResult = boolResult and self.insert(item)
        return boolResult
                
    def find(self, key):
        ptr = self.root
        while ptr:
            if(key == ptr.key):
                return True
            elif(key > ptr.key):
                ptr = ptr.right
            else:
                ptr = ptr.left
        return False
    
    def delete(self, key):
        #alternate between using inorder predecessor and successor
        ptr = self.root
        while ptr:
            if(key == ptr.key):
                #If leaf node:
                if(not ptr.left and not ptr.right):
                    #root node
                    if(not ptr.parent):
                        self.root = None
                    elif(ptr.parent.right == ptr):
                        ptr.parent.right = None
                    else:
                        ptr.parent.left = None
                    ptr = None
                    return True
                #If only 1 child (right)
                elif(not ptr.left and ptr.right):
                    #root node
                    if(not ptr.parent):
                        self.root = ptr.right
                    elif(ptr.parent.right == ptr):
                        ptr.parent.right = ptr.right
                    else:
                        ptr.parent.left = ptr.right
                    ptr.right.parent = ptr.parent
                    ptr = None
                    return True
                #If only 1 child (left)
                elif(ptr.left and not ptr.right):
                    #root node
                    if(not ptr.parent):
                        self.root = ptr.left
                    if(ptr.parent.right == ptr):
                        ptr.parent.right = ptr.left
                    else:
                        ptr.parent.left = ptr.left
                    ptr.left.parent = ptr.parent
                    ptr = None                    
                    return True
                #If 2 children
                else:
                    if(self.replaceWithSuccessor):
                        #Greatest Right Child (inorder successor)
                        childptr = ptr.right
                        while childptr.left:
                            childptr = childptr.left
                        ptr.key = childptr.key
                        #if replacement node has a right child
                        if(childptr.right):
                            if(childptr.parent.right == childptr):
                                childptr.parent.right = childptr.right
                            else:
                                childptr.parent.left = childptr.right
                            childptr.right.parent = childptr.parent
                        else:
                            if(childptr.parent.right == childptr):
                                childptr.parent.right = None
                            else:
                                childptr.parent.left = None
                        childptr = None
                    else:
                        #Greatest Left Child (inorder predecessor)
                        childptr = ptr.left
                        while childptr.right:
                            childptr = childptr.right
                        ptr.key = childptr.key
                        #if replacement node has a left child
                        if(childptr.left):
                            if(childptr.parent.right == childptr):
                                childptr.parent.right = childptr.left
                            else:
                                childptr.parent.left = childptr.left
                            childptr.left.parent = childptr.parent
                        else:
                            if(childptr.parent.right == childptr):
                                childptr.parent.right = None
                            else:
                                childptr.parent.left = None
                        childptr = None
                    self.replaceWithSuccessor = not self.replaceWithSuccessor
                    return True
            elif(key > ptr.key):
                ptr = ptr.right
            else:
                ptr = ptr.left
        return False
    
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
        copy = BST()
        if(not self.root):
            return copy
        dfsS = Stack()
        dfsS.push(self.root)
        cur = dfsS.pop()
        while cur:
            copy.insert(cur.key)
            if(cur.right):
                dfsS.push(cur.right)
            if(cur.left):
                dfsS.push(cur.left)
            cur = dfsS.pop()
        return copy
    
    def findMin(self):
        if(not self.root):
            return None
        ptr = self.root
        while ptr.left:
            ptr = ptr.left
        return ptr.key

    def findMax(self):
        if(not self.root):
            return None
        ptr = self.root
        while ptr.right:
            ptr = ptr.right
        return ptr.key