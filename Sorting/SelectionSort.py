#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/9/2013

# Selection Sort implementation
# Stable sort, preserve order of equal elements
# In-place sort
# Efficient for small data sets

# O(n^2) - worst/AVG/best case
# O(1) auxilary - worst case space complexity 

import random

def SelectionSort(unsortedList):
    if len(unsortedList) < 2:
        return unsortedList
    for index in range(0,len(unsortedList)-1):
        minValue = float('inf')
        swapIndex = None
        for current in range(index,len(unsortedList)):
            if unsortedList[current] < minValue:
                minValue = unsortedList[current]
                swapIndex = current
        temp = unsortedList[index]
        unsortedList[index] = minValue
        unsortedList[swapIndex] = temp
    return unsortedList

if __name__ == '__main__':
    empty = []
    print("Empty Result: %s\n"%(SelectionSort(empty)))
    one = [1]
    print("One Element Result: %s\n"%(SelectionSort(one)))
    two = [2,1]
    print("Two Element Result: %s\n"%(SelectionSort(two)))
    three = [2,3,1]
    print("Three Element Result: %s\n"%(SelectionSort(three)))
    
    #Positives Only
    unsortedList = [x for x in range(0,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = SelectionSort(unsortedList)
    print("SelectionSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Negatives Only
    unsortedList = [x for x in range(-100,0)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = SelectionSort(unsortedList)
    print("SelectionSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Positives and Negatives
    unsortedList = [x for x in range(-100,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = SelectionSort(unsortedList)
    print("SelectionSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList)) 