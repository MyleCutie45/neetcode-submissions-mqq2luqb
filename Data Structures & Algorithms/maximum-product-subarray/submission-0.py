class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                curMax,curMin=curMin,curMax
            curMax = max(nums[i],nums[i]*curMax)
            curMin = min(nums[i],nums[i]*curMin)
            res = max(res,curMax)
        return res