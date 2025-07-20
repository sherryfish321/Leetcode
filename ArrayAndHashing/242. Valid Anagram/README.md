**242. Valid Anagram**  
Link: [Valid Anagram](https://neetcode.io/problems/is-anagram?list=neetcode150)  
Difficulty: Easy  
Topics: Array, Hashmap  

=======================================================================================

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Can the input array be empty?  
- Is the array sorted?  
- Is there any time or space complexity requirement?  

Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Sort: Sort the array and check if the next number is equal to the previous number, then return True. Otherwise, run through the array and return False.
- HashSet: Store each number in a set. If the number is already in the set, then return True. Otherwise, run through the array and return False.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
1. Create an empty set.
2. If the current number already exists in the set -> return True. Else, store the number in a set.
3. Reach the end of the array without a duplicate number, then return False.  
- Mock Interview: I'll initialize an empty set. Then, as I iterate through the array, for each number, I check whether it already exists in the set. If it does, I return true immediately. Otherwise, I add it to the set.
If I reach the end of the loop without finding any duplicates, I return false.  

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(N)
Space Complexity: O(N)
