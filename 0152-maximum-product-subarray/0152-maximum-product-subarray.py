class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = nums[0]
        currmax = nums[0]
        currmin = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                currmax, currmin = currmin, currmax

            currmax = max(nums[i], nums[i] * currmax)
            currmin = min(nums[i], nums[i] * currmin)

            result = max(result, currmax)

        return result