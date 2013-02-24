#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/14/2013

from LinkedList_Circular import CircularLinkedList
from LinkedList_Circular import CircularNode
import unittest

class TestLinkedListCircular(unittest.TestCase):
    
    def setUp(self):
        self.A = CircularLinkedList()
        for data in [3,2,1]:
            self.A.insert(data)

    def testEmpty(self):
        emptyList = CircularLinkedList()
        expResult = "HEAD(None) <> TAIL(None)"
        result = str(emptyList)
        self.assertEqual(result, expResult)
        print("\ntestEmpty PASSED!")
        
    def testInsert(self):
        expResult = "HEAD(1) < (3)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(1) > TAIL(3)"
        result = str(self.A)
        self.assertEqual(result, expResult)
        print("\ntestInsert PASSED!")
        
    def testAppend(self):
        self.A.append(4)
        
        expResult = "HEAD(1) < (4)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(4) (3)<-[4]->(1) > TAIL(4)"
        result = str(self.A)
        self.assertEqual(result, expResult)
        print("\ntestAppend PASSED!")
        
    def testReturnIndex(self):
        result = self.A.returnIndex(1)
        expResult = 0
        self.assertEqual(result, expResult)
        print("\ntestReturnIndex #1 PASSED!")
        
        result = self.A.returnIndex(2)
        expResult = 1
        self.assertEqual(result, expResult)
        print("\ntestReturnIndex #2 PASSED!")
        
        result = self.A.returnIndex(3)
        expResult = 2
        self.assertEqual(result, expResult)
        print("\ntestReturnIndex #3 PASSED!")
        
        result = self.A.returnIndex(4)
        expResult = None
        self.assertEqual(result, expResult)
        print("\ntestReturnIndex #4 PASSED!")
        
    def testUpdateIndex(self):
        boolResult = self.A.updateIndex(0,4)
        expResult = "HEAD(4) < (3)<-[4]->(2) (4)<-[2]->(3) (2)<-[3]->(4) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestUpdateIndex #1 PASSED!")
        
        boolResult = self.A.updateIndex(1,5)
        expResult = "HEAD(4) < (3)<-[4]->(5) (4)<-[5]->(3) (5)<-[3]->(4) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestUpdateIndex #2 PASSED!")
        
        boolResult = self.A.updateIndex(2,6)
        expResult = "HEAD(4) < (6)<-[4]->(5) (4)<-[5]->(6) (5)<-[6]->(4) > TAIL(6)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestUpdateIndex #3 PASSED!")
        
        boolResult = self.A.updateIndex(3,7)
        expResult = "HEAD(4) < (6)<-[4]->(5) (4)<-[5]->(6) (5)<-[6]->(4) > TAIL(6)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestUpdateIndex #4 PASSED!")
        
        boolResult = self.A.updateIndex(-1,7)
        expResult = "HEAD(4) < (6)<-[4]->(5) (4)<-[5]->(6) (5)<-[6]->(4) > TAIL(6)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestUpdateIndex #5 PASSED!")
        
    def testDeleteIndex(self):
        boolResult = self.A.deleteIndex(4)
        expResult = "HEAD(1) < (3)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(1) > TAIL(3)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteIndex #1 PASSED!")
        
        boolResult = self.A.deleteIndex(2)
        expResult = "HEAD(1) < (2)<-[1]->(2) (1)<-[2]->(1) > TAIL(2)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteIndex #2 PASSED!")
        
        boolResult = self.A.deleteIndex(-1)
        expResult = "HEAD(1) < (2)<-[1]->(2) (1)<-[2]->(1) > TAIL(2)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteIndex #3 PASSED!")
        
        boolResult = self.A.deleteIndex(0)
        expResult = "HEAD(2) < (2)<-[2]->(2) > TAIL(2)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteIndex #4 PASSED!")
        
        boolResult = self.A.deleteIndex(0)
        expResult = "HEAD(None) <> TAIL(None)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteIndex #5 PASSED!")
        
        boolResult = self.A.deleteIndex(0)
        expResult = "HEAD(None) <> TAIL(None)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteIndex #6 PASSED!")
        
    def testInsertBeforeIndex(self):
        boolResult = self.A.insertBeforeIndex(-1,0)
        expResult = "HEAD(1) < (3)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(1) > TAIL(3)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeIndex #1 PASSED!")
        
        boolResult = self.A.insertBeforeIndex(0,4)
        expResult = "HEAD(4) < (3)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(4) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeIndex #2 PASSED!")
        
        boolResult = self.A.insertBeforeIndex(3,5)
        expResult = "HEAD(4) < (3)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(5) (2)<-[5]->(3) (5)<-[3]->(4) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeIndex #3 PASSED!")
        
        boolResult = self.A.insertBeforeIndex(5,6)
        expResult = "HEAD(4) < (6)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(5) (2)<-[5]->(3) (5)<-[3]->(6) (3)<-[6]->(4) > TAIL(6)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeIndex #4 PASSED!")
        
        boolResult = self.A.insertBeforeIndex(7,6)
        expResult = "HEAD(4) < (6)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(5) (2)<-[5]->(3) (5)<-[3]->(6) (3)<-[6]->(4) > TAIL(6)" 
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeIndex #4 PASSED!")
        
    def testInsertAfterIndex(self):
        boolResult = self.A.insertAfterIndex(-2,0)
        expResult = "HEAD(1) < (3)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(1) > TAIL(3)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterIndex #1 PASSED!")
        
        boolResult = self.A.insertAfterIndex(-1,4)
        expResult = "HEAD(4) < (3)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(4) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterIndex #2 PASSED!")
        
        boolResult = self.A.insertAfterIndex(2,5)
        expResult = "HEAD(4) < (3)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(5) (2)<-[5]->(3) (5)<-[3]->(4) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterIndex #3 PASSED!")
        
        boolResult = self.A.insertAfterIndex(4,6)
        expResult = "HEAD(4) < (6)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(5) (2)<-[5]->(3) (5)<-[3]->(6) (3)<-[6]->(4) > TAIL(6)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterIndex #4 PASSED!")
        
        boolResult = self.A.insertAfterIndex(6,6)
        expResult = "HEAD(4) < (6)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(5) (2)<-[5]->(3) (5)<-[3]->(6) (3)<-[6]->(4) > TAIL(6)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterIndex #5 PASSED!")
        
    def testDeleteData(self):
        boolResult = self.A.deleteData(4)
        expResult = "HEAD(1) < (3)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(1) > TAIL(3)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteData #1 PASSED!")
        
        boolResult = self.A.deleteData(3)
        expResult = "HEAD(1) < (2)<-[1]->(2) (1)<-[2]->(1) > TAIL(2)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteData #2 PASSED!")

        boolResult = self.A.deleteData(1)
        expResult = "HEAD(2) < (2)<-[2]->(2) > TAIL(2)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteData #3 PASSED!")
        
        boolResult = self.A.deleteData(2)
        expResult = "HEAD(None) <> TAIL(None)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteData #4 PASSED!")
        
        boolResult = self.A.deleteData(2)
        expResult = "HEAD(None) <> TAIL(None)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteData #5 PASSED!")
        
    def testDeleteAllData(self):
        self.A.append(1)
        boolResult = self.A.deleteAllData(1)
        expResult = "HEAD(2) < (3)<-[2]->(3) (2)<-[3]->(2) > TAIL(3)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteAllData #1 PASSED!")
        
        boolResult = self.A.deleteAllData(1)
        expResult = "HEAD(2) < (3)<-[2]->(3) (2)<-[3]->(2) > TAIL(3)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestDeleteAllData #2 PASSED!")
        
    def testDeleteList(self):
        self.A.deleteList()
        expResult = "HEAD(None) <> TAIL(None)"
        result = str(self.A)
        self.assertEqual(result, expResult)
        print("\ntestDeleteList PASSED!")
        
    def testInsertAfterEveryData(self):
        self.A.append(1)
        boolResult = self.A.insertAfterEveryData(1,4)
        expResult = "HEAD(1) < (4)<-[1]->(4) (1)<-[4]->(2) (4)<-[2]->(3) (2)<-[3]->(1) (3)<-[1]->(4) (1)<-[4]->(1) > TAIL(4)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterEveryData #1 PASSED!")
        
        boolResult = self.A.insertAfterEveryData(0,5)
        expResult = "HEAD(1) < (4)<-[1]->(4) (1)<-[4]->(2) (4)<-[2]->(3) (2)<-[3]->(1) (3)<-[1]->(4) (1)<-[4]->(1) > TAIL(4)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertAfterEveryData #2 PASSED!")        
    
    def testInsertBeforeEveryData(self):
        self.A.append(1)
        boolResult = self.A.insertBeforeEveryData(1,4)
        expResult = "HEAD(4) < (1)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(4) (3)<-[4]->(1) (4)<-[1]->(4) > TAIL(1)"
        result = str(self.A)
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeEveryData #1 PASSED!")
        
        boolResult = self.A.insertBeforeEveryData(0,5)
        expResult = "HEAD(4) < (1)<-[4]->(1) (4)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(4) (3)<-[4]->(1) (4)<-[1]->(4) > TAIL(1)"
        result = str(self.A)
        self.assertFalse(boolResult)
        self.assertEqual(result, expResult)
        print("\ntestInsertBeforeEveryData #2 PASSED!")    
    
    def testCopyList(self):
        B = CircularLinkedList()
        B = self.A.copyList()
        
        self.A.append(4)
        B.append(5)
        
        expAResult = "HEAD(1) < (4)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(4) (3)<-[4]->(1) > TAIL(4)"
        expBResult = "HEAD(1) < (5)<-[1]->(2) (1)<-[2]->(3) (2)<-[3]->(5) (3)<-[5]->(1) > TAIL(5)"
        Aresult = str(self.A)
        Bresult = str(B)
        
        self.assertEqual(expAResult, Aresult)
        self.assertEqual(expBResult, Bresult)
        self.assertNotEqual(Aresult,Bresult)
        print("\ntestCopyList PASSED!")
    
    def testFindMthToLastNode(self):
        expResult = None
        result = self.A.findMthToLastNode(-1)
        self.assertEqual(result,expResult)
        print("\ntestFindMthToLastNode #1 PASSED!")
        
        expResult = None
        result = self.A.findMthToLastNode(0)
        self.assertEqual(result,expResult)
        print("\ntestFindMthToLastNode #2 PASSED!")
        
        expResult = 3
        result = self.A.findMthToLastNode(1)
        self.assertEqual(result,expResult)
        print("\ntestFindMthToLastNode #3 PASSED!")
        
        expResult = 2
        result = self.A.findMthToLastNode(2)
        self.assertEqual(result,expResult)
        print("\ntestFindMthToLastNode #4 PASSED!")
        
        expResult = 1
        result = self.A.findMthToLastNode(3)
        self.assertEqual(result,expResult)
        print("\ntestFindMthToLastNode #5 PASSED!")

        expResult = None
        result = self.A.findMthToLastNode(4)
        self.assertEqual(result,expResult)
        print("\ntestFindMthToLastNode #6 PASSED!")
    
if __name__ == '__main__':
    unittest.main()