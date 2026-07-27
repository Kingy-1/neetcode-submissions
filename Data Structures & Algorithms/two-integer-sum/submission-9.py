from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict()

        for i, num in enumerate(nums):
            complement = target-num
            if complement in temp.keys():
                return([temp[complement], i])
            temp[num] = i