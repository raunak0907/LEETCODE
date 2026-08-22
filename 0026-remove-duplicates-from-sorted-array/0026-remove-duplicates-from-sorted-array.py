class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique = []

        for i in nums:
            if i not in unique:
                unique.append(i)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)