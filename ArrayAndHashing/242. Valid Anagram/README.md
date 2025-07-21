**242. Valid Anagram**  
Link: [Valid Anagram](https://neetcode.io/problems/is-anagram?list=neetcode150)  
Difficulty: Easy  
Topics: HashTable, String  

=======================================================================================

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Can the input array be empty?  
- Will the length of the two arrays be different?  
- Is there any time or space complexity requirement?  

Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Hashtable: As we iterate through the string, we can store each character in a Hashtable. Therefore, if the character is already in the Hashtable, then its count is incremented by 1. Otherwise, we can add the character to the Hashtable and set it by 1.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
1. Create a Hashtable for s & t respectively.
2. Iterate through the string. If the character is already in the Hashtable, count += 1. Else, add the character to the Hashtable and its count = 1.
3. Compare two Hashtable.

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n + m)
Space Complexity: O(1)
