class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # There are m*n = t values if we flatten the array to 1D
        # m = rows = len(matrix)
        # n = cols = len(matrix(0))
        
        # Then we need a way of converting t to a real matrix index

        # The current row is the value of t // 4 since it rounds down
        # the column is the value of t - (t//4)*4

        # Then we can binary search matrix[t] by converting the row and column to t


        r = len(matrix)

        if r == 0:
            return False
        
        c = len(matrix[0])
        
        if c == 0:
            return False
        
        # 1D representation of matrix --> t
        t = r * c

        end = t
        start = 0

        while start < end:
            mid = (end + start) // 2
            mR = mid // c
            mC = mid - (mid // c) * c
            value = matrix[mR][mC]

            if value == target:
                return True
            elif value < target:
                # search right array
                start = mid + 1
            elif value > target:
                # search left array
                end = mid
        
        return False


