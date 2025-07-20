class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preMap = {}
        for i, n in enumerate(nums):
            if n in preMap:
                return True
            preMap[n] = i
        return False
      
# improve the code by using hash set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        
