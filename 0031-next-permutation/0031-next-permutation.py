class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the pivot (first element from the right that breaks descending order)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
                
        # If no pivot is found, the array is strictly descending (the very last permutation).
        # We just reverse the whole array to reset to the lowest permutation.
        if pivot == -1:
            self.reverse(nums, 0, n - 1)
            return
            
        # Step 2: Find the smallest element to the right of the pivot that is strictly greater than the pivot
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                # Step 3: Swap them
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break
                
        # Step 4: Reverse the suffix starting right after the pivot
        self.reverse(nums, pivot + 1, n - 1)

    # Bare-metal C-style array reversal (O(1) memory)
    def reverse(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1