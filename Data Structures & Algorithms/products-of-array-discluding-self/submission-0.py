class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums)):
            opuri = 1
            for j in range(0,len(nums)):
                if i == j:
                    continue
                opuri *= nums[j]
            res.append(opuri)
        return res