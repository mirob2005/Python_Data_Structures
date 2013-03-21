#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/--/2013

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


from BST_recursive import BST
from ADTs.Queue_head import Queue

class Node:
    def __init__(self,key,left,right,parent):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        #Balance Factor
        self.BF = 0
        self.height = 1
        
class AVLTree(BST):
    def rotateLeft(self,root):
        if root.key > root.parent.key:
            right = True
            left = False
        else:
            right = False
            left = True
        parent = root.parent
        root.parent = root.right
        root.right.left = root
        root.right.parent = parent
        if(right):
            parent.right = root.right
        else:
            parent.left = root.right
        root.right = None
        root.height -= 2
        root.BF = 0

    def rotateRight(self,root):
        pass

    def calcBF(self,root):
        #print('Calc for %s'%root.key)
        if root.right and root.left:
            root.height = max(root.right.height, root.left.height) + 1
            root.BF = root.left.height - root.right.height
        elif root.right and not root.left:
            root.height = root.right.height + 1
            root.BF = -root.right.height
        elif not root.right and root.left:
            root.height = root.left.height + 1
            root.BF = root.left.height
        if root.BF > 1:
            #print('%s is Left Heavy'%root.key)
            if root.left.BF >= 0:
                print('Single Right Rotation Needed')
            else:
                print('2 rotations needed L-R')
        elif root.BF < -1:
            print('%s is Right Heavy'%root.key)
            if root.right.BF <= 0:
                print('Single Left Rotation Needed')
                self.rotateLeft(root)
            else:
                print('2 rotations needed R-L')
        if root.parent:
            self.calcBF(root.parent)
    
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
                self.calcBF(root.right)
                return True
            newRoot = root.right
        else:
            if(not root.left):
                root.left = Node(key,None,None,root)
                self.calcBF(root.left)
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
            string += ('(Height: %s, BF: %s)'%(cur.height, cur.BF))
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
        copy = SplayTree()
        cur = self.root
        if cur:
            copy.root = Node(cur.key, None, None, None)
            self.copy(cur, copy.root)
        return copy
    
    def copy(self, cur, copyCur):
        if cur.left:
            copyCur.left = Node(cur.left.key,None,None,copyCur)
            self.copy(cur.left,copyCur.left)
        if cur.right:
            copyCur.right = Node(cur.right.key,None,None,copyCur)
            self.copy(cur.right,copyCur.right)
            
if __name__ == '__main__':
    avl = AVLTree()
    
    for value in [10,15,5,16,17]:
        #print('\nInserting %d'%value)
        avl.insert(value)
        
    print(avl)