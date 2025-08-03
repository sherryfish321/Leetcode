class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            # Current container area
            area = width * height
            # Update max_area if the current one is greater
            max_area = max(area, max_area)
            # Move the pointer to the shorter line inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
