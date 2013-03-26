#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/25/2013

# Implements a AVL tree.
# Uses a balance factor to determine if a tree rotation is necessary.
# The Balance Factor is calculated as follows:
#   height(left-subtree) - height(right-subtree)
# If BF = -1,0,1: Balanced
# If BF <-1 OR >1: Rotation Necessary

#Rotation Rules:
#   BF = -2 for P, P's right subtree is heavy
#       IF BF of R(right-child) = -1 or 0 then single left rotation P root (R-R case)
#       IF BF of R(right-child) = +1 then 2 rotations needed:
#           right rotation R root then left rotation P root (R-L case)

#   BF = +2 for P, P's left subtree is heavy
#       IF BF of L(left-child) = +1 or 0 then single right rotation P root (L-L case)
#       IF BF of L(left-child) = -1 then 2 rotations needed:
#           left rotation L root then right rotation P root (L-R case)

#After A Rotate LEFT recalculate the BF as follows:
#   root.BF = root.BF + 1 - min(child.BF,0)
#   child.BF = child.BF + 1 + max(root.BF,0)

#After A Rotate RIGHT recalculate the BF as follows:
#   root.BF = root.BF - 1 - max(child.BF,0)
#   child.BF = child.BF - 1 + min(root.BF,0)

from BST_recursive import BST
from ADTs.Queue_head import Queue
import random

class Node:
    def __init__(self,key,left,right,parent, BF=0):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        #Balance Factor
        self.BF = BF
        
class AVLTree(BST):
    def rotateLeft(self,root):
        #print('Rotating %s left'%root.key)
        child = root.right
        if root.parent:
            parent = root.parent
            if root.key > root.parent.key:
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
        
        #UpdateBF
        root.BF = root.BF + 1 - min(child.BF,0)
        child.BF = child.BF + 1 + max(root.BF,0)

    def rotateRight(self,root):
        #print('Rotating %s right'%root.key)
        child = root.left
        if root.parent:
            parent = root.parent
            if root.key > root.parent.key:
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
        
        #UpdateBF
        root.BF = root.BF - 1 - max(child.BF,0)
        child.BF = child.BF - 1 + min(root.BF,0)

    def calcBFAfterInsert(self,root):
        if not root or not root.parent:
            return
        parent = root.parent
        #print('Calc for %s'%parent.key)
        if not root.right and not root.left:
            root.BF = 0
        if root.key < parent.key:
            parent.BF += 1
        else:
            parent.BF -= 1
        #BUG FIX
        if (not root.right and root.BF < 0) or\
        (not root.left and root.BF > 0):
            root.BF = -root.BF
        self.checkBalance(parent)
        if parent.BF == 1 or parent.BF == -1:
            self.calcBFAfterInsert(parent)
            
    def calcBFAfterDelete(self,root,sign):
        #print('Root key %s, sign %s'%(root.key,sign))
        if not root:
            return
        #print('Calc for %s'%root.key)
        rotation = False
        if not root.left and not root.right:
            root.BF = 0
        else:
            if sign == -1:
                root.BF -= 1
            elif sign == 1:
                root.BF += 1
            rotation = self.checkBalance(root)
        #BUG FIX
        if (not root.right and root.BF < 0) or\
        (not root.left and root.BF > 0):
            root.BF = -root.BF
        if rotation and root.parent:
            #The rotation recalculates the BF, can skip to the parent
            root = root.parent
        if root.parent:
            #If root.BF == 0, it means that the BF was +-1,
            #This makes this subtree shorter thus we need to propagate upwards
            if root.BF == 0:
                if root.key < root.parent.key:
                    sign = -1
                else:
                    sign = 1
                self.calcBFAfterDelete(root.parent,sign)
            
    def checkBalance(self,root):
        if not root.left and not root.right:
            root.BF = 0
            return False
        if root.BF >1:
            if root.left.BF >= 0:
                #print('Single Right Rotation Needed')
                self.rotateRight(root)
            else:
                #print('2 rotations needed L-R')
                pivot = root.left
                self.rotateLeft(pivot)
                self.rotateRight(root)
            return True
        elif root.BF < -1:
            if root.right.BF <=0:
                #print('Single Left Rotation Needed')
                self.rotateLeft(root)
            else:
                #print('2 rotations needed R-L')
                pivot = root.right
                self.rotateRight(pivot)
                self.rotateLeft(root)
            return True
        else:
            return False
    
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
                self.calcBFAfterInsert(root.right)
                return True
            newRoot = root.right
        else:
            if(not root.left):
                root.left = Node(key,None,None,root)
                self.calcBFAfterInsert(root.left)
                return True
            newRoot = root.left
        return self.insert(key, newRoot)
    
    def delete(self, key, root=None):
        #replace using inorder predecessor
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
                    #Sign is used to determine BF
                    sign = 0
                elif(root.parent.right == root):
                    sign = 1
                    root.parent.right = None
                else:
                    sign = -1
                    root.parent.left = None
                parent = root.parent
                root = None
                self.calcBFAfterDelete(parent,sign)
                return True
            #If only 1 child (right)
            elif(not root.left and root.right):
                #root node
                if(not root.parent):
                    self.root = root.right
                    sign = 0
                elif(root.parent.right == root):
                    sign = 1
                    root.parent.right = root.right
                else:
                    sign = -1
                    root.parent.left = root.right
                root.right.parent = root.parent
                parent = root.parent
                root = None
                self.calcBFAfterDelete(parent,sign)
                return True
            #If only 1 child (left)
            elif(root.left and not root.right):
                #root node
                if(not root.parent):
                    sign = 0
                    self.root = root.left
                if(root.parent.right == root):
                    sign = 1
                    root.parent.right = root.left
                else:
                    sign = -1
                    root.parent.left = root.left
                root.left.parent = root.parent
                parent = root.parent
                root = None
                self.calcBFAfterDelete(parent,sign)
                return True
            #If 2 children
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
                        #Used for calculating BF
                        sign = 1
                    else:
                        childptr.parent.left = childptr.left
                        sign = -1
                    childptr.left.parent = childptr.parent
                else:
                    if(childptr.parent.right == childptr):
                        childptr.parent.right = None
                        sign = 1
                    else:
                        childptr.parent.left = None
                        sign = -1
                parent = childptr.parent
                childptr = None
                self.calcBFAfterDelete(parent,sign)
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
            string += ('(BF: %s)'%(cur.BF))
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
        copy = AVLTree()
        cur = self.root
        if cur:
            copy.root = Node(cur.key, None, None, None,cur.BF)
            self.copy(cur, copy.root)
        return copy
    
    def copy(self, cur, copyCur):
        if cur.left:
            copyCur.left = Node(cur.left.key,None,None,copyCur,cur.left.BF)
            self.copy(cur.left,copyCur.left)
        if cur.right:
            copyCur.right = Node(cur.right.key,None,None,copyCur,cur.right.BF)
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
            string += ('(%s)<-'%cur.parent.key if cur.parent else '(None)<-')
            string += str(cur.key)
            string += ('(BF:%s)'%(cur.BF))
            string += ('->(%s,'%cur.left.key if cur.left else '->(None,')
            string += ('%s)\n'%cur.right.key if cur.right else 'None)\n')
            if(cur.left):
                bfsQ.enQueue(cur.left)
            if(cur.right):
                bfsQ.enQueue(cur.right)
            cur = bfsQ.deQueue()
        if string == '':
            string = '(Empty)'
        return string

    
if __name__ == '__main__':
    avl = AVLTree()
    
    listToSort = [48, 59, 26, 99, 1, 24, 41, 87, 95, 88, 57, 58, 71, 39, 73, \
                  62, 27, 79, 60, 68,7, 66, 65, 84, 93, 54, 49, 21, 98, 29, 11, 40, \
                  31, 16, 38, 37, 76, 83, 77, 12, 80, 6, 85, 3, 22, 17, 97, 69, 5, \
                  75, 47, 9, 15, 82, 53, 94, 89, 14, 30, 19, 63, 0, 20, 64, 43, 96, \
                  46, 86, 52, 34, 42, 44, 36, 51, 72, 74, 67, 25, 70, 4, 78, 18,92, \
                  23, 90, 2, 10, 13, 45, 56, 28, 100, 50, 91, 35, 33, 81, 61, 32, 8, 55]
    for value in listToSort:
        #print('Inserting %s'%value)
        avl.insert(value)

    result = True
    for value in listToSort:
        result = result and avl.find(value)
    print()
    print(result)
    print()
    
    print(avl.outputTesting())