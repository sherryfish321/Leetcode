**125. Valid Palindrome**  
Link: [Valid Palidrome](https://neetcode.io/problems/is-palindrome?list=neetcode150)  
Difficulty: Easy
Topics: TwoPointers, String

=======================================================================================

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- Can the input array be empty? Yes, the result should be true
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Reverse String: The method is removing non-alphanumeric characters, then compare cleaned string with it reverse version.
- Two Pointers: Skip non-alphanumeric characters, compare characters from both ends toward the center, and lowercase during comparison

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea(This method uses extra memory O(n)):
  1. Create a new empty string
  2. Loop through each character in the string. If it is alphanumeric, append its lowercase form to the empty string.
  3. Compare the new string with its reverse, and return the result

- Implementation:
  1. Create two pointers, left and right, at the start and the end of the string
  2. While l < r:
    1. move l forward if s[l] is not alphanumeric, or move r backward if s[r] is not alphanumeric
    2. Compare s[l] and s[r] in lower case
    3. If it does not match, return false. Else, move both pointers inward
  3. If all matches, return true 

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(1), since no extra created


