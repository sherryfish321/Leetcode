**42. Trapping Rain Water**  
Link: [Trapping Rain Water](https://neetcode.io/problems/trapping-rain-water?list=neetcode150)  
Difficulty: Hard
Topics: TwoPointers, Array

=======================================================================================
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
![image]()

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000


=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement? 
- Can the input array be empty? No, there is exactly one solution.
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Two Pointers: We can use two pointers from both ends, and move the pointer to the shorter line
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. I
  
Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(1), since no extra space used

