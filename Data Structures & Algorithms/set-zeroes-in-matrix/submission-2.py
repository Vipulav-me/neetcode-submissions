class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        firstrow = False
        firstcol = False

        for j in range(n):
            if matrix[0][j] == 0:
                firstrow = True
        for i in range(m):
            if matrix[i][0] == 0:
                firstcol = True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstrow:
            for j in range(n):
                matrix[0][j] = 0
        if firstcol:
            for i in range(m):
                matrix[i][0] = 0



                
        