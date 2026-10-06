class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        maxp=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count>maxp:
                    maxp=count
            else:
                count=0
        return maxp
        