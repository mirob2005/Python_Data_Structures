#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/25/2013

# Binary Heap implemented using an array instead of a binary tree data structure
# Children are at a[2i+1] and a[2i+2]
# Parent is at a[floor((i-1)/2)]
# where the array goes from 0 to n-1 and the root is at index 0

class BinaryHeap:
    def __init__(self):
        self.nodes = []
        
    def __str__(self):
            return self.traverseBFS()
    
    def traverseBFS(self):
        string = ""
        index = 0
        size = len(self.nodes)
        for node in self.nodes:
            parent = self.getParent(index)
            leftChild = self.getLeftChild(index)
            rightChild = self.getRightChild(index)
            string += ("\n%s - (%s|%s, %s)"% (node,parent,leftChild,rightChild))
            index += 1
        return string if not self.isEmpty() else "(Empty)"
    
    def returnBFS(self):
        return self.nodes
    
    def insert(self,key):
        self.nodes.append(key)
        self.heapifyUp()
        return True
    
    def insertList(self, alist):
        boolResult = True
        for item in alist:
            if(self.insert(item) == False):
                boolResult = False
        return boolResult
    
    def delete(self):
        if self.isEmpty():
            return None
        returnValue = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()
        self.heapifyDown(0, self.getLeftChildIndex(0), self.getRightChildIndex(0))
        return returnValue
    
    def peek(self):
        return self.nodes[0] if not self.isEmpty() else None
    
    def heapifyUp(self):
        child = len(self.nodes)-1
        parent = self.getParentIndex(child)
        while(self.nodes[child] > self.nodes[parent]):
            temp = self.nodes[child]
            self.nodes[child] = self.nodes[parent]
            self.nodes[parent] = temp
            child = parent
            parent = self.getParentIndex(child)
            
    def heapifyDown(self,parent,left,right):
        if not self.validChild(left) and not self.validChild(right):
            return
        if not self.validChild(right) or self.nodes[left] > self.nodes[right]:
            if(self.nodes[left] > self.nodes[parent]):
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[left]
                self.nodes[left] = temp
                parent = self.getLeftChildIndex(parent)
            else:
                return
        else:
            if(self.nodes[right] > self.nodes[parent]):
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[right]
                self.nodes[right] = temp
                parent = self.getRightChildIndex(parent)
            else:
                return
        self.heapifyDown(parent, self.getLeftChildIndex(parent), self.getRightChildIndex(parent))
            
    def validChild(self,index):
        return True if index < len(self.nodes) else False
            
    def getLeftChildIndex(self,index):
        return ((2*index)+1)
    
    def getLeftChild(self,index):
        child = self.getLeftChildIndex(index)
        return self.nodes[child] if self.validChild(child) else None
    
    def getRightChildIndex(self,index):
        return ((2*index)+2)
    
    def getRightChild(self,index):
        child = self.getRightChildIndex(index)
        return self.nodes[child] if self.validChild(child) else None
    
    def getParentIndex(self,index):
        return int((index-1)/2)
    
    def getParent(self,index):
        return self.nodes[self.getParentIndex(index)] if index > 0 else None
    
    def isEmpty(self):
        return len(self.nodes)==0
    
    def copyHeap(self):
        copy  = BinaryHeap()
        copy.insertList(self.returnBFS())
        return copy
    
    def merge(self, heap):
        heapData = heap.returnBFS()
        self.insertList(heapData)
    
if __name__ == '__main__':
    
    bh = BinaryHeap()
    
    for data in range(0,6):
        bh.insert(data)
        
    print(bh)
    
    print(bh.delete())
    
    print(bh)