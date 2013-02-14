class Element:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    def __str__(self):
        head = self.head
        string = "["
        while head:
            string += head.value + " "
            head = head.next
        return string + "]"
    
    def push(self, element):
        self.head = Element(element, self.head)

    
    def pop(self):
        if self.empty(): return None
        result = self.head.value
        self.head = self.head.next
        return result
    
    def empty(self):
        return self.head == None

if __name__ == "__main__":
    
    stack = Stack()
    elements = ["first", "second", "third", "fourth"]
    for e in elements:
        stack.push(e)
        
    print(stack)

    result = []
    while not stack.empty():
        result.append(stack.pop())

    assert result == ["fourth", "third", "second", "first"]
