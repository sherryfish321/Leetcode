**150. Evaluate Reverse Polish Notation**  
Link: [Evaluate Reverse Polish Notation](https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150)  
Difficulty: Medium  
Topics: Stack, Array

=======================================================================================

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can we assume the stack will always have two elements when we encounter an operator?
  Ans. Yes, valid RPN means every operator follows exactly two operands.
- Are all operands integers?
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Stack: This is a stack-based problem. We can push numbers onto the stack. When we encounter an operator, pop two numbers, compute, and push the result back.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Create an empty stack
  2. Traverse each token in tokens
     - If it is a number -> convert to int -> push onto the stack
     - If it is an operator -> pop two numbers and apply the operator -> push the result back
  3. At the end, the only element left in the stack is the answer
  
Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(n)
