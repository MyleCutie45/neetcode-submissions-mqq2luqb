class DSU:
    def __init__(self,n):
        self.Parent=list(range(n+1))
        self.Size = [1] * (n+1)
    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node] 
    def Union(self,a,b):
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n)]
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.Union(u,v):
                return [u,v]
        return []