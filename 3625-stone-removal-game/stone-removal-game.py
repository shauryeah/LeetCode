class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(10,0,-1):
            if i%2==0:
                if n-i<0:
                    return False
                else:
                    Alice=n-i
                    n=Alice
            else:
                if n-i<0:
                    return True
                else:
                    Bob=n-i
                    n=Bob