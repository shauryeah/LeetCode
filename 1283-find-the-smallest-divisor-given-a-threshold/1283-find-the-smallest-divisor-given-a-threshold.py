class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left=1
        right=max(nums)
        while(left<right):
            mid=(left+right)//2
            summ=0
            for i in nums:
                summ+=(i+mid-1)/mid
            if summ<=threshold:
                right=mid
            else:
                left=mid+1
        return right