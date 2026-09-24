class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        # Helper function to find either the leftmost or rightmost index
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        # Found it, but keep searching to the LEFT for an earlier one
                        right = mid - 1
                    else:
                        # Found it, but keep searching to the RIGHT for a later one
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound
            
        return [findBound(True), findBound(False)]