class Solution:
    def numberOfSubarrays(self, nums, k):
        count = {0: 1}
        odd = 0
        ans = 0

        for num in nums:
            if num % 2 == 1:
                odd += 1

            if odd - k in count:
                ans += count[odd - k]

            if odd in count:
                count[odd] += 1
            else:
                count[odd] = 1

        return ans