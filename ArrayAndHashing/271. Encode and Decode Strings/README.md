**271. Encode and Decode Strings**  
Link: [Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode?list=neetcode150)  
Difficulty: Medium  
Topics: 

=======================================================================================

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Can the input array be empty?
- Is there any time or space complexity requirement?

Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- String manipulation: The problem involves using string in various ways, such as splitting strings, replacing characters, and building new strings. In this situation, the encode function replaces each string from the input list and builds a single encoded string. The decoding function deconstructs the single string and reconstructs it to the original input list.
- Delimiter-based parsing: The appropriate strategy here is length-prefixed encoding using a delimiter (e.g., "5*hello"). This ensures we can safely handle any characters in the string.
  
Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
- Encoding function:
  1. Create a single string
  2. For each string in the list, replace each string with {length}*{string}
  3. Joined all encoded elements together and returned them as a single string
- Decoding function:
  1. Create a list and initialize a pointer i = 0
  2. Move another pointer j forward until it finds the "*"
  3. The length of each word is slicing the substring from i to j, and converting it to an integer
  4. Append the slicing string(from j + 1 to j + 1 + length) to the list
  5. Move pointer i to the next segment and construct the original input list

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: 
- encode: O(m), where m is the total number of characters in the input list
- decode: O(m), since each character is scanned once
Space Complexity:
- encode: O(1) auxiliary space, O(m) output
- decode: O(n + m), where n is the number of strings, m is total character count

