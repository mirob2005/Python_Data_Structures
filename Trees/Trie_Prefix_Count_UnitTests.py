#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/3/2013

from Trie_Prefix_Count import Trie
import unittest

class TestPrefixTrie(unittest.TestCase):
    
    def setUp(self):
        self.empty = Trie()
        self.t = Trie()
        
        self.t.add('bob')
        self.t.add('apple')
        
    def testEmpty(self):
        words = self.empty.traversePrefixes()
        
        self.assertEqual(words,'Empty')
        
        print('\ntestEmpty PASSED')
    
    def testInsert(self):
        self.empty.add('bob')
        words = self.empty.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1)')
        
        self.empty.add('apple')
        words = self.empty.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1), a (1), ap (1), app (1), '\
                         'appl (1), apple (1)')
        
        print('\ntestInsert PASSED')
    
    def testIsMember(self):
        result = self.t.isMember('bob') and self.t.isMember('apple')
        self.assertTrue(result)
        
        result = self.t.isMember('bab') or self.t.isMember('bobo') or \
            self.t.isMember('apples') or self.t.isMember('dave')
        self.assertFalse(result)
        
        print('\ntestIsMember PASSED')
        
    def testCommonPrefix(self):
        self.t.add('at')
        words = self.t.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1), a (2), ap (1), app (1), appl (1), '\
                         'apple (1), at (1)')
        result = self.t.getValue('at')
        self.assertEqual(result, 1)
        result = self.t.isMember('at')
        self.assertTrue(result)
        
        self.t.add('ate')
        result = self.t.getValue('ate')
        self.assertEqual(result, 1)
        result = self.t.isMember('ate')
        self.assertTrue(result)
        
        result = self.t.getValue('at')
        self.assertEqual(result, 2)
        result = self.t.isMember('at')
        self.assertTrue(result)
        
        words = self.t.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1), a (3), ap (1), app (1), appl (1), '\
                         'apple (1), at (2), ate (1)')
        
        self.t.remove('at')
        words = self.t.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1), a (2), ap (1), app (1), appl (1), '\
                         'apple (1), at (1), ate (1)')
        
        result = self.t.isMember('at')
        self.assertFalse(result)
        self.assertEqual(self.t.getValue('at'),1)
        
        result = self.t.isMember('ate')
        self.assertTrue(result)
        self.assertEqual(self.t.getValue('ate'),1)
        
        self.t.add('at')
        result = self.t.getValue('at')
        self.assertEqual(result, 2)
        result = self.t.isMember('at')
        self.assertTrue(result)
        
        words = self.t.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1), a (3), ap (1), app (1), appl (1), '\
                         'apple (1), at (2), ate (1)')
        
        self.t.remove('ate')
        words = self.t.traversePrefixes()
        self.assertEqual(words,'b (1), bo (1), bob (1), a (2), ap (1), app (1), appl (1), '\
                         'apple (1), at (1)')
        
        result = self.t.isMember('at')
        self.assertTrue(result)
        self.assertEqual(self.t.getValue('at'),1)
        
        result = self.t.isMember('ate')
        self.assertFalse(result)
        self.assertEqual(self.t.getValue('ate'),None)
        
        print('\ntestCommonPrefix PASSED')
    
    def testRemove(self):
        self.t.add('add')
        result = self.t.isMember('add')
        self.assertTrue(result)
        
        result = self.t.traversePrefixes()
        self.assertEqual(result, 'b (1), bo (1), bob (1), a (2), ap (1), app (1), appl (1), '\
                         'apple (1), ad (1), add (1)')
        
        boolResult = self.t.remove('apple')
        self.assertTrue(boolResult)
        result = self.t.traversePrefixes()
        self.assertEqual(result, 'b (1), bo (1), bob (1), a (1), ad (1), add (1)')
        
        boolResult = self.t.remove('add')
        self.assertTrue(boolResult)
        result = self.t.traversePrefixes()
        self.assertEqual(result, 'b (1), bo (1), bob (1)')
        
        boolResult = self.t.remove('bob')
        self.assertTrue(boolResult)
        result = self.t.traversePrefixes()
        self.assertEqual(result, 'Empty')
        
        print('\ntestRemove PASSED')
    
    def testGetValue(self):
        result = self.t.getValue('bob')
        self.assertEqual(result, 1)
        
        result = self.t.getValue('apple')
        self.assertEqual(result, 1)
        
        result = self.t.getValue('bo')
        self.assertEqual(result, 1)
        
        result = self.t.getValue('dave')
        self.assertEqual(result, None)
        
        print('\ntestGetValue PASSED')
    
if __name__ == '__main__':
    unittest.main()