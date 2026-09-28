class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res=0
        count=0
        for num in range(len(nums)):
            if count==0:
                res=nums[num]
            if nums[num]==res:
                count+=1
            else:
                count-=1
        return res
