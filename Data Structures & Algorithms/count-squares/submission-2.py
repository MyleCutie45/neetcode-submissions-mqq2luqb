from collections import defaultdict


class CountSquares:

    def __init__(self):
        self.mapo = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x,y = point
        self.mapo[x][y] += 1

    def count(self, point: List[int]) -> int:
        x,y = point
        res=0
        for y1,c in self.mapo[x].items():
            if y1==y: continue
            d = y1-y 
            res+=c*self.mapo[x+d][y]*self.mapo[x+d][y1]
            res+=c*self.mapo[x-d][y]*self.mapo[x-d][y1]
        return res
