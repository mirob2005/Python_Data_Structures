from LinkedList_Single import LinkedList
from LinkedList_Single import Node

class DoublyNode(Node):
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList(LinkedList):
    #Inherits __init__ , returnIndex(index), updateIndex(index), findMthToLastNode(M)
        
    def __str__(self):
        ptr = self.head
        string = "HEAD <"
        while ptr:
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
        return string + " > TAIL"
    
    def insert(self, data):
        if(self.head==None):
            self.head = DoublyNode(data,self.head, None)
        else:
            oldHead = self.head
            self.head = DoublyNode(data,self.head, None)
            oldHead.prev = self.head
        
    def append(self, data):
        ptr = self.head
        if(ptr == None):
            self.insert(data)
        else:
            while ptr.next:
                ptr=ptr.next
            ptr.next = DoublyNode(data, None, ptr)
    
    def insertBeforeIndex(self,index,data):
        if(index <0):
            return False
        if(index==0):
            self.insert(data)
            return True
        ptr=self.head
        currentIndex=0
        while ptr:
            if(currentIndex+1 == index):                
                ptr.next = DoublyNode(data,ptr.next,ptr)
                if(ptr.next.next != None):
                    ptr.next.next.prev = ptr.next
                return True
            currentIndex+=1
            ptr=ptr.next
        return False
    
    def insertAfterIndex(self,index,data):
        if(index <-1):
            return False
        if(index ==-1):
            self.insert(data)
            return True
        currentIndex=0
        ptr=self.head
        while ptr:
            if(currentIndex==index):
                ptr.next = DoublyNode(data,ptr.next,ptr)
                if(ptr.next.next != None):
                    ptr.next.next.prev = ptr.next
                return True
            currentIndex+=1
            ptr=ptr.next
        return False
    
    def deleteIndex(self, index):
        if(index<0 or self.head == None):
            return False
        ptr = self.head
        if(index==0):
            self.head = self.head.next
            ptr.next = None
            self.head.prev = None
            return True
        currentIndex=0
        while ptr.next:
            if(currentIndex+1 == index):
                self.deletePtr(ptr)
                return True
            ptr=ptr.next
            currentIndex+=1
        return False
    
    def deleteData(self, data):
        ptr = self.head
        if(ptr == None):
            return False
        if(self.head.data == data):
            self.head = self.head.next
            ptr.next = None
            self.head.prev = None
            return True
        while ptr.next:
            if(ptr.next.data == data):
                self.deletePtr(ptr)
                return True
            ptr = ptr.next
        return False
    
    def deletePtr(self, ptr):
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
    
    def deleteList(self):
        ptr = self.head
        while self.head:
            print("\nDeleting %d" % self.head.data)
            self.head = self.head.next
            ptr.next = None            
            if(self.head != None): self.head.prev = None
            ptr = self.head
            print("\t%s" % self)
        self.head = None
        
    def copyList(self):
        copy = DoublyLinkedList()

        ptr = self.head
        while ptr:
            copy.append(ptr.data)
            ptr = ptr.next
        
        return copy
        
    def insertAfterEveryData(self,data,dataToInsert):
        if(self.head == None):
            return False
        success = False
        ptr = self.head
        while ptr:
            if(ptr.data == data):
                ptr.next = DoublyNode(dataToInsert,ptr.next,ptr)
                if(ptr.next.next != None):
                    ptr.next.next.prev = ptr.next
                success = True
                ptr = ptr.next
            ptr = ptr.next
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
        while ptr.next:
            if(ptr.next.data == data):
                ptr.next = DoublyNode(dataToInsert,ptr.next,ptr)
                if(ptr.next.next != None):
                    ptr.next.next.prev = ptr.next
                success = True
                ptr = ptr.next
            ptr = ptr.next
        return success

if __name__ == '__main__':
    alist = DoublyLinkedList()
    
    for data in [4,3,2,1]:
        alist.insert(data)
    print(alist)
