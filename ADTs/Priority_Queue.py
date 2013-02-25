#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/23/2013

from Binary_Heap_Array_Structure import BinaryHeap

class PriorityQueue:
    def __init__(self):
        self.order = BinaryHeap()
    def __str__(self):
        temp = self.order.copyHeap()
        front = temp.delete()
        string = ("<Front>")
        while front:
            string+= (" %s"%front)
            front = temp.delete()
        string += " <BACK>"
        return string
    def enQueue(self,key):
        self.order.insert(key)
    def deQueue(self):
        return self.order.delete()
    
if __name__ == '__main__':
    pq = PriorityQueue()
    
    print(pq)
    print(pq.deQueue())
    
    for data in [1,2,6,4,2,8,9,6,4,3,2,6,7,8,9,10,11,23,53,56,78,98,78,645,23]:
        pq.enQueue(data)
        
    print(pq)
    
    print("First Item: %s"%pq.deQueue())
    print(pq)
    
    pq.enQueue(100)
    pq.enQueue(53)
    pq.enQueue(-1)
    
    print(pq)