class Solution(object):
    def maxArea(self, height):
        water = 0
        i,j = 0,len(height)-1
        while i < j:
            area = (j-i) * min(height[i],height[j])
            water = max(water,area)
            if (height[i]<height[j]):
                i+=1
            else:
                j-=1
        return water
        