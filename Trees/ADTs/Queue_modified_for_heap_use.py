#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/23/2013

# This Queue also features the ability to delete the last thing added to the
# queue and insert an item in front of the Queue to be used in Binary_Heap.py
# to keep track of the upcoming node's parents as described in Binary_Heap.py.

class Element:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = None        
        
    def __str__(self):
        ptr = self.head
        if(self.head==None):
            string = "Front < > Back"
        else:
            string = "Front < "
            while ptr:
                string += ("%s "%ptr.data)
                ptr = ptr.next
            string += "> Back"
        return string
    
    def insert(self,data):
        #Insert in Front of Queue
        self.head = Element(data,self.head)
    
    def getLast(self):
        if(not self.head):
            return None
        ptr = self.head
        if(ptr.next):
            while ptr.next.next:
                ptr = ptr.next
            returnValue = ptr.next.data
            ptr.next = None
        else:
            returnValue = ptr.data
            self.head = None
        return returnValue
        
        
    def enQueue(self,data):
        #Append the most recent node to the end
        ptr = self.head
        if(ptr == None):
            self.head = Element(data,self.head)
        else:
            while ptr.next:
                ptr=ptr.next
            ptr.next = Element(data, None)
        
    def deQueue(self):
        #move head ptr and return previous head
        if(self.head == None):
            return None
        ptr = self.head
        self.head = self.head.next
        ptr.next = None
        return ptr.data
    
if __name__ == '__main__':
    myQ = Queue()
    
    for data in [1,2,3,4]:
        myQ.enQueue(data)
        
    print(myQ)
    
    print(myQ.getLast())
    print(myQ)
    #for key in ['First','Second','Third','Fourth','Fifth']:
    #    print("%s element out: %s" % (key,myQ.deQueue()))
    #    print (myQ)
    #    
    #print("Test Empty: %s"%myQ.deQueue())
    #print (myQ)
    #
    #print("_______")
    #for data in [1,2,3,4]:
    #    print("Adding %s" % data)
    #    myQ.enQueue(data)
    #    print(myQ)
    #    print("Adding %s" % data)
    #    myQ.enQueue(data)
    #    print(myQ)
    #    print("Removing %s"%myQ.deQueue())
    #    print(myQ)
    #
    #print(myQ)
    #print("_______")
    #
    #first = myQ.deQueue()
    #while first != None:
    #    print("Removing %s"% first)
    #    print(myQ)
    #    first = myQ.deQueue()