class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for number in numSet:
            # Check if number is the start of the sequence
            if (number - 1) not in numSet:
                # we reached the first number in a sequence
                length = 0
                while(number + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest