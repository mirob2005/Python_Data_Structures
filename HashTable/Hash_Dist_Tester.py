#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/5/2013

#Distribution:
#100 Buckets
#LOW:    507 entries
#HIGH:   3715 entries
#TOTAL: 147644 entries
#Load Factor:   1476.44 entries per bucket
#Time to ADD ALL: 55.77 seconds


#1,000 Buckets
#LOW:    36 entries
#HIGH:   413 entries
#TOTAL: 147644 entries
#Load Factor:   147.644 entries per bucket
#Time to ADD ALL: 6.49 seconds

#10,000 Buckets
#LOW:    1 entries
#HIGH:   59 entries
#TOTAL: 147644 entries
#Load Factor:   14.7644 entries per bucket
#Time to ADD ALL: 3.98 seconds

#100,000 Buckets
#LOW:    1 entries
#HIGH:   12 entries
#TOTAL: 147644 entries
#Load Factor:   1.47644 entries per bucket
#Time to ADD ALL: 3.84 seconds

import time
from HashTable import HashTable

fileIn = open('../Lorem_ipsum.txt','r').read()
words = fileIn.split(' ')

start1 = time.clock()
print("HashTable(100) start time:%f"%start1)
ht = HashTable(100)

wordCount = 0
for word in words:
    ht.add(str(wordCount)+word, wordCount)
    wordCount += 1
add1 = time.clock()
print("HashTable(100) add time:%f\n"%(add1-start1))
    
print(ht.printDistribution())

print('\n')

start2 = time.clock()
print("HashTable(1000) start time:%f"%start2)
ht2 = HashTable(1000)

wordCount = 0
for word in words:
    ht2.add(str(wordCount)+word, wordCount)
    wordCount += 1
add2 = time.clock()
print("HashTable(1000) add time:%f"%(add2-start2))
print(ht2.printDistribution())

print('\n')

start3 = time.clock()
print("HashTable(10000) start time:%f"%start3)
ht3 = HashTable(10000)

wordCount = 0
for word in words:
    ht3.add(str(wordCount)+word, wordCount)
    wordCount += 1
add3 = time.clock()
print("HashTable(10000) add time:%f"%(add3-start3))
print(ht3.printDistribution())

print('\n')

start4 = time.clock()
print("HashTable(100000) start time:%f"%start4)
ht4 = HashTable(100000)

wordCount = 0
for word in words:
    ht4.add(str(wordCount)+word, wordCount)
    wordCount += 1
add4 = time.clock()
print("HashTable(100000) add time:%f"%(add4-start4))
print(ht4.printDistribution())