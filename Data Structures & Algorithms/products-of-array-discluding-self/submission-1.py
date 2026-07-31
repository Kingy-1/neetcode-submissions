class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        create list called ans

        For each number in nums:
            create another list called temp equalling nums
            pop the i'th number from temp
            ans.append(math.prod(temp))
            insert the i'th number from temp at the same index
        
        return ans
        """

        ans = []

        for index, number in enumerate(nums):
            temp = nums
            temp.pop(index)
            ans.append(math.prod(temp))
            temp.insert(index, number)
        
        return ans