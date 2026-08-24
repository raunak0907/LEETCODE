class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)

        while l < r:
            mid = (l + r) // 2

            total = 0
            for n in nums:
                total += (n + mid - 1) // mid

                if total > threshold:
                    break

            if total <= threshold:
                r = mid
            else:
                l = mid + 1

        return l