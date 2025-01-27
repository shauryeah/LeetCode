class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in [2,3,5]:
            if n==0:
                return False
            while n%i==0:
                n=n//i
            if n==1:
                return True 
        return False