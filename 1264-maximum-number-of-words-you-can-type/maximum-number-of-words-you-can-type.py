class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        counter=0
        n=0
        L=list(brokenLetters)
        L2=text.split()
        for i in L2:
            for j in L:
                if i.count(j)==0:
                    counter+=1
            if counter==len(L):
                n+=1
            counter=0
        return n        