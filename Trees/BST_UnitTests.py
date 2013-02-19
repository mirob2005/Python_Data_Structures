from BST_iterative import BST as BST_iter
import unittest

class TestBST(unittest.TestCase):
    
    def setUp(self):
        self.perfect = BST_iter()
        for key in [7,3,1,5,0,6,2,4,11,9,8,10,13,12,14]:
            self.perfect.insert(key)
            
        self.degenerate = BST_iter()
        for key in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
            self.degenerate.insert(key)
            
        self.balanced = BST_iter()
        for key in [7,5,3,1,2,0,4,6,12,10,9,11,13,14,8]:
            self.balanced.insert(key)
        
        self.rightHeavy = BST_iter()
        for key in [5,3,10,1,4,0,2,7,6,9,8,13,11,14,12]:
            self.rightHeavy.insert(key)
        
        self.leftHeavy = BST_iter()
        for key in [11,13,12,14,6,3,8,9,7,4,1,5,2,0,10]:
            self.leftHeavy.insert(key)
            
        self.treeList = [self.perfect, self.degenerate, self.balanced, self.rightHeavy, self.leftHeavy]
        
    def testEmpty(self):
        tree = BST_iter()
        expResult = str([])
        self.assertEqual(expResult, tree.printBFS())
        self.assertEqual(expResult, tree.printDFSinorder())
        self.assertEqual(expResult, tree.printDFSpostorder())
        self.assertEqual(expResult, tree.printDFSpreorder())
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        tree = BST_iter()
        boolResult = tree.insert(7)
        expResult = str([7])
        self.assertTrue(boolResult)
        self.assertEqual(expResult, tree.printBFS())
        self.assertEqual(expResult, tree.printDFSinorder())
        self.assertEqual(expResult, tree.printDFSpostorder())
        self.assertEqual(expResult, tree.printDFSpreorder())
        print("\ntestInsert PASSED")
        
    def testBFS(self):
        expResult = str([7,3,11,1,5,9,13,0,2,4,6,8,10,12,14])
        self.assertEqual(expResult, self.perfect.printBFS())
        
        expResult = str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.assertEqual(expResult, self.degenerate.printBFS())
        
        expResult = str([7,5,12,3,6,10,13,1,4,9,11,14,0,2,8])
        self.assertEqual(expResult, self.balanced.printBFS())
        
        expResult = str([5,3,10,1,4,7,13,0,2,6,9,11,14,8,12])
        self.assertEqual(expResult, self.rightHeavy.printBFS())
        
        expResult = str([11,6,13,3,8,12,14,1,4,7,9,0,2,5,10])
        self.assertEqual(expResult, self.leftHeavy.printBFS())
        print("testBFS PASSED")
        
    def testDFSinorder(self):
        expResult = str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.assertEqual(expResult, self.perfect.printDFSinorder())
        self.assertEqual(expResult, self.degenerate.printDFSinorder())
        self.assertEqual(expResult, self.balanced.printDFSinorder())
        self.assertEqual(expResult, self.rightHeavy.printDFSinorder())
        self.assertEqual(expResult, self.leftHeavy.printDFSinorder())
        print("\ntestDFSinorder PASSED")
        
    def testDFSpreorder(self):
        expResult = str([7,3,1,0,2,5,4,6,11,9,8,10,13,12,14])
        self.assertEqual(expResult, self.perfect.printDFSpreorder())
        expResult = str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.assertEqual(expResult, self.degenerate.printDFSpreorder())
        expResult = str([7,5,3,1,0,2,4,6,12,10,9,8,11,13,14])
        self.assertEqual(expResult, self.balanced.printDFSpreorder())
        expResult = str([5,3,1,0,2,4,10,7,6,9,8,13,11,12,14])
        self.assertEqual(expResult, self.rightHeavy.printDFSpreorder())
        expResult = str([11,6,3,1,0,2,4,5,8,7,9,10,13,12,14])
        self.assertEqual(expResult, self.leftHeavy.printDFSpreorder())
        print("\ntestDFSpreorder PASSED")
        
    def testDFSpostorder(self):
        expResult = str([0,2,1,4,6,5,3,8,10,9,12,14,13,11,7])
        self.assertEqual(expResult, self.perfect.printDFSpostorder())
        expResult = str([14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])
        self.assertEqual(expResult, self.degenerate.printDFSpostorder())
        expResult = str([0,2,1,4,3,6,5,8,9,11,10,14,13,12,7])
        self.assertEqual(expResult, self.balanced.printDFSpostorder())
        expResult = str([0,2,1,4,3,6,8,9,7,12,11,14,13,10,5])
        self.assertEqual(expResult, self.rightHeavy.printDFSpostorder())
        expResult = str([0,2,1,5,4,3,7,10,9,8,6,12,14,13,11])
        self.assertEqual(expResult, self.leftHeavy.printDFSpostorder())
        print("\ntestDFSpostorder PASSED")
        
    def testFind(self):
        for tree in self.treeList:
            self.assertTrue(tree.find(0))
            self.assertFalse(tree.find(15))
            self.assertFalse(tree.find(-1))
            self.assertTrue(tree.find(14))
        print("\ntestFind PASSED")
        
    def testDuplicateInsert(self):
        boolResult = self.perfect.insert(1)
        self.assertFalse(boolResult)
        boolResult = self.balanced.insert(1)
        self.assertFalse(boolResult)
        boolResult = self.degenerate.insert(1)
        self.assertFalse(boolResult)
        boolResult = self.rightHeavy.insert(1)
        self.assertFalse(boolResult)
        boolResult = self.leftHeavy.insert(1)
        self.assertFalse(boolResult)
        print("\ntestDuplicateInsert PASSED")
        
    def testCopy(self):
        balancedCopy = self.balanced.copyTree()
        balancedCopy.insert(15)
        degenerateCopy = self.degenerate.copyTree()
        degenerateCopy.insert(15)
        perfectCopy = self.perfect.copyTree()
        perfectCopy.insert(15)
        rightHeavyCopy = self.rightHeavy.copyTree()
        rightHeavyCopy.insert(15)
        leftHeavyCopy = self.leftHeavy.copyTree()
        leftHeavyCopy.insert(15)
        
        #Test to make sure previous trees were not changed
        expResult = str([7,3,11,1,5,9,13,0,2,4,6,8,10,12,14])
        self.assertEqual(expResult, self.perfect.printBFS())
        
        expResult = str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
        self.assertEqual(expResult, self.degenerate.printBFS())
        
        expResult = str([7,5,12,3,6,10,13,1,4,9,11,14,0,2,8])
        self.assertEqual(expResult, self.balanced.printBFS())
        
        expResult = str([5,3,10,1,4,7,13,0,2,6,9,11,14,8,12])
        self.assertEqual(expResult, self.rightHeavy.printBFS())
        
        expResult = str([11,6,13,3,8,12,14,1,4,7,9,0,2,5,10])
        self.assertEqual(expResult, self.leftHeavy.printBFS())
        
        #Tests to see that the new trees were changed
        expResult = str([7,3,11,1,5,9,13,0,2,4,6,8,10,12,14,15])
        self.assertEqual(expResult, perfectCopy.printBFS())
        
        expResult = str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        self.assertEqual(expResult, degenerateCopy.printBFS())
        
        expResult = str([7,5,12,3,6,10,13,1,4,9,11,14,0,2,8,15])
        self.assertEqual(expResult, balancedCopy.printBFS())
        
        expResult = str([5,3,10,1,4,7,13,0,2,6,9,11,14,8,12,15])
        self.assertEqual(expResult, rightHeavyCopy.printBFS())
        
        expResult = str([11,6,13,3,8,12,14,1,4,7,9,15,0,2,5,10])
        self.assertEqual(expResult, leftHeavyCopy.printBFS())
        
        print("\ntestCopy PASSED")
        
    def testFindMin(self):
        expResult = 0
        for tree in self.treeList:
            self.assertEqual(expResult,tree.findMin())
        print("\ntestFindMin PASSED")
        
    def testDelete(self):
        pass
    
if __name__ == '__main__':
    unittest.main()