#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/23/2013

from Binary_Heap_Tree_Structure import BinaryHeap
import unittest

class TestBST(unittest.TestCase):
    
    def setUp(self):
        self.empty = BinaryHeap()
        self.tester = BinaryHeap()
        
    def testEmpty(self):
        expResult = "(Empty)"
        result = self.empty.traverseBFS()
        self.assertEqual(result,expResult)
        print("\ntestEmpty PASSED")
        
    def testDeleteEmpty(self):
        result = self.empty.delete()
        expResult = None
        
        expPrintResult = "(Empty)"
        printResult = self.empty.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertEqual(printResult, expPrintResult)
        print("\ntestDeleteEmpty PASSED")
        
    
    def testInsertEmpty(self):
        self.empty.insert(1)
        expResult = "\n1 - (None|None, None)"
        result = self.empty.traverseBFS()
        self.assertEqual(result,expResult)
        print("\ntestInsertEmpty PASSED")
    
    def testInsert(self):
        expResult = "(Empty)"
        result = self.tester.traverseBFS()
        self.assertEqual(result,expResult)
        
        boolResult = self.tester.insert(0)
        expResult = "\n0 - (None|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(1)
        expResult = "\n1 - (None|0, None)\n0 - (1|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(2)
        expResult = "\n2 - (None|0, 1)\n0 - (2|None, None)\n1 - (2|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(3)
        expResult = "\n3 - (None|2, 1)\n2 - (3|0, None)\n1 - (3|None, None)\n"\
                    "0 - (2|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(4)
        expResult = "\n4 - (None|3, 1)\n3 - (4|0, 2)\n1 - (4|None, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(5)
        expResult = "\n5 - (None|3, 4)\n3 - (5|0, 2)\n4 - (5|1, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)\n1 - (4|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(6)
        expResult = "\n6 - (None|3, 5)\n3 - (6|0, 2)\n5 - (6|1, 4)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(7)
        expResult = "\n7 - (None|6, 5)\n6 - (7|3, 2)\n5 - (7|1, 4)\n"\
                    "3 - (6|0, None)\n2 - (6|None, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (3|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(8)
        expResult = "\n8 - (None|7, 5)\n7 - (8|6, 2)\n5 - (8|1, 4)\n"\
                    "6 - (7|0, 3)\n2 - (7|None, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (6|None, None)\n3 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(9)
        expResult = "\n9 - (None|8, 5)\n8 - (9|6, 7)\n5 - (9|1, 4)\n"\
                    "6 - (8|0, 3)\n7 - (8|2, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (7|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(10)
        expResult = "\n10 - (None|9, 5)\n9 - (10|6, 8)\n5 - (10|1, 4)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (8|None, None)\n7 - (8|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(11)
        expResult = "\n11 - (None|9, 10)\n9 - (11|6, 8)\n10 - (11|5, 4)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n5 - (10|1, None)\n"\
                    "4 - (10|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (5|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(12)
        expResult = "\n12 - (None|9, 11)\n9 - (12|6, 8)\n11 - (12|10, 4)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (11|1, 5)\n"\
                    "4 - (11|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(13)
        expResult = "\n13 - (None|9, 12)\n9 - (13|6, 8)\n12 - (13|10, 11)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (12|1, 5)\n11 - (12|4, None)\n"\
                    "0 - (6|None, None)\n3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (11|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(14)
        expResult = "\n14 - (None|9, 13)\n9 - (14|6, 8)\n13 - (14|10, 12)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "0 - (6|None, None)\n3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        boolResult = self.tester.insert(15)
        expResult = "\n15 - (None|14, 13)\n14 - (15|9, 8)\n13 - (15|10, 12)\n"\
                    "9 - (14|6, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "6 - (9|0, None)\n3 - (9|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        #CHECK MIDDLE INSERT
        boolResult = self.tester.insert(10)
        expResult = "\n15 - (None|14, 13)\n14 - (15|10, 8)\n13 - (15|10, 12)\n"\
                    "10 - (14|9, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "9 - (10|0, 6)\n3 - (10|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (9|None, None)\n"\
                    "6 - (9|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        #CHECK LEAF INSERT / NEGATIVE VALUES
        boolResult = self.tester.insert(-1)
        expResult = "\n15 - (None|14, 13)\n14 - (15|10, 8)\n13 - (15|10, 12)\n"\
                    "10 - (14|9, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "9 - (10|0, 6)\n3 - (10|-1, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (9|None, None)\n"\
                    "6 - (9|None, None)\n-1 - (3|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        print("\ntestInsert PASSED")
    
    def testInsertList(self):
        alist = [x for x in range(16)]
        boolResult = self.tester.insertList(alist)
        expResult = "\n15 - (None|14, 13)\n14 - (15|9, 8)\n13 - (15|10, 12)\n"\
                    "9 - (14|6, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "6 - (9|0, None)\n3 - (9|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        
        print("\ntestInsertList PASSED")
        
    def testPeek(self):
        alist = [x for x in range(16)]
        boolResult = self.tester.insertList(alist)
        expResult = "\n15 - (None|14, 13)\n14 - (15|9, 8)\n13 - (15|10, 12)\n"\
                    "9 - (14|6, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "6 - (9|0, None)\n3 - (9|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        
        peek = self.tester.peek()
        self.assertEqual(peek,15)
        self.assertEqual(self.empty.peek(),None)
        print("\ntestPeek PASSED")
        
    def testMerge(self):
        alist = [x for x in range(14)]
        boolResult = self.tester.insertList(alist)
        expResult = "\n13 - (None|9, 12)\n9 - (13|6, 8)\n12 - (13|10, 11)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (12|1, 5)\n11 - (12|4, None)\n"\
                    "0 - (6|None, None)\n3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (11|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        blist = [x for x in range(14,16)]
        boolResult = self.empty.insertList(blist)
        expResult = "\n15 - (None|14, None)\n14 - (15|None, None)"
        result = self.empty.traverseBFS()
        self.assertEqual(result, expResult)
        self.assertTrue(boolResult)
        
        self.tester.merge(self.empty)
        expResult = "\n15 - (None|14, 13)\n14 - (15|9, 8)\n13 - (15|10, 12)\n"\
                    "9 - (14|6, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "6 - (9|0, None)\n3 - (9|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(result, expResult)
        
        print("\ntestMerge PASSED")
    
    def testCopyHeap(self):
        boolResult = self.tester.insertList([0,1,2,3,4,5])
        expResult = "\n5 - (None|3, 4)\n3 - (5|0, 2)\n4 - (5|1, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)\n1 - (4|None, None)"
        result = self.tester.traverseBFS()
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        
        copy = self.tester.copyHeap()
        expResult = "\n5 - (None|3, 4)\n3 - (5|0, 2)\n4 - (5|1, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)\n1 - (4|None, None)"
        result = copy.traverseBFS()
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        
        print("\ntestCopyHeap PASSED")
        
    def testDelete(self):
        #Test to confirm valid data before deletes
        alist = [x for x in range(16)]
        boolResult = self.tester.insertList(alist)
        expResult = "\n15 - (None|14, 13)\n14 - (15|9, 8)\n13 - (15|10, 12)\n"\
                    "9 - (14|6, 3)\n8 - (14|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "6 - (9|0, None)\n3 - (9|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)\n0 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertTrue(boolResult)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 15
        expResult = "\n14 - (None|9, 13)\n9 - (14|6, 8)\n13 - (14|10, 12)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (13|1, 5)\n12 - (13|4, 11)\n"\
                    "0 - (6|None, None)\n3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (12|None, None)\n11 - (12|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
    
        returnedValue = self.tester.delete()
        expValue = 14
        expResult = "\n13 - (None|9, 12)\n9 - (13|6, 8)\n12 - (13|10, 11)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (12|1, 5)\n11 - (12|4, None)\n"\
                    "0 - (6|None, None)\n3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)\n"\
                    "4 - (11|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 13
        expResult = "\n12 - (None|9, 11)\n9 - (12|6, 8)\n11 - (12|10, 4)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n10 - (11|1, 5)\n"\
                    "4 - (11|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (10|None, None)\n5 - (10|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 12
        expResult = "\n11 - (None|9, 10)\n9 - (11|6, 8)\n10 - (11|5, 4)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n5 - (10|1, None)\n"\
                    "4 - (10|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (8|None, None)\n"\
                    "7 - (8|None, None)\n1 - (5|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 11
        expResult = "\n10 - (None|9, 5)\n9 - (10|6, 8)\n5 - (10|1, 4)\n"\
                    "6 - (9|0, 3)\n8 - (9|2, 7)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (8|None, None)\n7 - (8|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 10
        expResult = "\n9 - (None|8, 5)\n8 - (9|6, 7)\n5 - (9|1, 4)\n"\
                    "6 - (8|0, 3)\n7 - (8|2, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (6|None, None)\n"\
                    "3 - (6|None, None)\n2 - (7|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 9
        expResult = "\n8 - (None|7, 5)\n7 - (8|6, 2)\n5 - (8|1, 4)\n"\
                    "6 - (7|0, 3)\n2 - (7|None, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (6|None, None)\n3 - (6|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 8
        expResult = "\n7 - (None|6, 5)\n6 - (7|3, 2)\n5 - (7|1, 4)\n"\
                    "3 - (6|0, None)\n2 - (6|None, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)\n0 - (3|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 7
        expResult = "\n6 - (None|3, 5)\n3 - (6|0, 2)\n5 - (6|1, 4)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)\n1 - (5|None, None)\n"\
                    "4 - (5|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 6
        expResult = "\n5 - (None|3, 4)\n3 - (5|0, 2)\n4 - (5|1, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)\n1 - (4|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
    
        returnedValue = self.tester.delete()
        expValue = 5
        expResult = "\n4 - (None|3, 1)\n3 - (4|0, 2)\n1 - (4|None, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 4
        expResult = "\n3 - (None|2, 1)\n2 - (3|0, None)\n1 - (3|None, None)\n"\
                    "0 - (2|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 3
        expResult = "\n2 - (None|0, 1)\n0 - (2|None, None)\n1 - (2|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 2
        expResult = "\n1 - (None|0, None)\n0 - (1|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 1
        expResult = "\n0 - (None|None, None)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = 0
        expResult = "(Empty)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
        
        returnedValue = self.tester.delete()
        expValue = None
        expResult = "(Empty)"
        result = self.tester.traverseBFS()
        self.assertEqual(returnedValue, expValue)
        self.assertEqual(result, expResult)
    
        print("\ntestDelete PASSED")
        
    def testAlternateInsertDelete(self):
        #This thoroughly tests the ability to keep track of where to insert the
        #next item even after multiple deletes
        
        for data in [0,1,2,3,4,5,6,7]:
            self.tester.insert(data)
            
        returnValue = self.tester.delete()
        self.assertEqual(returnValue,7)
        returnValue = self.tester.delete()
        self.assertEqual(returnValue,6)
        returnValue = self.tester.delete()
        self.assertEqual(returnValue,5)
        returnValue = self.tester.delete()
        self.assertEqual(returnValue,4)
        
        boolResult = self.tester.insert(4)
        self.assertTrue(boolResult)
        result = self.tester.traverseBFS()
        expResult = "\n4 - (None|3, 1)\n3 - (4|0, 2)\n1 - (4|None, None)\n"\
                    "0 - (3|None, None)\n2 - (3|None, None)"
        self.assertEqual(result, expResult)
        
        returnValue = self.tester.delete()
        self.assertEqual(returnValue,4)
        
        while(self.tester.delete()):
            pass
        
        self.assertEqual(self.tester.traverseBFS(),"(Empty)")
        
        for data in range(101):
            self.tester.insert(data)
            
        for data in range(101):
            returnValue = self.tester.delete()
            self.assertEqual(returnValue, (100-data), "%s, 100-%s"%(returnValue,data))
        
        print("\ntestAlternateInsertDelete PASSED")
        
if __name__ == '__main__':
    unittest.main()