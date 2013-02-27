#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/26/2013

# O(n log n) best/AVG case performance
# O(n^2) worst case performance - already sorted array using left-most element as pivot
# O(n) auxiliary space
# Not a stable sort
# Not in Place
# This implementation uses the middle index as the pivot

# Pick an element, called a pivot, from the list.
# Reorder the list so that all elements with values less than the pivot come
#   before the pivot, while all elements with values greater than the pivot
#   come after it
# Recursively sort the sub-list of elements with smaller values and
#   separately the sub-list of elements with greater values.

import random

def QuickSort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList
    
    pivot = unsortedList[int(len(unsortedList)/2)]
    unsortedList = unsortedList[0:int(len(unsortedList)/2)] + unsortedList[int(len(unsortedList)/2)+1:]
    less = []
    greater = []
    for x in unsortedList:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return QuickSort(less) + [pivot] + QuickSort(greater)

if __name__ == '__main__':
    empty = []
    print("Empty Result: %s\n"%(QuickSort(empty)))
    one = [1]
    print("One Element Result: %s\n"%(QuickSort(one)))
    two = [2,1]
    print("Two Element Result: %s\n"%(QuickSort(two)))
    three = [2,3,1]
    print("Three Element Result: %s\n"%(QuickSort(three)))
    
    #Positives Only
    unsortedList = [x for x in range(0,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = QuickSort(unsortedList)
    print("QuickSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Negatives Only
    unsortedList = [x for x in range(-100,0)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = QuickSort(unsortedList)
    print("QuickSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Positives and Negatives
    unsortedList = [x for x in range(-100,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = QuickSort(unsortedList)
    print("QuickSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList)) 