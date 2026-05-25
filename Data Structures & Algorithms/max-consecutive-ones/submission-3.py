class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        maxu = 0
        for i in range(len(nums)):
            if nums[i] == 1: 
                maxu +=1
                res = max(res,maxu)
            else:
                maxu = 0
            
        return res