**22. Generate Parentheses**  
Link: [Generate Parentheses](https://neetcode.io/problems/generate-parentheses?list=neetcode150)  
Difficulty: Medium  
Topics: Stack, String

=======================================================================================

You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can the output array be disordered?
- Can duplicates appear?
- What is the definition of "well-formed"?
    
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Backtrack: This is a backtracking problem, which can ensure all valid combinations of parentheses are generated.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Use recursion to build each string
  2. Keep track of open(number of "(") and close(number of ")")
  3. If open < n -> add "(" -> open + 1
  4. If close < open -> add ")" -> close + 1
  5. When the string reaches length 2*n, add it to the result
  
Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(4ⁿ / √n)
- The actual number of valid combinations of n pairs of parentheses is the Catalan number(O(4ⁿ / √n)).  
  This is the number of valid strings, which equals the number of recursive paths explored.
Space Complexity: O(n)
