class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1

        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1

        result = ''.join(stack[i:])

        if result == "":
            return "0"

        return result