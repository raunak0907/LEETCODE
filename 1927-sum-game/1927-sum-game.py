class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        left = right = 0
        q_left = q_right = 0

        for i in range(n):
            if num[i] == '?':
                if i < n // 2:
                    q_left += 1
                else:
                    q_right += 1
            elif i < n // 2:
                left += int(num[i])
            else:
                right += int(num[i])

        if (q_left + q_right) % 2:
            return True

        diff = left - right

        return diff != (q_right - q_left) * 9 // 2