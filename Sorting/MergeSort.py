#Michael Robertson
#mirob2005@gmail.com
#Completed: 2/26/2013

# O(n log n) best/AVG/worst running time to sort.
# O(n) auxiliary space
# Stable sort, preserve order of equal elements
# Not in-place
# More efficient at handling slow-to-access sequential media
# Good for sorting a Linked List

# Divide the unsorted list into n sublists, each containing 1 element
# Repeatedly merge sublists to produce new sublists until there is only 1 sublist
#   remaining. This will be the sorted list.

import random

def MergeSort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList
    
    left = []
    right = []
    
    left = unsortedList[0:int(len(unsortedList)/2)]
    right = unsortedList[int(len(unsortedList)/2):]
    
    left = MergeSort(left)
    right = MergeSort(right)
    
    return Merge(left,right)

def Merge(left, right):
    result = []
    
    while len(left) > 0 or len(right) > 0:
        if len(left) == 0:
            for data in right:
                result.append(data)
            break
        elif len(right) == 0:
            for data in left:
                result.append(data)
            break
        else:
            if right[0] < left[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
    return result

if __name__ == '__main__':
    empty = []
    print("Empty Result: %s\n"%(MergeSort(empty)))
    one = [1]
    print("One Element Result: %s\n"%(MergeSort(one)))
    two = [2,1]
    print("Two Element Result: %s\n"%(MergeSort(two)))
    three = [2,3,1]
    print("Three Element Result: %s\n"%(MergeSort(three)))
    
    #Positives Only
    unsortedList = [x for x in range(0,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = MergeSort(unsortedList)
    print("MergeSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Negatives Only
    unsortedList = [x for x in range(-100,0)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = MergeSort(unsortedList)
    print("MergeSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Positives and Negatives
    unsortedList = [x for x in range(-100,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = MergeSort(unsortedList)
    print("MergeSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList)) 