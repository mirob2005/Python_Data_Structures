#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/19/2013

from Trie import Trie
import unittest

class TestBST(unittest.TestCase):
    
    def setUp(self):
        self.empty = Trie()
        self.t = Trie()
        
        self.t.add('bob',2)
        self.t.add('apple', 3)
        
    def testEmpty(self):
        words = self.empty.traverseWords()
        
        self.assertEqual(words,'Empty')
        
        print('\ntestEmpty PASSED')
    
    def testInsert(self):
        self.empty.add('bob',2)
        words = self.empty.traverseWords()
        self.assertEqual(words,'bob')
        
        self.empty.add('apple', 3)
        words = self.empty.traverseWords()
        self.assertEqual(words,'bob apple')
        
        print('\ntestInsert PASSED')
    
    def testIsMember(self):
        result = self.t.isMember('bob') and self.t.isMember('apple')
        self.assertTrue(result)
        
        result = self.t.isMember('bo') or self.t.isMember('bobo') or self.t.isMember('ap') or \
        self.t.isMember('dave')
        self.assertFalse(result)
        
        print('\ntestIsMember PASSED')
    
    def testRemove(self):
        pass
    
    def testUpdateValue(self):
        result = self.t.updateValue('bob',10)
        self.assertTrue(result)
        checkValue = self.t.getValue('bob')
        self.assertEqual(checkValue, 10)
        
        result = self.t.updateValue('apple',12)
        self.assertTrue(result)
        checkValue = self.t.getValue('apple')
        self.assertEqual(checkValue, 12)
        
        result = self.t.updateValue('app',1)
        self.assertTrue(result)
        checkValue = self.t.getValue('app')
        self.assertEqual(checkValue, 1)
        
        result = self.t.updateValue('dave',12)
        self.assertFalse(result)
        checkValue = self.t.getValue('dave')
        self.assertEqual(checkValue, None)
        
        print('\ntestUpdateValue PASSED')
    
    def testGetValue(self):
        result = self.t.getValue('bob')
        self.assertEqual(result, 2)
        
        result = self.t.getValue('apple')
        self.assertEqual(result, 3)
        
        result = self.t.getValue('bo')
        self.assertEqual(result, None)
        
        result = self.t.getValue('dave')
        self.assertEqual(result, None)
        
        print('\ntestGetValue PASSED')
    
if __name__ == '__main__':
    unittest.main()