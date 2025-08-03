**11. Container With Most Water**  
Link: [Container With Most Water](https://neetcode.io/problems/max-water-container?list=neetcode150)  
Difficulty: Medium
Topics: TwoPointers, Sort

=======================================================================================
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
![iimage]()



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

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

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n^2)
Space Complexity: O(n)

