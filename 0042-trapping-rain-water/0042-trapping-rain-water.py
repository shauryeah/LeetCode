class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        leftMax=0
        rightMax=0
        totWater=0
        while(left<right):
            if(height[left]<height[right]):
                leftMax=max(height[left],leftMax)
                totWater+=leftMax-height[left]
                left+=1
            else:
                rightMax=max(height[right],rightMax)
                totWater+=rightMax-height[right]
                right-=1
        return totWater
        