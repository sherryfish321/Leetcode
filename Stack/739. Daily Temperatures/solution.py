class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        # Loop through each day
        for i in range(len(temperatures)):
            # Check if the current temperature is higher than the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop() # Index of the previous lower temperature
                res[pre] = i - pre # Days waited for a warmer temperature
           # Push current index to the stack
            stack.append(i)
        return res
