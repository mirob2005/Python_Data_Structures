#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/4/2013

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
        self.next = [None for x in range(0,95)]
        
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
        for child in self.root.next:
            if child!=None:
                self.output += child.key + (" (%s), "%child.value)
                self.traverse(child,'')
        if self.output == '':
            self.output = 'Empty'
        return self.output.rstrip(', ')
        
    def traverse(self,root,prefix):
        prefix += root.key
        for node in root.next:
            if node!=None:
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
                if node !=None:
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
        index = ord(key[0])-32
        if root.next[index] != None:
            root.next[index].value +=1
        else:
            root.next[index] = Node(key[0])
        return self.add(key[1:],root.next[index])
    
    def remove(self, key):
        if not self.isMember(key, self.root):
            return False
        return self.removeHelper(key, self.root,0)
    
    def removeHelper(self,key,root,keyIndex):
        index = ord(key[keyIndex])-32
        if root.next[index] != None:
            #No next neighbors and value is 1
            #Clear the element completely and recurse back and test previous index
            #Already Know it is a member so can do this without checking length
            children = False
            for child in root.next[index].next:
                if child != None:
                    children = True
                    break
            if not children and root.next[index].value == 1:
                root.next[index] = None
                self.removeHelper(key,root,keyIndex-1)
            #Last element in key with a next neighbor and the value is > 1
            #We don't have to worry about value issues since isMember is checked first
            #Decrement the value and recurse back through the previous nodes
            elif keyIndex == len(key)-1 and children and root.next[index].value > 1:
                root.next[index].value -= 1
                return True
            else:
                #Not the last key and there is a next neighbor, recurse further
                self.removeHelper(key,root.next[index],keyIndex+1)
                #This runs after the last element is deleted or decremented
                #It checks earlier nodes to see if they also need deleted and
                #   if not then decrement
                children = False
                for child in root.next[index].next:
                    if child != None:
                        children = True
                        break
                if not children and root.next[index].value == 1:
                    root.next[index] = None
                else:
                    root.next[index].value -=1
                return True
        return False
    
    def isMember(self, key, root=None):
        if not type(key) == str or not key:
            return False
        if not root:
            root = self.root
        index = ord(key[0])-32
        if root.next[index] != None:
            #This 'IF' checks to make sure we don't determine a prefix
            #   that hasn't been individually added to be a member
            #Example if we add 'ate', we say 'at' is not a member unless
            #   we specifically add 'at'
            #This ensures that we can't remove all of the prefixes for a
            #   word such as add 'ate' but then remove 'at' from it leaving
            #   a dangling 'e'
            if len(key) == 1:
                suffixCount = 0
                for child in root.next[index].next:
                    if child!=None:
                        suffixCount += child.value
                #It is a member only if the value for that node is greater than
                #   the sum of it's children
                #Ex: we add 'ate' and 'at'. The value for 'at' is 2, 'ate' is 1, so we
                #   can safely remove only 1 'at'
                if root.next[index].value > suffixCount:
                    return True
                else:
                    return False
            return self.isMember(key[1:],root.next[index])
        return False
    
    def getValue(self,key,root=None):
        if not type(key) == str or not key:
            return None
        if not root:
            root = self.root
        index = ord(key[0])-32
        if root.next[index] != None:
            if len(key) == 1 and root.next[index].value:
                return root.next[index].value
            else:
                return self.getValue(key[1:],root.next[index])
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
    