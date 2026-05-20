import heapq
#(effort, r, c)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dist = [[float("inf")] * COLS for _ in range(ROWS)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while heap:
            e,r,c = heapq.heappop(heap)
            if (r,c) == (ROWS-1,COLS-1):
                return e
            if e > dist[r][c]:
                continue
            for (dr,dc) in directions:
                nr = r+dr 
                nc = c+dc 
                if 0<=nr<ROWS and 0<=nc<COLS:
                    d = abs(heights[nr][nc]-heights[r][c])
                    ne = max(e,d)
                    if ne < dist[nr][nc]:
                        dist[nr][nc] = ne
                        heapq.heappush(heap,(ne,nr,nc))
        return 0

