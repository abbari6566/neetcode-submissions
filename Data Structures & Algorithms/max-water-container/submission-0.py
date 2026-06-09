class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_max_area=0
        l=0
        r=len(heights)-1
        while l<r:
            #calculate area
            new_area = abs((l-r) * min(heights[l],heights[r]))
            if new_area > cur_max_area:
                cur_max_area = new_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return cur_max_area