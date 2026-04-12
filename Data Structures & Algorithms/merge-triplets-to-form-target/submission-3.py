class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        sett = set()
        for fork in triplets:
            if (fork[0] > target[0] or fork[1] > target[1] or fork[2] > target[2]):
                continue 
            for i,v in enumerate(fork):
                if v == target[i]:
                    sett.add(i)
        return len(sett) == 3
