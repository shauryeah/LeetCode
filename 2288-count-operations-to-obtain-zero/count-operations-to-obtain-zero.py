class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        m=0
        while True:
            if num1==0 or num2==0:
                return m
            elif num1>=num2:
                num1=num1-num2
                m+=1
            else:
                num2=num2-num1
                m+=1
        return m
            