#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/13/2013

from Splay_Tree import SplayTree
import unittest
import random

class TestSplay(unittest.TestCase):
    
    def setUp(self):
        self.st = SplayTree()
        
    def testEmpty(self):
        self.assertEqual(self.st.traverseBFS(),'(Empty)')
        self.assertFalse(self.st.find(1))
        self.assertEqual(self.st.findMax(),None)
        self.assertEqual(self.st.findMin(),None)
        self.assertEqual(self.st.findRecentAccessed(),None)
        self.assertFalse(self.st.delete(1))
        self.assertTrue(self.st.insert(5))
        self.assertEqual(self.st.traverseBFS(),'(None)<-5->(None,None)\n')
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        self.assertTrue(self.st.insert(1))
        string = '(None)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertTrue(self.st.insert(5))
        string = '(None)<-5->(1,None)\n(5)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)

        self.assertTrue(self.st.insert(3))
        string = '(None)<-3->(1,5)\n(3)<-1->(None,None)\n(3)<-5->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)

        self.assertTrue(self.st.insert(7))
        string = '(None)<-7->(5,None)\n(7)<-5->(3,None)\n(5)<-3->(1,None)\n'\
        '(3)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)

        self.assertTrue(self.st.insert(2))
        string = '(None)<-2->(1,5)\n(2)<-1->(None,None)\n(2)<-5->(3,7)\n'\
        '(5)<-3->(None,None)\n(5)<-7->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)

        self.assertTrue(self.st.insert(9))
        string = '(None)<-9->(2,None)\n(9)<-2->(1,7)\n(2)<-1->(None,None)\n'\
        '(2)<-7->(5,None)\n(7)<-5->(3,None)\n(5)<-3->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertTrue(self.st.insert(8))
        string = '(None)<-8->(7,9)\n(8)<-7->(2,None)\n(8)<-9->(None,None)\n'\
        '(7)<-2->(1,5)\n(2)<-1->(None,None)\n(2)<-5->(3,None)\n'\
        '(5)<-3->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertTrue(self.st.insert(10))
        string = '(None)<-10->(9,None)\n(10)<-9->(8,None)\n(9)<-8->(7,None)\n'\
        '(8)<-7->(2,None)\n(7)<-2->(1,5)\n(2)<-1->(None,None)\n(2)<-5->(3,None)\n'\
        '(5)<-3->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertTrue(self.st.insert(6))
        string = '(None)<-6->(5,9)\n(6)<-5->(2,None)\n(6)<-9->(7,10)\n'\
        '(5)<-2->(1,3)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n(2)<-1->(None,None)\n'\
        '(2)<-3->(None,None)\n(7)<-8->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertTrue(self.st.insert(4))
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        print('\ntextInsert PASSED')
        
    def testDFSinorder(self):
        boolResult = True
        for value in [1,5,3,7,2,9,8,10,6,4]:
            boolResult = boolResult and self.st.insert(value)
        self.assertTrue(boolResult)
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        keys = [4, 3, 2, 1, 5, 6, 9, 7, 8, 10]
        self.assertEqual(self.st.traverseDFSpreorder(),keys)

        keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(self.st.traverseDFSinorder(),keys)
        
        keys = [1, 2, 3, 8, 7, 10, 9, 6, 5, 4]
        self.assertEqual(self.st.traverseDFSpostorder(),keys)
        
        print("\ntestDFS(pre&in&post)order PASSED")
        
    def testFind(self):
        boolResult = True
        for value in [1,5,3,7,2,9,8,10,6,4]:
            boolResult = boolResult and self.st.insert(value)
        self.assertTrue(boolResult)
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertFalse(self.st.find(0))
        self.assertEqual(self.st.traverseBFS(),string)
        
        #Same result as duplicate insert
        self.assertTrue(self.st.find(7))
        string = '(None)<-7->(5,9)\n(7)<-5->(4,6)\n(7)<-9->(8,10)\n'\
        '(5)<-4->(3,None)\n(5)<-6->(None,None)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n(4)<-3->(2,None)\n(3)<-2->(1,None)\n'\
        '(2)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertTrue(self.st.find(4))
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,7)\n'\
        '(3)<-2->(1,None)\n(5)<-7->(6,9)\n(2)<-1->(None,None)\n'\
        '(7)<-6->(None,None)\n(7)<-9->(8,10)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        print("\ntestFind PASSED")
        
    def testDuplicateInsert(self):
        boolResult = True
        for value in [1,5,3,7,2,9,8,10,6,4]:
            boolResult = boolResult and self.st.insert(value)
        self.assertTrue(boolResult)
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        #Same result as find(7)
        self.assertFalse(self.st.insert(7))
        string = '(None)<-7->(5,9)\n(7)<-5->(4,6)\n(7)<-9->(8,10)\n'\
        '(5)<-4->(3,None)\n(5)<-6->(None,None)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n(4)<-3->(2,None)\n(3)<-2->(1,None)\n'\
        '(2)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        print("\ntestDuplicateInsert PASSED")
        
    #def testCopy(self):
    #    print("\ntestCopy PASSED")
    #
    
    def testFindMin(self):
        boolResult = True
        for value in [1,5,3,7,2,9,8,10,6,4]:
            boolResult = boolResult and self.st.insert(value)
        self.assertTrue(boolResult)
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.findMin(),1)
        
        self.assertFalse(self.st.find(0))
        self.assertEqual(self.st.traverseBFS(),string)
        self.assertEqual(self.st.findMin(),1)
        
        self.assertTrue(self.st.find(7))
        string = '(None)<-7->(5,9)\n(7)<-5->(4,6)\n(7)<-9->(8,10)\n'\
        '(5)<-4->(3,None)\n(5)<-6->(None,None)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n(4)<-3->(2,None)\n(3)<-2->(1,None)\n'\
        '(2)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        self.assertEqual(self.st.findMin(),1)
        
        self.assertTrue(self.st.find(4))
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,7)\n'\
        '(3)<-2->(1,None)\n(5)<-7->(6,9)\n(2)<-1->(None,None)\n'\
        '(7)<-6->(None,None)\n(7)<-9->(8,10)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        self.assertEqual(self.st.findMin(),1)
        
        print("\ntestFindMin PASSED")
        
    def testFindMax(self):
        boolResult = True
        for value in [1,5,3,7,2,9,8,10,6,4]:
            boolResult = boolResult and self.st.insert(value)
        self.assertTrue(boolResult)
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.findMax(),10)
        
        self.assertFalse(self.st.find(0))
        self.assertEqual(self.st.traverseBFS(),string)
        self.assertEqual(self.st.findMax(),10)
        
        self.assertTrue(self.st.find(7))
        string = '(None)<-7->(5,9)\n(7)<-5->(4,6)\n(7)<-9->(8,10)\n'\
        '(5)<-4->(3,None)\n(5)<-6->(None,None)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n(4)<-3->(2,None)\n(3)<-2->(1,None)\n'\
        '(2)<-1->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        self.assertEqual(self.st.findMax(),10)
        
        self.assertTrue(self.st.find(4))
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,7)\n'\
        '(3)<-2->(1,None)\n(5)<-7->(6,9)\n(2)<-1->(None,None)\n'\
        '(7)<-6->(None,None)\n(7)<-9->(8,10)\n(9)<-8->(None,None)\n'\
        '(9)<-10->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        self.assertEqual(self.st.findMax(),10)
        print("\ntestFindMax PASSED")
        
    #def testDeleteLeaf(self):
    #    print("\ntestDeleteLeaf PASSED")
    #    
    def testDeleteFail(self):
        self.assertFalse(self.st.delete(1))
        boolResult = True
        for value in [1,5,3,7,2,9,8,10,6,4]:
            boolResult = boolResult and self.st.insert(value)
        self.assertTrue(boolResult)
        string = '(None)<-4->(3,5)\n(4)<-3->(2,None)\n(4)<-5->(None,6)\n'\
        '(3)<-2->(1,None)\n(5)<-6->(None,9)\n(2)<-1->(None,None)\n'\
        '(6)<-9->(7,10)\n(9)<-7->(None,8)\n(9)<-10->(None,None)\n'\
        '(7)<-8->(None,None)\n'
        self.assertEqual(self.st.traverseBFS(),string)
        
        self.assertFalse(self.st.delete(0))
        self.assertTrue(self.st.delete(1))
        self.assertFalse(self.st.delete(1))
        
        print("\ntestDeleteFail PASSED")
    #
    #def testDeleteInternal(self):
    #    print("\ntestDeleteInternal PASSED")
    #    
    #def testDeleteRoot(self):
    #    print("\ntestDeleteRoot PASSED")

    def testListSort(self):
        listToSort = [x for x in range(0,101,1)]
        random.shuffle(listToSort)
        for value in listToSort:
            self.st.insert(value)
            
        sortedList = self.st.traverseDFSinorder()
        self.assertEqual(sortedList,[x for x in range(0,101,1)])
        print("\ntestListSort PASSED")
        
    def testRecentAccessed(self):
        boolResult = True
        listToSort = [x for x in range(0,101,1)]
        random.shuffle(listToSort)
        for value in listToSort:
            boolResult = boolResult and self.st.insert(value)
            self.assertEqual(self.st.findRecentAccessed(),value)
        self.assertTrue(boolResult)
        
        self.assertTrue(self.st.find(7))
        self.assertEqual(self.st.findRecentAccessed(),7)
        
        print("\ntestRecentAccessed PASSED")
    
if __name__ == '__main__':
    unittest.main()