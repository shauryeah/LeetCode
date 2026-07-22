class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if(k>sum(candies)):
            return 0
        left=1
        right=max(candies)
        while(left<right):
            mid=(left+right+1)//2
            summ=0
            for i in candies:
                summ+=i//mid
            if(summ>=k):
                left=mid
            else:
                right=mid-1
        return left

