class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=0
        for ch in t:
            if left<len(s) and s[left]==ch:
                left+=1
        return left==len(s)
        