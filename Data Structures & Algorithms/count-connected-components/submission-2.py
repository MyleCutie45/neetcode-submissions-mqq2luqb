class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            for nigga in adj[i]:
                if not visit[nigga]:
                    visit[nigga] = True
                    dfs(nigga)
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res+=1
        return res
                
