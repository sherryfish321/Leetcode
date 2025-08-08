**206. Reverse Linked List**  
Link: [Reverse Linked List](https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150)  
Difficulty: Easy  
Topics: LinkedList, Recursion  

=======================================================================================

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000  

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can the input array have all the same elements?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- This is a common reverse problem, we can use three pointers: next, previous, current to slove 
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea(Iteration):
  1. Initialize a pointer prev = None, which will become the new tail of the reversed list.
  2. Loop through the list until the head becomes None.
  3. In each iteration:
     - Let curr = head, to hold the current node.
     - Move head forward to head.next to advance the loop.
     - Point curr.next to prev to reverse the link. <- This is the key operation
     - Move prev forward to curr. <- prev becomes the new head of the reversed list so far
  5. Return prev at the end  
     
- Second idea(Recursion):
  1. Base case: If the list is empty or has one node, return that node.
  2. Recursively call reverseList on the rest of the list.
  3. After reversing the rest, make head.next.next = head to reverse the link.
  4. Set head.next = None to break the original forward link.
  5. Return the new head (which comes from the deepest recursive call).  
  
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(1), no extra memory is used beyond a few pointers
