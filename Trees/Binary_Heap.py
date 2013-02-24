#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/23/2013

# This uses a queue for BFS traversal for printing purposes.
# It also uses a modified queue to keep track of nodes that will
#   be future subroots/parents.  If the current parent's children is
#   full we grab the next item in the queue to be the parent for the
#   upcoming children. Each time we add a node, we add it to the
#   queue. Each time we delete, we delete the last item added to
#   the queue hence the need to have a getLast() method.
# It uses a stack to keep track of parents who's children were
#   recently filled in. Need this so we can backtrack to these
#   previously filled parents in the case of deletes.  We then put
#   the parent we were on before backtracking back into the
#   queue but in the front of the line for inserting once again
#   hence the need for the insert() method.

from ADTs.Queue_modified_for_heap_use import Queue
from ADTs.Stack import Stack

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
        self.past = Stack()
        
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
            #print("Stacking %d"%self.current.key)
            self.past.push(self.current)
            return True
        if(self.current.left and self.current.right):
            self.current = self.queue.deQueue()
            #print("DeQ %d"%self.current.key)
            #print("Stacking %d"%self.current.key)
            self.past.push(self.current)
        if(not self.current.left):
            self.current.left = Node(key, self.current,None,None)
            #print("Qing1 %d"%self.current.left.key)
            self.queue.enQueue(self.current.left)
            self.heapifyUp(self.current.left)
            return True
        elif(not self.current.right):
            self.current.right = Node(key, self.current,None,None)
            self.queue.enQueue(self.current.right)
            #print("Qing2 %d"%self.current.right.key)
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
            returned = self.queue.getLast()
            #print("deQing %s"%returned.key)
        elif(self.current.left):
            if(self.current == self.root):
                self.root.key = self.current.left.key
                self.current.left.parent = None
                self.current.left = None
                returned = self.queue.getLast()
                #print("deQing %s"%returned.key)
            else:
                self.root.key = self.current.left.key
                self.current.left.parent = None
                self.current.left = None
                returned = self.queue.getLast()
                #print("deQing %s"%returned.key)
                pop = self.past.pop()
                #print("Popping and inserting %s"%pop.key)
                self.queue.insert(pop)
                self.current = self.past.pop()
                self.past.push(self.current)
        else:
            pop = self.past.pop()
            #print("Popping%s"%pop.key)
            self.root = None
        self.heapifyDown(self.root)
        return returnValue
    
    def heapifyDown(self, ptr):
        #root is none, or no children to swap
        if(not ptr or (not ptr.left and not ptr.right)):
            return
        if(not ptr.right or ptr.left.key > ptr.right.key):
            if(ptr.left.key > ptr.key):
                temp = ptr.key
                ptr.key = ptr.left.key
                ptr.left.key = temp
                ptr = ptr.left
            else:
                return
        else:
            if(ptr.right.key > ptr.key):
                temp = ptr.key
                ptr.key = ptr.right.key
                ptr.right.key = temp
                ptr = ptr.right
            else:
                return
        self.heapifyDown(ptr)


if __name__ == '__main__':
    
    bh = BinaryHeap()
    
    bh.insert(0)
    print("After Inserting %d : %s\n"%(0,bh))
    bh.insert(1)
    print("After Inserting %d :%s\n"%(1,bh))
    returned = bh.delete()
    print("After Delete %d: %s\n"%(returned,bh))
    
    bh.insert(2)
    print("After Inserting %d : %s\n"%(2,bh))
    bh.insert(3)
    print("After Inserting %d :%s\n"%(3,bh))
    returned = bh.delete()
    print("After Delete %d: %s\n"%(returned,bh))
    
    bh.insert(4)
    print("After Inserting %d : %s\n"%(4,bh))
    bh.insert(5)
    print("After Inserting %d :%s\n"%(5,bh))
    returned = bh.delete()
    print("After Delete %d: %s\n"%(returned,bh))
    
    returned = bh.delete()
    print("After Delete %d: %s\n"%(returned,bh))
    
    returned = bh.delete()
    print("After Delete %d: %s\n"%(returned,bh))
    
    returned = bh.delete()
    print("After Delete %d: %s\n"%(returned,bh))
    
    bh.insert(6)
    print("After Inserting %d : %s\n"%(6,bh))
    bh.insert(7)
    print("After Inserting %d :%s\n"%(7,bh))
    bh.insert(8)
    print("After Inserting %d :%s\n"%(8,bh))
    bh.insert(9)
    print("After Inserting %d :%s\n"%(9,bh))