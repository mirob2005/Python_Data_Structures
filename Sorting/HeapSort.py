#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/25/2013

# Similar to Binary_Heap_Array_Structure.py but this includes a sorting mechanic
# O(n log n) running time to sort.
# O(n log n) to build heap + O(n log n) to swap each max value and heapify
# O(n) - Space Complexity

import random

class HeapSort:
    def __init__(self, unsortedList):
        self.nodes = []
        self.insertList(unsortedList)
        self.index = 1
        
    def __str__(self):
        return str(self.nodes)
    
    def getSorted(self):
        maxValue = self.delete()
        while self.index < len(self.nodes)-1:
            self.index += 1
            maxValue = self.delete()
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
        #Swap the first and last available nodes (self.index increments after each delete)
        self.nodes[0] = self.nodes[-self.index]
        self.nodes[-self.index] = returnValue
        self.heapifyDown(0, self.getLeftChildIndex(0), self.getRightChildIndex(0))
        return returnValue
    
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
        return True if index < len(self.nodes)-self.index else False
            
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
    
if __name__ == '__main__':
    
    a = [x for x in range(0,101)]
    random.shuffle(a)
    
    print("Shuffled List: %s\n"%a)
    
    heap = HeapSort(a)
    sortedList = heap.getSorted()
    a.sort()
    
    print("Heap Sorted: %s\n" % sortedList)
    print("List Sorted: %s\n" % a)
    print("Sorted %s"%(sortedList == a))