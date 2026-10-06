class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prev:
                return [prev[diff],i]
            prev[n]=i
        return prev
        