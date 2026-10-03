class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zero=0
        ans=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            length=right-left+1
            if length>ans:
                ans=length
        return ans
        