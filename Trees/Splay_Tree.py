#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/13/2013

# Implements a Splay Tree that uses a queue for BFS traversal,
#   and recursion for DFS traversals. Alternates between replacing a deleted
#   node with the inorder predecessor and inorder successor to help
#   balancing.  Inherits BFS, insertList, __str__, print methods, and Node
#   class from iterative BST approach since recursion is not needed for these.

from BST_iterative import BST as BST_iter
from BST_iterative import Node
        
class SplayTree(BST_iter):
    def splay(self, node):
        if node == self.root:
            print("node is root")
            return
        elif node.parent == self.root:
            print('ZIG for %s'%node.key)
            if node.key < self.root.key:
                print('<')
                self.root.left = node.right
                node.right = self.root
            else:#node.key > self.root.key
                print('>')
                self.root.right = node.left
                node.left = self.root
            self.root = node
            node.parent = None
            if self.root.left:
                self.root.left.parent = self.root
            if self.root.right:
                self.root.right.parent = self.root
            print('ROOT = %s'%self.root.key)
            print('PARENT = %s'%self.root.parent.key if self.root.parent else None)
            print('LEFT = %s'%self.root.left.key if self.root.left else None)
            print('RIGHT = %s'%self.root.right.key if self.root.right else None)
            print()
            if self.root.left:
                print("LEFT PARENT = %s"%self.root.left.parent.key if self.root.left.parent else None)
                print("LEFT LEFT = %s"%self.root.left.left.key if self.root.left.left else None)
                print("LEFT Right = %s"%self.root.left.right.key if self.root.left.right else None)
            if self.root.right:
                print("RIGHT PARENT = %s"%self.root.right.parent.key if self.root.right.parent else None)
                print("RIGHT LEFT = %s"%self.root.right.left.key if self.root.right.left else None)
                print("RIGHT Right = %s"%self.root.right.right.key if self.root.right.right else None)
            print('____________________')
        else:
            #Parent is not the root
            #Zig-Zig Operation
            #print("Parent = %s"% node.parent.key)
            #print("Parent's Parent = %s"% node.parent.parent.key if node.parent.parent else None)
            if (node.key < node.parent.key and node.parent.key < node.parent.parent.key) or \
                (node.key > node.parent.key and node.parent.key > node.parent.parent.key):
                print('ZIGZIG for %s'%node.key)
                self.splay(node.parent)
                self.splay(node)
            #Zig-Zag Operation
            else:
                print('ZIGZAG for %s'%node.key)
                parent = node.parent
                gparent = node.parent.parent
                print("Parent = %s"% parent.key)
                print("Parent's Parent = %s"% gparent.key if gparent else None)
                if parent.key < gparent.key:
                    print('parent < gparent')
                    gparent.left = node
                    parent.right = node.left
                    node.parent = gparent
                    node.left = parent
                    parent.parent = node
                    print('Gparent = %s'%gparent.key)
                    print('GparentL = %s'%gparent.left.key)
                    
                else:
                    print('parent > gparent')
                    gparent.right = node
                    parent.left = node.right
                    node.parent = gparent
                    node.right = parent
                    parent.parent = node
                    #print('Root is %s'%self.root.key)
                    print('Gparent = %s'%gparent.key)
                    print('GparentR = %s'%gparent.right.key)
                    print('GparentL = %s'%gparent.left.key if gparent.left else None)
                    print()
                    print('GparentRP = %s'%gparent.right.parent.key)
                    print('GparentRR = %s'%gparent.right.right.key)
                    print('GparentRL = %s'%gparent.right.left.key if gparent.right.left else None)
                    
                    print('GparentRRP = %s'%gparent.right.right.parent.key if gparent.right.right.parent else None)
                    print('GparentRRL = %s'%gparent.right.right.left.key if gparent.right.right.left else None)
                    print('GparentRRR = %s'%gparent.right.right.right.key if gparent.right.right.right else None)
                self.splay(node)
            print('____________________')
                
    def insert(self, key, root=None):
        if(not self.root):
            self.root = Node(key,None,None,None)
            return True
        if(not root):
            root = self.root
        if(key == root.key):
            self.splay(root)
            return False
        elif(key > root.key):
            if(not root.right):
                root.right = Node(key,None,None,root)
                self.splay(root.right)
                return True
            newRoot = root.right
        else:
            if(not root.left):
                root.left = Node(key,None,None,root)
                self.splay(root.left)
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
    
    def findRecentAccessed(self):
        return self.root.key
    
if __name__ == '__main__':
    st = SplayTree()
    
    for value in [10,15,5,6,9,7,12]:
        st.insert(value)
        
    print('--------------------')
    print(st)
    #print(st.findRecentAccessed())