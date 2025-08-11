**19. Remove Nth Node From End of List**  
Link: [Remove Nth Node From End of List](https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode150)  
Difficulty: Medium
Topics: LinkedList

=======================================================================================

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Is the input array always in ascending order?
- Can there be only one node?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- We can use two pointers fast and slow to slove this problem, slow pointer moves one step and fast moves two steps forward at a time.
- Reverse the second half.
- Merge two lists by alternating nodes.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Use slow and fast pointer to find the middle of hthe list.
  2. Iteratively reverse the list starting at second, producing the prev as the head of the reversed half list.
  3. With first = head and second = prev, repeatedly take one node from first, then one node from second, until second is exhausted.
     
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Time Complexity: O(n), each node is visited a constant number of times.
Space Complexity: O(1), no extra space.
