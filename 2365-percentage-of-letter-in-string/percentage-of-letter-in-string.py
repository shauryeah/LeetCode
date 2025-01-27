class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        n=0.0
        for i in list(s):
            if i==letter:
                n+=1
        k=float(len(list(s)))
        p=n/k
        return int(p*100)
