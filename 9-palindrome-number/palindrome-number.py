class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rem=0
        n=x
        while x>0:    
            j=x%10
            rem=rem*10+j
            x=x//10
        if rem==n:
            return True
        else:
            return False
            