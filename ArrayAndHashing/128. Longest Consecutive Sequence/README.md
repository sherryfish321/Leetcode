**128. Longest Consecutive Sequence**  
Link: [Longest Consecutive Sequence](https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150)  
Difficulty: Medium  
Topics: Hashset, Array

=======================================================================================

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- What should I return for an empty array? 0
- What should I return if the array has no sequence? 0
- If there are duplicates in the sequence, what should I return?
- Can the input array be empty? Yes
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Hashset: It is a set-based lookup problem, related to hashing and prefix sequence building.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Convert the array to a set for lookup
  2. Iterate through each number, check if it is the start of the sequence
  3. If it is, use a while loop to count how far the sequence extends
  4. Track and update the maxmium of the sequence's length
  5. Return the longest length found


Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n), since each number is inserted into the set once
Space Complexity: O(n), since the set stores up to n distinct elements


