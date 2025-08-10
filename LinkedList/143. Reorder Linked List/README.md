**143. Reorder Linked List**  
Link: [Reorder Linked List](https://neetcode.io/problems/reorder-linked-list?list=neetcode150)  
Difficulty: Medium
Topics: LinkedList

=======================================================================================

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000

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
