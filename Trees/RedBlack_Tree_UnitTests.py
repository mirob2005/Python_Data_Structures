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
        self.result = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        
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
        
        self.assertTrue(self.rb.insert(12))
        string = '(NoneB)<-30B->(6B,47B)\n'\
                 '(30B)<-6B->(2R,12R)\n'\
                 '(30B)<-47B->(NoneB,NoneB)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(64))
        string = '(NoneB)<-30B->(6B,47B)\n'\
                 '(30B)<-6B->(2R,12R)\n'\
                 '(30B)<-47B->(NoneB,64R)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(47B)<-64R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(62))
        string = '(NoneB)<-30B->(6B,62B)\n'\
                 '(30B)<-6B->(2R,12R)\n'\
                 '(30B)<-62B->(47R,64R)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(62B)<-47R->(NoneB,NoneB)\n'\
                 '(62B)<-64R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(98))
        string = '(NoneB)<-30B->(6B,62R)\n'\
                 '(30B)<-6B->(2R,12R)\n'\
                 '(30B)<-62R->(47B,64B)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(62R)<-47B->(NoneB,NoneB)\n'\
                 '(62R)<-64B->(NoneB,98R)\n'\
                 '(64B)<-98R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(93))
        string = '(NoneB)<-30B->(6B,62R)\n'\
                 '(30B)<-6B->(2R,12R)\n'\
                 '(30B)<-62R->(47B,93B)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(62R)<-47B->(NoneB,NoneB)\n'\
                 '(62R)<-93B->(64R,98R)\n'\
                 '(93B)<-64R->(NoneB,NoneB)\n'\
                 '(93B)<-98R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(95))
        string = '(NoneB)<-62B->(30R,93R)\n'\
                 '(62B)<-30R->(6B,47B)\n'\
                 '(62B)<-93R->(64B,98B)\n'\
                 '(30R)<-6B->(2R,12R)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(93R)<-64B->(NoneB,NoneB)\n'\
                 '(93R)<-98B->(95R,NoneB)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(98B)<-95R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(97))
        string = '(NoneB)<-62B->(30R,93R)\n'\
                 '(62B)<-30R->(6B,47B)\n'\
                 '(62B)<-93R->(64B,97B)\n'\
                 '(30R)<-6B->(2R,12R)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(93R)<-64B->(NoneB,NoneB)\n'\
                 '(93R)<-97B->(95R,98R)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(97B)<-95R->(NoneB,NoneB)\n'\
                 '(97B)<-98R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(99))
        string = '(NoneB)<-62B->(30B,93B)\n'\
                 '(62B)<-30B->(6B,47B)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(30B)<-6B->(2R,12R)\n'\
                 '(30B)<-47B->(NoneB,NoneB)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(6B)<-2R->(NoneB,NoneB)\n'\
                 '(6B)<-12R->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(3))
        string = '(NoneB)<-62B->(30B,93B)\n'\
                 '(62B)<-30B->(6R,47B)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(30B)<-6R->(2B,12B)\n'\
                 '(30B)<-47B->(NoneB,NoneB)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(6R)<-2B->(NoneB,3R)\n'\
                 '(6R)<-12B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(2B)<-3R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(4))
        string = '(NoneB)<-62B->(30B,93B)\n'\
                 '(62B)<-30B->(6R,47B)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(30B)<-6R->(3B,12B)\n'\
                 '(30B)<-47B->(NoneB,NoneB)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(6R)<-3B->(2R,4R)\n'\
                 '(6R)<-12B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(3B)<-2R->(NoneB,NoneB)\n'\
                 '(3B)<-4R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(5))
        string = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(NoneB,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        self.assertTrue(self.rb.insert(7))
        string = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        self.assertEqual(self.rb.outputTesting(),string)
        
        print('\ntextInsert PASSED')
        
    def testDFSorder(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        keys = [62,6,3,2,4,5,30,12,7,47,93,64,97,95,98,99]
        self.assertEqual(self.fullRB.traverseDFSpreorder(),keys)
    
        self.insertList.sort(reverse=False)
        self.assertEqual(self.fullRB.traverseDFSinorder(),self.insertList)
        
        keys = [2,5,4,3,7,12,47,30,6,64,95,99,98,97,93,62]
        self.assertEqual(self.fullRB.traverseDFSpostorder(),keys)
        
        print("\ntestDFS(pre&in&post)order PASSED")
    
    def testFind(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        random.shuffle(self.insertList)
        for item in self.insertList:
            self.assertTrue(self.fullRB.find(item))
        
        #FAIL FIND
        failFinds = [x for x in range(0,101)]
        for item in self.insertList:
            if item in failFinds:
                failFinds.remove(item)
        for item in failFinds:
            self.assertFalse(self.fullRB.find(item))
    
        print("\ntestFind PASSED")
        
    def testDuplicateInsert(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        #Duplicate Insert should fail and NOT change the output
        for item in self.insertList:
            self.assertFalse(self.fullRB.insert(item))
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        print("\ntestDuplicateInsert PASSED")
        
    def testCopy(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        copy = self.fullRB.copyTree()
        self.assertEqual(copy.outputTesting(),self.result)
        
        self.assertTrue(self.fullRB.insert(1))
        self.assertTrue(copy.insert(0))
        
        #fullRB after inserting 1
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(1R,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(2B)<-1R->(NoneB,NoneB)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        #The copy after inserting 0
        newCopy = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(0R,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(2B)<-0R->(NoneB,NoneB)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        self.assertEqual(copy.outputTesting(),newCopy)
        print("\ntestCopy PASSED")
    
    def testFindMin(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        #Find Min
        self.assertEqual(self.fullRB.findMin(),2)
        
        #Insert New Min
        self.assertTrue(self.fullRB.insert(0))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(0R,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,99R)\n'\
                 '(2B)<-0R->(NoneB,NoneB)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'\
                 '(98B)<-99R->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Find New Min
        self.assertEqual(self.fullRB.findMin(),0)
    
        print("\ntestFindMin PASSED")
        
    def testFindMax(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        #Find Max
        self.assertEqual(self.fullRB.findMax(),99)
        
        #Insert New Max
        self.assertTrue(self.fullRB.insert(100))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,99B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-99B->(98R,100R)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'\
                 '(99B)<-98R->(NoneB,NoneB)\n'\
                 '(99B)<-100R->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Find New Max
        self.assertEqual(self.fullRB.findMax(),100)
        
        print("\ntestFindMax PASSED")
        
    def testDeleteLeaf(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        #Delete does not require rotations or color changes
        self.assertTrue(self.fullRB.delete(99))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,NoneB)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Delete does not require rotations or color changes
        self.assertTrue(self.fullRB.delete(7))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(NoneB,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,NoneB)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Delete requires rotation and color changes
        self.assertTrue(self.fullRB.delete(2))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(4R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-4R->(3B,5B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(4R)<-3B->(NoneB,NoneB)\n'\
                 '(4R)<-5B->(NoneB,NoneB)\n'\
                 '(30R)<-12B->(NoneB,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Delete requires color changes
        self.assertTrue(self.fullRB.delete(5))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(4R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-4B->(3R,NoneB)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(4B)<-3R->(NoneB,NoneB)\n'\
                 '(30R)<-12B->(NoneB,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Delete requires color changes
        self.assertTrue(self.fullRB.delete(12))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(4R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-4B->(3R,NoneB)\n'\
                 '(6B)<-30B->(NoneB,47R)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(4B)<-3R->(NoneB,NoneB)\n'\
                 '(30B)<-47R->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        print("\ntestDeleteLeaf PASSED")
        
    def testDeleteFail(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        #FAIL DELETES (keys not present)
        failDeletes = [x for x in range(0,101)]
        for item in self.insertList:
            if item in failDeletes:
                failDeletes.remove(item)
        for item in failDeletes:
            self.assertFalse(self.fullRB.delete(item))
            
        #Check to make sure tree was not changed
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        #Successfully delete 99
        self.assertTrue(self.fullRB.delete(99))
        newResult = '(NoneB)<-62B->(6B,93B)\n'\
                 '(62B)<-6B->(3R,30R)\n'\
                 '(62B)<-93B->(64B,97R)\n'\
                 '(6B)<-3R->(2B,4B)\n'\
                 '(6B)<-30R->(12B,47B)\n'\
                 '(93B)<-64B->(NoneB,NoneB)\n'\
                 '(93B)<-97R->(95B,98B)\n'\
                 '(3R)<-2B->(NoneB,NoneB)\n'\
                 '(3R)<-4B->(NoneB,5R)\n'\
                 '(30R)<-12B->(7R,NoneB)\n'\
                 '(30R)<-47B->(NoneB,NoneB)\n'\
                 '(97R)<-95B->(NoneB,NoneB)\n'\
                 '(97R)<-98B->(NoneB,NoneB)\n'\
                 '(4B)<-5R->(NoneB,NoneB)\n'\
                 '(12B)<-7R->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        #Try to delete 99 again
        self.assertFalse(self.fullRB.delete(99))
        
        #Check to make sure tree was not changed
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        print("\ntestDeleteFail PASSED")
    
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
    
    def testDeleteTree(self):
        self.assertEqual(self.fullRB.outputTesting(),self.result)
        
        self.fullRB.deleteTree()
        newResult = '(Empty)'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
    
        for item in range(0,101):
            self.assertFalse(self.fullRB.delete(item))
            self.assertFalse(self.fullRB.find(item))
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        self.assertTrue(self.fullRB.insert(99))
        newResult = '(NoneB)<-99B->(NoneB,NoneB)\n'
        self.assertEqual(self.fullRB.outputTesting(),newResult)
        
        print("\ntestDeleteTree PASSED")
    
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