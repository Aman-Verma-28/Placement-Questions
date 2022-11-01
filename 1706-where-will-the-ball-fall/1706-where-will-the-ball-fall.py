class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        answer = []
        columns = len(grid[0])
        rows = len(grid)
        
        
        for column in range(columns):
            row = 0
            cur_column = column
            new_column = column
            while row<rows:
                new_column += grid[row][cur_column]
                if new_column==-1 or new_column==columns:
                    answer.append(-1)
                    break
                if grid[row][new_column]!=grid[row][cur_column]:
                    answer.append(-1)
                    break
                row +=  1
                cur_column = new_column
            if row==rows:
                answer.append(new_column)
        
        return answer
            