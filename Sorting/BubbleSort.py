#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/8/2013

#Simple BubbleSort implementation
# Stable sort, preserve order of equal elements
# In-place sort

# O(n^2) - worst/AVG case
# O(n) - best case (already sorted list)
# O(1) auxilary - worst case space complexity 

import random

def BubbleSort(unsortedList):
    if len(unsortedList) < 2:
        swap = False
    else:
        swap = True
    while swap:
        swap = False
        for index in range(0,len(unsortedList)-1):
            if unsortedList[index] > unsortedList[index+1]:
                temp = unsortedList[index]
                unsortedList[index] = unsortedList[index+1]
                unsortedList[index+1] = temp
                swap = True
    return unsortedList

if __name__ == '__main__':
    empty = []
    print("Empty Result: %s\n"%(BubbleSort(empty)))
    one = [1]
    print("One Element Result: %s\n"%(BubbleSort(one)))
    two = [2,1]
    print("Two Element Result: %s\n"%(BubbleSort(two)))
    three = [2,3,1]
    print("Three Element Result: %s\n"%(BubbleSort(three)))
    
    #Positives Only
    unsortedList = [x for x in range(0,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = BubbleSort(unsortedList)
    print("BubbleSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Negatives Only
    unsortedList = [x for x in range(-100,0)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = BubbleSort(unsortedList)
    print("BubbleSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList))
    
    #Positives and Negatives
    unsortedList = [x for x in range(-100,101)]
    random.shuffle(unsortedList)
    
    print("UnsortedList: %s\n"%unsortedList)
    sortedList = BubbleSort(unsortedList)
    print("BubbleSort Returned: %s\n"%sortedList)
    
    unsortedList.sort()
    print("Using list.sort() returned: %s\n"%unsortedList)
    
    print("Sorted?: %s\n\n"%(unsortedList==sortedList)) 