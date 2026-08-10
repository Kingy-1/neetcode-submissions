class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # it is in ascending order apparently

        left = 0
        right = len(numbers) - 1
        c_sum = 0

        while left < right:
            c_sum = numbers[left] + numbers[right]

            if c_sum == target:
                return [left + 1, right + 1]
            elif c_sum > target:
                right -= 1
                continue
            elif c_sum < target:
                left += 1
                continue

        