class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        s = {0: 1}
        prefix = 0

        for n in nums:
            prefix += n

            if prefix - k in s:
                count += s[prefix - k]

            if prefix in s:
                s[prefix] += 1
            else:
                s[prefix] = 1

        return count