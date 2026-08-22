class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count=0
        max=0
        for i in nums:
            if i==1:
                count+=1
                if count>max:
                    max=count
            else:
                count=0
        return max