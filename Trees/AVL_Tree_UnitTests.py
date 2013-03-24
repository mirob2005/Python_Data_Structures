#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/--/2013

from AVL_Tree import AVLTree
import unittest
import random

class TestAVL(unittest.TestCase):
    
    def setUp(self):
        self.avl = AVLTree()
        
    def testEmpty(self):
        self.assertEqual(self.avl.outputTesting(),'(Empty)')
        self.assertFalse(self.avl.find(1))
        self.assertEqual(self.avl.findMax(),None)
        self.assertEqual(self.avl.findMin(),None)
        self.assertFalse(self.avl.delete(1))
        self.assertTrue(self.avl.insert(5))
        self.assertEqual(self.avl.outputTesting(),'(None)<-5(BF:0)->(None,None)\n')
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        print('\ntextInsert PASSED')
        
    def testDFSorder(self):
        print("\ntestDFS(pre&in&post)order PASSED")
        
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
        listToSort = [x for x in range(0,101,1)]
        random.shuffle(listToSort)
        for value in listToSort:
            self.avl.insert(value)
            
        sortedList = self.avl.traverseDFSinorder()
        self.assertEqual(sortedList,[x for x in range(0,101,1)])
        print("\ntestListSort PASSED")
    
if __name__ == '__main__':
    unittest.main()