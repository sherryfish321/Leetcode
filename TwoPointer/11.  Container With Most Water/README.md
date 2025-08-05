**11. Container With Most Water**  
Link: [Container With Most Water](https://neetcode.io/problems/max-water-container?list=neetcode150)  
Difficulty: Medium
Topics: TwoPointers

=======================================================================================
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
![iimage](TwoPointer/11.  Container With Most Water/Example.png)  
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
- Is there any time or space complexity requirement? 
- Can the input array be empty? No, there is exactly one solution.
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Two Pointers: We can use two pointers from both ends, and move the pointer to the shorter line
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Initialize two pointers from both ends
  2. While l < r
     - Calculate the width: r - l
     - Calculate the height: min(heights[r], heights[l])
     - Calculate the area: width * height
     - Update the maximum area
     - Move the pointer to the shorter line
  3. After finishing, return the max_area
  
Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(1), since no extra space used

