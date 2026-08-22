class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=0
        prod=1
        temp=n
        while(n>0):
            rem=n%10
            summ+=rem
            prod*=rem
            n=n//10
        return temp%(summ+prod)==0