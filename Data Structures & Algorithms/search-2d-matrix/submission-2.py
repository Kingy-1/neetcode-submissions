class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][len(matrix[i])-1] > target:
                # binary search matrix[i]
                start = 0
                end = len(matrix[i]) - 1

                while start < end:
                    mid = (end + start) // 2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        # search left array
                        end = mid
                    elif matrix[i][mid] < target:
                        # search right array
                        start = mid + 1
            elif matrix[i][len(matrix[i])-1] == target:
                return True
        
        return False
        