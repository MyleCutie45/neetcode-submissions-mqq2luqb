class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def addGoku(r,c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return
            q.append([r,c])
            visit.add((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        dihlen = 0
        while q:
            for i in range(len(q)):
                i , j = q.popleft()
                grid[i][j] = dihlen
                addGoku(i+1,j)
                addGoku(i-1,j)
                addGoku(i,j+1)
                addGoku(i,j-1)
            dihlen += 1