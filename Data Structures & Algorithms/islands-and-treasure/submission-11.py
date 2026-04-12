class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r,c):
            stepmom = 0
            q = deque([(r, c)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True
            while q:
                for _ in range(len(q)):
                    nigga, nigger = q.popleft()
                    if grid[nigga][nigger] == 0:
                        return stepmom
                    for dih1,dih2 in directions:
                        puh1 = nigga + dih1 
                        puh2 = nigger + dih2
                        if (0 <= puh1 < ROWS and 0 <= puh2 < COLS and
                            not visit[puh1][puh2] and grid[puh1][puh2] != -1):
                            visit[puh1][puh2] = True
                            q.append([puh1,puh2])
                stepmom += 1
            return INF
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]==INF):
                    grid[i][j] = bfs(i,j)
