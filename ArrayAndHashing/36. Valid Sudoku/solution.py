from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to trach seen numbers in rows, cols, boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # Check for duplicates in current row, col, box
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[r//3, c//3]):
                    return False
                # Add the number to the correspoding row, col, box
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[r//3, c//3].add(board[r][c])
        return True
