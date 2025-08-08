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
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Sort the cars by positioning in descending order
- Use a stack to keep track of the fleets by storing the time each car needs to reach the target
- If a car reaches later than the car before it, then it forms a new fleet
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Pair each car's position and speed using zip().
  2. Sort the cars based on their starting position in descending order.
  3. Compute the time each car takes to reach the target.
  4. Use a stack to count fleets:
     - If the current car takes longer than the car ahead of it, it can not catch up, so it is a new fleet. -> push onto the stack
     - If the current car takes less or equal, it joins the previous fleet. -> do not push onto the stack
  5. Return the number of fleets using len(stack)
   
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(nlogn)
Space Complexity: O(n)
