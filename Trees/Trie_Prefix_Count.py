#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/3/2013

#Trie is built using a Tree-like structure
#Each node contains a single character and number of times prefix added
#Each word can be created by going from the root down any branch to a
#   terminating node or a node where the value of the parent node is greater
#   than the sum of the values of the children nodes
#The traversePrefixes method goes through each branch and strings together
#   all prefixes

from ADTs.Queue_head import Queue
from ADTs.Stack import Stack

class Node:
    def __init__(self,key):
        self.key = key
        self.value = 1
        self.next = []
        
class Trie:
    def __init__(self):
        self.root = Node(None)
        self.output = ''

    def __str__(self):
        string = "BFS: %s"%str(self.traverseBFS())
        string += "\nPrefixes: %s"%str(self.traversePrefixes())
        return string

    def traversePrefixes(self):
        self.output = ''
        if not self.root.next:
            self.output = 'Empty'
        for child in self.root.next:
            self.output += child.key + (" (%s), "%child.value)
            self.traverse(child,'')
        return self.output.rstrip(', ')
        
    def traverse(self,root,prefix):
        prefix += root.key
        for node in root.next:
            self.output += prefix + node.key + (" (%s), "%node.value)
            if node.next and node.value:            
                self.traverse(node,prefix)

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
    
    #IF key already exists, it just updates the counts
    def add(self, key, root=None):
        if not type(key) == str:
            return False
        if not key:
            return True
        if not root:
            root = self.root
        for node in root.next:
            if key[0] in node.key:
                node.value +=1
                return self.add(key[1:],root.next[root.next.index(node)])
        root.next.append(Node(key[0]))
        return self.add(key[1:],root.next[-1])
    
    def remove(self, key):
        if not self.isMember(key, self.root):
            return False
        return self.removeHelper(key, self.root,0)
    
    def removeHelper(self,key,root,index):
        for node in root.next:
            if key[index] in node.key:
                #No next neighbors and value is 1
                #Delete the element completely and recurse back and test previous index
                #Already Know it is a member so can do this without checking length
                if not node.next and node.value == 1:
                    del root.next[root.next.index(node)]
                    self.removeHelper(key,root,index-1)
                #Last element in key with a next neighbor and the value is > 1
                #We don't have to worry about value issues since isMember is checked first
                #Decrement the value and recurse back through the previous nodes
                elif index == len(key)-1 and node.next and node.value > 1:
                    node.value -= 1
                    return True
                else:
                    #Not the last key and there is a next neighbor, recurse further
                    self.removeHelper(key,node,index+1)
                    #This runs after the last element is deleted or decremented
                    #It checks earlier nodes to see if they also need deleted and
                    #   if not then decrement
                    if not node.next and node.value == 1:
                        del root.next[root.next.index(node)]
                    else:
                        node.value -=1
                    return True
        return False
    
    def isMember(self, key, root=None):
        if not type(key) == str or not key:
            return False
        if not root:
            root = self.root
        for node in root.next:
            if key[0] in node.key:
                if len(key) == 1 and not node.next:
                    return True
                else:
                    #This 'IF' checks to make sure we don't determine a prefix
                    #   that hasn't been individually added to be a member
                    #Example if we add 'ate', we say 'at' is not a member unless
                    #   we specifically add 'at'
                    #This ensures that we can't remove all of the prefixes for a
                    #   word such as add 'ate' but then remove 'at' from it leaving
                    #   a dangling 'e'
                    if len(key) == 1:
                        suffixCount = 0
                        for child in node.next:
                            suffixCount += child.value
                        #It is a member only if the value for that node is greater than
                        #   the sum of it's children
                        #Ex: we add 'ate' and 'at'. The value for 'at' is 2, 'ate' is 1, so we
                        #   can safely remove only 1 'at'
                        if node.value > suffixCount:
                            return True
                        else:
                            return False
                    return self.isMember(key[1:],root.next[root.next.index(node)])
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
    
    t.add('bob')
    
    t.add('bad')
    t.add('bad')
    t.add('ba')
    t.add('bat')

    
    print(t)
    deleteMe = 'ba'
    if(t.remove(deleteMe)):
        print("\nAfter delete '%s':\n%s"%(deleteMe, t))
    
    deleteMe = 'ba'
    if(t.remove(deleteMe)):
        print("\nAfter delete '%s':\n%s"%(deleteMe, t))
    else:
        print("\nDelete '%s' Failed:\n%s"%(deleteMe, t))
    
    deleteMe = 'ba'
    if(t.remove(deleteMe)):
        print("\nAfter delete '%s':\n%s"%(deleteMe, t))
    else:
        print("\nDelete '%s' Failed:\n%s"%(deleteMe, t))
    