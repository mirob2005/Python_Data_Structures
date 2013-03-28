#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/--/2013

from RedBlack_Tree import RedBlackTree
import unittest
import random

class TestRedBlackTree(unittest.TestCase):
    
    def setUp(self):
        self.rb = RedBlackTree()
        self.fullRB = RedBlackTree()
        
        self.insertList = [47,30,2,6,12,64,62,98,93,95,97,99,3,4,5,7]
        for item in self.insertList:
            self.assertTrue(self.fullRB.insert(item))
        self.result = ''
        
        
    def testEmpty(self):
        self.assertEqual(self.rb.outputTesting(),'(Empty)')
        self.assertFalse(self.rb.find(1))
        self.assertEqual(self.rb.findMax(),None)
        self.assertEqual(self.rb.findMin(),None)
        self.assertFalse(self.rb.delete(1))
        self.assertTrue(self.rb.insert(5))
        self.assertEqual(self.rb.outputTesting(),'(NoneB)<-5B->(NoneB,NoneB)\n')
        print("\ntestEmpty PASSED")
        
    def testInsert(self):
        self.assertTrue(self.rb.insert(47))
        string = '(NoneB)<-47B->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(30))
        string = '(NoneB)<-47B->(30R,NoneB)\n'\
                 '(47B)<-30R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
    
        self.assertTrue(self.rb.insert(2))
        string = '(NoneB)<-30B->(2R,47R)\n'\
                 '(30B)<-2R->(NoneB,NoneB)\n'\
                 '(30B)<-47R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
    
        self.assertTrue(self.rb.insert(6))
        string = '(NoneB)<-30B->(2B,47B)\n'\
                 '(30B)<-2B->(NoneB,6R)\n'\
                 '(30B)<-47B->(NoneB,NoneB)\n'\
                 '(2B)<-6R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        #self.assertTrue(self.rb.insert(12))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(64))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(62))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(98))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(93))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(95))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(97))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(99))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(3))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(4))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(5))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        #
        #self.assertTrue(self.rb.insert(7))
        #string = ''
        #self.assertEqual(self.rb.outputTesting(),string)
        
        print('\ntextInsert PASSED')
    #    
    #def testDFSorder(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    keys = []
    #    self.assertEqual(self.fullRB.traverseDFSpreorder(),keys)
    #
    #    self.insertList.sort(reverse=False)
    #    self.assertEqual(self.fullRB.traverseDFSinorder(),self.insertList)
    #    
    #    keys = []
    #    self.assertEqual(self.fullRB.traverseDFSpostorder(),keys)
    #    
    #    print("\ntestDFS(pre&in&post)order PASSED")
    #
    #def testFind(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    random.shuffle(self.insertList)
    #    for item in self.insertList:
    #        self.assertTrue(self.fullRB.find(item))
    #    
    #    #FAIL FIND
    #    failFinds = [x for x in range(0,101)]
    #    for item in self.insertList:
    #        if item in failFinds:
    #            failFinds.remove(item)
    #    for item in failFinds:
    #        self.assertFalse(self.fullRB.find(item))
    #
    #    print("\ntestFind PASSED")
    #    
    #def testDuplicateInsert(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #Duplicate Insert should fail and NOT change the output
    #    for item in self.insertList:
    #        self.assertFalse(self.fullRB.insert(item))
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    print("\ntestDuplicateInsert PASSED")
    #    
    #def testCopy(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    copy = self.fullRB.copyTree()
    #    self.assertEqual(copy.outputTesting(),self.result)
    #    
    #    self.assertTrue(self.fullRB.insert(1))
    #    self.assertTrue(copy.insert(0))
    #    
    #    #fullRB after inserting 1
    #    newResult = ''
    #    #The copy after inserting 0
    #    newCopy = ''
    #    
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    self.assertEqual(copy.outputTesting(),newCopy)
    #    print("\ntestCopy PASSED")
    #
    #def testFindMin(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #Find Min
    #    self.assertEqual(self.fullRB.findMin(),2)
    #    
    #    #Insert New Min
    #    self.assertTrue(self.fullRB.insert(0))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Find New Min
    #    self.assertEqual(self.fullRB.findMin(),0)
    #
    #    print("\ntestFindMin PASSED")
    #    
    #def testFindMax(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #Find Max
    #    self.assertEqual(self.fullRB.findMax(),99)
    #    
    #    #Insert New Max
    #    self.assertTrue(self.fullRB.insert(100))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Find New Max
    #    self.assertEqual(self.fullRB.findMax(),100)
    #    
    #    print("\ntestFindMax PASSED")
    #    
    #def testDeleteLeaf(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #Delete requires rotations
    #    self.assertTrue(self.fullRB.delete(99))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Delete does not require rotations
    #    self.assertTrue(self.fullRB.delete(7))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Delete requires rotations
    #    self.assertTrue(self.fullRB.delete(2))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Delete does not require rotations
    #    self.assertTrue(self.fullRB.delete(5))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Delete requires rotations
    #    self.assertTrue(self.fullRB.delete(12))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    print("\ntestDeleteLeaf PASSED")
    #    
    #def testDeleteFail(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #FAIL DELETES (keys not present)
    #    failDeletes = [x for x in range(0,101)]
    #    for item in self.insertList:
    #        if item in failDeletes:
    #            failDeletes.remove(item)
    #    for item in failDeletes:
    #        self.assertFalse(self.fullRB.delete(item))
    #        
    #    #Check to make sure tree was not changed
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #Successfully delete 99
    #    #Delete requires rotations
    #    self.assertTrue(self.fullRB.delete(99))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Try to delete 99 again
    #    self.assertFalse(self.fullRB.delete(99))
    #    
    #    #Check to make sure tree was not changed
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    print("\ntestDeleteFail PASSED")
    #
    #def testDeleteInternal(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    #No rotations necessary
    #    self.assertTrue(self.fullRB.delete(3))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    #No rotations necessary
    #    self.assertTrue(self.fullRB.delete(4))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    #Rotations Necessary
    #    self.assertTrue(self.fullRB.delete(98))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    #No Rotations Necessary
    #    self.assertTrue(self.fullRB.delete(6))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Rotations Necessary
    #    self.assertTrue(self.fullRB.delete(5))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Rotations Necessary
    #    self.assertTrue(self.fullRB.delete(7))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    #1 Rotation Necessary
    #    self.assertTrue(self.fullRB.delete(2))
    #    newResult = ''
    #             
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    print("\ntestDeleteInternal PASSED")
    #    
    #def testDeleteRoot(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    self.assertTrue(self.fullRB.delete(93))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(64))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Requires Rotation
    #    self.assertTrue(self.fullRB.delete(62))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(47))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    #Requires Rotation
    #    self.assertTrue(self.fullRB.delete(30))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(12))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(7))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(6))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(5))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(4))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.delete(97))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    self.assertTrue(self.fullRB.delete(95))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    self.assertTrue(self.fullRB.delete(3))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    self.assertTrue(self.fullRB.delete(98))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    self.assertTrue(self.fullRB.delete(2))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    self.assertTrue(self.fullRB.delete(99))
    #    newResult = '(Empty)'
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    for item in range(0,101):
    #        self.assertFalse(self.fullRB.delete(item))
    #        self.assertFalse(self.fullRB.find(item))
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    print("\ntestDeleteRoot PASSED")
    #
    #def testDeleteTree(self):
    #    self.assertEqual(self.fullRB.outputTesting(),self.result)
    #    
    #    self.fullRB.deleteTree()
    #    newResult = '(Empty)'
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #
    #    for item in range(0,101):
    #        self.assertFalse(self.fullRB.delete(item))
    #        self.assertFalse(self.fullRB.find(item))
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    self.assertTrue(self.fullRB.insert(99))
    #    newResult = ''
    #    self.assertEqual(self.fullRB.outputTesting(),newResult)
    #    
    #    print("\ntestDeleteTree PASSED")
    
    def testListSort(self):
        listToSort = [x for x in range(0,101,1)]
        
        for item in listToSort:
            random.shuffle(listToSort)
            for value in listToSort:
                self.rb.insert(value)
                
            sortedList = self.rb.traverseDFSinorder()
            self.assertEqual(sortedList,[x for x in range(0,101,1)])
            self.rb.deleteTree()

        print("\ntestListSort PASSED")
    
if __name__ == '__main__':
    unittest.main()