#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/17/2013

# Typical stack, all operations act on the head/top of the stack.

class Element:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    def __str__(self):
        ptr = self.head
        string = "TOP\n"
        if(self.head):
            while ptr:
                string += ("%s\n"%ptr.data)
                ptr = ptr.next
        else:
            string += "Empty\n"
        return string
    
    def push(self, element):
        self.head = Element(element, self.head)

    
    def pop(self):
        if self.empty(): return None
        result = self.head.data
        self.head = self.head.next
        return result
    
    def empty(self):
        return self.head == None

if __name__ == "__main__":
    
    myS = Stack()
    for data in [1,2,3,4,5]:
        myS.push(data)
        
    print(myS)
    
    for key in ['First','Second','Third','Fourth','Fifth']:
        print("%s element out: %s" % (key,myS.pop()))
        print (myS)
        
    print("Test Empty: %s"%myS.pop())
    print (myS)
    
    print("_______")
    for data in [1,2,3,4]:
        print("Adding %s" % data)
        myS.push(data)
        print(myS)
        print("Adding %s" % data)
        myS.push(data)
        print(myS)
        print("Removing %s"%myS.pop())
        print(myS)
    
    print(myS)
    print("_______")
    
    first = myS.pop()
    while first != None:
        print("Removing %s"% first)
        print(myS)
        first = myS.pop()
