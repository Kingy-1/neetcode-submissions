class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # If nums is longer than set nums
        # Therefore there are duplicates
        # Return true
        if len(nums) > len(set(nums)):
            return True
        return False