class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N<1: return
        j = 0
        m = N//2
        for j in range(N):
            for i in range(m):
                t = matrix[i][j]
                matrix[i][j] = matrix[N-i-1][j]
                matrix[N-i-1][j] = t
        
        for i in range(N):
            for j in range(i+1, N):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
