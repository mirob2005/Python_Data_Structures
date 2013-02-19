from BST import BST
import unittest

class TestBST(unittest.TestCase):
    
    def setUp(self):
        self.perfect = BST()
        for key in [7,3,1,5,0,6,2,4,11,9,8,10,13,12,14]:
            self.perfect.insert(key)
            
        self.degenerate = BST()
        for key in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
            self.degenerate.insert(key)
            
        self.balanced = BST()
        for key in [7,5,3,1,2,0,4,6,12,10,9,11,13,14,8]:
            self.balanced.insert(key)
        
        self.rightHeavy = BST()
        for key in [5,3,10,1,4,0,2,7,6,9,8,13,11,14,12]:
            self.rightHeavy.insert(key)
        
        self.leftHeavy = BST()
        for key in [11,13,12,14,6,3,8,9,7,4,1,5,2,0,10]:
            self.leftHeavy.insert(key)
        
    def testEmpty(self):
        tree = BST()
        expResult = str([])
        self.assertEqual(expResult, tree.printBFS())
        self.assertEqual(expResult, tree.printDFSinorder())
        self.assertEqual(expResult, tree.printDFSpostorder())
        self.assertEqual(expResult, tree.printDFSpreorder())
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        tree = BST()
        tree.insert(7)
        expResult = str([7])
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
        
    #def testDFSinorder(self):
    #    expResult = str([])
    #    self.assertEqual(expResult, self.perfect.printDFSinorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.degenerate.printDFSinorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.balanced.printDFSinorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.rightHeavy.printDFSinorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.leftHeavy.printDFSinorder())
    #    print("testDFSinorder PASSED")
    #    
    #def testDFSpreorder(self):
    #    expResult = str([])
    #    self.assertEqual(expResult, self.perfect.printDFSpreorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.degenerate.printDFSpreorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.balanced.printDFSpreorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.rightHeavy.printDFSpreorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.leftHeavy.printDFSpreorder())
    #    print("testDFSpreorder PASSED")
    #    
    #def testDFSpostorder(self):
    #    expResult = str([])
    #    self.assertEqual(expResult, self.perfect.printDFSpostorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.degenerate.printDFSpostorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.balanced.printDFSpostorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.rightHeavy.printDFSpostorder())
    #    expResult = str([])
    #    self.assertEqual(expResult, self.leftHeavy.printDFSpostorder())
    #    print("testDFSpostorder PASSED")

    
if __name__ == '__main__':
    unittest.main()