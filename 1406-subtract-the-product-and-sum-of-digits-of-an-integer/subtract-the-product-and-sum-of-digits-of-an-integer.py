class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        d=[]
        while n>0:
            d.append(n%10)
            n//=10
        d.reverse()
        p=1
        q=0
        for i in d:
            q+=i
            p=p*i
        return p-q