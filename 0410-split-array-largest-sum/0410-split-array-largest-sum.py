class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = (l + r) // 2

            parts = 1
            current = 0

            for n in nums:
                if current + n > mid:
                    parts += 1
                    current = 0

                current += n

            if parts <= k:
                r = mid
            else:
                l = mid + 1

        return l