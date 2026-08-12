class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        Area=0
        while(left<right):
            Area=max(Area,min(height[left],height[right])*(right-left))
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return Area


