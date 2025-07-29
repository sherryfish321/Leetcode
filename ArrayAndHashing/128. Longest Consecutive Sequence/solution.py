class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookup time
        set_num = set(nums)
        # Variable to store the length of the longest consecutive sequence
        longest = 0
        for num in nums:
            # Ensure the number is a start of the sequence
            if (num - 1) not in set_num:
                # Initialize the length of the current sequence
                length = 1
                # Check if the next number exists, then add 1 to the length
                while (num + length) in set_num:
                    length += 1
                # Update the new longest value
                longest = max(longest, length)
        return longest
