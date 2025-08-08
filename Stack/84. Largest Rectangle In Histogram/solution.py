class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0) # Sentinel: Ensure all elements in the stack are processed
        for h in range(len(heights)):
            while stack and heights[h] < heights[stack[-1]]:
                height_index = stack.pop() # Index of the bar to compute area with
                height = heights[height_index] # Height of the popped bar
                if not stack:
                    width = h
                else:
                    width = h - stack[-1] -1 # Width between current and previous bar
                maxArea = max(maxArea, width * height)
            # Push current bar index to the stack
            stack.append(h)
        return maxArea
        
