**21. Merge Two Sorted Lists**  
Link: [Merge Two Sorted Lists](https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode150)  
Difficulty: Easy  
Topics: LinkedList, Recursion  

=======================================================================================

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Are the input lists always sorted in ascening order?
- Can one or both lists be empty?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- We can use two pointers list1 and list2 to track.
- Use a dummy node to simplify operation.
- Always put the smaller current node to the merged list.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea(Iteration):
  1. Creata a dummy node as a start of the merged list.
  2. Use tail pointer to track the last node in the merged list.
  3. While both lists are not empty:
     - Compare list1.val and list2.val
     - Append the smaller one to tail.next
     - Move that list's pointer forward
     - Move the tail forward (This moves the tail pointer so next insertion happens at the end of the list)
  4. After the loop, one list might still have nodes left. Append the remaining list directly to the tail.next
  5. Return dummy.next (Dummy just a placeholder, the real head starts at dummy.next)
     
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n + m), since each node is visited exactly once
Space Complexity: O(1), because only dummy and tail are extra
