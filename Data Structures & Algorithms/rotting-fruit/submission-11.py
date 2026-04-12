from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        qi = deque()
        dihlen = 0
        cac = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    cac += 1
                if grid[r][c] == 2:
                    qi.append((r,c))
        while(cac > 0 and qi):
            for i in range(len(qi)):
                r,c = qi.popleft()
                for dih1,dih2 in directions:
                    puh1,puh2 = r+dih1,c+dih2
                    if(puh1 in range(len(grid)) and puh2 in range(len(grid[0])) and grid[puh1][puh2] == 1):
                        qi.append((puh1,puh2))
                        grid[puh1][puh2] = 2
                        cac -= 1
            dihlen += 1
        return dihlen if cac == 0 else -1