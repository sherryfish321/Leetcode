**20. Valid Parentheses**  
Link: [Valid Parentheses](https://neetcode.io/problems/validate-parentheses?list=neetcode150)  
Difficulty: Easy  
Topics: Stack

=======================================================================================

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement? 
- Can the input array be empty?
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Stack: We can push opening brackets into the stack and pop only if matching closing brackets appear

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
  1. Create an empty stack
  2. Traverse each character in the string
     - If it is an opening bracket, push it to the stack
     - If it is a closing bracket:
       - Check if the stack is empty, return False
       - If the top of the stock matches the opening bracket -> Yes, pop -> No, return False
  3. After traversing, if the stack is mapped -> all matched -> return True
  4. Else, return False
  
Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(n)

