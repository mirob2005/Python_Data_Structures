#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/3/2013

#Trie is built using a Tree-like structure
#Each node contains a single character and possibly a value
#Each word can be created by going from the root down any branch to a
#   terminating node or a node with a value(for prefixes)
#The traverseWords method goes through each branch and strings together
#   the words added to the trie by using the logic above.  

from ADTs.Queue_head import Queue
from ADTs.Stack import Stack

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = []
        
class Trie:
    def __init__(self):
        self.root = Node(None,None)
        self.output = ''

    def __str__(self):
        string = "BFS: %s"%str(self.traverseBFS())
        string += "\nWords: %s"%str(self.traverseWords())
        return string
    
    def __contains__(self, key):
        pass

    
    def traverseWords(self):
        self.output = ''
        if not self.root.next:
            self.output = 'Empty'
        for child in self.root.next:
            self.traverse(child,'')
        return self.output.rstrip(', ')
        
    def traverse(self,root,prefix):
        prefix += root.key
        for node in root.next:
            if node.next and not node.value:
                self.traverse(node,prefix)
            elif node.next and node.value:
                self.output += prefix + node.key + ' '# + (" (%s), "%node.value)
                self.traverse(node,prefix)
            else:
                self.output += prefix + node.key + ' '# + (" (%s), "%node.value)

    def traverseBFS(self):
        keys = []
        bfsQ = Queue()
        bfsQ.enQueue(self.root)
        cur = bfsQ.deQueue()
        while cur:
            if(cur != self.root):
                keys.append(cur.key)
            for node in cur.next:
                bfsQ.enQueue(node)
            cur = bfsQ.deQueue()
        return ', '.join([str(key) for key in keys])
    
    #IF key already exists, it just updates the value
    def add(self, key, value, root=None):
        if not type(key) == str:
            return False
        if not key:
            root.value = value
            return True
        if not root:
            root = self.root
        for node in root.next:
            if key[0] in node.key:
                return self.add(key[1:],value,root.next[root.next.index(node)])
        root.next.append(Node(key[0],None))
        return self.add(key[1:],value,root.next[-1])
    
    def remove(self, key):
        if not self.isMember(key, self.root):
            return False
        return self.removeHelper(key, self.root,0)
    
    def removeHelper(self,key,root,index):
        for node in root.next:
            if key[index] in node.key:
                #No next neighbors and value is set
                #Delete the element completely and recurse back and test previous index
                if not node.next and node.value != None:
                    del root.next[root.next.index(node)]
                    self.removeHelper(key,root,index-1)
                #Last element in key with a next neighbor and the value is set
                #Clear the value and DONE
                elif index == len(key)-1 and node.next and node.value != None:
                    node.value = None
                    return True
                else:
                    #Not the last key and there is a next neighbor, recurse further
                    self.removeHelper(key,node,index+1)
                    #This runs after the last element is deleted, and proccesses
                    #earlier nodes to check if they also need deleted
                    if not node.next and node.value == None:
                        del root.next[root.next.index(node)]
                    return True
        return False
    
    def isMember(self, key, root=None):
        if not type(key) == str or not key:
            return False
        if not root:
            root = self.root
        for node in root.next:
            if key[0] in node.key:
                if len(key) == 1 and node.value:
                    return True
                else:
                    return self.isMember(key[1:],root.next[root.next.index(node)])
        return False

    def updateValue(self,key,value, root=None):
        if not type(key) == str or not key:
            return False
        if not root:
            root = self.root
        for node in root.next:
            if key[0] in node.key:
                if len(key) == 1:
                    node.value = value
                    return True
                else:
                    return self.updateValue(key[1:],value,root.next[root.next.index(node)])
        return False
    
    def getValue(self,key,root=None):
        if not type(key) == str or not key:
            return None
        if not root:
            root = self.root
        for node in root.next:
            if key[0] in node.key:
                if len(key) == 1 and node.value:
                    return node.value
                else:
                    return self.getValue(key[1:],root.next[root.next.index(node)])
        return None
    
if __name__ == '__main__':
    
    t = Trie()
    
    t.add('bob',1)
    
    t.add('bad',2)
    t.add('ba',5)
    t.add('bat',3)
    t.add('banner',4)
    t.add('banno',4)
    t.add('add',3)
    t.add('apple',4)
    t.add('at',5)
    t.add('ate',6)
    
    print(t)
    deleteMe = 'ate'
    t.remove(deleteMe)
    print("\nAfter delete '%s':\n%s"%(deleteMe, t))
    
    print()
    
    print("ADDED?%s"%t.add('bob',2))
    
    print(t)
