class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0

        for n in s:
            if n - 1 not in s:
                current = n

                while current + 1 in s:
                    current += 1

                longest = max(longest, current - n + 1)

        return longest