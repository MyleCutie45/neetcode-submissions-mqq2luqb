class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x=y=z=False
        for fork in triplets:
            if(fork[0]==target[0] and fork[1]<=target[1] and fork[2]<=target[2]):
                x=True
            if(fork[0]<=target[0] and fork[1]==target[1] and fork[2]<=target[2]):
                y=True
            if(fork[0]<=target[0] and fork[1]<=target[1] and fork[2]==target[2]):
                z=True
        return True if x and y and z else False