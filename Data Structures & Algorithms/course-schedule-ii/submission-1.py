class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a , b in prerequisites:
            adj[b].append(a)
        state=[0]*numCourses
        stack = []
        cycle = False
        def dfs(i):
            nonlocal cycle
            if state[i] == 1:
                cycle = True
                return
            if state[i] == 2:
                return
            state[i] = 1
            for niga in adj[i]:
                dfs(niga)
            state[i] = 2
            stack.append(i)
        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)
        if cycle:
            return []
        return stack[::-1]