**84. Largest Rectangle In Histogram**  
Link: [Largest Rectangle In Histogram](https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150)  
Difficulty: Hard  
Topics: Stack, Array

=======================================================================================

You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can there be zero-height bars?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- A monotonic increasing stack is used to track bar indices.
- When the current bar is less than the top of the stack, we start calculating areas.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Add a 0 to ensure all stack items are popped at the end.
  2. Iterate through the heights with index h
      - While the stack is not empty and the current bar is less than the top of the stack:
         - Pop the index from the stack
         - Compute the width:
           - If the stack is empty, width = h
           - Else, width = h - stack[-1] - 1
         - Compute area: width * height
         - Updata the maximum area
      - Append h to the stack
 3. Return maxArea
   
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(n), since the stack may hold up to n indices
