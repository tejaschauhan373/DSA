# Time Complexity of Operation on different data structure & Approaches

## Useful resources

1. [Python wiki for complexity of data structure](https://wiki.python.org/moin/TimeComplexity)
2. [Concept of binary tree](https://www.geeksforgeeks.org/difference-between-full-and-complete-binary-tree/)
3. [Complexity Analysis of Recursion](https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/1669/)
4. [Dynamic Programming](https://leetcode.com/explore/featured/card/dynamic-programming/630/an-introduction-to-dynamic-programming/4034/)

## List of Data Structure and its Time Complexity

1. List
    1. Push : O(1) -> at end, O(N) -> at starting
    2. Pop :  O(1) -> at end, O(N) -> at starting
    3. Get Item : O(1)
    4. Get length : O(1)
       <br>

2. Dictionary
    1. Set Item : O(1)
    2. Delete Item : O(1)
    3. Get Item : O(1)
       <br>

3. Set
    1. Insert Item : O(1)
    2. Delete Item : O(1)
    3. Get Item : O(1)
       <br>

4. Singly Linked List:
    1. Push : O(N) -> at end, O(1) -> at starting
    2. Pop :  O(N) -> at end, O(1) -> at starting
    3. Get Item : O(N)
    4. Get length : O(N)
       <br>

5. Binary Tree
    1. Get Item : O(N) ; N = Total Nodes in Binary Tree
    2. Insertion : O(N) ; N = Total Nodes in Binary Tree
    3. Deletion : O(N) ; N = Total Nodes in Binary Tree
       <br>

6. Binary Search Tree
    1. Get Item : O(H) ; H = Height in Binary Tree
    2. Insertion : O(H) ; H = Height in Binary Tree
    3. Deletion : O(H) ; H = Height in Binary Tree
       <br>

7. Heaps & Priority Queue:
    1. Push : O(LogN)
    2. PopMin/PopMax : O(LogN)
    3. GetMin/GetMax : O(1)
    4. Heap is complete binary tree, hence height is always O(LogN)
    5. In a max heap, the smallest element is always at a leaf node. So we need to check for all lead nodes for the
       minimum value. Worst case complexity will be O(N)
    6. Heap sort is efficient, consistent (Best TC = Average TC = The Worst TC) and uses minimum memory.

8. Trie:
    1. Insert : O(key length)
    2. Search : O(key length)
    3. The shape or the structure of trie will depend upon what data has been inserted, the order of insertion of
       different strings doesn't matter in case of trie.
    4. Looking up data in a trie is faster in the worst case, O(m) time of hash table.
    5. The worst-case lookup speed in an imperfect hash table is O(N) time, but far more typically is O(1), with O(m)
       time spent evaluating the hash.
    6. Some tries can require more space than a hash table.
    7. In trie, memory may be allocated for each character in the search string, rather than a single chunk of memory
       for the whole entry, as in most hash tables.
    8. Also, for each character creating a node takes more memory than storing the string directly.
    9. Trie can be useful for the following applications:
        1. Autocomplete Feature in Google Search
        2. Sorting a Set of Strings
        3. Full-text search

9. Graph:
    1. Most asked algorithms in interview:
        1. Graph Traversal, BFS, DFS
        2. Shortest Path
        3. Implicit Graphs (2D Matrix)
        4. Problems
    2. Graph can be represented in below two ways:
        1. Adjacency Matrix
            1. Space Complexity = O(V^2) ; N = number of vertices in graph
        2. Hash table with key as node and value as list of adjacent nodes;
            1. Space Complexity = O(V+E) ; V = no. of vertices in graphs, E = no. of edges in graphs