class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix = [[] for i in range(9)]
        column = [{} for i in range(9)]

        n = 0

        for index, row in enumerate(board):
            n = 0
            row[3*n:3*(n+1)]

            if index <= 2:
                for i in range(0, 3):
                    matrix[i] += (row[3*n:3*(n+1)])
                    n += 1
            elif index <= 5:
                for i in range(3, 6):
                    matrix[i] += (row[3*n:3*(n+1)])
                    n += 1
            else:
                for i in range(6, 9):
                    matrix[i] += (row[3*n:3*(n+1)])
                    n += 1            
            
            rows = []
            # Checks for rows
            for j, num in enumerate(row):
                #column[j][num] += 1
                column[j][num] = 1 + column[j].get(num, 0)
                if column[j][num] > 1 and num != ".":
                    print(column[j], j)
                    return False
                if num in rows and num != ".":
                    return False
                rows.append(num)

        # Checks for each square
        for square in matrix:
            counts = {}
            for number in square:
                counts[number] = 1 + counts.get(number, 0)
                if counts[number] > 1 and number != ".":
                    return False

        return True