class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width

                if area > ans:
                    ans = area

            stack.append(i)

        return ans