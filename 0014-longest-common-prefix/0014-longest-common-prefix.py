class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maxx=''
        string=strs[0]
        if(len(strs)==1):
            return strs[0]
        for i in range(len(string)):
            for j in range(1,len(strs)):
                if i<len(strs[j]) and strs[j][i]==string[i]:
                    continue
                else:
                    return maxx
            maxx+=string[i]
        return maxx

        