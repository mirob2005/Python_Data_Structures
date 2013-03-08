# *Trees:*
## *Binary Search Tree:*
### *Operations:*
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

## *Binary Heap:*
### *Operations:*
- traverseBFS
- insert (with heapifyUp to ensure heap property)
- insertList
- delete (with heapifyDown to ensure heap property)
- merge (2 heaps -> 1 heap)
- peek (get max value)
- copyHeap

### *Types:*
- Tree Structure (uses ptrs)
- Array Structure (no ptrs needed) in ADT directory

Units Tests to test each operation and to ensure proper tracking
of next insert/delete location to ensure shape property

## *Trie:*
### *Operations:*
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
