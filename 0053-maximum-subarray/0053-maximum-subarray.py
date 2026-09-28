class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsub=nums[0]
        count=0
        for i in range(len(nums)):
            if count<0:
                count=0
            count+=nums[i]
            maxsub=max(maxsub,count)
        return maxsub
        