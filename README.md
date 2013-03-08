Python Data Structures
======================
### Lorem_ipsum.txt included for testing and timing purposes.
### Currently used to test Tries and Hash Table

## *ADTS:*
- Queue with head and tail ptr, insert new at head, remove old at tail
- Queue with only head ptr, remove old at head, append new to the end
- Stack (push/pop at head)
- Priority Queue (uses an array-based Binary Heap)

## *Linked List Operations:*
- insert
- append
- returnIndex
- updateIndex
- deleteIndex
- insertBeforeIndex
- insertAfterIndex
- deleteData
- deleteAllData
- insertAfterEveryData
- insertBeforeEveryData
- deleteList
- copyList
- findMthToLastNode

### *Types:*
- Single LL with head pointer
- Double LL with head pointer
- Circular LL with head & tail pointers

Unit Tests to test all 3 types and each operation

## *Binary Search Tree Operations:*
- insert
- insertList
- find
- delete
- traverseBFS
- traverseDFSpreorder
- traverseDFSinorder
- traverseDFSpostorder
- copyTree
- findMin
- findMax

### *Types:*
- Iterative (uses Queue(head ptr) and Stack for traversals)
- Recursive (inherits from iterative approach, reimplements insert,find,delete,DFS,findMin,findMax)

Unit Tests to test each operation for both types

## *Binary Heap Operations:*
- traverseBFS
- insert (with heapifyUp to ensure heap property)
- insertList
- delete (with heapifyDown to ensure heap property)
- merge (2 heaps -> 1 heap)
- peek (get max value)
- copyHeap

### *Types:*
- Tree Structure (uses ptrs)
- Array Structure (no ptrs needed)

Units Tests to test each operation and to ensure proper tracking
of next insert/delete location to ensure shape property

## *Trie Operations:*
- traverse(Words|Prefixes) - Outputs words for generic type or all prefixes for prefix count versions
- traverseBFS
- add
- remove
- isMember (full words or prefixes specifically added)
- updateValue (Generic type only)
- getValue

### *Types:*
- Generic - allows adding words with a corresponding value, all prefix node values are None
- Prefix Count - user only adds words, values correspond to number of times that prefix is used
- Prefix Count Speed - Same as above, but using more space to allow for faster indexing

Unit tests to test each operation for all 3 types

## *Sorting:*
### Selection Sorts:
- HeapSort - uses an array-based binary heap, in-place sort, not stable,
    O(n) best case, O(n log n) AVG/worst case performance, O(1) auxiliary space

### Merge Sorts:
- MergeSort - not in place, stable sort, O(n log n) best/AVG/worst case performance,
    O(n) auxiliary space

### Exchange Sorts:
- QuickSort - not in place, not stable, O(n log n) best/AVG, O(n^2) worst case
    performance, O(n) auxiliary space, fastest on average

Tested using language provided sort method to compare the result on a random.shuffle() list

## *Hash Table Operations:*
- add
- updateValue
- delete
- lookUp
- hash

### *Types:*
- Separate Chaining Collision resolution
Unit tests to test each operation

## *TODO:*
- Self-balancing BST - Red-Black Tree, Splay Tree, AVL Tree
- Graphs (various types), impl. objects/ptrs, adjacency L/M, incidence L/M
