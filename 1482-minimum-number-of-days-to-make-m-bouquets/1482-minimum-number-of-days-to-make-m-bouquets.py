class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        left=1
        right=max(bloomDay)
        if(len(bloomDay)<m*k):
            return -1
        while(left<right):
            mid=(left+right)//2
            consecutive=0
            bou=0
            for i in bloomDay:
                if i<=mid:
                    consecutive+=1
                    if(consecutive==k):
                        bou+=1
                        consecutive=0
                else:
                    consecutive=0
            if(bou>=m):
                right=mid
            else:
                left=mid+1
        return right
                
