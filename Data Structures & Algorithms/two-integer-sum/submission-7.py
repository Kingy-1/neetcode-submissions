from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        temp = defaultdict()

        for i, num in enumerate(nums):
            complement = target-num
            if complement in temp.keys():
                return([temp[complement], i])
            temp[num] = i
        """
        print(temp) 
        
        # temp is nums
        # for each letter in nums check if 7-that letter is in nums
        # if so add the index of that value
        # 
        lookingFor = None
        found = False

        for index, value in enumerate(nums):
            if lookingFor == value:
                print(value)
                ans.append(index)
            
            complement = target-value
            if complement in nums and not found and temp[complement] != index:
                ans.append(index)
                found = True
                print(value)
                lookingFor = target-value
        
        
        return [ans[0], ans[1]]
        """
