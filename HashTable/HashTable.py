#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/7/2013

#Hash Table is built using a list of buckets, initialized to None
#When an entry is added to a given bucket, the bucket stores the entries in a list
#The bucket used is decided using the defined 'hash' method which returns an index
#   based off a hashing value modulo number of buckets in the hash table defined at
#   object initialization.
#The hashing value is calculated as follows:
#   ord(character)-32*95^placement
#   ord returns the decimal value of the ASCII character
#The printable ASCII chars are decimal 32 to 126, by subtracting 32 we get: 0 to 94
#Example: key  = 'test'
#ord('t')-32 = 84 *95 ^0 = 84
#ord('e')-32 = 69 *95 ^1 = 6555
#ord('s')-32 = 83 *95 ^2 = 749075
#ord('t')-32 = 84 *95 ^3 = 72019500
#Hashing Value = 72019500 + 749075 + 6555 + 84 = 72775214
#Index = Hashing Value % numBuckets

#Results in a unique hashing value for any key


class Entry:
    def __init__(self,key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self,numBuckets):
        if type(numBuckets) != int or numBuckets < 0:
            numBuckets = 1
        self.numBuckets = numBuckets
        self.buckets = [None for x in range(0,self.numBuckets)]
        
    def __str__(self):
        string = '{'
        for bucket in self.buckets:
            if bucket != None:
                for entry in bucket:
                    if type(entry.key) ==str:
                        string += ("'%s': "%entry.key)
                    else:
                        string += ("%s: "%entry.key)
                    if type(entry.value) ==str:
                        string += ("'%s', "%entry.value)
                    else:
                        string += ("%s, "%entry.value)
        return string.rstrip(', ') + "}"
    
    def hash(self,key):
        if not key:
            return None
        power = 0
        hashing = 0
        for char in key:
            hashing += (ord(char)-32)*pow(95,power)
            power += 1
        index = hashing % self.numBuckets
        return index
    
    def add(self,key,value):
        index = self.hash(str(key))
        if index < 0 or index > self.numBuckets:
            return False
        if self.buckets[index] == None:
            self.buckets[index] = [Entry(key,value)]
            return True
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    entry.value = value
                    return True
            self.buckets[index].append(Entry(key,value))
            return True
    
    def updateValue(self,key,value):
        index = self.hash(str(key))
        if index == None:
            return False
        if self.buckets[index] == None:
            #print("Key Not Found!")
            return False
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    entry.value = value
                    return True
            #print("Key Not Found!")
            return False
    
    def delete(self,key):
        index = self.hash(str(key))
        if index == None:
            return False
        if self.buckets[index] == None:
            #print("Key Not Found!")
            return False
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    self.buckets[index].remove(entry)
                    return True
            #print("Key Not Found!")
            return False
    
    def lookUp(self,key):
        index = self.hash(str(key))
        if index == None:
            return False
        if self.buckets[index] == None:
            #print("Key Not Found!")
            return False
        else:
            for entry in self.buckets[index]:
                if entry.key == key:
                    return entry.value
            #print("Key Not Found!")
            return False
        
    def printDistribution(self):
        string = ''
        bucketNum = 0
        MIN = None
        MAX = 0
        TOTAL = 0
        for bucket in self.buckets:
            if bucket != None:
                #string += ("Bucket Number %d has: "%bucketNum)
                count = 0
                for entry in bucket:
                    count += 1
                #string += ("%d entries\n"%count)
                TOTAL += count
                if count > MAX:
                    MAX = count
                if MIN == None or count < MIN:
                    MIN = count
            else:
                pass
                #string += ("Bucket Number %d has 0 entries\n"%(bucketNum))
            bucketNum +=1
        string += ("Largest Bucket has %d entries\n"\
                       "Smallest Bucket has %d entries\nTotal entries: %d\n"\
                       "Avg bucket size is %f"%(MAX,MIN,TOTAL,(TOTAL/self.numBuckets)))
        return string
    
if __name__ == '__main__':
    ht = HashTable(100)
    
    print(ht)
    
    ht.add('bob',2)
    ht.add(11,3)
    ht.add('11',4)
    
    ht.add(' ',5)
    print(ht)
    
    print()
    print(ht.lookUp(11))
    #print(ht.printDistribution())