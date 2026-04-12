class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" ):
                return
            grid[r][c] = "0"
            for [dih1,dih2] in directions:
                dfs(r+dih1,c+dih2)
        for row in range(ROWS):
            for col in range(COLS):
                if(grid[row][col] == "1"):
                    dfs(row,col)
                    islands += 1
        return islands 