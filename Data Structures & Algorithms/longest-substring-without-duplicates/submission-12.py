class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        temp = {}

        for r, letter in enumerate(s):
            if letter in temp and temp[letter] >= l:
                l = temp[letter] + 1
            
            temp[letter] = r
            longest = max(longest, r - l + 1)

        return longest