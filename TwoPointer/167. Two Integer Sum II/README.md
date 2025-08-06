**167. Two Integer Sum II**  
Link: [Two Integer Sum II](http://neetcode.io/problems/two-integer-sum-ii?list=neetcode150)  
Difficulty: Medium
Topics: TwoPointers, Array

=======================================================================================

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement? Your solution must use O(1) additional space.
- Can the input array be empty?
- Can the output of two numbers not be in order?
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Two Pointers: Create two pointers, one at the start and another at the end of the array. If the sum of the numbers at the two pointers is greater than the target, decrement the right pointer; else, increment the left pointer. Continue this process until reach the target.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Initialize two pointers that represent the left and the right of the array.
  2. Check if the sum of the two numbers pointed to by the pointers is equal to the target.
     - If it is equal, add 1 to the index, since the question is 1-indexed, then return the answer.
     - If the sum is smaller than the target, increment the left pointer by 1.
     - Else, decrement the right pointer by 1.

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(1), since only two integer pointers are used. 


