class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The goal is to get the longest consecutive sequence of elements
        Each element in the sequence must be 1 larger than the previous

        We want to find anything unique about the question:
        For each sequence there is no number in nums that is 1 less than
            the starting number
        
        For each sequence there is no number in nums that is 1 more than
            the last number
        
        If you can find the last number of a sequence and the first number
            of a sequence you can simply subtract the two and add one to
            get the length of the sequence
        
        Add each length to a list and return the max value of that list
        """

        numSet = set(nums)
        longest = 0

        for number in numSet:
            # Check if number is the start of the sequence
            if (number - 1) not in numSet:
                # we reached the first number in a sequence
                length = 1
                for num in numSet:
                    # If the (number + 1) is in the set add 1 to length
                    # Increase number by 1
                    if (number + 1) in numSet:
                        length += 1
                        number += 1
                    else:
                        if length > longest:
                            longest = length
                        break

        return longest 
                