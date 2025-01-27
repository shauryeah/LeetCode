class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        L=[]
        for i in range(1,n+1):
            if n%i==0:
                L.append(i)
        if len(L)>=k:
            return L[k-1]
        else:
            return -1


        