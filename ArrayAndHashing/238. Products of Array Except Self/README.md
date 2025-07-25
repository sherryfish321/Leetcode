**238. Products of Array Except Self**  
Link: [Products of Array Except Self](https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150)  
Difficulty: Medium  
Topics: Array

=======================================================================================

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Can the input array be empty?
  Ans: The minimum input has two numbers.
- Is there any time or space complexity requirement?

Match
> - See if this problem matches a problem category (e.g., Strings/Arrays) and strategies or patterns within the category
- This is a prefix and suffix problem. We can create two lists to solve the problem. One list stores the product of all the numbers to the left of each element, and another one stores the product of all the numbers to the right of each element. By multiplying the two lists, we can get the result.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
1. Create an oupur array with n numbers 1
2. First Pass(prefix):
   - Travel from left ot right
   - At each index i, store the product of all elements to the left of i
   - Use a variable prefix to track the cumulative product
4. Second Pass(suffix):
   - Travel from right to left
   - At each index i, store the product of all elements to the right of i
   - Use a variable suffix to track the cumulative product  

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(n)
