class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for index, value in enumerate(nums):
            for j, val in enumerate(nums):
                if j <= index:
                    continue
                if val + value == target:
                    return[index, j]
        
        return ans
