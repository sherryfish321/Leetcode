class Solution:
    def encode(self, strs: List[str]) -> str:
        encodestring = ""
        for s in strs:
            encodestring += f"{len(s)}*{s}" # "neet" -->-- "4*neet"
        return encodestring
      
    def decode(self, s: str) -> List[str]:
        decodelist = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "*": # Move j forward until we find the "*"
                j += 1
            length = int(s[i:j]) # Extract the number of length between i and j, e.g. j = 1 -->-- "*" & i = 0 -->-- s[0:1] = 4 
            word = s[j+1 : j+1+length] # s[2:6] -->- "neet"
            decodelist.append(word) 
            i = j + 1 + length #Move i to the start of the next encoded word segment
        return decodelist

