class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxp=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count>maxp:
                    maxp=count
            else:
                count=0
        return maxp