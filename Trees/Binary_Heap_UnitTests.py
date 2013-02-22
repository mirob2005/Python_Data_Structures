from Binary_Heap import BinaryHeap
import unittest

class TestBST(unittest.TestCase):
    
    def setUp(self):
        self.empty = BinaryHeap()
        self.one = BinaryHeap()
        self.two = BinaryHeap()
        self.three = BinaryHeap()
        self.five = BinaryHeap()
        self.large = BinaryHeap()
        
        self.one.insert(1)
        self.two.insertList([1,2])
        self.three.insertList([1,2,3])
        self.five.insertList([1,2,3,4,5])
        data = [x for x in range(13)]
        self.large.insertList(data)
        
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
        self.one.insert(5)
        expResult = "\n5 - (None|1, None)\n1 - (5|None, None)"
        result = self.one.traverseBFS()
        self.assertEqual(result,expResult)
        
        self.two.insert(5)
        expResult = "\n5 - (None|1, 2)\n1 - (5|None, None)\n2 - (5|None, None)"
        result = self.two.traverseBFS()
        self.assertEqual(result,expResult)
        
        self.three.insert(5)
        expResult = "\n5 - (None|3, 2)\n3 - (5|1, None)\n2 - (5|None, None)\n1 - (3|None, None)"
        result = self.three.traverseBFS()
        self.assertEqual(result,expResult)
        
        self.five.insert(5)
        expResult = "\n5 - (None|4, 5)\n4 - (5|1, 3)\n5 - (5|2, None)\n1 - (4|None, None)\n3 - (4|None, None)\n2 - (5|None, None)"
        result = self.five.traverseBFS()
        self.assertEqual(result,expResult)
        
        #More Tests...
        print("\ntestInsert PASSED")
    
    def testDelete(self):
        result = self.one.delete()
        expResult = 1
        printResult = self.one.traverseBFS()
        expPrintResult = "(Empty)"
        
        self.assertEqual(result, expResult)
        self.assertEqual(printResult, expPrintResult)
        
        #More Tests...
        print("\ntestDelete PASSED")
    
if __name__ == '__main__':
    unittest.main()