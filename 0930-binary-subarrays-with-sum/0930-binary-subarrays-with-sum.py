class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        total = 0
        ans = 0

        for num in nums:
            total += num

            if total - goal in count:
                ans += count[total - goal]

            if total in count:
                count[total] += 1
            else:
                count[total] = 1

        return ans