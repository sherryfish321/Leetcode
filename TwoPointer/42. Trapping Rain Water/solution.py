class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        # Track the maximum height to the left and right of the current pointers 
        l_max, r_max = 0, 0
        # Travse until pointers meet
        while l < r:
            # Always process the smaller side
            if height[l] < height[r]:
                if height[l] < l_max:
                    # Accumulate water
                    water += l_max - height[l]
                else: 
                    # Update left_max if the current wall is taller
                    l_max = height[l]
                l += 1
            # Repeat the same logic on the right side
            else:
                if height[r] < r_max:
                    water += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        return water
