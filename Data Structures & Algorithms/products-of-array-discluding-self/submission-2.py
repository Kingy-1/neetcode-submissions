class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        for index, number in enumerate(nums):
            temp = nums
            temp.pop(index)
            ans.append(math.prod(temp))
            temp.insert(index, number)
        
        return ans