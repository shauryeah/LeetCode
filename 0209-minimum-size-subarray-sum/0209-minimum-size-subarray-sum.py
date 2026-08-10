class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if(sum(nums)<target):
            return 0
        ans=float('inf')
        right=0
        left=0
        summ=0
        while(right<len(nums)):
            summ+=nums[right]
            while(summ>=target):
                ans=min(ans,right-left+1)
                summ-=nums[left]
                left+=1
            right+=1
        return ans