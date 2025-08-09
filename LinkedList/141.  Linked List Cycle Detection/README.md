**141. Linked List Cycle Detection**  
Link: [Linked List Cycle Detection](https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150)  
Difficulty: Easy  
Topics: LinkedList, Recursion  

=======================================================================================

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1

Output: false
Constraints:

1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can the input list be empty?
- Can there be only one node?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- We can use two pointers fast and slow to slove this problem, slow pointer moves one step and fast moves two steps forward at a time.
- If there is a cycle, they will eventually meet. Else, the fast or fast.next will become None.
- This is Floyd's Tortoise and Hare Algorithm.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Iitialize two pointers fast and slow, both pointing to head.
  2. Loop while the fast and fast.next are not None:
     - Move slow one step forward
     - Move fast two steps forward
     - If slow == fast, return True
  3. If loop ends without meeting, return False.
     
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Time Complexity: O(n), each node is visited at most twice
Space Complexity: O(1), only two pointer used
