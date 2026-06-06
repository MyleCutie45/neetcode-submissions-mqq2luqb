class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_max = 0
        dfd = defaultdict(int)
        for i in range(n):
            dfd[nums[i]]+=1
            count_max = max(dfd[nums[i]],count_max)
        for num,count in dfd.items():
            if count == count_max:
                return num
