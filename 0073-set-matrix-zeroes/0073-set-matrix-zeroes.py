class Solution(object):

    def setZeroes(self, matrix):
        rows = len(matrix)
        col = len(matrix[0])
        first_row_zero = False

        # 1. Check if the first row originally contains any zero
        for j in range(col):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # 2. Use row 0 and col 0 as flags for the rest of the grid
        for i in range(1, rows):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 3. Update inner subgrid based on flags
        for i in range(1, rows):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. Zero out the first column if matrix[0][0] was set as a flag
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        # 5. Zero out the first row if it originally contained a zero
        if first_row_zero:
            for j in range(col):
                matrix[0][j] = 0

        
        