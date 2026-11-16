class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Start at the middle and get the value
        mid = len(nums) // 2
        next = nums
        
        WHILE NEXT ARRAY SIZE IS GREATER THAN 0:
            
            if nums[mid] is greater than target:
                search left array
                next = [next[0]: mid+1]
            if nums[mid] is less than target:
                search right array
                next = [next[mid: len(next)]]
            if nums[mid] = target:
                return mid
        
        mid = len(next) // 2
        """

        start = 0
        end = len(nums)

        while (start < end):
            mid = (end + start) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # search left array
                end = mid
            elif nums[mid] < target:
                # search right array
                start = mid + 1
        
        return -1