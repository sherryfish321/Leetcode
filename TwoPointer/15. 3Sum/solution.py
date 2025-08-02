class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Create a result list
        res = []
        # Sort the input array
        nums.sort()
        # Loop through the array
        for i in range(len(nums)):
            # Skip duplicate values for the first number and avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Create two pointers, one from the left, and one from the right 
            l = i + 1
            r = len(nums) - 1
          
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip the duplicates for the left pointer
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip the duplicates for the right pointer
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # Move both pointers to the next distinct elements
                    l = l + 1
                    r = r - 1
    
                elif total < 0:
                    l += 1
    
                else:
                    r -= 1
        return res
