class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=(l+r)//2
            d=1
            current=0
            for w in weights:
                if current+w>m:
                    d+=1
                    current=0
                current+=w
            if d<=days:
                r=m
            else:
                l=m+1
        return l

        