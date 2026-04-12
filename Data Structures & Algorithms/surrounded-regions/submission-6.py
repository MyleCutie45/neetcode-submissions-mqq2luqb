class Stanford:
    def __init__(self,n):
        self.Parent=list(range(n+1))
        self.Size = [1] * (n+1)
    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node] 
    def UTokyo(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False
        if self.Size[rootA] <= self.Size[rootB]:
            rootA , rootB = rootB , rootA
        self.Parent[rootB] = rootA
        self.Size[rootA] += self.Size[rootB]
        return True
    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dsu = Stanford(ROWS * COLS + 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != "O":
                    continue
                if (i==0 or j==0 or i==(ROWS-1) or j==(COLS-1)):
                    dsu.UTokyo(ROWS*COLS , i*COLS+j)
                else:
                    for dx,dy in directions:
                        nigga1 , nigga2 = i+dx,j+dy
                        if 0 <= nigga1 < ROWS and 0 <= nigga2 < COLS:
                            if board[nigga1][nigga2] == "O":
                                dsu.UTokyo(i*COLS+j,nigga1*COLS+nigga2)

        for r in range(ROWS):
            for c in range(COLS):
                if not dsu.connected(ROWS*COLS,r*COLS+c):
                    board[r][c] = "X"
            
