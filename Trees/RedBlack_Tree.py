#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/29/2013

# Implements a Red-Black Tree
# Similar to a BST except that each node has a color component, which is used
#   to help ensure a balance tree.
# The Red-Black tree must maintain these properties:
#   1) Every node is either red or black.
#   2) The root is black.
#   3) Every leaf (NIL) is black.
#   4) If a node is red, then both of its children is black.
#   5) For each node, all simple paths from the node to descendant leaves must
#       contain the same number of black nodes.

#This implementation does not use include the NIL leaf nodes which saves space.
#   Extra lines of code are required to check for a reference to a NIL node.

# Height is at most 2 log(n+1) > AVL tree height
# Therefore, time complexity:
#       Search - avg/worst case: O(log n)
#       Insert - avg/worst case: O(log n)
#       Delete - avg/worst case: O(log n)

from BST_recursive import BST
from ADTs.Queue_head import Queue
import random

class Node:
    def __init__(self,key,left,right,parent,color):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        #Color, True - Red, False - Black
        self.color = color
    
    def isLeftChild(self):
        if not self.parent:
            return False
        if self.parent.left == self:
            return True
        else:
            return False

    def isRightChild(self):
        if not self.parent:
            return False
        if self.parent.right == self:
            return True
        else:
            return False
        
class RedBlackTree(BST):
    def rotateLeft(self,root):
        #print('Rotating %s left'%root.key)
        child = root.right
        if root.parent:
            parent = root.parent
            if root.isRightChild():
                parent.right = child
            else:
                parent.left = child
            child.parent = parent
        else:
            self.root = child
            child.parent = None
        if child.left:
            root.right = child.left
            child.left.parent = root
        else:
            root.right = None    
        root.parent = child
        child.left = root

    def rotateRight(self,root):
        #print('Rotating %s right'%root.key)
        child = root.left
        if root.parent:
            parent = root.parent
            if root.isRightChild():
                parent.right = child
            else:
                parent.left = child
            child.parent = parent
        else:
            self.root = child
            child.parent = None
        if child.right:
            root.left = child.right
            child.right.parent = root
        else:
            root.left = None    
        root.parent = child
        child.right = root

    def checkColorAfterInsert(self,root):
        #print('Checking color for key %s'%root.key)
        parent = root.parent
        if not parent:
            return
        #While the parent is RED
        if parent.color == True:
            if parent.isLeftChild():
                #print('Parent is left child')
                sibling = parent.parent.right
                if sibling and sibling.color == True:
                    #print('Setting %s Black'%parent.key)
                    parent.color = False
                    #print('Setting %s Black'%sibling.key)
                    sibling.color = False
                    #print('Setting %s Red'%parent.parent.key)
                    parent.parent.color = True
                    self.checkColorAfterInsert(parent.parent)
                else:
                    #print('Rotating')
                    if root.isRightChild():
                        root = root.parent
                        self.rotateLeft(root)
                    #print('Setting %s Black'%parent.key)
                    root.parent.color = False
                    #print('Setting %s RED'%parent.parent.key)
                    root.parent.parent.color = True
                    self.rotateRight(root.parent.parent)
            else:
                #print('Parent is right child')
                sibling = parent.parent.left
                if sibling and sibling.color == True:
                    #print('Setting %s Black'%parent.key)
                    parent.color = False
                    #print('Setting %s Black'%sibling.key)
                    sibling.color = False
                    #print('Setting %s RED'%parent.parent.key)
                    parent.parent.color = True
                    self.checkColorAfterInsert(parent.parent)
                else:
                    #print('Rotating')
                    if root.isLeftChild():
                        root = root.parent
                        self.rotateRight(root)
                    #print('Setting %s Black'%parent.key)
                    root.parent.color = False
                    #print('Setting %s RED'%parent.parent.key)
                    root.parent.parent.color = True
                    self.rotateLeft(root.parent.parent)
        if self.root.color:
            pass
            #print('Setting Root %s BLACK'%self.root.key)
        self.root.color = False
                
    
    def insert(self, key, root=None):
        if(not self.root):
            self.root = Node(key,None,None,None,False)
            return True
        if(not root):
            root = self.root
        if(key == root.key):
            return False
        elif(key > root.key):
            if(not root.right):
                root.right = Node(key,None,None,root,True)
                self.checkColorAfterInsert(root.right)
                return True
            newRoot = root.right
        else:
            if(not root.left):
                root.left = Node(key,None,None,root,True)
                self.checkColorAfterInsert(root.left)
                return True
            newRoot = root.left
        return self.insert(key, newRoot)
    
    def checkColorAfterDelete(self,root):
        #print('Fixing color for key %s'%root.key)
        #print('Node Color: %s'%root.color)
        while root != self.root and root.color == False:
            if root.isLeftChild():
                sibling = root.parent.right
                if sibling and sibling.color == True:
                    #print('Setting %s Black'%sibling.key)
                    sibling.color = False
                    #print('Setting %s Red'%root.parent.key)
                    root.parent.color = True
                    self.rotateLeft(root.parent)
                    sibling = root.parent.right
                if (not sibling.left or sibling.left.color == False) and (not sibling.right or sibling.right.color == False):
                    #print('Setting %s Red'%sibling.key)
                    sibling.color = True
                    root = root.parent
                else:
                    if not sibling.right or sibling.right.color == False:
                        #print('Setting %s Black'%sibling.left.key)
                        sibling.left.color = False
                        #print('Setting %s Red'%sibling.key)
                        sibling.color = True
                        self.rotateRight(sibling)
                        sibling = root.parent.right
                    #print('Setting %s %s'%(sibling.key,'Red' if root.parent.color else "Black"))
                    sibling.color = root.parent.color
                    #print('Setting %s Black'%root.parent.key)
                    root.parent.color = False
                    #print('Setting %s Black'%sibling.right.key)
                    if sibling.right:
                        sibling.right.color = False
                    self.rotateLeft(root.parent)
                    root = self.root
            else:#root.isRightChild()
                sibling = root.parent.left
                if sibling and sibling.color == True:
                    #print('Setting %s Black'%sibling.key)
                    sibling.color = False
                    #print('Setting %s Red'%root.parent.key)
                    root.parent.color = True
                    self.rotateRight(root.parent)
                    sibling = root.parent.left
                if (sibling and (not sibling.left or sibling.left.color == False) and (not sibling.right or sibling.right.color == False)):
                    #print('Setting %s Red'%sibling.key)
                    sibling.color = True
                    root = root.parent
                else:
                    if sibling and (not sibling.left or sibling.left.color == False):
                        #print('Setting %s Black'%sibling.right.key)
                        sibling.right.color = False
                        #print('Setting %s Red'%sibling.key)
                        sibling.color = True
                        self.rotateLeft(sibling)
                        sibling = root.parent.left
                    #print('Setting %s %s'%(sibling.key,'Red' if root.parent.color else "Black"))
                    if sibling:
                        sibling.color = root.parent.color
                        #print('Setting %s Black'%sibling.left.key)
                        if sibling.left:
                            sibling.left.color = False
                    #print('Setting %s Black'%root.parent.key)
                    root.parent.color = False
                    self.rotateRight(root.parent)
                    root = self.root
        if root.color:
            pass
            #print('Setting %s Black'%root.key)
        root.color = False
    
    def delete(self, key, root=None):
        #replace using inorder predecessor
        if(not root):
            if(not self.root):
                return False
            root = self.root
        if(key == root.key):
            #IF root is BLACK, need to fix colors
            fix = True if not root.color else False
            #If leaf node:
            if(not root.left and not root.right):
                if fix:
                    self.checkColorAfterDelete(root)
                #root node
                if(not root.parent):
                    self.root = None
                    return True
                elif(root.parent.right == root):
                    root.parent.right = None
                else:
                    root.parent.left = None
                parent = root.parent
                root = None
                return True
            #If only 1 child (right)
            elif(not root.left and root.right):
                #root node
                if(not root.parent):
                    self.root = root.right
                    self.root.color = False
                elif(root.parent.right == root):
                    root.parent.right = root.right
                else:
                    root.parent.left = root.right
                if fix:
                    self.checkColorAfterDelete(root.right)
                root.right.parent = root.parent
                parent = root.parent
                root = None
                return True
            #If only 1 child (left)
            elif(root.left and not root.right):
                #root node
                if(not root.parent):
                    self.root = root.left
                    self.root.color = False
                elif(root.parent.right == root):
                    root.parent.right = root.left
                else:
                    root.parent.left = root.left
                if fix:
                    self.checkColorAfterDelete(root.left)
                root.left.parent = root.parent
                parent = root.parent
                root = None
                return True
            #If 2 children
            else:
                #Greatest Left Child (inorder predecessor)
                childptr = root.left
                while childptr.right:
                    childptr = childptr.right
                root.key = childptr.key
                fix = True if not childptr.color else False
                #if replacement node has a left child
                if(childptr.left):
                    if fix:
                        self.checkColorAfterDelete(childptr.left)
                    if(childptr.parent.right == childptr):
                        childptr.parent.right = childptr.left
                    else:
                        childptr.parent.left = childptr.left
                    childptr.left.parent = childptr.parent
                else:
                    if fix:
                        self.checkColorAfterDelete(childptr)
                    if(childptr.parent.right == childptr):
                        childptr.parent.right = None
                    else:
                        childptr.parent.left = None
                parent = childptr.parent
                childptr = None
                return True
        elif(key > root.key):
            if(root.right):
                return self.delete(key, root.right)
        else:
            if(root.left):
                return self.delete(key,root.left)
        return False
    
    def traverseBFS(self):
        string = ''
        bfsQ = Queue()
        bfsQ.enQueue(self.root)
        cur = bfsQ.deQueue()
        while cur:
            string += ('\n(%s)\n'%cur.parent.key if cur.parent else '\n(None)\n')
            string += ('<%s>'%str(cur.key))
            string += ('\n(%s,'%cur.left.key if cur.left else '\n(None,')
            string += ('%s)\n____'%cur.right.key if cur.right else 'None)\n____')
            if(cur.left):
                bfsQ.enQueue(cur.left)
            if(cur.right):
                bfsQ.enQueue(cur.right)
            cur = bfsQ.deQueue()
        if string == '':
            string = '(Empty)'
        return string
    
    def copyTree(self):
        copy = RedBlackTree()
        cur = self.root
        if cur:
            copy.root = Node(cur.key, None, None, None,cur.color)
            self.copy(cur, copy.root)
        return copy
    
    def copy(self, cur, copyCur):
        if cur.left:
            copyCur.left = Node(cur.left.key,None,None,copyCur,cur.left.color)
            self.copy(cur.left,copyCur.left)
        if cur.right:
            copyCur.right = Node(cur.right.key,None,None,copyCur,cur.right.color)
            self.copy(cur.right,copyCur.right)
            
    def deleteTree(self):
        cur = self.root
        self.deleteTreeHelper(cur)
    
    def deleteTreeHelper(self,cur):
        if cur.left:
            self.deleteTreeHelper(cur.left)
        if cur.right:
            self.deleteTreeHelper(cur.right)
        #print('Deleting %s'%cur.key)
        if cur.parent:
            if cur.key > cur.parent.key:
                cur.parent.right = None
            else:
                cur.parent.left = None
        else:
            self.root = None
    
    def outputTesting(self):
        string = ''
        bfsQ = Queue()
        bfsQ.enQueue(self.root)
        cur = bfsQ.deQueue()
        while cur:
            string += ('(%s%s)<-'%(cur.parent.key,'R' if cur.parent.color else 'B') if cur.parent else '(NoneB)<-')
            string += str(cur.key)
            string += ('%s'%'R' if cur.color else 'B')
            string += ('->(%s%s,'%(cur.left.key,'R' if cur.left.color else 'B') if cur.left else '->(NoneB,')
            string += ('%s%s)\n'%(cur.right.key,'R' if cur.right.color else 'B') if cur.right else 'NoneB)\n')
            if(cur.left):
                bfsQ.enQueue(cur.left)
            if(cur.right):
                bfsQ.enQueue(cur.right)
            cur = bfsQ.deQueue()
        if string == '':
            string = '(Empty)'
        return string

    
if __name__ == '__main__':
    rb = RedBlackTree()
    
    #listToInsert = [48, 59, 26, 99, 1, 24, 41, 87, 95, 88, 57, 58, 71, 39, 73, \
    #              62, 27, 79, 60, 68,7, 66, 65, 84, 93, 54, 49, 21, 98, 29, 11, 40, \
    #              31, 16, 38, 37, 76, 83, 77, 12, 80, 6, 85, 3, 22, 17, 97, 69, 5, \
    #              75, 47, 9, 15, 82, 53, 94, 89, 14, 30, 19, 63, 0, 20, 64, 43, 96, \
    #              46, 86, 52, 34, 42, 44, 36, 51, 72, 74, 67, 25, 70, 4, 78, 18,92, \
    #              23, 90, 2, 10, 13, 45, 56, 28, 100, 50, 91, 35, 33, 81, 61, 32, 8, 55]
    
    listToInsert = [3,2,97,95,98,99]
    for value in listToInsert:
        print('Inserting %s'%value)
        rb.insert(value)
    
    result = True
    for value in listToInsert:
        result = result and rb.find(value)
    print()
    print(result)
    print()
    
    print(rb.outputTesting())
    
    rb.delete(3)
    print(rb.outputTesting())
    #while True:
    #    try:
    #        reply = input('Enter Key to Insert:')
    #    except EOFError:
    #        break
    #    else:
    #        num = int(reply)
    #        print(rb.insert(num))
    #        print(rb.outputTesting())