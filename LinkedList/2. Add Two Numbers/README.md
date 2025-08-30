**2. Add Two Numbers**  
Link: [Add Two Numbers](https://neetcode.io/problems/add-two-numbers?list=neetcode150)  
Difficulty: Medium
Topics: LinkedList

=======================================================================================

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:

Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can the input array be empty?
- Does the linked list have a cycle?
- Can the input lists have different lengths?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- We can use two pointers to traverse the two lists, dummy head to simplify building the result, and a carry variable to propagate overflow.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Create a dummy node and a cur pointer that appends new result nodes
  2. Maintain carry = 0
  3. While any of l1, l2, carry remains:
     - Read current digit v1 and v2
     - Compute the sum = v1 + v2 + carry
     - Update carry = val // 10 and val = val % 10
     - Append val as a new node to the result
  4. Return dummy.next
  
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Time Complexity: O(m + n), where m is the length of l1 and n is the length of l2
Space Complexity: O(1)
