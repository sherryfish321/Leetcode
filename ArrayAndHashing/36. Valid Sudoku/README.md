**36. Valid Sudoku**  
Link: [Valid Sudoku](https://neetcode.io/problems/valid-sudoku?list=neetcode150)  
Difficulty: Medium  
Topics: Hashset, Array

=======================================================================================

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:

![image](https://github.com/sherryfish321/Leetcode/blob/90f743d085b2cb2549b0ff098df5cfe52fb8541c/ArrayAndHashing/36.%20Valid%20Sudoku/sudoku.png)  
Input: board =   
[["1","2",".",".","3",".",".",".","."],  
 ["4",".",".","5",".",".",".",".","."],  
 [".","9","8",".",".",".",".",".","3"],  
 ["5",".",".",".","6",".",".",".","4"],  
 [".",".",".","8",".","3",".",".","5"],  
 ["7",".",".",".","2",".",".",".","6"],  
 [".",".",".",".",".",".","2",".","."],  
 [".",".",".","4","1","9",".",".","8"],  
 [".",".",".",".","8",".",".","7","9"]]  

Output: true
Example 2:

Input: board =   
[["1","2",".",".","3",".",".",".","."],  
 ["4",".",".","5",".",".",".",".","."],  
 [".","9","1",".",".",".",".",".","3"],  
 ["5",".",".",".","6",".",".",".","4"],  
 [".",".",".","8",".","3",".",".","5"],  
 ["7",".",".",".","2",".",".",".","6"],  
 [".",".",".",".",".",".","2",".","."],  
 [".",".",".","4","1","9",".",".","8"],  
 [".",".",".",".","8",".",".","7","9"]]  

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Is there any time or space complexity requirement?
- If inputs only contain ".", what should I return? False?
  
Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Hashset: When iterating through the array, we can store each number in a set. If the number is already in the hashset, then return false. Otherwise, add the number to the set. Then reach the end of the array and return true

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea:
1. Create three hashsets(viz defaultdict()) to track seen numbers for each row, each column, and each 3*3 box.
2. Travse the board by using two nested loops.
3. For each number:  
   - If the number is already in the set, then return false
   - Otherwise, add it to the respective set.
4. Reach the end of the array, and return true.

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(1), always fixed 81 numbers in a 9 X 9 board.
Space Complexity: O(1), fixed-size problem.

