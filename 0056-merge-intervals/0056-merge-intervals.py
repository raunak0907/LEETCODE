from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals=[]
        for i in intervals:
            if not merged_intervals or merged_intervals[-1][1]<i[0]:
                merged_intervals.append(i)
            else:
                merged_intervals[-1][1]=max(merged_intervals[-1][1],i[1])
        return merged_intervals
        