# Set matrix zero
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        CORE INITUITION:
            iterate first row and first column to see if there is any zero. If yes, mark it as 0 else dont
            then go over matrix in nested loop and see if we find any zero mark first row and first col as zero

            second pass - if first row or col is zero, make entire row as zero

            also go over and make entire row or col as zero if firstRowZero or firstColZero == 0
        """

        firstRowZero = firstColZero = False

        m = len(matrix) # rows
        n = len(matrix[0]) # columns

        for j in range(n):
            # iterate over columns of the first row to check if it contains a zero
            if matrix[0][j] == 0:
                firstRowZero = True
                break

        for i in range(m):
            # iterate over columns of the first row to check if it contains a zero
            if matrix[i][0] == 0:
                firstColZero = True
                break

        # iterate over matrix excpet first row & col and then mark first row and col of that indices as 0 if we find any 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # now if first row / first col of any i or j == 0 then entire i,j = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # if firstRowZero then make entire column zero
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # if firstColZero then make entire row zero
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0

# rotate by 90deg
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Perform Transpose
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # Reverse each row
            for row in matrix:
                row.reverse()


# spiralMatrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        if not matrix or not matrix[0]:
            return []

        res = []

        top = 0
        left = 0

        bottom = rows-1
        right = cols-1

        while top<=bottom and left<=right:

            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for j in range(bottom, top-1, -1):
                    res.append(matrix[j][left])
                left+=1

        return res
