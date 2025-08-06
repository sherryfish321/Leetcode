**15. 3Sum**  
Link: [3Sum](https://neetcode.io/problems/three-integer-sum?list=neetcode150)  
Difficulty: Medium
Topics: TwoPointers, Sort

=======================================================================================

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement? Your solution must use O(1) additional space.
- Can the input array be empty?
- What should I output if there is no triplet? Ans. In Example 2, if there is no answer, we should return Output: []
- Do you know if the output array is sorted?
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Sort and Two Pointers: Sort enables skipping duplicates and allows efficient pointers swifting from both ends
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Sort the input array
  2. Create a result list
  3. Loop through the list and check if the num[i] is a duplicate, then skip the duplicates
  4. Initialize two pointers, the left pointer at the start of i+1, and the right pointer at the end of the array
  5. Check if the sum of the numbers pointed by the two pointers is equal to 0
     - If the total is equal to 0, append the triplet to the res list. Skip if nums[l] == nums[l + 1] and increment l by 1, or skip if nums[r] == nums[r - 1] and decrement by 1.
     - If the total is bigger than 0, decrement the right pointer by 1.
     - If the total is smaller than 0, increment the left pointer by 1. 
  6. After finishing, return the res list.

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n^2)
Space Complexity: O(n)

