class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currsub=0
        currmax=nums[0]
        for i in range(len(nums)):
            if currsub<0:
                currsub=0
            currsub+=nums[i]
            currmax=max(currmax,currsub)
        return currmax
        