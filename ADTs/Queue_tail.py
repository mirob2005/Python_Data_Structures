class Element:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        ptr = self.head
        if(self.head==None and self.tail == None):
            string = "Last(None) < > First(None)"
        else:
            string = ("Last(%s) < "% self.head.data)
            while ptr != self.tail:
                #string += ("(%s-%s-%s), "% (str(ptr.prev.data),str(ptr.data),str(ptr.next.data)))
                string += ("(%s), "%ptr.data)
                ptr = ptr.next
            if(self.tail != None):
                string += ("(%s)"%self.tail.data)
                #string += ("(%s-%s-%s)"% (str(self.tail.prev.data),str(self.tail.data),str(self.tail.next.data)))
            string += (" > First(%s)"% self.tail.data)
        return string
        
    def enQueue(self,data):
        if(self.head == None):
            self.head = Element(data, self.head, self.tail)
            self.tail = self.head
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        else:
            ptr = self.head
            self.head = Element(data, self.head, self.tail)
            ptr.prev = self.head
            self.tail.next = self.head
        
    def deQueue(self):
        if(self.head == None):
            return None
        if(self.head == self.tail):
            returnData = self.tail.data
            self.head = None
            self.tail = None
            return returnData
        ptr = self.tail
        returnData = self.tail.data
        self.tail = self.tail.prev
        ptr.next = None
        ptr.prev = None
        ptr = None
        self.tail.next = self.head
        self.head.prev = self.tail
        return returnData
    
if __name__ == '__main__':
    myQ = Queue()
    
    for data in [1,2,3,4,5]:
        myQ.enQueue(data)
        
    print(myQ)
    
    for key in ['First','Second','Third','Fourth','Fifth']:
        print("%s element out: %s" % (key,myQ.deQueue()))
        print (myQ)
        
    print("Test Empty: %s"%myQ.deQueue())
    print (myQ)
    
    print("_______")
    for data in [1,2,3,4]:
        print("Adding %s" % data)
        myQ.enQueue(data)
        print(myQ)
        print("Adding %s" % data)
        myQ.enQueue(data)
        print(myQ)
        print("Removing %s"%myQ.deQueue())
        print(myQ)
    
    print(myQ)
    print("_______")
    
    first = myQ.deQueue()
    while first != None:
        print("Removing %s"% first)
        print(myQ)
        first = myQ.deQueue()