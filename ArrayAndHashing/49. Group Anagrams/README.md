**242. Group Anagrams**  
Link: [Group Anagrams](https://neetcode.io/problems/anagram-groups?list=neetcode150)  
Difficulty: Medium  
Topics: Array, Map, Sort

=======================================================================================

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Will the length of the string in a list be different?  
- Is there any time or space complexity requirement? 

Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Sort: We can sort characters in each word, and same anagram will have the same sorted string.
- Hashtable: We can use character frequency as a key, implemented as a fixed-length array.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First Idea:
1. Create a map
2. Iterate through the string. If the sorted string is already a key in the map, then append the string to the corresponding list. Else, create a new key-value pair.
3. Return the values as a list
- Improve my first idea: Iterate each string and use a hashtable to store different anagram groups, and use the character frequency as the key of each group.
1. Create a map
2. Initialize an array of size 26 to count the frequency of each character.
3. Convert the list to a tuple, and use it as the key of the dictionary, then appen the string to the corresponding list.
4. Return the values as a list

Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n * m)
Space Complexity: O(m)
