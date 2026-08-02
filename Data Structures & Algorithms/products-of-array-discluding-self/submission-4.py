class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Previous multiple
        # Post multiple
        # Multiply previous by post for each value

        pre = []
        for index, value in enumerate(nums):
            if index == 0:
                pre.append(1)
            else:
                pre.append(nums[index-1]*pre[index-1])
        
        output = [1 for _ in range(len(nums))]


        for i in range(len(output)-1, -1, -1):
            if i == len(output)-1:
                output[i] *= 1
            else:
                output[i] *= output[i+1] * nums[i+1]
        
        ans = []

        for i in range(len(output)):
            ans.append(pre[i] * output[i])

        print(pre)
        print(output)
        print(ans)
        return ans
