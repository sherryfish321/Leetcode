**88. Merge Sorted Array**  
Difficulty: Easy
Topics: Array, Sort

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time complexity reqirement?
- 

Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- This problem matches the merge and sort methods.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
1. Write the elements of num2 into the end of the num1
2. Sort num1 list

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O((n+m)log(n+m))
The cost of sorting a list of length x using a built-in sorting algorithm is O(xlogx).  
Because in this case, we're sorting a list of length m+n, we get a total time complexity of O((n+m)log(n+m)).
Space Complexity: O(n)
