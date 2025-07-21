class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cha = defaultdict(list)
        for i in strs:
            sorted_i = " ".join(sorted(i)) #"tatto" -->-- ["a", "o", "t", "t", "t"] -->-- join --> "aottt"
            cha[sorted_i].append(i) 
        return list(cha.values()) # retrieve all the values of the map and turn them into a list of lists

# Improve the code with better time and space complexity
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        # Initialize a count list for all 26 letters of the alphabet
        count = [0]  * 26
        # Count the frequency of each letter in the string
        for c in count:
            # Use the count list as a key of the dictionary
            count[ord(c) - ord(a)] += 1
        # Convert the count list to a tuple to make it hashable and use it as a dictionary key. Next, append the string to the list corresponding to the key of the dictionary.
        res[tuple(count)].append(s)
    return list(res.values())
        
