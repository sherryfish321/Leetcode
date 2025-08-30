**138. Copy Linked List with Random Pointer**  
Link: [Copy Linked List with Random Pointer](https://neetcode.io/problems/copy-linked-list-with-random-pointer?list=neetcode150)  
Difficulty: Medium
Topics: LinkedList, HashMap

=======================================================================================

You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Example 1:

Input: head = [[3,null],[7,3],[4,0],[5,1]]

Output: [[3,null],[7,3],[4,0],[5,1]]
Example 2:

Input: head = [[1,null],[2,2],[3,2]]

Output: [[1,null],[2,2],[3,2]]


=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can the input array be empty?
- Does the linked list have a cycle?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- This problem involves a linked list and a hash mapping. We need to copy the graph-like structure and maintain a mapping between old and new nodes.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  We use a two-pass approach with a HashMap
  1. Create a map from old nodes to new nodes
     - Traverse the linked list, and for each original node, create a new node with the same value
     - Store the mapping oldNode -> newNode in the dictionary
  3. Assign pointers
     - Traverse the list again
     - For each copy, set its copy's next and random using the dictionary
       copy.next = map[old.next]
       copy.random = map[old.random]
  5. Return the copy of the head
  
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Time Complexity: O(n), because of two pass approach
Space Complexity: O(n)
