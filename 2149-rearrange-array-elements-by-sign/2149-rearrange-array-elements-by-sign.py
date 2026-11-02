class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        l,r=0,1
        res=[0]*n
        for i in range(n):
            if nums[i]>0:
                res[l]=nums[i]
                l+=2
            else:
                res[r]=nums[i]
                r+=2
        return res