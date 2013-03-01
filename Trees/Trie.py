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

    def __str__(self):
        string = "BFS: %s"%str(self.traverseBFS())
        string += "\nWords: %s"%str(self.traverseWords())
        string += "\nDFSpreorder: %s"%str(self.traverseDFSpreorder())
        return string
    
    def __contains__(self, key):
        pass
    
    def traverseWords(self):
        string = ''
        if not self.root.next:
            string = 'Empty'
        for node in self.root.next:
            for child in node.next:
                string += str(node.key)
                string += self.traverseKey(child)
                string += ' '
        string = string.strip(' ')
        return string

    def traverseKey(self,root):
        string = str(root.key)
        if root.next:
            for node in root.next:
                string += self.traverseKey(node)
        return string
    
    def traverseDFSpreorder(self, root = True):
        if(root == True):
            root = self.root
        #root, left subtree, right subtree
        if(not root):
            return []
        if root == self.root:
            return [self.traverseDFSpreorder(node) for node in root.next]
        else:
            return [root.key, root.value] + [self.traverseDFSpreorder(node) for node in root.next]
            
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
        return self.removeHelper(key, self.root)
    
    def removeHelper(self,key,root):
        for node in root.next:
            if key[0] in node.key:
                if len(key) ==1 or len(node.next) == 1:
                    del root.next[root.next.index(node)]
                    return True
                else:
                    return self.removeHelper(key[1:],node)
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
    t.add('add',3)
    t.add('apple',4)
    t.add('at',5)
    t.add('ate',6)
    
    print(t)
    #print(t.traverseWords())
    