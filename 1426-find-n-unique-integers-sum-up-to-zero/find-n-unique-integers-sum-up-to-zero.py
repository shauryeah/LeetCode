class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L=[]
        for i in range(1,n+1):
            if n%2==0:
                for j in range(1,n/2+1):
                    L.append(j)
                for k in range(1,n/2+1):
                    L.append(-k)
            else:
                for j in range(1,((n-1)/2)+1):
                    L.append(j)
                for k in range(1,((n-1)/2)+1):
                    L.append(-k)
                L.append(0)
            return L