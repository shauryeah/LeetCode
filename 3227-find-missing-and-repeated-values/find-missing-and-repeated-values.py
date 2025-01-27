class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        arr=[]
        lis=[]
        for q in range(1,(len(grid))**2+1):
            lis.append(q)
        for i in grid:
            for j in i:
                if j in lis:
                    lis.remove(j)
                else:
                    arr.append(j)
        arr.append(lis[0])
        return arr
        
        
