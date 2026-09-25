class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res= ""
        count = 0

        for c in s:
            if c == '(':
                if count > 0:
                    res+= c
                count += 1

            else:
                count -= 1
                if count > 0:
                    res += c

        return res