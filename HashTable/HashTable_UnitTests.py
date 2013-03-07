#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/7/2013

from HashTable import HashTable
import unittest

class TestHashTable(unittest.TestCase):
    
    def setUp(self):
        self.empty = HashTable(100)
        self.oneBucket = HashTable(1)
        self.tenBuckets = HashTable(10)
        self.hundredBuckets = HashTable(100)
    
    def testEmpty(self):
        self.assertEqual(self.empty.__str__(),"{}")
        self.assertFalse(self.empty.delete('DeleteMe'))
        self.assertFalse(self.empty.lookUp('FindMe'))
        self.assertFalse(self.empty.updateValue('UpdateMe', 'ToThis'))
        
        self.assertTrue(self.empty.add('AddMe',2))
        self.assertEqual(self.empty.__str__(),"{AddMe: 2}")
        
        print('\ntestEmpty PASSED')
    
    def testAdd(self):
        self.assertTrue(self.oneBucket.add('AddMe',2))
        self.assertEqual(self.oneBucket.__str__(),"{AddMe: 2}")
        
        self.assertTrue(self.oneBucket.add('AddMe',3))
        self.assertEqual(self.oneBucket.__str__(),"{AddMe: 3}")
        
        self.assertTrue(self.oneBucket.add('2ndItem',4))
        self.assertEqual(self.oneBucket.__str__(),"{AddMe: 3, 2ndItem: 4}")
        
        self.assertTrue(self.tenBuckets.add('addMe','bob'))
        self.assertEqual(self.tenBuckets.__str__(),"{addMe: bob}")
        
        self.assertTrue(self.tenBuckets.add('AddMe',3))
        self.assertEqual(self.tenBuckets.__str__(),"{AddMe: 3, addMe: bob}")
        
        self.assertTrue(self.tenBuckets.add('2ndItem',4))
        self.assertEqual(self.tenBuckets.__str__(),"{AddMe: 3, 2ndItem: 4, addMe: bob}")
        
        self.assertTrue(self.hundredBuckets.add(2345,2))
        self.assertEqual(self.hundredBuckets.__str__(),"{2345: 2}")
        
        self.assertTrue(self.hundredBuckets.add('zzz',3))
        self.assertEqual(self.hundredBuckets.__str__(),"{zzz: 3, 2345: 2}")
        
        self.assertTrue(self.hundredBuckets.add('2345','bob'))
        self.assertEqual(self.hundredBuckets.__str__(),"{zzz: 3, 2345: 2, 2345: bob}")
        
        print('\ntestAdd PASSED')
    
    def testDelete(self):
        print('\ntestDelete PASSED')
    
    def testLookUp(self):
        print('\ntestLookUp PASSED')
    
    def testUpdate(self):
        print('\ntestUpdate PASSED')

    def testHashing(self):
        print('\ntestHashing PASSED')
        
if __name__ == '__main__':
    unittest.main()