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
    2. A  well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. The crucial point here is that unlike a BST with numbers your comparison complexity at any node is not O(1) but instead O(m) (Since in the worst case your string at any node differs from your pattern at the last letter).
In the worst case you'll have to compare your pattern with O(log n) nodes.
    3. Using Trie, we can search the key in O(M) time. 
    4. Contains a HashMap (pointer of alphabet size - use hash to map chars to indexes
    ) and a boolean in each node. Boolean for checking if the node is a word since it could also be a prefix.

* Inorder, Preorder, Postorder: Code Always Have Recursion(Left), Recursion(Right) stabled, only the print statement changes
    1. Inorder: Left First Then Root Then Right
    1. Preorder: Root First Then Left then Right 
    1. Postorder: Left Then Right Then Root
  
* Depth-first search = Depth increases gradually

* Breadth-first search = Breadth increases gradually - Check the code for the Binary Search Tree

* Binary-tree -> Recursion or Queues

* Bubble Sort -> until array is sorted - walk through and swap elements leading to number of times swapped - 1 4 5 7 2 3 -> 1 4 5 2 3 7 -> 1 4 2 3 5 7 -> 1 2 3 4 5 7

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

