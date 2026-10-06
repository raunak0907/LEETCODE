class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        l,r=0,1
        res=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res[l]=nums[i]
                l+=2
            else:
                res[r]=nums[i]
                r+=2
        return res







        