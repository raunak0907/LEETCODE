class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=nums[0]
        currmax=nums[0]
        currmin=nums[0]
        for n in nums[1:]:
            if n<0:
                currmax,currmin=currmin,currmax
            currmax=max(n,n*currmax)
            currmin=min(n,n*currmin)
            result= max(result,currmax)
        return result
        