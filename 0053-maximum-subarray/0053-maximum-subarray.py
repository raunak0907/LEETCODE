class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsub=nums[0]
        currsub=0
        for i in range(len(nums)):
            if currsub<0:
                currsub=0
            currsub+=nums[i]
            maxsub=max(maxsub,currsub)
        return maxsub
        