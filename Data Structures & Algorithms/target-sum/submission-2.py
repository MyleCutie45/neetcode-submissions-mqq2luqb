#dp[i][s] = number of ways to reach sum s using first i elements

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        n = len(nums)
        dp = [[0]*(total*2+1) for _ in range(n+1)]
        offset = total
        dp[0][offset] = 1
        for i in range(1,n+1):
            num = nums[i-1]   
            for s in range(-total,total+1):
                if dp[i-1][s+offset] != 0: #Is there at least 1 way to reach sum s using the first i-1 elements?
                    dp[i][s+offset+num] += dp[i-1][s+offset]
                    dp[i][s+offset-num] += dp[i-1][s+offset]
        return dp[n][target+offset]