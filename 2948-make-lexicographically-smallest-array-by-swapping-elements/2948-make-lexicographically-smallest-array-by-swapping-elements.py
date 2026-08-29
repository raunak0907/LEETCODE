from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each number with its original index and sort by the number
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        
        res = [0] * n
        i = 0
        
        # Group elements that belong to the same connected component
        while i < n:
            j = i + 1
            # Continue expanding the group as long as adjacent differences are <= limit
            while j < n and sorted_nums[j][0] - sorted_nums[j-1][0] <= limit:
                j += 1
            
            # The current component spans from index i to j-1 in sorted_nums
            # Extract and sort their original indices
            indices = sorted(sorted_nums[k][1] for k in range(i, j))
            
            # Place the sorted values back into the sorted original indices
            for k in range(len(indices)):
                res[indices[k]] = sorted_nums[i + k][0]
            
            # Move to the next component
            i = j
            
        return res