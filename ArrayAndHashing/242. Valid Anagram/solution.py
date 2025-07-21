class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for i in list(s):
            count1[i] = count1.get(i, 0) + 1
        for j in list(t):
            count2[j] = count2.get(j, 0) + 1
        return count1 == count2

# improve the code by using at most 26 different characters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False

      count_s = {}
      count_t = {}
      
      for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1
      return count_s == count_t
        

        


