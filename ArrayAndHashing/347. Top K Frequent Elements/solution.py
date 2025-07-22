# Firsh idea(Time complexity: O(N log N), space complexity: O(N))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1 
        sort_res = sorted(res.items(), key = lambda x : x[1], reverse = True) # x[1] = value, and the original sort is ascending. Use reverse = True change it to descending,
        result = [item[0] for item in sort_res[:k]] # item[0] = key(number) 
        return result

# Improve the code by using bucket sort, which has better efficiency(Time complexity: O(N), space complexity: O(N))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    fre = [[] for _ in range(len(nums) + 1)] #Initialize a frequency bucket, each bucket stores the number of that frequency.
    for num in nums:
        count[num] = count.get(num, 0) + 1 # Count the frequency of each number in the input array.
    for n, m in count.items(): # 
        fre[m].append(n) # Append the number to the bucket with index equal to the frequency.
    res = []
    for i in range(len(fre) -1, 0, -1): # Iterate from the highest frequency down to 1
        for num in fre[i]:
            res.append(num)
            if len(res) == k:
                return res

# Use Counter(Most fast, but not recommend to use at interview)
from collections import Counter
def topKFrequent(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]
