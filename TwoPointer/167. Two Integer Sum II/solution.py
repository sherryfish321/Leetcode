class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        l, r = 0, len(numbers) - 1
        while l < r:
            # Check if the sum matches the target, then return the 1-based indices
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1] # Add 1 to convert from 0-based to 1-based index
            # If the sum is bigger than the target, decrement the right pointer  
            elif numbers[l] + numbers[r] > target:
                r -= 1
            # If the sum is smaller than the target, increment the left pointer
            else:
                l +=1
