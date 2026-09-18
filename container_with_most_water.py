class Solution(object):
    def maxArea(self, height):
        max_water=0
        lp=0
        rp=len(height)-1
        while(lp<rp):
            width=rp-lp
            bar_height=min(height[lp],height[rp])
            water=width*bar_height
            max_water=max(max_water,water)
            if height[lp]<height[rp]:
                lp+=1
            else:
                rp-=1
        return max_water

