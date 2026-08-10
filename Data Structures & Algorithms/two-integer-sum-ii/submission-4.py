class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # it is in ascending order apparently

        left = 0
        right = len(numbers) - 1
        c_sum = 0
        ans = []

        while left < right:
            c_sum = numbers[left] + numbers[right]

            if c_sum == target:
                ans.append(left+1)
                ans.append(right+1)
                return ans
            elif c_sum > target:
                right -= 1
                continue
            elif c_sum < target:
                left += 1
                continue
        return [1,3]

        