class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)    
        # Step 1: Initialize the output array with 1s
        output = [1] * n
        # Step 2: First Pass (prefix)
        prefix = 1
        # Compute the product of all elements to the left of each index
        for i in range(n):
            output[i] *= prefix      # Set output[i] to the product of all previous elements
            prefix *= nums[i]        # Update prefix to the num[i] for the next iteration
        # Step 3: Second Pass (suffix)
        suffix = 1
        # Compute the product of all elements to the right of each index
        for i in range(n-1, -1, -1): # Travse from the end of the array to the beginning
            output[i] *= suffix      # Set output[i] to the product of all elements from right  
            suffix *= nums[i]        # Update suffix to the num[i] for the next iteration
        return output
