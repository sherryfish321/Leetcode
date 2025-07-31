class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum(): # isalnum(): python build-in function
                new += char.lower()
        return new == new[::-1]
      
# Improve the code by using two pointers(no more strings and datastructures)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers, left at the beginning, and right at the end
        l, r = 0, len(s) - 1
        while l < r:
            # Move left forward if the current character is not alphanumeric 
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move right backward if the current character is not alphanumeric
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return false
            # Update and move both pointers inward
            l, r = l + 1, r - 1
        return true
    
    def alphaNum(self, c)
        return (ord("A") <= ord(c) <= ord("Z") or #Uppercase letters
                ord("a") <= ord(c) <= ord("z") or #Lowercase letters
                ord("0") <= ord(c) <= ord("9")) # digits
      #ore(): converts an integer Unicode code point to its corresponding character
