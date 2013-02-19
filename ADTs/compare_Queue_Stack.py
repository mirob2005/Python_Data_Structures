from Queue_head import Queue
from Stack import Stack

myQ = Queue()
myS = Stack()

for data in [1,2,3,4,5]:
    myQ.enQueue(data)
    myS.push(data)
    
print("Queue:")
print(myQ)

print("\nStack: ")
print(myS)


print("Removing first element: ")
print("Queue returned: %s"%myQ.deQueue())
print("Stack returned: %s"%myS.pop())

print("\nQueue:")
print(myQ)

print("\nStack: ")
print(myS)

print("Adding a 6 element:")
myQ.enQueue(6)
myS.push(6)
print("\nQueue:")
print(myQ)

print("\nStack: ")
print(myS)

print("Removing next element: ")
print("Queue returned: %s"%myQ.deQueue())
print("Stack returned: %s"%myS.pop())

print("\nEmptying both...")
queueReturned = myQ.deQueue()
stackReturned = myS.pop()
while queueReturned and stackReturned:
    print("Queue Returned: %s"% queueReturned)
    print("Stack Returned: %s"% stackReturned)
    queueReturned = myQ.deQueue()
    stackReturned = myS.pop()
    
print("\nFinal: ")
print("Queue:")
print(myQ)

print("\nStack: ")
print(myS)