class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def recursion(row, col, grid, dp):
            if row==0 and col==0:
                return grid[row][col]
            
            if dp[row][col] != -1:
                return dp[row][col]
            
            if col - 1 >= 0:
                left = grid[row][col] + recursion(row, col-1, grid, dp)
            else:
                left = sys.maxsize
            
            if row - 1 >= 0:
                up = grid[row][col] + recursion(row-1, col, grid, dp)
            else:
                up = sys.maxsize
                
            val = min(left, up)
            dp[row][col]=val
            
            return val
        
        
        row = len(grid)
        col = len(grid[0])
        dp=[[-1 for i in range(col+1)] for j in range(row+1)]
        return recursion(row-1, col-1, grid, dp)