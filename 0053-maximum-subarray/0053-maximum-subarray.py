class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        count=0
        maxp=nums[0]
        for i in range(len(nums)):
            if count<0:
                count=0
            count+=nums[i]
            maxp=max(maxp,count)
        return maxp
        