class Solution:
    def beautySum(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            count={}
            for j in range(i,len(s)):
                count[s[j]]=count.get(s[j],0)+1
                maxi=max(count.values())
                mini=min(count.values())
                total+=maxi-mini
        return total

        