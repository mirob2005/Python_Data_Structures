class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        ptr = self.head
        string = "HEAD <"
        while ptr:
            if(ptr == self.head):
                string += " "
            string += "["+ str(ptr.data)
            if(ptr.next == None):
                string+="]->(None)"
            else:
                string += "]->("+str(ptr.next.data)+") "
            ptr = ptr.next
        return string + " > TAIL"
    
    def insert(self, data):
        self.head = Node(data,self.head)
        
    def append(self, data):
        ptr = self.head
        if(ptr == None):
            self.insert(data)
        else:
            while ptr.next:
                ptr=ptr.next
            ptr.next = Node(data, None)
        
    def returnIndex(self, data):
        ptr = self.head
        index = 0
        while ptr:
            if(ptr.data == data):
                return index
            index += 1
            ptr=ptr.next
        return None
    
    def updateIndex(self,index,data):
        if(index<0 or self.head == None):
            return False
        currentIndex = 0
        ptr = self.head
        while ptr:
            if(currentIndex == index):
                ptr.data = data
                return True
            currentIndex+=1
            ptr=ptr.next
        return False
    
    def deleteIndex(self, index):
        if(index<0 or self.head == None):
            return False
        ptr=self.head
        if(index==0):
            self.head = self.head.next
            ptr.next = None
            return True
        currentIndex=0
        while ptr.next:
            if(currentIndex+1 == index):
                self.deletePtr(ptr)
                return True
            ptr=ptr.next
            currentIndex+=1
        return False    

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
                ptr.next = Node(data,ptr.next)
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
                ptr.next = Node(data,ptr.next)
                return True
            currentIndex+=1
            ptr=ptr.next
        return False
    
    def deleteData(self, data):
        ptr = self.head
        if(ptr == None):
            return False
        if(self.head.data == data):
            self.head = self.head.next
            ptr.next = None
            return True
        while ptr.next:
            if(ptr.next.data == data):
                self.deletePtr(ptr)
                return True
            ptr = ptr.next
        return False
    
    def deletePtr(self,ptr):
        tempptr = ptr.next.next
        ptr.next.next = None
        ptr.next = tempptr 

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
        while ptr:
            if(ptr.data == data):
                ptr.next = Node(dataToInsert,ptr.next)
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
                ptr.next = Node(dataToInsert,ptr.next)                
                success = True
                ptr = ptr.next
            ptr = ptr.next
        return success
    
    def deleteList(self):
        ptr  = self.head
        while self.head:
            #print("\nDeleting %d" % self.head.data)
            self.head = self.head.next
            ptr.next = None
            ptr = self.head
            #print("\t%s" % self)
        self.head = None
    
    def copyList(self):
        copy = LinkedList()
        
        ptr = self.head
        while ptr:
            copy.append(ptr.data)
            ptr = ptr.next
        
        return copy
    
    def findMthToLastNode(self, M):
        if(M <= 0):
            return None
        ptr = self.head
        mBehindPtr = self.head
        for i in range(0,M,1):
            if(ptr == None):
                return None
            ptr = ptr.next
        while ptr:
            ptr = ptr.next
            mBehindPtr = mBehindPtr.next
        return mBehindPtr.data

if __name__ == '__main__':
    alist = LinkedList()
    
    for data in [0,3,0,1]:
        alist.insert(data)
    print(alist)