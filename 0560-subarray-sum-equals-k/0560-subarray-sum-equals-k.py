class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s={0:1}
        count=0
        prefix=0
        for n in nums:
            prefix+=n
            if prefix-k in s:
                count+=s[prefix-k]

            s[prefix]=s.get(prefix,0)+1
        return count