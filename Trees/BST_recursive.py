from BST_iterative import BST as BST_iter
from BST_iterative import Node
#Inherit BFS, insertList, __str__, print methods,
#and Node class from iterative approach
        
class BST(BST_iter):
    def insert(self, key, root=None):
        if(not self.root):
            self.root = Node(key,None,None,None)
            return True
        if(not root):
            root = self.root
        if(key == root.key):
            return False
        elif(key > root.key):
            if(not root.right):
                root.right = Node(key,None,None,root)
                return True
            newRoot = root.right
        else:
            if(not root.left):
                root.left = Node(key,None,None,root)
                return True
            newRoot = root.left
        return self.insert(key, newRoot)
    
    def find(self, key, root=None):
        if(not root):
            if(not self.root):
                return False
            root = self.root
        if(key == root.key):
            return True
        elif(key > root.key):
            if(not root.right):
                return False
            return self.find(key,root.right)
        else:
            if(not root.left):
                return False
            return self.find(key,root.left)
    
    def delete(self, key):
        #alternate between using inorder predecessor and successor
        pass
    
    def traverseDFSpreorder(self, root = True):
        # Enables inheritance from BST_iterative (assumes root if none provided)
        if(root == True):
            root = self.root
        #root, left subtree, right subtree
        if(not root):
            return []
        return [root.key] + self.traverseDFSpreorder(root.left) + self.traverseDFSpreorder(root.right)
    
    def traverseDFSinorder(self, root = True):
        # Enables inheritance from BST_iterative (assumes root if none provided)
        if(root == True):
            root = self.root
        #left, root, right subtree
        if(not root):
            return []
        return self.traverseDFSinorder(root.left) + [root.key] + self.traverseDFSinorder(root.right)
    
    def traverseDFSpostorder(self, root = True):
        # Enables inheritance from BST_iterative (assumes root if none provided)
        if(root == True):
            root = self.root
        #left, right, root
        if(not root):
            return []
        return self.traverseDFSpostorder(root.left) + self.traverseDFSpostorder(root.right) + [root.key]
    
    def copyTree(self):
        copy = BST()
        copy.insertList(self.traverseDFSpreorder(self.root))
        return copy
    
    def findMin(self, root=None):
        if(not root):
            if(not self.root):
                return None
            root = self.root
        if(root.left):
            return self.findMin(root.left)
        return root.key
    
    def findMax(self, root=None):
        if(not root):
            if(not self.root):
                return None
            root = self.root
        if(root.right):
            return self.findMax(root.right)
        return root.key