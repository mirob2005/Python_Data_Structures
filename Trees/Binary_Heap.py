from ADTs.Queue_head import Queue

class Node:
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        
class BinaryHeap:
    def __init__(self):
        self.root = None
        self.current = None
        self.queue = Queue()
        
    def __str__(self):
        return self.traverseBFS()
    
    def traverseBFS(self):
        string = ""
        bfsQ = Queue()
        bfsQ.enQueue(self.root)
        cur = bfsQ.deQueue()
        while cur:
            string += ("\n%s - (%s|%s, %s)"%(cur.key,
                                           cur.parent.key if cur.parent else None,
                                           cur.left.key if cur.left else None,
                                           cur.right.key if cur.right else None))
            if(cur.left):
                bfsQ.enQueue(cur.left)
            if(cur.right):
                bfsQ.enQueue(cur.right)
            cur = bfsQ.deQueue()
        if(string == ""):
            string = "(Empty)"
        return string
    
    def insert(self, key):
        if(not self.root):
            self.root = Node(key, None, None, None)
            self.current = self.root
            return True
        if(self.current.left and self.current.right):
            self.current = self.queue.deQueue()
        if(not self.current.left):
            self.current.left = Node(key, self.current,None,None)
            self.queue.enQueue(self.current.left)
            self.heapifyUp(self.current.left)
            return True
        elif(not self.current.right):
            self.current.right = Node(key, self.current,None,None)
            self.queue.enQueue(self.current.right)
            self.heapifyUp(self.current.right)
            return True
        return False
    
    def insertList(self, alist):
        boolResult = True
        for item in alist:
            if(self.insert(item) == False):
                boolResult = False
        return boolResult
        
    def heapifyUp(self, node):
        while(node.parent and node.key > node.parent.key):
            temp = node.parent.key
            node.parent.key = node.key
            node.key = temp
            node = node.parent
            
    def delete(self):
        if(not self.root):
            return None
        returnValue = self.root.key
        if(self.current.right):
            self.root.key = self.current.right.key
            self.current.right.parent = None
            self.current.right = None
        elif(self.current.left):
            self.root.key = self.current.left.key
            self.current.left.parent = None
            self.current.left = None
        else:
            self.root = None
        self.heapifyDown(self.root)
        return returnValue
    
    def heapifyDown(self, ptr):
        if(not ptr or (not ptr.left and not ptr.right)):
            return
        if(not ptr.right or ptr.left.key > ptr.right.key):
            temp = ptr.key
            ptr.key = ptr.left.key
            ptr.left.key = temp
            ptr = ptr.left
        else:
            temp = ptr.key
            ptr.key = ptr.right.key
            ptr.right.key = temp
            ptr = ptr.right
        self.heapifyDown(ptr)


if __name__ == '__main__':
    
    bh = BinaryHeap()
    
    print(bh)
    
    print(bh.delete())
    
    bh.insert(1)
    bh.insert(2)
    print(bh)
    
    #for key in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
    #    bh.insert(key)
    #
    #print(bh)
    #
    #print("\nReturned : %s" % str(bh.delete()))
    #
    #print(bh)