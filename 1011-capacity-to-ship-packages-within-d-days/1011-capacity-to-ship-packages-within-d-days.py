class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        if days==1:
            return sum(weights)
        left= max(weights)
        right=sum(weights)
        ans=float('inf')
        while(left<right):
            mid=(left+right)//2
            shipdays=1
            current=0
            for i in weights:
                if i+current<=mid:
                    current+=i
                else:
                    shipdays+=1
                    current=i
            if(shipdays<=days):
                ans=min(ans,mid)
                right=mid
            else:
                left=mid+1
        return right
            


