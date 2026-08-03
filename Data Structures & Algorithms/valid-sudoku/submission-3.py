class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        For each row there must be num 1-9
        For each column there must be num 1-9
        For each 3x3 area there must be num 1-9
        """

        """
        A simple solution could be one where:
        We check every single row and check each square

        For each square we check if there are any duplicates
            Could do this by getting len of set and comparing
            it to the matrix length
        
        Make 9 lists which store the value of each matrix
        """

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
                column[j][num] = 1 + column[j].get(num, 0)
                if column[j][num] > 1 and num != ".":
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