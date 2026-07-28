class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        sort the list
        nums = sorted(nums)
        longest_run = 0

        if len(nums) <= 1:
            return len(nums)
        
        # This value is the running longest score
        
        test = 0

        for index, value in enumerate(nums):
            if test is greater than current longest_run longest_run = test
            
            check if the next value is greater than current value
            so 
            if nums[index+1] = value + 1:
                test += 1
            else:
                test = 0

            if test > longest_run:
                longest_run = test
        
        return longest_run

        """

        temp = sorted(set(nums))
        longest_run = 1
        print(temp)

        if len(nums) <= 1:
            return len(nums)
        
        test = 1

        for index, value in enumerate(temp):
            #if test is greater than current longest_run longest_run = test
            
            #check if the next value is greater than current value
            #so
            print(f"This is the length {len(temp)}")
            print(f"This is the index: {index}")
            if index + 1 == len(temp):
                return longest_run
            
            if temp[index+1] == value + 1:
                print("good")
                test += 1
            else:
                print("bad")
                test = 1

            if test > longest_run:
                longest_run = test
        
        return longest_run
