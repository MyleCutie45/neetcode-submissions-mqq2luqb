#(time_needed, row, col)

import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            t,r,c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == n-1 and c == n-1:
                return t
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc 
                if 0 <= nr < n and 0 <= nc < n:
                    if(nr,nc) not in visited:
                        new_t = max(t,grid[nr][nc])
                        heapq.heappush(heap,(new_t,nr,nc))
        