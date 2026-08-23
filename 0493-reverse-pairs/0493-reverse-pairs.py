class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(arr):
            if len(arr) <= 1:
                return 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            count = merge_sort(left) + merge_sort(right)

            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                count += j

            i = j = 0
            arr.clear()

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1

            arr.extend(left[i:])
            arr.extend(right[j:])

            return count

        return merge_sort(nums)