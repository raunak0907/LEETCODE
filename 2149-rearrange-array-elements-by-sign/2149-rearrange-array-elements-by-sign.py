class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        l,r=0,1
        res=[0]*len(nums)
        for k in range(len(nums)):
            if nums[k]>0:
                res[l]=nums[k]
                l+=2
            else:
                res[r]=nums[k]
                r+=2
        return res
        