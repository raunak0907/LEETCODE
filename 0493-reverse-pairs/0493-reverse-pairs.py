class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        s = SortedList()
        res = 0
        for a in nums:
            res += len(s) - s.bisect_right(a * 2)
            s.add(a)
        return res