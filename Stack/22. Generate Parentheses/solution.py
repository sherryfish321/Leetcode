class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current, open, close):
            # pring(len("(())")) --> 4
            if len(current) == n * 2:
                res.append(current)
                return
            # Can add "(", if we haven't used up all open brackets
            if open < n:
                backtrack(current + "(", open + 1, close)
            # Can add ")" only if close brackets are smaller than open brackets
            if close < open:
                backtrack(current + ")", open, close + 1)
        # Start the backtracking process at open = 0 and close = 0
        backtrack("", 0, 0)
        return res
        
