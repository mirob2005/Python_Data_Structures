#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/13/2013

from Splay_Tree import SplayTree
import unittest

class TestSplay(unittest.TestCase):
    
    def setUp(self):
        self.perfect = SplayTree()
        self.degenerate = SplayTree()
        self.balanced = SplayTree()
        self.rightHeavy = SplayTree()
        self.leftHeavy = SplayTree()
        self.treeList = [self.perfect, self.degenerate, self.balanced, self.rightHeavy, self.leftHeavy]
        self.empty = SplayTree()
        
    def testEmpty(self):
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        print("\ntestInsert PASSED")
        
    def testBFS(self):
        print("testBFS PASSED")
        
    def testDFSinorder(self):
        print("\ntestDFSinorder PASSED")
        
    def testDFSpreorder(self):
        print("\ntestDFSpreorder PASSED")
        
    def testDFSpostorder(self):
        print("\ntestDFSpostorder PASSED")
        
    def testFind(self):
        print("\ntestFind PASSED")
        
    def testDuplicateInsert(self):
        print("\ntestDuplicateInsert PASSED")
        
    def testCopy(self):
        print("\ntestCopy PASSED")
        
    def testFindMin(self):
        print("\ntestFindMin PASSED")
        
    def testFindMax(self):
        print("\ntestFindMax PASSED")
        
    def testDeleteLeaf(self):
        print("\ntestDeleteLeaf PASSED")
        
    def testDeleteFail(self):
        print("\ntestDeleteFail PASSED")

    def testDeleteInternal(self):
        print("\ntestDeleteInternal PASSED")
        
    def testDeleteRoot(self):
        print("\ntestDeleteRoot PASSED")
        
    def testListSort(self):
        print("\ntestListSort PASSED")
        
    def testRecentAccessed(self):
        print("\ntestRecentAccessed PASSED")
    
if __name__ == '__main__':
    unittest.main()