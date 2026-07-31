class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        create list called ans
        for each index, number in enumerate(nums):
            temp = 1
            we want to loop through nums skipping every number that
            is the same as the index we are currently at
                temp *= (number we are currently at in the inner loop)
            ans.append(temp)
        return ans
        """

        ans = []

        for index, number in enumerate(nums):
            temp = 1
            for i, num in enumerate(nums):
                if index != i:
                    temp *= num
            ans.append(temp)
        
        return ans