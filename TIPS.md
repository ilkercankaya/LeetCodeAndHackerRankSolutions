## Technical Part 

* Always Have Hashtable at the top of your mind

* Write functions to keep everything clean and easily changeable

* Sorted Array -> Possibly Indicates Binary Search

* Duplicate Elements -> HashTable

* Sorting Array O(N log(N)) - Best Time with Merge Sort but Quick Sort is generally better

* Find Max Element Unsorted -> O(N) Comparision Algorithm

* Finding All Subsets -> O(2^n)

* Finding All Permutations -> O(N!)

* HashSets -> No Duplicates + Internally contains HashMap + Stores set such as {1, 4, 7, 23, 14}, Key and Values are the same

* Tress -> Root = First, Leaf = Last

* Binary Search Tress -> Left = Smaller, Right = Bigger 

* BST + Sorted -> Insert = O(log N), find O(log N)

* Prefix -> A prefix of a string S is a substring of S that occurs at the beginning of S. "banana" -> "b", "ba", "ban"

* Suffix -> A suffix of a string S is a substring that occurs at the end of S. "banana" -> "a", "na", "ana"

* Balanced Tree Assumption On Interviews

* Trie -> reTrieval [Video Explanation Here](https://www.youtube.com/watch?v=-urNrIAQnNo)
    1. A tree that stores strings. Used for string search such as prefix, suffix. [E.g](https://www.hackerrank.com/challenges/contacts/problem)
    2. Can be used for word validation such as when the user is typing a word we can look up trie to see if the word is valid and maybe even suggest to complete the words.
    
    3. A  well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. The crucial point here is that unlike a BST with numbers your comparison complexity at any node is not O(1) but instead O(m) (Since in the worst case your string at any node differs from your pattern at the last letter).
In the worst case you'll have to compare your pattern with O(log n) nodes.
    4. Using Trie, we can search the key in O(M) time. 
    5. Contains a HashMap (pointer of alphabet size - use hash to map chars to indexes
    ) and a boolean in each node. Boolean for checking if the node is a word since it could also be a prefix.

* Inorder, Preorder, Postorder: Code Always Have Recursion(Left), Recursion(Right) stabled, only the print statement changes
    1. Inorder: Left First Then Root Then Right
    1. Preorder: Root First Then Left then Right 
    1. Postorder: Left Then Right Then Root
  
* Depth-first search = Depth increases gradually

* Breadth-first search = Breadth increases gradually - Check the code for the Binary Search Tree

* Binary-tree -> Recursion or Queues

* Recursion time complexity: [Example Here.](https://www.youtube.com/watch?v=gCsfk2ei2R8)
    1. **Substitution Method:** We make a guess for the solution and then we use mathematical induction to prove the the guess is correct or incorrect.

    2. **Recurrence Tree Method:** In this method, we draw a recurrence tree and calculate the time taken by every level of tree.The pattern is typically a arithmetic or geometric series.

    3. **Master Method:** Master Method is a direct way to get the solution. The master method works only for following type of recurrences or for recurrences that can be transformed to following type.
    T(n) = aT(n/b) + f(n) where a >= 1 and b > 1
    
* Sorting algorithms always have avg run time as worst cases except: **Quick Sort, Bucket Sort**

* **Insertion sort**:
    1. O(N^2) worst case, O(N) best; [E.g:](https://www.youtube.com/watch?v=JU767SDMDvA)
    2. Keep a sorted, unsorted list.
   
* **Selection sort**: 
    1. O(N^2) worst case, O(N^2) best; [E.g:](https://www.youtube.com/watch?v=g-PGLbMth_g)
    2. Find minimum from unsorted partition by iterating with minimum-finder algo with O(N), move it to sorted partition.
    3. Worst sorting algorithm.

* **Bubble Sort** -> until array is sorted - walk through and swap elements leading to number of times swapped - 1 4 5 7 2 3 -> 1 4 5 2 3 7 -> 1 4 2 3 5 7 -> 1 2 3 4 5 7

* **Heap Sort:** [E.g.](https://www.youtube.com/watch?v=2DmK_H7IdTo&t=76s) [E.g. 2](https://www.youtube.com/watch?v=2fA1FdxNqiE)
    1. Create max heap with given array O(N logN)
    2. Remove the largest element
    3. Place it in the sorted position
    4. Space Complexity O(1) since the root is swapped with the last element before the heapify call. [E.g.](https://stackoverflow.com/questions/22233532/why-does-heap-sort-have-a-space-complexity-of-o1)
    5. Ascending sort -> Form a Max-Heap, Descending Sort -> Form a min-heap.
    6. Build Max Heap: Start from non last leafs (len(A) // 2 - 1 for 0 index) and call heapify down, NOT HEAPIFY UP, this is because build max heap traverses from last non leaf node and keeps making the subtrees a heap, if heapify up was called it would mess the subtrees with the elements coming from up. [E.g.](https://www.youtube.com/watch?v=HI97KDV23Ig)

* **Quicksort (Also known as Partition Sort):**
    1. Pivot: All the elements smallers than pivot should be on left and all the elements greater than pivot should be on right.
    2. The process of making the list in 1. is called partitioning
    3. Partitioning only ensures that the pilot is placed in the correct position of the array. The left and right sub-arrays are arranged randomly.
    4. After partitioning the problem is broke down into 2 sub problems, sort the array on the left and the right.
    5. Divide and Conquer.
    6. Not a stable algorithm.
    7. Space complexity O(log(N)) due to stack frames. (2 calls from the middle of the array adds up to 2*logN but it is O(logN))
    8. Naive Approach Space complexity O(N) due to stack frames. Pivot is always chosen as the smallest element leading to N stack calls to partitioning.
    9. [Space complexity reduce method.](https://www.geeksforgeeks.org/quicksort-tail-call-optimization-reducing-worst-case-space-log-n/amp/) After partitioning, the partition with the fewest elements is (recursively) sorted first, requiring at most O(log n) space. Then the other partition is sorted using tail recursion or iteration, which doesn't add to the call stack. This idea, as discussed above, was described by R. Sedgewick, and keeps the stack depth bounded by O(log n).
    10. [Check Method II For Complete Explanation Space Complexity.](http://www.cs.nthu.edu.tw/~wkhon/algo08-tutorials/tutorial2b.pdf) if (there is X with length(X) < n/2) call Qsort(X) else partition X into X’and X’’ until all X are processed
        1. The idea of Method II is tail recursion
        2. Call recursion only when sub-problem is small enough
        3. First solves sub-problem with smaller size
    11. Average and Best Running time of O(N logN) due to logN times (best pivot picking) partitioning (which has O(N) time complexity).
    12. Worst case of O(N^2) due to picking the smallest as the pivot leads to N calls to partitioning (which has O(N) time complexity).
    13. This is a tail recursive algorithm.
    14. Median Of Three: Pick 3 elements chosen as first, middle, last, then sort them in the original array and use the median as the pivot. Eliminates the problem with (almost) sorted input. Compared to picking the pivot randomly:
        1. It ensures that one common case (fully sorted data) remains optimal.
        2. It's more difficult to manipulate into giving the worst case.
        3. A PRNG is often relatively slow.
    15. Pick a pivot and put that at the last index to run the partitioning algo.
    16. Pick i = 0, j = last element before pivot and iterate until i meets an element that is greater than the pivot and j meets an element that is smaller than the pivot. Swap these elements and keep on iterating until i and j have crossed. Swap the element at i with the pivot.
        1. Should i and j stop when they see elements equal to the pivot? Intuitively They should do the same thing, otherwise they will cause an imbalance. 
        2. For instance if i stops and j does not stop all elements equal to the pivot end up in S2
        3. If i and j both stop when they see elements equal to the pivot, there will be many swaps between identical elements. Although this seems useless, the positive effect is that i and j will cross in the middle, so the partition creates (nearly)  equal sized partitions.
        4. Consequently, if i and j do NOT stop, this would create very uneven partitions. (similar to choosing the first element!)
    
* **Quick Select:** Use the idea of partitioning recursively to find the kth smallest element. This makes one recursive call instead of two as in Naive Quicksort. Average O(N) time complexity, worst O(N^2). Use a good pivot to avoid worst.
    1. T(n) = cn + T(n/2)
    2. c(n + n/2 + n/4 + ... + 2 + 1) = c(2n) = O(n) 

* **Head vs Tail Recursion:**
    1. **(Non-Tail-Recursive) Head Recursion**: You make a recursive call first then do the calculation once the call is back. This method is prone to stack overflow if we exceed the stack limit.
    
           public int factorial(int n) {
           if (n == 0) {
              return 1;
           } else {
              return n * factorial(n - 1);
           }
    2. **Tail Recursion**: A recursive function is tail recursive when recursive call is the last thing executed by the function.
    3. Tail recursion doesnt add to the call stack. [E.g.](https://stackoverflow.com/questions/33923/what-is-tail-recursion) 
    Although some languages does not support it such as Java.
    4. _Tail call elimination:_ The tail recursive functions considered better than non tail recursive functions as tail-recursion can be optimized by compiler. The idea used by compilers to optimize tail-recursive functions is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use 
    
* **Call Stack:** A call stack is a stack data structure that stores information about the active subroutines of a computer program. This kind of stack is also known as an execution stack, program stack, control stack, run-time stack, or machine stack, and is often shortened to just "the stack". [E.g.](https://www.youtube.com/watch?v=Q2sFmqvpBe0)

* A _stable_ sorting algorithm is said to be if two objects with equal keys appear in the same order in sorted output as they appear in the input unsorted array. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, Count Sort. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

* **In-place vs out-of-place**:
    1. In-place means that the algorithm is O(1) space. Algorithm that uses O(1) extra space in
addition to the original input
    1. Out-of-place means that the algorithm is NOT O(1) space.
    
***Priority Queue**: A priority queue is an abstract data type which is like a regular queue or stack data structure, but where additionally each element has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.

* **Heap**: A Heap is a special Tree-based data structure in which the tree is a complete binary tree. An array is used to store the nodes with level order. Generally, Heaps can be of two types:
    1. **Min-Heap**: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
    2. **Max-Heap**: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
    3. Insertion as breadth-depth therefore it always has a height of LogN. Uses bubble'ing to interchange an newly added element to top.
    4. **Insertion - Bubbling E.g. Min Heap**: Check the parent, if it is greater than our node swap them.
    5. **Removing**: If root is removed then we have an empty spot. Swap that empty with the last added element. Bubble down the new root. Compare the root with its both children and swap it with the smallest child.
    6. **Removing wrt. Key**: Find the node with O(N) search and delete the node and swap the last node with the deleted current. After that ONLY HEAPIFYDOWN from that node is required. Proof: If a node at a level is swapped with the last node since the last node is greater than the current node, it is guranteed that the new value is always bigger than its parent. However, it is not guaranteed that the value is the smallest wrt. all children.
    7. **Indexing**: Parent = index is current index; parent = (index - 1) / 2, left = index * 2 + 1, right = index * 2 + 2
    8. **Heapify up - bubble up**: When we switch the current node with the root since the root was smaller than the other node, the swapped node it guaranteed to be smaller than the other child node.
    9. **Heapify down - bubble down**: We switch the current node with the smallest of the children since the smallest node must be the root.
    10. **Advantages**: Useful for accessing the smallest node in O(1) time, schedulers (where the earliest item is desired), find the kth smallest value O(k * logN) {logN due to heapify after deleting root}, median finder.
    11. O(N logN) to build the heap since we make insert calls with each element that could lead to heapify up.
    12. But if the array is given initially it is O(N) due to the heapify call for the each subtrees starting from non leaves.
    13. Find the largest kth number is find the smallest n-k th number in min heap.
    
* Priority Queue vs Heap: A heap is an implementation of priority queue with BST's. A normal Priority Queue can have O(N) add time where as a heap has O(logN) add.

* A full binary tree (sometimes proper binary tree or 2-tree) is a tree in which every node other than the leaves has two children. In a full binary tree all nodes have either 0 or 2 children. Both types of nodes can appear at all levels in the tree

* A complete binary tree is a binary tree is a tree that follows the heap structures, add and remove from furthest breadth-first search see if the tree can be formed OR ANOTHER DEF: At the level above the leaves nodes can have 0, 1 or 2 children. ALSO, the last level must be filled from left to right without leaving any gaps. Other than these levels all nodes must have 2 children.

* A perfect binary tree is a binary tree where each nodes except the leaves have 2 children.

* **Depth** Of Root = 0 (Same as level), **Height** of Leaf = 0, The depth of a node is the number of edges from the node to the tree's root node.
A root node will have a depth of 0. The height of a node is the number of edges on the longest path from the node to a leaf.
A leaf node will have a height of 0.

* Maximum number of nodes in a height of h with n nodes: ceil(n / (2^(h + 1)))

* **Stack Memory vs Heap Memory**:
    1. Stack Memory: Variables allocated on the stack are stored directly to the memory and access to this memory is very fast, and it's allocation is dealt with when the program is **compiled**. When a function or a method calls another function which in turns calls another function etc., the execution of all those functions remains suspended until the very last function returns its value. The stack is always reserved in a LIFO order, the most recently reserved block is always the next block to be freed. This makes it really simple to keep track of the stack, freeing a block from the stack is nothing more than adjusting one pointer.

    2. Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, but the heap size is only limited by the size of virtual memory . Element of the heap have no dependencies with each other and can always be accessed randomly at any time. You can allocate a block at any time and free it at any time. This makes it much more complex to keep track of which parts of the heap are allocated or free at any given time.
    
    3. You can use the stack if you know exactly how much data you need to allocate before compile time and it is not too big.	You can use heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.
    
    4. In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap. Stack is thread specific and Heap is application specific. The stack is important to consider in exception handling and thread executions.



## Behavioural Part

* Resume Walk-Through

* Current job -> Beginning of the career -> Go Towards Chronologically

* Quick shows of success

* Drive the interviewer with giving details of the projects that you took an interesting part

* Describe weaknesses, dont cover them

* Mention Hobbies -> HackerRank + Hackathons + Online Courses

## 3 Ways To Approach An Algorithm 

 1. **BUD**
    1. **Bottlenecks**: Find what causes the algorithm to be slow and fix its time complexity.
    2. **Unnecessary Work**: A unnecessary work after a condition is met could be avoided e.g. with break or pass statements.
    3. **Duplicate Work**: A repeated work could be avoided by look up tables.
 
 2. **Space / Time Tradeoffs (Hash Tables)**
 
 3. **D.I.Y:** Solve the algorithm my your brain and copy that algorithm to your code.
## Solve Algorithms in 7 Steps

1. LISTEN THE QUESTION - ASK FOR CLARIFICATION IF NEEDED

2. HAVE AN EXAMPLE - NOT A SMALL CASE

3. THINK OF A BRUTE FORCE WORST CASE

4. OPTIMIZE THE ALGORITHM ON THE HAND

5. WALK THROUGH THE ALGORITHM - DATA STRUCTURES && STRUCTURE OF THE CODE && CONSISTENT + DESCRIPTIVE NAMING

6. CODE THE CODE

7. TEST THE CODE OF ALGORITHM BY RUNNING THE CODE STEP-By-STEP ON THE BOARD WITH A DIFFERENT SMALLER TEST CASE THAN 2. + AN EDGE CASE

