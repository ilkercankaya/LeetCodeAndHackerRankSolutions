## Tips
    I have taken notes of key points within my journey of studying algorithms, data structures. 

## Technical Part 

* Always Have Hashtable at the top of your mind

* Write functions to keep everything clean and easily changeable

* Sorted Array -> Possibly Indicates Binary Search

* Duplicate Elements -> HashTable

* Sorting Array O(N log(N)) - Best Time with Merge Sort but Quick Sort is generally better

* Find Max Element Unsorted -> O(N) Comparision Algorithm

* Finding All Subsets -> O(2^n) - Each element can either appear or not giving two options leading to 2^N.

* Finding All Permutations -> O(N!)

* HashSets -> No Duplicates + Internally contains HashMap + Stores set such as {1, 4, 7, 23, 14}, Key and Values are the same

* Tress -> Root = First, Leaf = Last

* Binary Search Tress -> Left = Smaller, Right = Bigger 

* BST + Sorted -> Insert = O(log N), find O(log N)


* **Queue vs. Stack**:
    1. Queue: FIFO (First in First Out). The insert operation is also called **enqueue** and the new element is always added at the end of the queue. The delete operation is called **dequeue**. You are only allowed to remove the first element. To implement a queue, we may use a dynamic structure such as a vector or a linked list.
        1. Circular Queue: We may use a fixed-size array and two pointers to indicate the starting position and the ending position. And the goal is to reuse the wasted storage we mentioned previously.
    2. Stack: First in Last Out.

* **Monotonic Stack, Monotonic Queue**:
    * Stacks that are strictly increasing or decreasing.
    * Solves find closest element to right or left problems.
    * 4 3 2 1 -> Stack is 4->3->2->1. Image the next element is 5. This means that 5 will pop everything that is smaller than it.
    This will mean that our new number on the iteration is actually the closest number that is greater than the all the popped nums otherwise they would have been popped by another number.
    [Check Here For More Info](https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6)

* **Call Stack:** A call stack is a stack data structure that stores information about the active subroutines of a computer program. This kind of stack is also known as an execution stack, program stack, control stack, run-time stack, or machine stack, and is often shortened to just "the stack". [E.g.](https://www.youtube.com/watch?v=Q2sFmqvpBe0)

* A _stable_ sorting algorithm is said to be if two objects with equal keys appear in the same order in sorted output as they appear in the input unsorted array. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, Count Sort. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

* **In-place vs out-of-place**:
    1. In-place In-place means that the algorithm does not use extra space for manipulating the input but may require a small though nonconstant extra space for its operation. Usually, this space is O(log n), though sometimes anything in o(n) (Smaller than linear) is allowed. For array of 1073741824 size it is only taking 30 units of space.
    2. Out-of-place means that the algorithm is NOT in-place so according to the definition above it is considered any space usage greater than O(log n).
  
* **Dangling pointers:** Pointer which points to a de-allocated memory. Happens generally when two pointers are pointing towards the same memory address. Could lead to crashes.

* **Space complexity of a recursive function:** Look at the recursion tree and try to capture a moment where the recursion call stack is at its max. Iterate from beginning to end if your are having bad time. Just because the recursive calls are high does not mean that the space complexity will be high.

* **Stack Memory vs Heap Memory**:
    1. Stack Memory: Variables allocated on the stack are stored directly to the memory and access to this memory is very fast, and it's allocation is dealt with when the program is **compiled**. When a function or a method calls another function which in turns calls another function etc., the execution of all those functions remains suspended until the very last function returns its value. The stack is always reserved in a LIFO order, the most recently reserved block is always the next block to be freed. This makes it really simple to keep track of the stack, freeing a block from the stack is nothing more than adjusting one pointer.

    2. Variables allocated on the heap have their memory allocated at run time and accessing this memory is a bit slower, but the heap size is only limited by the size of virtual memory . Element of the heap have no dependencies with each other and can always be accessed randomly at any time. You can allocate a block at any time and free it at any time. This makes it much more complex to keep track of which parts of the heap are allocated or free at any given time.
    
    3. You can use the stack if you know exactly how much data you need to allocate before compile time and it is not too big.	You can use heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.
    
    4. In a multi-threaded situation each thread will have its own completely independent stack but they will share the heap. Stack is thread specific and Heap is application specific. The stack is important to consider in exception handling and thread executions.

* If a node X is added to the queue in the kth round, the length of the shortest path between the root node and X is exactly k. That is to say, you are already in the shortest path the first time you find the target node. 


* Never forget to take the time complexity of built-in operations into consideration when you compute the time complexity for your solution.

* _**Amortized Analysis**_ is used for algorithms where an occasional operation is very slow, but most of the other operations are faster. In Amortized Analysis, we analyze a sequence of operations and guarantee a worst case average time which is lower than the worst case time of a particular expensive operation. [E.g](https://www.geeksforgeeks.org/analysis-algorithm-set-5-amortized-analysis-introduction/)
    1. The amortized analysis doesn’t involve probability. There is also another different notion of average case running time where algorithms use randomization to make them faster and expected running time is faster than the worst case running time. These algorithms are analyzed using Randomized Analysis. Examples of these algorithms are Randomized Quick Sort, Quick Select and Hashing. We will soon be covering Randomized analysis in a different post.
    2. The Amortized Analysis done for Dynamic Array example is called Aggregate Method.
 
* **Iterators:**
    1. An iterator is an object that enables a programmer to traverse a container, particularly lists.
    2. Essentially, an iterator can be used to iterate over any container object. For our purpose, the container object is a binary search tree. If such an iterator is defined, then the traversal logic can be abstracted out and we can simply make use of the iterator to process the elements in a certain order.
            
            1. new_iterator = BSTIterator(root);
            2. while (new_iterator.hasNext())
            3.     process(new_iterator.next());

## Encapsulation vs Abstraction 

* Encapsulation hides variables or some implementation that may be changed so often in a class to prevent outsiders access it directly. They must access it via getter and setter methods.

* Abstraction is used to hiding something too but in a higher degree(class, interface). Clients use an abstract class(or interface) do not care about who or which it was, they just need to know what it can do.

* Abstraction lets you focus on what the object does instead of how it does, while Encapsulation means hiding the internal details of how an object works. When you keep internal working details private, you can change it later with a better method.

* In Java, Abstraction is supported using interface and abstract class while Encapsulation is supported using access modifiers e.g. public, private and protected.

## Time Analysis
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

* Sorting algorithms always have avg run time as worst cases except: **Quick Sort, Bucket Sort**

## Trees / Binary / Binary Search

* A full binary tree (sometimes proper binary tree or 2-tree) is a tree in which every node other than the leaves has two children. In a full binary tree all nodes have either 0 or 2 children. Both types of nodes can appear at all levels in the tree

* A complete binary tree is a binary tree is a tree that follows the heap structures, add and remove from furthest breadth-first search see if the tree can be formed OR ANOTHER DEF: At the level above the leaves nodes can have 0, 1 or 2 children. ALSO, the last level must be filled from left to right without leaving any gaps. Other than these levels all nodes must have 2 children.

* A perfect binary tree is a binary tree where each nodes except the leaves have 2 children.

* Traverse to left most child in a BT complexity is O(N) due to the fact that the BT can be a list basically but if it is said to be a balanced BST, then iterating to left most child is O(logN)

* **Depth** Of Root = 0 (Same as level), **Height** of Leaf = 0, The depth of a node is the number of edges from the node to the tree's root node.
A root node will have a depth of 0. The height of a node is the number of edges on the longest path from the node to a leaf.
A leaf node will have a height of 0.

*  A leaf is a node with no children.

* Maximum number of nodes in a height of h with n nodes: ceil(n / (2^(h + 1)))
        
* Inorder, Preorder, Postorder: Code Always Have Recursion(Left), Recursion(Right) stabled, only the print statement changes
    1. Inorder: Left First Then Root Then Right
    1. Preorder: Root First Then Left then Right 
    1. Postorder: Left Then Right Then Root
    1. Look at the root position and made will be clear.
    1. Post-order is widely use in [mathematical expression. E.g.](https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/992/). It is easier to write a program to parse a post-order expression. You can easily figure out the original expression using the inorder traversal. However, it is not easy for a program to handle this expression since you have to check the priorities of operations. If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.

* In Binary Search Tree, **Inorder Successor** of an input node can also be defined as the node with the smallest key greater than the key of input node.

*  _**Top-down vs Bottom-up:**_
    1. **_"Top-down" Solution:_**
    "Top-down" means that in each recursion level, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. So the "top-down" solution can be considered as kind of preorder traversal. Could also be used with tail call optimization if possible.

    2. _**"Bottom-up" Solution:**_
    "Bottom-up" is another recursion solution. In each recursion level, we will firstly call the functions recursively for all the children nodes and then come up with the answer according to the return values and the value of the root node itself. This process can be regarded as kind of postorder traversal. 
    
    3. Can you determine some parameters to help the node know the answer of itself? Can you use these parameters and the value of the node itself to determine what should be the parameters parsing to its children? If the answers are both yes, try to solve this problem using a "top-down" recursion solution.

    4. Or you can think the problem in this way: for a node in a tree, if you know the answer of its children, can you calculate the answer of the node? If the answer is yes, solving the problem recursively from bottom up might be a good way.

* To understand if a code is "Top-down" or "Bottom-Up" check the code. Imagine the call stack.

* If we are traversing only a node at a time (either going left of a node or right of a node) and top-down approach is used to solve the problem. We can reduce the space complexity to O(1) by using tail-call optimization. [Example: Lowest Common Ancestor of a Binary Search Tree.](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/)

* Balanced Tree Assumption On Interviews

## Bit Manipulation

* a XOR a is 0. a XOR a XOR b is b.

* Bits needed to present a number is log(N)

* ~k == -(k+1)

* Bitmask approach is important.

* a ^ b = c, then a ^ c = b

## Two-Pointer Approach

* Use _**two-pointer technique**_ is that you want to iterate the array from two ends to the middle. So you can use the two-pointer technique:
One pointer starts from the beginning while the other pointer starts from the end.
And it is worth noting that this technique is often used in a _**sorted array**_.

* Using the two-pointer technique when you need:
    1. One slow-runner and one fast-runner at the same time.
    2. The key to solving with this kind of strategyis to determine the movement strategy for both pointers.
 

## Java Knowledge

* In Java, _**Vector vs ArrayList:**_ [Read it Here.](https://www.geeksforgeeks.org/vector-vs-arraylist-java/)
    1. Vector is _**synchronized**_, which means only one thread at a time can access the code, while arrayList is not synchronized, which means multiple threads can work on arrayList at the same time
    2. ArrayList is **_faster_**, since it is non-synchronized, while vector operations give slower performance since they are synchronized (thread-safe). If one thread works on a vector, it has acquired a lock on it, which forces any other thread wanting to work on it to have to wait until the lock is released.
    3.  ArrayList and Vector both grow and shrink dynamically to maintain optimal use of storage – but the way they resize is different. ArrayList increments 50% of the current array size if the number of elements exceeds its capacity, while vector increments 100% – essentially doubling the current array size.

* 2D - Arrays:
    1. **C++** stores the two-dimensional array as a one-dimensional array. So actually A[i][j] equals to A[i * N + j] if we defined A as a one-dimensional array which also contains M * N elements.
    2. **In Java**, the two-dimensional array is actually a one-dimensional array which contains M elements, each of which is an array of N integers.

* String comparison:
     1. **C++,** we may use "==" to compare two strings due to built-in operator overloading
     2. **Java,** we may not use "==" to compare two strings. When we use "==", it actually compares whether these two objects are the same object.

* In some languages (like C++), the string is mutable. That is to say, you can modify the string just like what you did in an array. In some other languages (like Java and Python), the string is immutable. 
This feature will bring several problems. [Check Java Here](https://leetcode.com/playground/g4kbNuNZ)

* In Java, strings s1 + s2 is O(s1.length() + s2.length()) since each string is copied into a new string two consecutive for loops .
 if you assume N concatenations of Strings of length M, then the complexity is O(M * N ^ 2).
 
* In Java, since the string is immutable, concatenation works by first allocating enough space for the new string, copy the contents from the old string and append to the new string.
            
        int n = 10000;
        for (int i = 0; i < n; i++) {
            s += "hello";
        }
    Therefore, the time complexity in total will be:
5 + 5 × 2 + 5 × 3 + … + 5 × n
= 5 × (1 + 2 + 3 + … + n)
= 5 × n × (n + 1) / 2,

    With StringBuilder this could be reduced to O(M * N) where M is the size of the string.

* If you did want your string to be mutable, you can convert it to a char array then modify and convert back to a string.

* StringBuffer is synchronized, meaning thread safe. This means that two threads can’t call StringBuffer methods simultaneously. On the other hand, StringBuilder is non-synchronized, meaning not thread safe though StringBuilder is faster.

* Usually, StringBuffer.append simply needs to add its input to the end of its buffer. The amount of time this takes has no dependency on the current size of the StringBuffer. 

* **_Fail-fast vs Fail-safe:_** [Read it Here.](https://javaconceptoftheday.com/fail-fast-and-fail-safe-iterators-in-java-with-examples/)
    1. A system is called fail-fast if it is shut down immediately when an error occurred. These systems don’t carry on with the errors. They immediately stop operating when a fault is occurred in the system. The errors in the fail-fast systems are immediately exposed. 
        But, fail-safe systems are not like that. They don’t stop operating even when a fault is occurred in the system. They continue the operation by hiding the errors. They don’t expose the errors immediately. They carry on with the errors.
    2. Iterators in java give us the facility to traverse over the Collection objects. Iterators returned by the Collection are either fail-fast in nature or fail-safe in nature. Fail-Fast iterators immediately throw ConcurrentModificationException if a collection is modified while iterating over it.
       Where as Fail-Safe iterators don’t throw any exceptions if a collection is modified while iterating over it. Because, they operate on the clone of the collection, not on the actual collection.
       But, they don’t throw any exceptions if the collection is modified by the iterator’s own methods like remove().
    3. Fail-fast method uses the following to know whether the collection is modified or not, they use an internal flag called modCount which is updated each time a collection is modified. Every time when an Iterator calls the next() method, it checks the modCount. If it finds the modCount has been updated after this Iterator has been created, it throws ConcurrentModificationException.
    4. Fail-Safe iterators don’t throw any exceptions if the collection is modified while iterating over it. Because, they iterate on the clone of the collection not on the actual collection. So, any structural modifications done on the actual collection goes unnoticed by these iterators. But, these iterators have some drawbacks. One of them is that it is not always guaranteed that you will get up-to-date data while iterating. Because any modifications to collection after the iterator has been created is not updated in the iterator. One more disadvantage of these iterators is that there will be additional overhead of creating the copy of the collection in terms of both time and memory.
    5. The iterators returned by the ArrayList, Vector, HashMap etc are all Fail-Fast in nature.
    6. Iterator returned by ConcurrentHashMap is a fail-safe iterator.

## Linked List

* In linked list questions, _**two pointers approach**_ is very useful. It is also possible to navigate to the middle with tow-pointers approach
by setting the speed difference to 1. This could be useful to do things in one pass.

* Dummy Head could also be helpful to iterate over linked list with ease. Create a new head with empty val and then attach it as the head and connect the original linked list to it and iterate over it. In the end, delete the head or return head.next as the new head.

* Analysis of Linked-Lists
   * In linked lists delete and add operations are considered O(1) if we know the nodes that we need to operate on if not depending on whether it is a singly linked list or a doubly time complexity could vary up to O(N).
   Generally they are assumed to be O(1) since we do not need to shift each elements like in an array deletion.
   * However, there is an intuitive way to make the delete O(1). Might cause errors which I can not tell directly. [Question Here!](https://leetcode.com/problems/delete-node-in-a-linked-list/)
   * Delete operation in a doubly-linked-list would be truly O(1) if we were given the node to delete since the node has next and prev we could traverse in O(1) time
but in singly linked list it would be O(N) since we would need to find the nodes prev to delete it and re-link.
   * [Full Time Complexity Table Here](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/29/screen-shot-2018-04-28-at-174531.png)

## Python Knowledge

* In Python consecutive comma operators are evaluated from right to left. All the expressions to the right of the assignment operator are evaluated before any of the assignments are made.
            
            a = 5
            b = 4
            a, b = a + b, a
            print a, b
            # 9, 5; first a is assigned to b and then a + b is assigned to a.

* In Python 3//2 = 1 but -3//2 = -2 due to ***the floor*** operation. Your result using integer division is being rounded down toward the more negative value of -2. (This is also known as "Floor division")

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
            
* A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
            
            # example 1
            def make_printer(msg):
                def printer():
                    print msg
                return printer
            
            printer = make_printer('Foo!')
            printer()
            
            # example 2
            def Counter(x):
                # x += 10 makes x increment by 10
                message = "I am a closure"
                def _increment():
                    nonlocal x
                    x += 1
                    print(x, message)
                return _increment
            
            
            counter = Counter(0)
            counter() #1
            counter() #1
            counter() #1
            
            def make_printer(msg):
                def printer(msg=msg):
                    print msg
                return printer
            # this is not an enclosure since msg is also a local variable of printer since it was passed with parameter call
            
  * What is going above is that When _Counter_ is called, a new frame is put on the stack with the compiled code for the printer function as a constant and the value of _x and message_ as a local. It then creates and returns the function. Because the function printer references the _x and message_ variable, it is kept alive after the _Counter_ function has returned.

  * This technique by which the data is attached to some code even after end of those other original functions is called as closures in python.

  * Increment is being called with the function calls and it has stored _x and message_ as locals from the inital call of Counter(0). 

  * Nested and enclosure functions only have read-only access to the enclosing scope of variables if nonlocal keyword is not specified.
  
* When and why to use Closures:
     1. As closures are used as callback functions, they provide data hiding. This helps us to reduce the use of global variables.
        
     2. When we have few functions in our code, closures prove to be efficient way. But if we need to have many functions, then go for class (OOP).

* Matrix Rotation Problems (Rotate 90, 180, 270, 360 degree) could be with transpose with (right-to left fli or top-bottom flip) although the order of transpose and flips could differ.

* Function Passes in Python:
    * Python document refers it to as "pass by assignment"
    * Python does pass by value. What is being passed is just a pointer to the object that you're passing. So what is being copied isn't the object, but its object address.

            def f(x,y):
                 temp = x
                 x = y
                 y = temp
            # would not swap and change x or y, swaps the copy object refence of x and y
            
            def f(x):
                x.append(1)
            # would change since we are calling x with append method refering to original object


* The is operator may seem like the same as the equality operator but they are not same. The is checks if both the variables point to the same object whereas the == sign checks if the values for the two variables are the same. 

* Simply speaking Serialization is a process of converting an Object into stream of bytes so that it can be transferred over a network or stored in a persistent storage.

## Heap - Priority Queue
  
***Priority Queue**: A priority queue is an abstract data type which is like a regular queue or stack data structure, but where additionally each element has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority.

* **Heap**: A Heap is a special Tree-based data structure in which the tree is a complete binary tree. An array is used to store the nodes with level order. Generally, Heaps can be of two types:
    1. **Min-Heap**: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
    2. **Max-Heap**: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
    3. Insertion as breadth-depth therefore it always has a height of LogN. Uses bubble'ing to interchange an newly added element to top.
    4. **Insertion - Bubbling E.g. Min Heap**: Check the parent, if it is greater than our node swap them.
    5. **Removing** [Eg Here](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/heap-delete.html): If root is removed then we have an empty spot. Swap that empty with the last added element. Bubble down the new root. Compare the root with its both children and swap it with the smallest child.
    6. **Removing wrt. Key**: Find the node with O(N) search and delete the node and swap the last node with the deleted current. After that HEAPIFYDOWN or HEAPIFYUP from that node is required. 
    7. **Indexing**: Parent = index is current index; parent = (index - 1) / 2, left = index * 2 + 1, right = index * 2 + 2
    8. **Heapify up - bubble up**: When we switch the current node with the root since the root was smaller than the other node, the swapped node it guaranteed to be smaller than the other child node.
    9. **Heapify down - bubble down**: We switch the current node with the smallest of the children since the smallest node must be the root.
    10. **Advantages**: Useful for accessing the smallest node in O(1) time, schedulers (where the earliest item is desired), find the kth smallest value O(k * logN + N) {logN due to heapify after deleting root, N due to heapify}, median finder.
    11. O(N logN) to build the heap since we make insert calls with each element that could lead to heapify up.
    12. But if the array is given initially it is O(N) due to the heapify call for the each subtrees starting from non leaves.
    13. Find the largest kth number is find the smallest n-k th number in min heap.
   
* Priority Queue vs Heap: A heap is an implementation of priority queue with BT's. A normal Priority Queue can have O(N) add time where as a heap has O(logN) add.

* Do not confuse keeping the max through iterations with heaps. Keeping the max could be done without having to make a heap by just iteratively comparing the obtained value with the current one.

## Heapsort

* **Heap Sort:** [E.g.](https://www.youtube.com/watch?v=2DmK_H7IdTo&t=76s) [E.g. 2](https://www.youtube.com/watch?v=2fA1FdxNqiE)
    1. Create max heap with given array O(N)
    2. Remove the largest element
    3. Place it in the sorted position
    4. Space Complexity O(1) since the root is swapped with the last element before the heapify call. [E.g.](https://stackoverflow.com/questions/22233532/why-does-heap-sort-have-a-space-complexity-of-o1)
    5. Ascending sort -> Form a Max-Heap, Descending Sort -> Form a min-heap.
    6. Build Max Heap: Start from non last leafs (len(A) // 2 - 1 for 0 index) and call heapify down, NOT HEAPIFY UP, this is because build max heap traverses from last non leaf node and keeps making the subtrees a heap, if heapify up was called it would mess the subtrees with the elements coming from up. [E.g.](https://www.youtube.com/watch?v=HI97KDV23Ig)
        1. O(N) times, [Time Complexity proof Here!](https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/)
        2. Sum of Geometric Series [Explained Here!](https://www.youtube.com/watch?v=-5kIBPR2Npk)

## Quicksort + Quickselect

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

## Merge Sort

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

## Insertion sort

* **Insertion sort**:
    1. **O(N^2) worst case, O(N) best**; [E.g:](https://www.youtube.com/watch?v=JU767SDMDvA)
    2. Iterate through left to right. Swap the current element to its left until it is in correct position then continue from the next index of the swapped elements original position.
    3. Builds a sorted list from left to right in each iteration.
    3. Gives good performance when the list is almost sorted.
    4. Worst case time complexity of insertion sort where position of the data to be inserted is calculated using binary search
    does not change the time complexity. Applying binary search to calculate the position of 
    the data to be inserted doesn't reduce the time complexity of insertion sort. 
    This is because insertion of a data at an appropriate position involves two steps: 1. Calculate the position. 2. Shift the data from the position calculated in step #1 one step right to create a gap where the data will be inserted. 
    Using binary search reduces the time complexity in step #1 from O(N) to O(logN). But, the time complexity in step #2 still remains O(N). So, overall complexity remains O(N^2).
    5. **Best: O(N), Worst: O(N^2)**

## Counting Sort
* Inputs must be positive integers
* Used when the range of numbers is small.
* Counting sort assumes that each of the elements is an integer in the range 0 to k, for some integer k.
* Time complexity O(n + k) 
* Space complexity O(n + k)
* Stable
* Map objects to positive integers to do CS
* **How to:**
    1. Create an array with K elements
    2. Iterate through input array and count the elements of array
    3. Convert count array to summing array by summing its value and previous index value as the current value.
    4. Create a result array Iterate through input array and look at the current element and get its position by using 
    the summing array and decrement its index by one due to the fact that duplicate elements may occur.
    5. Repeat until input array is exhausted.

## Bucket Sort
* Store elements in buckets.
* Sort the buckets by *insertion sort.*
* The reason insertion sort is used in practice is that we expect the buckets to be small, and for small lists, insertion sort is much faster than anything else. Even when implementing merge sort or quicksort, insertion sort is used when the list gets small enough (say below 20 items or so).

## Selection sort

* **Selection sort**: 
    1. **O(N^2) worst case, O(N^2)** best; [E.g:](https://www.youtube.com/watch?v=g-PGLbMth_g)
    2. Find minimum from unsorted partition by iterating with minimum-finder algorithm with O(N), move it to sorted partition.
    3. Worst sorting algorithm.

## Bubble Sort

* **Bubble Sort:** 
    1. 1 4 5 7 2 3 -> 1 4 5 2 3 7 -> 1 4 2 3 5 7 -> 1 2 3 4 5 7
    2. Walk through the WHOLE array from left to right N times and swap the elements adjacent to each other on the iteration index.
    3. Takes the greatest element to the end of the array. Shortens the search range by one in each iteration.
    4. Could be optimised to break the loop if no elements are swapped during an iteration.
    5. **Best: O(N), Worst: O(N^2)**

##Recursion
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

* Recursion time complexity: [Example Here.](https://www.youtube.com/watch?v=gCsfk2ei2R8)
    1. **Substitution Method:** We make a guess for the solution and then we use mathematical induction to prove the the guess is correct or incorrect. K here is the step number. It is not and random number.

    2. **Recurrence Tree Method:** In this method, we draw a recurrence tree and calculate the time taken by every level of tree.The pattern is typically a arithmetic or geometric series.

    3. **Master Method:** Master Method is a direct way to get the solution. The master method works only for following type of recurrences or for recurrences that can be transformed to following type.
    T(n) = aT(n/b) + f(n) where a >= 1 and b > 1
   
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

## Hashtable And HashSet

* Hash Table is a data structure which organizes data using hash functions in order to support quick insertion and search.

* There are two different kinds of hash tables: hash set and hash map.

    1. The hash set is one of the implementations of a set data structure to store no repeated values.
    2. The hash map is one of the implementations of a map data structure to store (key, value) pairs.

* The hash function is the most important component of a hash table which is used to map the key to a specific bucket.  Ideally, a perfect hash function will be a one-one mapping between the key and the bucket. However, in most cases a hash function is not perfect and it is a tradeoff between the amount of buckets and the capacity of a bucket.

* Let's assume that the bucket, which holds the maximum number of keys, has N keys.
Typically, if N is constant and small, we can simply use an array to store keys in the same bucket. If N is variable or large, we might need to use height-balanced binary search tree instead.

* For some uses of hash tables, it's impossible to create them of the "right" size in advance, because it is not known how many elements will need to be held simultaneously during the lifetime of the table. If you want to keep fast access, you need to resize the table from time to time as the number of element grows. This resizing takes linear time with respect to the number of elements already in the table, and is usually done on an insertion, when the number elements passes a threshold.
These resizing operations can be made seldom enough that the amortized cost of insertion is still constant (by following a geometric progression for the size of the table, for instance doubling the size each time it is resized). But one insertion from time to time takes O(n) time because it triggers a resize.

* ***The load factor*** is the number of keys stored in the hash table divided by the capacity.
 
* The average time complexity of both insertion and search is still O(1). And the time complexity in the worst case is O(logN) for both insertion and search by using height-balanced BST. It is a trade-off between insertion and search.

* Duplicates are used to find with HashSet, and any problem relating to duplicates could maybe be solved with a hashSet.
 
* Checking if a key exists in a hashMap is O(1) due to hash function.

* ***Design The Key:***
    1. The choice of key is comparatively straightforward. Unfortunately, sometimes you have to think it over to design a suitable key when using a hash table.
    2. Actually, designing a key is to build a mapping relationship by yourself between the original information and the actual key used by hash map. When you design a key, you need to guarantee that
        1. All values belong to the same group will be mapped in the same group.
        2. Values which needed to be separated into different groups will not be mapped into the same group.
    3. This process is similar to design a hash function, but here is an essential difference. A hash function satisfies the first rule but might not satisfy the second one. But your mapping function should satisfy both of them.
    
## Disjoint Sets      
       
* Disjoint sets are used for computing equivalence relations.
Given a set S and a relation R, a R b, indicates that a is related to b with the relation R.

* An equivalence relation R satisfies the following properties
    * Reflexivity:
        * a R a, for all a in S
    * Symmetric:
        * a R b if and only if b R a
    * Transitivity:
        * a R b and b R c implies a R c
          
* Keep an array of N set identifiers, one for each item. The set that an element belongs to can be found in O(1) time.

* We want to have Find and Union methods, how could we make these.
    * Keep an array of N set identifiers, one for each item. The set that an element belongs to can be found in O(1) time. 0 0 1 1 2 1 3 3 - index numbers are object ID's
        1. Find is O(1) but Union is O(N) since union is done through iterating takes O(N). Suppose we union sets i and j.  Then we scan the array changing all j’s to i’s.
    * Better way is use ***a forest.*** Instead of tree nodes pointing to their children, these nodes will point to their parents! Union by making the parent of one tree’s root link to the root of the other tree
    * We represent a set of trees (a forest) implicitly using an array.
        * s[i] = -1 if i is a root.
        * s[i] = label of the parent if i is not a root.
    * Union can be implemented by making the parent link of one tree’s root link to the root node of the other tree.
        * -1 0 -1 1 0 Union 2 and 0 -> -1 0 0 1 0
        * A thing to note, the reason of needing nodes is that if we directly union two given numbers, we would miss out the other elements in the disjoint which is not the purpose of union. 
        All elements in both disjoint sets must be merged into one disjoint set.
        * Union operation takes O(1) time.
        * Find takes O(N) time. Time is proportional to the depth of the node for X.
        Worst Case: A tree of depth N-1 can result so the worst case time is O(N).
    * Optimize even further: 
    * ***Union By Rank:***
        * Rank is either height or size.
        * Union by size: If unions are done by size, the depth of any node is never more than log N. Initially the depth of a node is 0
        When its depth increases as the result of a union, it is placed in a tree at least twice as large as before.
        Thus the depth can be increased at most log N times.
            * Find becomes O(log N)
            * S[i] is the index of the parent if i is NOT root.
            * S[i] is –Size of the tree with root i – indicates it is a root Size keeps the number of nodes.
                * For example: 6 3 3 -3 0 6 -4 -1
        * ***Proof of O(logN):*** Let say we have 8 nodes N = 8. So If we start from 1 (when no nodes are connected) we double it to get 2 (first time), double it to get 4 (second time), double it to get 8=N (3rd time).
        So it seems we can double at max 3 times or lg8 times to connect all nodes
        Depth of a node x increases by 1 if another tree(T2) which is larger or equal to the size of tree(T1) containing x is merged. So now the size of merged tree(T12) is atleast doubled. Now if one more larger tree(T3) is merged with T12, the size is again, atleast doubled(T123) and depth of x further increases by 1.
        * Union by height: If unions are done by height, the height of a tree increases (by 1) only when equally deep trees are unioned
        This can only happen log N times
            * Find becomes O(log N)
            * S[i] is the index of the parent if i is NOT root.
            * S[i] is –Height -1 of the tree with root i. – indicates it is a root
            Height is the is the height of the tree rooted at i
            -1 is necessary for trees of height
        * Tree grows in depth by one when equal depth trees are union together otherwise depth is kept same.
        * Proof is same intuition with union by size.
    * ***Path COMPRESSION:***
        Path compression is a technique for dynamically changing the data structure during a find operation. When we perform find(x), the parent of every node from x to the root is changed to root. So subsequent find operations run faster (we are speculating though!)
    * The basic idea (and hope) behind path compression is that we do some extra work during a find, and hope that this will speed up future find operations.
    * **Union-by-Rank + Path compression** leads to find and union both as O(α(N)) where α(N) is ***The Inverse Ackermann Function.*** - Definition: A function of two parameters whose value grows very, very slowly. -
    * α(N) <= 4 for all the practical purposes.
* Space complexity is O(N)

## Binary Search 

* ***Search Space:*** In its simplest form, Binary Search operates on a contiguous sequence with a specified left and right index. This is called the Search Space.

* Binary Search is generally composed of 3 main sections:
    1. Pre-processing - Sort if collection is unsorted.
    2. Binary Search - Using a loop or recursion to divide search space in half after each comparison.
    3. Post-processing - Determine viable candidates in the remaining space.

* Could be used to find the first occurrence of an element in a sorted array.

* Three templates explained in LeetCode.

## N-ary Tree

* In graph theory, an m-ary tree is a rooted tree in which each node has no more than m children. A binary tree is the special case where m = 2, and a ternary tree is another case with m = 3 that limits its children to three.

* Trie is one of the most frequently used N-ary trees.

## Trie

* Trie, also called prefix tree, is a special form of a Nary tree.

* Prefix -> A prefix of a string S is a substring of S that occurs at the beginning of S. "banana" -> "b", "ba", "ban"

* Suffix -> A suffix of a string S is a substring that occurs at the end of S. "banana" -> "a", "na", "ana"

* A Trie is a special form of a Nary tree. Typically, a trie is used to store strings. Each Trie node represents a string (a prefix). 

* Trie -> reTrieval [Video Explanation Here](https://www.youtube.com/watch?v=-urNrIAQnNo)
    1. A tree that stores strings. Used for string search such as prefix, suffix. [E.g](https://www.hackerrank.com/challenges/contacts/problem)
    2. Can be used for word validation such as when the user is typing a word we can look up trie to see if the word is valid and maybe even suggest to complete the words.
    3. A  well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. The crucial point here is that unlike a BST with numbers your comparison complexity at any node is not O(1) but instead O(m) (Since in the worst case your string at any node differs from your pattern at the last letter).
In the worst case you'll have to compare your pattern with O(log n) nodes.
    4. Using Trie, we can search the key in O(M) time. 
    5. Contains a HashMap (pointer of alphabet size - use hash to map chars to indexes    ) and a boolean in each node. Boolean for checking if the node is a word since it could also be a prefix.

* One important property of Trie is that all the descendants of a node have a common prefix of the string associated with that node. That's why Trie is also called prefix tree.

* Trie is widely used in various applications, such as autocomplete, spell checker, etc.

* First Solution - Array    
    1 .The first solution is to use an array to store children nodes.
    2. For instance, if we store strings which only contains letter a to z, we can declare an array whose size is 26 in each node to store its children nodes. And for a specific character c, we can use c - 'a' as the index to find the corresponding child node in the array.
    3. It is really fast to visit a child node. It is comparatively easy to visit a specific child since we can easily transfer a character to an index in most cases. But not all children nodes are needed. So there might be some waste of space.
    
* Second Solution - Map
    1. The second solution is to use a hashmap to store children nodes.
    2. We can declare a hashmap in each node. The key of the hashmap are characters and the value is the corresponding child node.
    3. It is even easier to visit a specific child directly by the corresponding character. But it might be a little slower than using an array. However, it saves some space since we only store the children nodes we need. It is also more flexible because we are not limited by a fixed length and fixed range.

* For example, as we know, each Trie node represents a string but not all the strings represented by Trie nodes are meaningful. If we only want to store words in a Trie, we might declare a boolean in each node as a flag to indicate if the string represented by this node is a word or not.

## Algorithmic Paradigms

* **Divide And Conquer:** Breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem. Because divide-and-conquer solves subproblems recursively, each subproblem must be smaller than the original problem, and there must be a base case for subproblems.
    1. Divide the problem into a number of subproblems that are smaller instances of the same problem.
    2. Conquer the subproblems by solving them _**recursively**_. If they are small enough, solve the subproblems as base cases.
    3. Combine the solutions to the subproblems into the solution for the original problem.
    
    
* **Dynamic Programming:**
    1. _**Optimal substructure**_  — optimal solution can be constructed from optimal solutions of its subproblems.
    2. _**Overlapping sub-problems**_  — problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems.
    3. Once these two conditions are met we can say that this divide and conquer problem may be solved using dynamic programming approach.
    3. Requires i. and ii. and could also have extra methodologies either _**Memoization**_(Top-Down) or _**Tabulation**_(Bottom-Up)
    4. _**Memoization (uses top-down cache filling):**_  **Memoization** is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. The memoization technique is a good example that demonstrates how one can reduce compute time in exchange for some additional space. It starts with the highest-level subproblems (the ones closest to the original problem), and recursively calls the next subproblem, and the next. We save time when a subproblem A recurses into a subproblem B that has already been called. Since B and all subproblems below it are memoized, we can avoid repeating the entire recursion tree generated by B, saving a lot of computation.
    5. _**Tabulation (uses bottom-up cache filling):**_ It starts by solving the lowest level subproblem. The solution then lets us solve the next subproblem, and so forth. We iteratively solve all subproblems in this way until we’ve solved all subproblems, thus finding the solution to the original problem. We save time when a subproblem needs the answer to a subproblem that has been called before, and thus has had its value tabulated.
    6. The major differences between tabulation and memoization are:
        1. Tabulation has to look through the entire search space; memoization does not.
        2. Tabulation requires careful ordering of the subproblems is; memoization doesn’t care much about the order of recursive calls.
        3. If the original problem requires all subproblems to be solved, tabulation usually outperformes memoization by a constant factor. This is because tabulation has no overhead for recursion.
        4. If only some of the subproblems needs to be solved for the original problem to be solved, then memoization is preferrable since the subproblems are solved lazily, i.e. precisely the computations needed are carried out.
    7. Could be taught as dynamic programming is an extension of divide and conquer paradigm.

* Top-down and Bottom-Up are not the same in DP and BT algorithms. Top-down in DP means solving subproblems to solve the bigger problem where are in BT this is considered as bottom-up. (Imagine the execution tree.) 

## Greedy Algorithm

* **Greedy Algorithms:**
    * Solves a problem by doing what appears to be best (cheapest) thing at each step.
    * Not guaranteed to find the optimal solution.

## DFS
* Depth-first search = Depth increases gradually 

* DFS can suffer from stack overflow if the recursion number is too high. We can use a iterative stack version to overcome this since recursion limit is generally smaller than stack size limit. Python has 1000 as recursion limit by default.

* The first path you found in DFS is not always the shortest path.

* DFS and BFS could be written with same algorithm iteratively - using Queue(BFS), Stack(DFS)

* **Backtracking vs DFS:** [Answer Here!](https://stackoverflow.com/questions/49311627/intuition-behind-using-backtracking-and-not-dfs) 
    1. The difference between DFS and backtracking is subtle, but we can summarize like this: DFS is a technique for searching a graph, while backtracking is a problem solving technique (which consists of DFS + pruning, such programs are called backtrackers).
    2. Backtracking is far more efficient for solving some class of problems than the plain DFS.
The difference between DFS and backtracking is subtle, but we can summarize like this: DFS is a technique for searching a graph, while backtracking is a problem solving technique (which consists of DFS + pruning, such programs are called backtrackers). So, DFS visits each node until it finds the required value (in your case the target word), while backtracking is smarter - it doesn't even visit particular branches when it is certain that the target word would not be found there.
Imagine that you have a dictionary of all possible words and searching through the board to find all words that exist on the board (Boggle game). You start to traverse the board and stumble upon the letters 'J','A','C' in that order, so the current prefix is "JAC". Great. Let's look at the neighbors of the letter 'C', e.g. they are 'A', 'Q', 'D', 'F'. What would plain DFS do? It would skip 'A' because it came from that node to 'C', but it would then blindly visit each of the remaining nodes hoping to find some word, even though we know there are no words starting with "JACQ", "JACD" and "JACF". Backtracker would immediately prune branches with "JACQ", "JACD" and "JACF" by e.g. consulting an auxiliary trie data structure built from the dictionary. At some point even DFS would backtrack, but only when it does not have where to go - i.e. all surrounding letters have already been visited.
    3. The conventional DFS would for each node blindly check all neighbor nodes until it finds the target word or until all its neighbors are visited - it would only then backtrack. Backtracker on the other hand constantly checks whether we are on the "right track"
    4. DFS is a way to explore or traverse a graph. Uses the concept of going as deep as possible given the choices.
    Backtracking, while usually implemented via DFS, focuses more on the concept of pruning unpromising search subspaces as early as possible and stops the search when possible.
    5. Backtracking is used generally when we are asked to return a collection on valid answers rather than one answer.

## Backtracking 
* Could be thought as DFS + Pruning or optimized brute force.
* You can understand when a question is asking for a set of valid answers, this indicates that the question could be a backtracking quesiton.
* We have 3 keys to identify to write a backtracking algorithm. Model the problem in a ways such that:-
    1. _Our Choice:_ In each iteration we should identify what to do to our current process.
    2. _Our Constraint:_ Identify constraints to decide when to prune the backtracking and explore new paths.
    3. _Our Goal:_ Means when we have successfully reached a goal and we should add the current path to the results list.
    
## BFS

* Breadth-first search = Breadth increases gradually - Check the code for the Binary Search Tree.

## Graph Theory

* ***A graph G= (V, E)*** consists of
    1. A set of ***vertices*** (sometimes referred as Node), V, and
    2. A set of ***edges***, E.

* Each edge is a pair (v,w) where v and w are vertices.  Edges are sometimes referred to as arcs.

* In graph theory, ***a tree*** is an undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic undirected graph
    * What this means is that a tree refers to the usual known tree reference but only this time the edges are bidirectional making the whole tree as undirected graph.
    * "Tree" can also mean just an ***"acyclic connected graph"***.
    
* If the pair of vertices in an edge is ordered, then the graph is a directed graph (digraph).

* In an undirected graph with an edge (v,w), v is adjacent to w and w is adjacent to v.

* Sometimes an edge has a third component (v,w,weight).

* ***A path*** in a graph is a sequence of vertices w1,w2,w3,...wN such that (wi,wi+1) in E.

* The length of a path is the number of edges on a path (= N-1)

* ***A simple path*** is a path in a graph which does not have repeating vertices.

* ***A cycle*** in a directed graph is a path of length at least 1 such that w1= wN

* A directed graph with no cycles is called ***a directed acyclic graph (DAG)***

* An ***undirected graph*** is ***connected*** if there is a path from every vertex to every other vertex.

* A ***directed graph*** is ***strongly connected*** if there is a path from _u to w_ and _w to u_ for all vertices.

* ***A complete graph*** is a graph in which each pair of graph vertices is connected by an edge.
    1. In undirected graphs each vertex has n-1 edges
    2. In directed graph each vertex has 2 * (n-1) edges, in and out.

* ***Degree of a vertex (undirected graphs)***
    1. Number of edges incident on the vertex.

* ***In-degree of a vertex (digraphs)***
    1. Number of edges coming to a vertex

*   ***Out-degree of a vertex (digraphs)***
    1. Number of edges going from a vertex

* We can represent graphs by using a number of different representations:
    1. **Adjacency Matrix representation:**
        1. We use a 2-dimensional array of boolean values.
        2. A[i][j] = true(1) if (i,j)in E, 0 otherwise. 
        3. A[i][j] = weight if (i,j) in E, float("inf") otherwise. 
        4. The adjacency matrix representation uses O(|V|2) space.
        5. You can easily check if an edge exists or not in O(1) time.
        6. If the graph is sparse, the matrix will have a large number of 0 elements: 
            1. too much wasted space.
            2. We are allocating memory to represent data that is actually not there. (Not good!)
        7. Adjacency matrix representation is very easy to implement.

    2. **Adjacency List representation:**
        1. If the graph is sparse, a better (spacewise) alternative is the adjacency list representation.
        For each vertex we keep a list of the edges emanating from that vertex.
        For undirected graphs, we only need to keep the edge once.
        2. Total memory for adjacency lists is O(|E|)
        3. Total memory for array of pointers is O(|V|)
        4. Total memory for adjacency list representation is O(|V|+|E|) which is linear in the size of the graph.
        5. If the edges have weights they can be stored in the list elements.
        6. The vertices may have labels which are not integers
            1. Use a hash table to map names to integers.
            2. Use these integers to access the adjacency list vector.
        7. For undirected graphs we only keep the edges (v, w) where v < w.
            1. To see if an edge (v, w) exists where v > w, we look up to see if (w,v) exists.
        8. Adjacency list representation is exactly the same data structure for hash tables with separate chaining.

* We define the density of a graph G as D=|E| / M, where M is the maximum number of possible edges in G.
    1. For undirected graphs, there can be at most M=|V|(|V|-1)/2 edges.
    2. For digraphs, there can be at most M=|V|(|V|-1) edges.
    3. If D is close to 1 then it is dense, if it is close to 0 then it is sparse.
    
### Topological sort
    
   1. Topological sort is an ordering of vertices in a directed acyclic graph.
   2. If there is a path from vi to vj then vj appears after vi in the ordering.
   3. How It Works:
        1. Select vertex with in-degree 0 or 
        1. Print it out
        1. Remove it
        1. Repeat
   4. Note that a topological sort is not (necessarily) unique. This stems from the fact that at any point, we may have more than one vertex with in-degree 0 and we have to choose one among them
   5. While iterating on the algo, there is a cycle if there isnt any single vertex with in degree of 0. Ex. 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 4, 4-> 0, 5-> 0. First 5 is taken out then we found out that there are no vertices with a in-degree of 0 therefore there is a cycle.
    
    
        void Graph::topsort( )
        {
            Vertex v,w;
            for (int counter=0; counter < NUM_VERTICES; counter++)
            {
                // find a vertex with in-degree = 0
                  v = findNewVertexOfDegreeZero( );
        
                // there is a cycle if no such vertex exists
                  if (v == NOT_A_VERTEX)
                    throw CycleFound();
        
                  v.topNum = counter;
                // the next loop depends on the graph representation
                   // so it is in pseudocode
                for each w adjacent to v
                    w.indegree --;
            }
        }
        
        
   1. The function findNewVertexOfIndegreeZero()
    Scans the array of vertices looking for a vertex with indegree 0 (which has not been assigned a topological sort number)
    It returns NOT_A_VERTEX if no such vertex exists (thus graph has a cycle)
    This function takes O(|V|) time. Since there are |V| calls, total time is O(|V|^2)
   2. O(N2) running time is because of the linear search through the vertices.
   3. If the graph is sparse only a very small number vertices have 0 indegree.
    Only keep track of 0-indegree vertices
    At the beginning, put all such vertices in a separate place,
    When you decrease the indegrees, if the indegree of a node reaches 0, put that also there.
        
            void Graph::topsort( )
            {
                Queue q (NUM_VERTICES);
                int counter = 0;
                Vertex v,w;
                // pseudocode for initialization
                for each vertex v 
                    if (v.indegree == 0)   q.enqueue(v);
                // Check vertices in the queues
                while ( ! q.isEmpty( ) ) {
                    v = q.dequeue( );
                    v.topNum = ++counter;
                    // put new 0 indegree vertices to queue
                    for each w adjacent to v
                        if (––w.indegree == 0)  q.enqueue( w);
                }
                // At the end, check for cycles
                if (counter != NUM_VERTICES)  throw CycleFound( );	  
            }
   1.Initialization is O(|V|)(O(|V|+|E|)if indegrees are computed)
    The while loop is executed at most  O(|V|) times but the for loop  body in the while loop is executed a total of O(|E|) times.

   2. Total time is O(|V|+|E|). 


### Detect Cycle in a undirected graph:
   1. **Union-Find:**
        1. Make V sets.
        2. Look at the edges and merge the sets that are connect the vertices. 
        3. If looked vertices are already in a set then there is a cycle.
        4. **Time complexity: O(V * α(V)) by using both union-by-rank + path compression.**
        5. **Space complexity: O(V)**

   2. **DFS:**
        1. Select a node, create a visited set.
        2. Add the node to the visited set. From that node DFS into each child while keeping track of parent node of the dfs'ed child. 
        3. Check if the child contains any childs that has a node in visited set. If so there is a cycle.
        4. Repeat until either a cycle is found or all nodes are in visited set.
        
* The cost of a path v1,v2,v3,...,vN   is called as the weighted path length (the unweighted path length is just N-1)

* Shortest paths are not defined if there is such a cycle with negative values in it.

* Single-source shortest path problem in ***an unweighted graph.***
    1. Given as input a unweighted graph G=(V,E), and a distinguished vertex s, find the shortest weighted path from s to every other vertex.
    2. Finding the shortest path to only ONE other vertex is not any easier, asymptotically.
    3. Apply BFS such as in 01 matrix problem.
    4. Do BFS and check whether distance to the found node could be updated with our iteration level.
    5. Run time: **O(|V| + |E|)**

### Dijkstra’s algorithm:
   
   1. Dijkstra's Algorithm allows you to calculate the shortest path between one node (you pick which one) and every other node in the graph
   2. Dijkstra's original algorithm does not use a min-priority queue and runs in time O(|V|^2) |V| is the number of nodes).
   3. A very important thing is to note that each edge is only processed once.
   4. The implementation based on a min-priority queue implemented by a Fibonacci heap and running O(|E| + |V| log |V|) where |E| is the number of edges).
   5. Naive version: Scan the table to find min. dv at each step: O(|V|) to find the minimum
   ,O(|V|^2) total. Time to update dw is constant. One update per edge for a total of  O(|E|) **TOTAL: O(|E|+ |V|^2) = O(|V|^2)**
   6. With a Heap:
    
            1  function Dijkstra(Graph, source):
            2      dist[source] ← 0                           // Initialization
            3
            4      create vertex set Q
            5
            6      for each vertex v in Graph:           
            7          if v ≠ source
            8              dist[v] ← INFINITY                 // Unknown distance from source to v
            9          prev[v] ← UNDEFINED                    // Predecessor of v
            10
            11         Q.add_with_priority(v, dist[v])
            12
            13
            14     while Q is not empty:                      // The main loop
            15         u ← Q.extract_min()                    // Remove and return best vertex
            16         for each neighbor v of u:              // only v that are still in Q
            17             alt ← dist[u] + length(u, v) 
            18             if alt < dist[v]
            19                 dist[v] ← alt
            20                 prev[v] ← u
            21                 Q.decrease_priority(v, alt)
            22
            23     return dist, prev

        a. findmin can be done by a deletemin: O(log|V|), decrease as decreasekey: O(log|V|) each - as many as |E|  of them
        **Total: O(|V|log|V| + |E|log|V|) = O(|E|log|V|)** since O(|V|+|E|) is O(|E|) due to for N node to be connect there must be at least N-1 edges.
        If fibonacci heap is used it has O(1) decreasekey so the algorithm can get as optimal as: **Total: O(|E| + |V|log|V|)**
        2. One can avoid descrease key with using the visited node further to check when extracting from the heap. This would also require
        adding all the edges to a heap that is found within a vertex. This would mean that the heap can get as big as O(|E|). 
        The time complexity would grow up to be **O(|V| * log(|E|) + |E| * log(|E|))**
    
   * If we use Fibonacci Heaps then the complexity turns out to be O(|E|+|V|log| V|) where as if Binary Heap (Min Heap) is used its O((|E| + |V|) log |V|)

### Dijkstra vs. BFS 
   
   * Dijkstra's algorithm relies on the property that the shortest path from s to t is also the shortest path to any of the vertices along the path. This is exactly what BFS does.
   * Or in another perspective: how would Dijkstra's algorithm behave if all the weights were 1? Exactly like BFS.

### Minimum Spanning Trees
   
   * Tree formed from graph edges that connects all the vertices at minimum total cost
   * tree because it is acyclic
   * removal of any edge breaks the cycle
   * spanning because it spans all the vertices

#### Prims Algorithm


#### DFS Graph

* [Example Here!](https://www.youtube.com/watch?v=fI6X6IBkzcw)

* Keep a visited array and iterate by DFS until a visited node is found or a dead end is met. Then backtrack until another DFs is possible and continue from there. Backtracking occurs due to the nature of the code.

* If the graph is directed, our initial node might not be able to cover all of the nodes so we need to check if the visited node contains all the nodes in the end if not, choice a random unvisited node and do DFS from there.

* If the graph is undirected, our initial node will be able to cover all the nodes unless the graph is unconnected. Then we would need to threat DFS from all nodes again.

* If implemented, visited array should be looped and for every unvisited node DFS should be called. Note that a call to DFs might affect the future calls such as making the nodes visited value true so that DFS will not be called on that node in future.

* If the graph is undirected each edge is checked twice due to both ends of edges checking the edge.

* **Time Complexity: O(|V| + |E|)**

#### BFS Graph

* [Example Here!](https://www.youtube.com/watch?v=pyNl0ESkH24)

* If the graph is directed, our initial node might not be able to cover all of the nodes so we need to check if the visited node contains all the nodes in the end if not, choice a random unvisited node and do BFS from there.

* We need to mark the nodes visited as soon as our algorithm reaches that node. Not when its turn in queue comes. This is due to the fact that nodes in the same level could also be neighbours and adding them when their turn in queue shows up could lead to nodes getting add up more than once in the queue. Example: A->B, A->C, B->C. 

* If the graph is undirected, our initial node will be able to cover all the nodes unless the graph is unconnected. Then we would need to threat BFS from all nodes again.

* If the graph is undirected each edge is checked twice due to both ends of edges checking the edge.

* If the graph is undirected each edge is checked twice due to both ends of edges checking the edge.

* **Time Complexity: O(|V| + |E|)**

* BFS implementations differ in two ways:
    1. Process children to visited when seen as a neighbour.
    2. Process children to visited when its their turn.
    * Approach 2 is used when each edge costs the same. Then when the neighbour is met during neighbour check it means that this is the most optimal
    way to reach that neighbour node. Examples in: 01 Matrix, Walls And Gates
    * This change happens when BFS used in a weighted graph. This is due to the fact that when a node is seen during neighbour check
    this doesnt not mean that it is the optimal way to reach there ex:
    
    
     # dijkstra - using bfs with approach 1 would yield a non optimal answer
          A
         4 6
        B   C
         5 2
          D
    
    * Dijkstra can also be implemented using approach one, check 1102. Path With Maximum Minimum Value.

## Behavioural Part

* Resume Walk-Through

* Current job -> Beginning of the career -> Go Towards Chronologically

* Quick shows of success

* Drive the interviewer with giving details of the projects that you took an interesting part

* Describe weaknesses, dont cover them

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

