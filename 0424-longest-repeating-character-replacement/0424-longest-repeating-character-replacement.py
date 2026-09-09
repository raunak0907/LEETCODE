class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            if count[s[right]] > max_freq:
                max_freq = count[s[right]]

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            length = right - left + 1

            if length > ans:
                ans = length

        return ans