class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res=[0]*len(nums)
        l,r=0,1
        for i in range(len(nums)):
            if nums[i]>0:
                res[l]=nums[i]
                l+=2
            else:
                res[r]=nums[i]
                r+=2
        return res