from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a tuple of the letters in s and t
        # sort that tuple
        # Store the tuple as a key and the word as a value
        # if the dictionary has a length of 2 return False
        # else return true

        temp = defaultdict(list)

        sorted_s = tuple(sorted(s))
        sorted_t = tuple(sorted(t))

        temp[sorted_s].append(s)
        temp[sorted_t].append(t)

        if len(temp) > 1:
            return False
        
        return True