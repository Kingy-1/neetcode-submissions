from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            temp[sorted_word].append(word)
                
        return list(temp.values())