class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r=0,len(height)-1
        max_water=0
        while l<r:
            current_height=min(height[l],height[r])
            current_width=r-l
            current_area=current_height*current_width
            max_water=max(current_area,max_water)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_water
        