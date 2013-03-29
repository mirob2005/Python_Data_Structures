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

# *Self-Balancing BST's:*
## *AVL Tree:*
### *Operations:*
- insert (Balance Factor Calculations added)
- delete (Balance Factor Calculations added)
- deleteTree (new, none of the other trees has this added at this time)
- checkBalance (check the Balance Factor to see if a rotation(s) is necessary)
- calcBF (recalculate the BF for the the given root and all ancestors if necessary, insert version and delete version)
- rotateLeft
- rotateRight

- All redefined operations are recursive.

### *Rest of the operations are inherited from the recursive BST*

Unit Tests to test each operation and valid rotations.

## *Red-Black Tree:*
### *Operations:*
- insert (Color Check added)
- delete (Color Check added)
- deleteTree (Same as AVL)
- checkColor (determines the new coloring and if any rotations are needed - version for post-insert and post-delete)
- rotateLeft (Same as AVL)
- rotateRight (Same as AVL)

- All redefined operations are recursive.

### *Rest of the operations are inherited from the recursive BST*

Unit Tests to test each operation, valid rotations and correct coloring.

## *Splay Tree:*
### *Operations:*
- insert (splaying added)
- find (splaying added for valid/invalid finds)
- delete (splaying added for valid/invalid deletes)
- copyTree (redefined due to the structure of the splay tree varying based off order of inserts)
- findRecentAccessed (returns the root, only useful for a splay tree)
- splay (rotates the tree so that the most recent inserted/found node or parent of a recent delete is rotated to the root)

- All redefined operations are recursive.

### *Rest of the operations are inherited from the recursive BST*

Unit Tests to test each operation and valid splaying.