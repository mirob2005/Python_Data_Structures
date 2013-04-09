#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/8/2013

# Insertion Sort implementation
# Stable sort, preserve order of equal elements
# In-place sort
# Efficient for small data sets

# O(n^2) - worst/AVG case
# O(n) - best case (already sorted list)
# O(1) auxilary - worst case space complexity 

import random

def InsertionSort(unsortedList):
    if len(unsortedList) < 2:
        return unsortedList
    for index in range(1,len(unsortedList)):
        while unsortedList[index] < unsortedList[index-1]:
            temp = unsortedList[index]
            unsortedList[index] = unsortedList[index-1]
            unsortedList[index-1] = temp
            if index > 1:
                index -= 1
    return unsortedList

if __name__ == '__main__':
    empty = []
    print("Empty Result: %s\n"%(InsertionSort(empty)))
    one = [1]
    print("One Element Result: %s\n"%(InsertionSort(one)))
    two = [2,1]
    print("Two Element Result: %s\n"%(InsertionSort(two)))
    three = [2,3,1]
    print("Three Element Result: %s\n"%(InsertionSort(three)))
    
    #Positives Only
    unsortedList = [x for x in range(0,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = InsertionSort(unsortedList)
    print("InsertionSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Negatives Only
    unsortedList = [x for x in range(-100,0)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = InsertionSort(unsortedList)
    print("InsertionSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Positives and Negatives
    unsortedList = [x for x in range(-100,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = InsertionSort(unsortedList)
    print("InsertionSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList)) 