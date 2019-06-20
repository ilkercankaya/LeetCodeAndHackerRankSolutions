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

* **[Time Analysis:](https://www.geeksforgeeks.org/analysis-of-algorithms-set-3asymptotic-notations/)**
    1. **Big-O:** Upper bound. The Big O notation defines an upper bound of an algorithm, it bounds a function only from above.
                            
                  O(g(n)) = { f(n): there exist positive constants c and 
                  n0 such that 0 <= f(n) <= c*g(n) for all n >= n0}
    2. **Ω Omega Notation:** Ω notation provides an asymptotic lower bound. Generally not useful.
            
            Ω (g(n)) = {f(n): there exist positive constants c and
            n0 such that 0 <= c*g(n) <= f(n) forall n >= n0}.
                  
    3. **Θ Theta Notation:** The theta notation bounds a functions from above and below, so it defines exact asymptotic behavior. One can think of this as both Omega and Big-O Notation holds for the given theta notation.
    A simple way to get Theta notation of an expression is to drop low order terms and ignore leading constants. For example, consider the following expression.
3n3 + 6n2 + 6000 = Θ(n3)
    
            Θ(g(n)) = {f(n): there exist positive constants c1, c2 and n0
            such that 0 <= c1*g(n) <= f(n) <= c2*g(n) for all n >= n0}
    

* **[Average Case Analysis:](https://www.youtube.com/watch?v=ElhIcC4f710)** Sigma * P(i) * Cost(i). [Another Source Here](https://www.geeksforgeeks.org/analysis-of-algorithms-set-2-asymptotic-analysis/)
    
* Shallow Copy vs Deep Copy: [:] Operator - Shallow [Explained Here.](https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86)  
           
            a = [1,2,3,4]
            # Copy the pointer of a into b
            b = a
            
            
            a = [1,2,3,4]
            b = a[:]
            b[0] = 100
            a -> [1,2,3,4]
            b -> [100,2,3,4]
            
            
            a = [[1, 2], [2, 4]]
            b = a[:] #shallow copy
            >> b[0].append(3)  ## Edit the first element (i.e. [1, 2])
            >> b
            >> [[1, 2, 3], [2, 4]]
            
            >> a
            >> [[1, 2, 3], [2, 4]]

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
    1. Look at the root position and made will be clear.
    1. Post-order is widely use in [mathematical expression. E.g.](https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/992/). It is easier to write a program to parse a post-order expression. You can easily figure out the original expression using the inorder traversal. However, it is not easy for a program to handle this expression since you have to check the priorities of operations. If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.

*  _**Top-down vs Bottom-up:**_
    1. **_"Top-down" Solution:_**
    "Top-down" means that in each recursion level, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. So the "top-down" solution can be considered as kind of preorder traversal. Could also be used with tail call optimization if possible.

    2. _**"Bottom-up" Solution:**_
    "Bottom-up" is another recursion solution. In each recursion level, we will firstly call the functions recursively for all the children nodes and then come up with the answer according to the return values and the value of the root node itself. This process can be regarded as kind of postorder traversal. 
    
    3. Can you determine some parameters to help the node know the answer of itself? Can you use these parameters and the value of the node itself to determine what should be the parameters parsing to its children? If the answers are both yes, try to solve this problem using a "top-down" recursion solution.

    4. Or you can think the problem in this way: for a node in a tree, if you know the answer of its children, can you calculate the answer of the node? If the answer is yes, solving the problem recursively from bottom up might be a good way.

* To understand if a code is "Top-down" or "Bottom-Up" check the code. Imagine the call stack.

* Depth-first search = Depth increases gradually 

* Breadth-first search = Breadth increases gradually - Check the code for the Binary Search Tree

* Binary-tree -> Recursion or Queues

* **Recursion:** Recursion is an approach to solving problems using a function that calls itself as a subroutine. The recursion call continues until it reaches a point where the subproblem can be solved without further recursion. A recursive function should have the following properties so that it does not result in an infinite loop:
    1. A simple **_base case_** (or cases) also known as _bottom case_ — a terminating scenario that does not use recursion to produce an answer.
    2. A set of rules, also known as _**recurrence relation**_ that reduces all other cases towards the base case.
    3. Define recurrence relation and base cases then went to implement.
    
* There are mainly two parts of the space consumption that one should bear in mind when calculating the space complexity of a recursion algorithm: **recursion related** and **non-recursion related space.**
    1. **Recursion Related Space:** The recursion related space refers to the memory cost that is incurred directly by the recursion, i.e. the stack to keep track of recursive function calls. In order to complete a typical function call, the system should allocate some space in the stack to hold three important pieces of information:
        1. The returning address of the function call. Once the function call is completed, the program should know where to return to, i.e. the point before the function call; 
        2. The parameters that are passed to the function call; 
        3. The local variables within the function call.
        4. Example: Mergesort making copies of the array into subarrays in each iteration. Keeping previous iterations from the program such as the fibonacci series is not RRS!
    2. **Non-Recursion Related Space:** As suggested by the name, the non-recursion related space refers to the memory space that is not directly related to recursion, which typically includes the space (normally in heap) that is allocated for the global variables. 
        1. E.g: Keeping the values of previous fibonacci series calculations in a hashmap.

* It is due to these recursion related space consumption that sometimes one might run into a situation called stack overflow, where the stack allocated for a program reaches its maximum space limit and the program ends up with failure. Therefore, when designing a recursion algorithm, one should carefully evaluate if there is a possibility of stack overflow when the input scales up.
        
* Execution tree, which is a tree that is used to denote the execution flow of a recursive function in particular. Each node in the tree represents an invocation of the recursive function. Therefore, the total number of nodes in the tree corresponds to the number of recursion calls during the execution. Could be used to approximate time complexity.

* Given a recursion algorithm, its time complexity O(T) is typically the product of the number of recursion invocations (denoted as R) and the time complexity of calculation (denoted as O(s) that incurs along with each recursion call:
    1. **O(T) = R * O(s)**
    2. One could also use **Master Theorem** to find the answer.
    
* **Memoization** is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. The memoization technique is a good example that demonstrates how one can reduce compute time in exchange for some additional space.


* **Dynamic Programming:**
    1. _**Optimal substructure**_  — optimal solution can be constructed from optimal solutions of its subproblems.
    2. _**Overlapping sub-problems**_  — problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems.
    3. Once these two conditions are met we can say that this divide and conquer problem may be solved using dynamic programming approach.
    3. Requires i. and ii. and could also have extra methodologies either _**Memoization**_(Top-Down) or _**Tabulation**_(Bottom-Up)
    4. _**Memoization (uses top-down cache filling)**_  It starts with the highest-level subproblems (the ones closest to the original problem), and recursively calls the next subproblem, and the next. We save time when a subproblem A recurses into a subproblem B that has already been called. Since B and all subproblems below it are memoized, we can avoid repeating the entire recursion tree generated by B, saving a lot of computation.
    5. _**Tabulation (uses bottom-up cache filling)**_ It starts by solving the lowest level subproblem. The solution then lets us solve the next subproblem, and so forth. We iteratively solve all subproblems in this way until we’ve solved all subproblems, thus finding the solution to the original problem. We save time when a subproblem needs the answer to a subproblem that has been called before, and thus has had its value tabulated.
    6. The major differences between tabulation and memoization are:
        1. Tabulation has to look through the entire search space; memoization does not.
        2. Tabulation requires careful ordering of the subproblems is; memoization doesn’t care much about the order of recursive calls.
        3. If the original problem requires all subproblems to be solved, tabulation usually outperformes memoization by a constant factor. This is because tabulation has no overhead for recursion.
        4. If only some of the subproblems needs to be solved for the original problem to be solved, then memoization is preferrable since the subproblems are solved lazily, i.e. precisely the computations needed are carried out.
    7. Could be taught as dynamic programming is an extension of divide and conquer paradigm.

* Recursion time complexity: [Example Here.](https://www.youtube.com/watch?v=gCsfk2ei2R8)
    1. **Substitution Method:** We make a guess for the solution and then we use mathematical induction to prove the the guess is correct or incorrect. K here is the step number. It is not and random number.

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
        2. Call recursion only when sub-problem is small enough (N/2)
        3. Only doing recursion when a sub-array with (N/2) is there makes sure that O(log n) is met.
        4. First solves sub-problem with smaller size
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
     17. **Partition Algorithms**:   
        1. **Hoare-Partition:** Uses i = start and j = end and iterates until a bigger or equal element than pivot is found on the ith index, smaller or equal than pivot element is found at jth index. Swaps them in-between. Repeats until i < j.  
        2. **Lomuto-Partition:** Init pIndex = start, iterate from start to end -1 and check if an element is smaller then the pivot, if so change the elements at i and pIndex and increment pIndex. Idea is to push all the elements that are less than pivot to the left. Lastly swap the pivot and the element at pIndex.
        3. Hoare-Partition is faster than Lomuto-Partition but Lomuto is easier to understand and implement.
     18. **In-place or not:** Yes it is. In-place means that the algorithm does not use extra space for manipulating the input but may require a small though nonconstant extra space for its operation. Usually, this space is O(log n), though sometimes anything in o(n) (Smaller than linear) is allowed.
     
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
    2. **Tail Recursion**: A recursive function is tail recursive when recursive call is the last thing executed by the function. C, C++ support the optimization of tail recursion functions. On the other hand, Java and Python do not support tail recursion optimization.
    3. Tail recursion doesnt add to the call stack. [E.g.](https://stackoverflow.com/questions/33923/what-is-tail-recursion) 
    Although some languages does not support it such as Java.
    4. _Tail call elimination:_ The tail recursive functions considered better than non tail recursive functions as tail-recursion can be optimized by compiler. The idea used by compilers to optimize tail-recursive functions is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use 
    5. Tail recursion could optimize the space complexity of the algorithm, by eliminating the stack overhead incurred by recursion. More importantly, with tail recursion, one could avoid the problem of stack overflow that comes often with recursion
    6. Another advantage about tail recursion is that often times it is easier to read and understand, compared to non-tail-recursion. Because there is no post-call dependency in tail recursion (i.e. the recursive call is the final action in the function), unlike non-tail-recursion. 

* **Call Stack:** A call stack is a stack data structure that stores information about the active subroutines of a computer program. This kind of stack is also known as an execution stack, program stack, control stack, run-time stack, or machine stack, and is often shortened to just "the stack". [E.g.](https://www.youtube.com/watch?v=Q2sFmqvpBe0)

* **Merge Sort:**
    1. Divide And Conquer.
    2. Split the array until arrays with one elements are met.
    3. Examine the elements are store them back to temporary arrays.
    4. Merge smaller sorted arrays into bigger arrays making the bigger arrays sorted.
    5. **Merge:**
        1. Requires two _**sorted**_ arrays.
        2. Set i = 0, j = 0, a = 0. Iterate through sorted arrays by comparing their current indexes. Find the smaller element and add it to the bigger element and increment either i or j depending on where the element is picked from.
        3. After the iterations finish there will be an only one array which its elements are not added since the comparing while loop checks for whether the size of each the arrays are met
        . Use two while loops to add all of the left small arrays elements into the bigger array.
        4. Time complexity O(m+ n). 
    6. Space complexity O(n). .If stack frames is counted, then it's O(n)+ O(log n). [Explained here. ](https://www.youtube.com/watch?v=0nlPxaC2lTw&t=602s)Not an in-place algorithm. Naive version O(n logn) due to keeping all the arrays without deletion leads to n memory allocation in each level and since we are doing a total of log n allocations the complexity is O(n logn). If we delete the unused arrays we will have at most n (the left sub array and right subarray )+ right subbarays childs n / 2 + n / 4 + n/ 8... which is O(2n) which is O(n).
    7. Stable sorting algorithm since making "L <= R" ensures that both array have the original order reserved since we favor the left side before right side. E.g 1 2 2 2 3 => Left, 2 2 2 4 5 => Right. If we favor right over left, the order will be changed since the original array is 1 2 2 2 3 2 2 2 4 5.
    8. Time complexity O(n logn). Merge is O(m + n) = O(n) since m = n = n / 2, for loops are total of O(0 to middle) + O(middle to len(array)) = O(n). 

* **Divide And Conquer:** Breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem. Because divide-and-conquer solves subproblems recursively, each subproblem must be smaller than the original problem, and there must be a base case for subproblems.
    1. Divide the problem into a number of subproblems that are smaller instances of the same problem.
    2. Conquer the subproblems by solving them _**recursively**_. If they are small enough, solve the subproblems as base cases.
    3. Combine the solutions to the subproblems into the solution for the original problem.
    
    
* A _stable_ sorting algorithm is said to be if two objects with equal keys appear in the same order in sorted output as they appear in the input unsorted array. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, Count Sort. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

* **In-place vs out-of-place**:
    1. In-place In-place means that the algorithm does not use extra space for manipulating the input but may require a small though nonconstant extra space for its operation. Usually, this space is O(log n), though sometimes anything in o(n) (Smaller than linear) is allowed. For array of 1073741824 size it is only taking 30 units of space.
    2. Out-of-place means that the algorithm is NOT in-place so according to the definition above it is considered any space usage greater than O(log n).
    
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

* **Dangling pointers:** Pointer which points to a de-allocated memory. Happens generally when two pointers are pointing towards the same memory address. Could lead to crashes.

* **Space complexity of a recursive function:** Look at the recursion tree and try to capture a moment where the recursion call stack is at its max. Iterate from beginning to end if your are having bad time. Just because the recursive calls are high does not mean that the space complexity will be high.

* A full binary tree (sometimes proper binary tree or 2-tree) is a tree in which every node other than the leaves has two children. In a full binary tree all nodes have either 0 or 2 children. Both types of nodes can appear at all levels in the tree

* A complete binary tree is a binary tree is a tree that follows the heap structures, add and remove from furthest breadth-first search see if the tree can be formed OR ANOTHER DEF: At the level above the leaves nodes can have 0, 1 or 2 children. ALSO, the last level must be filled from left to right without leaving any gaps. Other than these levels all nodes must have 2 children.

* A perfect binary tree is a binary tree where each nodes except the leaves have 2 children.

* **Depth** Of Root = 0 (Same as level), **Height** of Leaf = 0, The depth of a node is the number of edges from the node to the tree's root node.
A root node will have a depth of 0. The height of a node is the number of edges on the longest path from the node to a leaf.
A leaf node will have a height of 0.

*  A leaf is a node with no children.

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

