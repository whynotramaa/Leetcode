class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of cols

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for col in range(n):
                        if matrix[i][col] != 0: #mark the entire row as -1 except already 0 valued
                            matrix[i][col] = None

                    for row in range(m):
                        if matrix[row][j]!=0: #mark the entire column as -1 excpet the oens that already 0
                            matrix[row][j] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
sol.setZeroes(matrix)
for row in matrix:
    print(row)



class SecondSolution:
    def setZeroesOptimal(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True
                break

        # check if first col has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
                break

        # traverse from 1,m and 1,n and if we have any zero, set [i][0] as 0 and [0][j] as 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # now set [i][j] = 0  if [i][0] or [0][j] == 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # if firstRowZero or firstColZero == 0, set row/matrix = 0
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j = n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
            nums[i+1:] = reversed(nums[i+1:])
            return nums
        else:
            nums.reverse()
            return nums
