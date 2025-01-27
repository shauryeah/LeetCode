class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        l1=list(word1)
        l2=list(word2)
        a=[]
        b=[]
        for i in l1:
            if i not in a:
                a.append(i)
        for i in l2:
            if i not in b:
                b.append(i)
        for i in a:
            n=l1.count(i)
            m=l2.count(i)
            if n>m:
                if n-m>3:
                    return False
            else:
                if m-n>3:
                    return False
        for j in b:
            n=l1.count(j)
            m=l2.count(j)
            if n>m:
                if n-m>3:
                    return False
            else:
                if m-n>3:
                    return False
        return True