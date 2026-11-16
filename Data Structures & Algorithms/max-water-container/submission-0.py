class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        area = (hi-lo)*min(heights[lo], heights[hi])
        store running max -> ans = 0 ans = max(area, ans)
        if heights[lo] <= heights[hi]:
            lo += 1
        elif heights[hi] <= heights[lo]:
            hi -= 1
        

        """

        lo = 0
        hi = len(heights) - 1
        ans = 0

        while lo < hi:
            area = (hi-lo) * min(heights[lo], heights[hi])
            ans = max(area, ans)

            if heights[lo] <= heights[hi]:
                lo += 1
            elif heights[hi] <= heights[lo]:
                hi -= 1
        
        return ans