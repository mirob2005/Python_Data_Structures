#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/5/2013

from HashTable import HashTable

class TestHashTable(unittest.TestCase):
    
    def setUp(self):
        self.empty = HashTable(100)
        self.oneBucket = HashTable(1)
        self.tenBuckets = HashTable(10)
        self.hundredBuckets = HashTable(100)
    
    def testEmpty(self):
        pass
    
    def testAdd(self):
        pass
    
    def testDelete(self):
        pass
    
    def testLookUp(self):
        pass
    
    def testUpdate(self):
        pass

    def testHashing(self):
        pass
        
if __name__ == '__main__':
    unittest.main()