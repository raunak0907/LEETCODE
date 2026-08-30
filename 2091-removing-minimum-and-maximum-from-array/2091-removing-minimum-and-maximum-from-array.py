class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_i = 0
        max_i = 0

        for i in range(n):
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] > nums[max_i]:
                max_i = i

        # Make min_i the smaller index
        if min_i > max_i:
            min_i, max_i = max_i, min_i

        # 1. Remove both from front
        front = max_i + 1

        # 2. Remove both from back
        back = n - min_i

        # 3. Remove min from front and max from back
        both = (min_i + 1) + (n - max_i)

        return min(front, back, both)