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
    
    def delete(self, key, root=None):
        #alternate between using inorder predecessor and successor
        if(not root):
            if(not self.root):
                return False
            root = self.root
        if(key == root.key):
            #If leaf node:
            if(not root.left and not root.right):
                #root node
                if(not root.parent):
                    self.root = None
                elif(root.parent.right == root):
                    root.parent.right = None
                else:
                    root.parent.left = None
                root = None
                return True
            #If only 1 child (right)
            elif(not root.left and root.right):
                #root node
                if(not root.parent):
                    self.root = root.right
                elif(root.parent.right == root):
                    root.parent.right = root.right
                else:
                    root.parent.left = root.right
                root.right.parent = root.parent
                root = None
                return True
            #If only 1 child (left)
            elif(root.left and not root.right):
                #root node
                if(not root.parent):
                    self.root = root.left
                if(root.parent.right == root):
                    root.parent.right = root.left
                else:
                    root.parent.left = root.left
                root.left.parent = root.parent
                root = None                    
                return True
            #If 2 children
            else:
                if(self.replaceWithSuccessor):
                    #Greatest Right Child (inorder successor)
                    childptr = root.right
                    while childptr.left:
                        childptr = childptr.left
                    root.key = childptr.key
                    #if replacement node has a right child
                    if(childptr.right):
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = childptr.right
                        else:
                            childptr.parent.left = childptr.right
                        childptr.right.parent = childptr.parent
                    else:
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = None
                        else:
                            childptr.parent.left = None
                    childptr = None
                else:
                    #Greatest Left Child (inorder predecessor)
                    childptr = root.left
                    while childptr.right:
                        childptr = childptr.right
                    root.key = childptr.key
                    #if replacement node has a left child
                    if(childptr.left):
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = childptr.left
                        else:
                            childptr.parent.left = childptr.left
                        childptr.left.parent = childptr.parent
                    else:
                        if(childptr.parent.right == childptr):
                            childptr.parent.right = None
                        else:
                            childptr.parent.left = None
                    childptr = None
                self.replaceWithSuccessor = not self.replaceWithSuccessor
                return True
        elif(key > root.key):
            if(root.right):
                return self.delete(key, root.right)
        else:
            if(root.left):
                return self.delete(key,root.left)
        return False
    
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