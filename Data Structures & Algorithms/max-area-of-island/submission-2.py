class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        maxx = 0
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 ):
                return 0
            grid[r][c] = 0
            count = 1
            for [dih1,dih2] in directions:
                count += dfs(r+dih1,c+dih2)
            return count
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col] == 1):
                    maxx = max(maxx,dfs(row,col))
        return maxx