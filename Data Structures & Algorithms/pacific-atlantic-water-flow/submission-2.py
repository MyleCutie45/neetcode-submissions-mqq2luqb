class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac , alt = set(), set()
        ROWS , COLS = len(heights) , len(heights[0])
        res = []
        def dfs(i,j,visit,dejavu):
            if(i<0 or j<0 or i>=ROWS or j>=COLS or (i,j) in visit or dejavu > heights[i][j]):
                return
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,alt,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,alt,heights[r][COLS-1])
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in alt:
                    res.append((i,j))
        return res