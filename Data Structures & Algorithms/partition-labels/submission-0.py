class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapo = {}
        for i,c in enumerate(s):
            mapo[c] = i
        size = end = 0
        res = []
        for i,c in enumerate(s):
            size += 1
            end = max(end,mapo[c])
            if i == end:
                res.append(size)
                size = 0
        return res