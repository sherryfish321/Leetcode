**739. Daily Temperatures**  
Link: [Daily Temperatures](https://neetcode.io/problems/daily-temperatures?list=neetcode150)  
Difficulty: Medium  
Topics: Stack, Array

=======================================================================================

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can temperatures repeat?
- What if the array only has one element?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- A monotonic decreasing stack is an efficient strategy to solve such problems
- The stack stores the indices of unresolved temperatures. As we iterate through the list, whenever we encounter a higher temperature than the one at the top of the stack. We know the current temperature is the "next warmer day".
- This avoids using a nested loop and ensures each temperature is only pushed and popped at most once
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Create a result array of 0
  2. Initialize a stack to keep track of indices whose warmer temperatures haven't been found yet
  3. Iterate through the temperatures:
     - While the current temperature is higher than the top of the stack
       - Pop from the stack and calculate the day waited
       - Update the result for that index
     - Puch current index onto the stack   
  
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n), since each element is pushed and popped at most once
Space Complexity: O(n)
