class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}         
        l = 0
        longest = 0

        for r, ch in enumerate(s):
            if ch in temp and temp[ch] >= l:
                l = temp[ch] + 1

            temp[ch] = r
            longest = max(longest, r - l + 1)

        return longest
