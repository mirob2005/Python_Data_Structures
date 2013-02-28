from ADTs.Queue_head import Queue

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = []
        
class Trie:
    def __init__(self):
        self.root = Node(None,None)

    def __str__(self):
        string = str(self.traverseBFS())
        string += "\n"
        string +=str(self.traverseDFSpreorder(self.root))
        return string
    
    def __contains__(self, key):
        pass
    
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
            keys.append([cur.key,cur.value])
            for node in cur.next:
                bfsQ.enQueue(node)
            cur = bfsQ.deQueue()
        return keys
    
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
        pass
    
    def isMember(self, key):
        pass
    
    def updateValue(self,key):
        pass
    
    def getValue(self,key):
        pass
    
if __name__ == '__main__':
    
    t = Trie()
    
    t.add('bob',1)
    t.add('bad',2)
    t.add('add',3)
    t.add('apple',4)
    t.add('at',5)
    
    print(t)
    
    #a = Node('b',None)
    #b = Node('o',None)
    #c = Node('b',1)
    #
    #a.next.append(b)
    #b.next.append(c)
    #
    #for node in a.next:
    #    if 'o' in node.key:
    #        print(True)
    #    else:
    #        print(False)
    
    
    