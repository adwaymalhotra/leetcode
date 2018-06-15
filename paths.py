class Solution:
#find the min path from 0,0 to (n-1,m-1)
    def minPathSum(self, grid):
        N = len(grid)
        M = 0
        if N<=0: return 0
        else: 
            M = len(grid[0])
            if M<=0: return 0
        
        for i in range(1,N):
            grid[i][0] += grid[i-1][0]
        for j in range(1,M):
            grid[0][j] += grid[0][j-1]
            
        for i in range(1,N):
            for j in range(1,M):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
