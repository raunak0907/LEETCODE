class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=(l+r)//2
            curr=0
            d=1
            for w in weights:
                if curr+w>m:
                    d+=1
                    curr=0
                curr+=w
            if d<=days:
                r=m
            else:
                l=m+1
        return l