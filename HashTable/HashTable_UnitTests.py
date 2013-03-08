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
        
        self.hashes = [[self.oneBucket,'One Bucket'], [self.tenBuckets,'Ten Buckets'], [self.hundredBuckets,'100 Buckets']]
    
    def testEmpty(self):
        self.assertEqual(self.empty.__str__(),"{}")
        self.assertFalse(self.empty.delete('DeleteMe'))
        self.assertFalse(self.empty.lookUp('FindMe'))
        self.assertFalse(self.empty.updateValue('UpdateMe', 'ToThis'))
        
        self.assertTrue(self.empty.add('AddMe',2))
        self.assertEqual(self.empty.__str__(),"{'AddMe': 2}")
        
        print('\ntestEmpty PASSED')
    
    def testAdd(self):
        for ht,name in self.hashes:
            self.assertTrue(ht.add('AddMe',2))
            self.assertEqual(ht.__str__(),"{'AddMe': 2}")
            
            self.assertTrue(ht.add('AddMe',3))
            self.assertEqual(ht.__str__(),"{'AddMe': 3}")
            
            self.assertTrue(ht.add('2ndItem',4))
            expResult1 = "\{'AddMe': 3, '2ndItem': 4\}"
            expResult2= "\{'2ndItem': 4, 'AddMe': 3\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
        
            print('\ntestAdd on %s PASSED'%name)
    
    def testDelete(self):
        for ht,name in self.hashes:
            self.assertTrue(ht.add('AddMe',2))
            self.assertEqual(ht.__str__(),"{'AddMe': 2}")
            
            self.assertTrue(ht.add('AddMe',3))
            self.assertEqual(ht.__str__(),"{'AddMe': 3}")
            
            self.assertTrue(ht.add('2ndItem',4))
            expResult1 = "\{'AddMe': 3, '2ndItem': 4\}"
            expResult2= "\{'2ndItem': 4, 'AddMe': 3\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            
            self.assertTrue(ht.delete('AddMe'))
            self.assertEqual(ht.__str__(),"{'2ndItem': 4}")
            
            self.assertFalse(ht.delete('AddMe'))
            self.assertTrue(ht.delete('2ndItem'))
            
            self.assertEqual(ht.__str__(),"{}")
        
            print('\ntestDelete on %s PASSED'%name)
    
    def testLookUp(self):
        for ht,name in self.hashes:
            self.assertTrue(ht.add('AddMe',3))
            self.assertEqual(ht.__str__(),"{'AddMe': 3}")
            
            self.assertTrue(ht.add('2ndItem',4))
            expResult1 = "\{'AddMe': 3, '2ndItem': 4\}"
            expResult2= "\{'2ndItem': 4, 'AddMe': 3\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            
            self.assertEqual(ht.lookUp('AddMe'), 3)
            self.assertEqual(ht.lookUp('2ndItem'), 4)
            
            self.assertFalse(ht.lookUp('missing'))
        
            print('\ntestLookUp on %s PASSED'%name)
    
    def testUpdate(self):
        for ht,name in self.hashes:
            self.assertTrue(ht.add('AddMe',3))
            self.assertEqual(ht.__str__(),"{'AddMe': 3}")
            
            self.assertTrue(ht.add('2ndItem',4))
            expResult1 = "\{'AddMe': 3, '2ndItem': 4\}"
            expResult2= "\{'2ndItem': 4, 'AddMe': 3\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            
            self.assertTrue(ht.updateValue('AddMe', 4))
            expResult1 = "\{'AddMe': 4, '2ndItem': 4\}"
            expResult2= "\{'2ndItem': 4, 'AddMe': 4\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            
            self.assertFalse(ht.updateValue('missing',4))
            
            print('\ntestUpdate on %s PASSED'%name)

    def testHashing(self):
        key = 'test'
        hashing = (ord('t')-32) + (ord('e')-32)*95 + (ord('s')-32)*95*95 + (ord('t')-32)*95*95*95
        self.assertEqual(hashing, 72775214)
        self.assertEqual(hashing%1, 0)
        self.assertEqual(hashing%10, 4)
        self.assertEqual(hashing%100, 14)
        
        key2 = '~ '
        hashing2 = (ord('~')-32) + (ord(' ')-32)*95
        self.assertEqual(hashing2, 94)
        for ht,name in self.hashes:
            self.assertEqual(ht.hash(''), None)
            self.assertEqual(ht.hash(key), hashing%ht.numBuckets)
            self.assertEqual(ht.hash(key2), hashing2%ht.numBuckets)
            
            print('\ntestHashing on %s PASSED'%name)
            
    def testKeyType(self):
        for ht,name in self.hashes:
            self.assertTrue(ht.add('11','2'))
            self.assertEqual(ht.__str__(),"{'11': '2'}")
            
            self.assertTrue(ht.add(11,3))
            expResult1 = "\{'11': '2', 11: 3\}"
            expResult2= "\{11: 3, '11': '2'\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            
            self.assertEqual(ht.lookUp('11'),'2')
            self.assertEqual(ht.lookUp(11),3)
            
            self.assertTrue(ht.updateValue('11',2))
            expResult1 = "\{'11': 2, 11: 3\}"
            expResult2= "\{11: 3, '11': 2\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            self.assertEqual(ht.lookUp('11'),2)
            
            self.assertTrue(ht.updateValue(11,'3'))
            expResult1 = "\{'11': 2, 11: '3'\}"
            expResult2= "\{11: '3', '11': 2\}"
            self.assertRegex(ht.__str__(), ('%s|%s' %(expResult1,expResult2)))
            self.assertEqual(ht.lookUp(11),'3')
            
            self.assertTrue(ht.delete(11))
            self.assertEqual(ht.__str__(),"{'11': 2}")
            
            self.assertFalse(ht.delete(11))
            
            self.assertTrue(ht.delete('11'))
            self.assertEqual(ht.__str__(),"{}")
            print('\ntestKeyType on %s PASSED'%name)
        
if __name__ == '__main__':
    unittest.main()