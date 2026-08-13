class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        neg=False
        if(x<0):
            x=-x
            neg=True
        arr=[]
        div=1
        while x>0:
            arr.append(x%10)
            x=x//10
        for i in range(len(arr)-1):
            div=div*10
        for i in arr:
            res+=div*i
            div//=10
        if res>2**31-1:
            return 0
        if not neg:
            return res
        else:
            return -res
            