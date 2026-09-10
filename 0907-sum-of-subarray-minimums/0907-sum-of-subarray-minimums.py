class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        stack = []
        ans = 0
        MOD = 10**9 + 7

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()

                left = mid - stack[-1] if stack else mid + 1
                right = i - mid

                ans += arr[mid] * left * right
                ans %= MOD

            stack.append(i)

        return ans