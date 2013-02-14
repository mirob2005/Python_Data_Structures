from LinkedList_Double import DoublyNode

#Inherits __init__ from DoublyNode
class CircularNode(DoublyNode):
    pass

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        if(self.head != None):
            string = ("HEAD(%d) <"%self.head.data)
        else:
            string = ("HEAD(None) <")
        ptr = self.head
        if(ptr != None):
            while True:
                if(ptr == self.head):
                    string += " "
                if(ptr.prev == None):
                    string += "(None)<-["
                else:
                    string += "("+ str(ptr.prev.data)+ ")<-["
                string += str(ptr.data)
                if(ptr.next == None):
                    string+="]->(None)"
                else:
                    string += "]->("+str(ptr.next.data)+") "
                ptr = ptr.next
                if(ptr == self.head): break
        if(self.tail != None):
            string+=(" > TAIL(%d)"%self.tail.data)
        else:
            string+= " > TAIL(None)"
        return string
    
    def insert(self, data):
        if(self.head==None):
            self.head = CircularNode(data,None,None)
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head
        else:
            oldHead = self.head
            self.head = CircularNode(data,self.head, self.tail)
            oldHead.prev = self.head
            self.tail.next = self.head
        
    def append(self, data):
        ptr = self.head
        if(ptr == None):
            self.insert(data)
        else:
            while ptr.next != self.head:
                ptr=ptr.next
            ptr.next = CircularNode(data, self.head, ptr)
            self.tail = ptr.next
            self.head.prev = self.tail
            
    def returnIndex(self, data):
        ptr = self.head
        index = 0
        if(ptr != None):
            while True:
                if(ptr.data == data):
                    return index
                index += 1
                ptr=ptr.next
                if(ptr == self.head): break
        return None
    
    def updateIndex(self,index,data):
        if(index <0 or self.head == None):
            return False
        currentIndex = 0
        ptr = self.head
        while True:
            if(currentIndex == index):
                ptr.data = data
                return True
            currentIndex+=1
            ptr=ptr.next
            if(ptr == self.head): break
        return False
    
    def deleteIndex(self, index):
        if(index<0 or self.head == None):
            return False
        ptr = self.head
        if(index==0):
            self.head = self.head.next
            ptr.next = None
            ptr.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
            return True
        currentIndex=0
        while ptr.next != self.head:
            if(currentIndex+1 == index):
                self.deletePtr(ptr)
                return True
            ptr=ptr.next
            currentIndex+=1
        return False
    
    def insertBeforeIndex(self,index,data):
        if(index==0):
            self.insert(data)
            return True
        if(index <0 or self.head == None):
            return False
        ptr=self.head
        currentIndex=0
        while True:
            if(currentIndex+1 == index):
                ptr.next = CircularNode(data,ptr.next,ptr)
                if(ptr == self.tail):
                    self.tail = ptr.next
                ptr.next.next.prev = ptr.next
                return True
            currentIndex+=1
            ptr=ptr.next
            if(ptr == self.head): break
        return False
    
    def insertAfterIndex(self,index,data):
        if(index ==-1):
            self.insert(data)
            return True        
        if(index <-1 or self.head == None):
            return False
        currentIndex=0
        ptr=self.head
        while True:
            if(currentIndex==index):
                ptr.next = CircularNode(data,ptr.next,ptr)
                if(ptr == self.tail):
                    self.tail = ptr.next                
                ptr.next.next.prev = ptr.next
                return True
            currentIndex+=1
            ptr=ptr.next
            if(ptr == self.head): break
        return False

    def deleteData(self, data):
        ptr = self.head
        if(ptr == None):
            return False
        if(self.head.data == data):
            self.head = self.head.next
            ptr.next = None
            ptr.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
            return True
        while ptr.next != self.head:
            if(ptr.next.data == data):
                self.deletePtr(ptr)
                return True
            ptr = ptr.next
        return False
    
    def deletePtr(self, ptr):
        if(ptr.next == self.tail):
            self.tail = ptr
        tempptr = ptr.next.next
        ptr.next.prev = None
        ptr.next.next = None
        ptr.next = tempptr
        if(ptr.next != None):
            ptr.next.prev = ptr
    
    def deleteAllData(self,data):
        success = self.deleteData(data)
        if(success):
            while(self.deleteData(data)):
                continue
        return success
        
    def insertAfterEveryData(self,data,dataToInsert):
        if(self.head == None):
            return False
        success = False
        ptr = self.head
        while True:
            if(ptr.data == data):
                ptr.next = CircularNode(dataToInsert,ptr.next,ptr)
                if(ptr == self.tail):
                    self.tail = ptr.next
                ptr.next.next.prev = ptr.next
                success = True
                ptr = ptr.next
            ptr = ptr.next
            if(ptr == self.head): break
        return success
    
    def insertBeforeEveryData(self,data,dataToInsert):
        if(self.head == None):
            return False
        success = False
        if(self.head.data == data):
            success = True
            self.insert(dataToInsert)
            ptr = self.head.next
        else:
            ptr = self.head
        while ptr.next != self.head:
            if(ptr.next.data == data):
                ptr.next = CircularNode(dataToInsert,ptr.next,ptr)
                if(ptr.next.next != None):
                    ptr.next.next.prev = ptr.next
                success = True
                ptr = ptr.next
            ptr = ptr.next
        return success
    
    def deleteList(self):
        ptr = self.head
        while self.head.next != self.head and self.head.prev != self.head:
            print("\nDeleting %d" % self.head.data)
            self.head = self.head.next
            ptr.next = None
            ptr.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
            ptr = self.head
            print("\t%s" % self)
        print("\nDeleting %d" % self.head.data)
        self.head.next = None
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = None
        self.head = None
        self.tail = None
        
    def copyList(self):
        copy = CircularLinkedList()
    
        ptr = self.head
        while True:
            copy.append(ptr.data)
            ptr = ptr.next
            if(ptr == self.head): break
        return copy
    
    def findMthToLastNode(self, M):
        if(M <= 0):
            return None
        ptr = self.tail
        for x in range(1,M):
            ptr = ptr.prev
            if(ptr == self.tail):
                return None
        return ptr.data
        

if __name__ == '__main__':
    alist = CircularLinkedList()

    for data in [4,3,2,1]:
        alist.insert(data)

    print(alist)