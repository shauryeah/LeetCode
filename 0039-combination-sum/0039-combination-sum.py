class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        def recursive(i,remainder):
            if(remainder==0):
                ans.append(path[:])
                return
            if(remainder<0 or i==len(candidates)):
                return
            path.append(candidates[i])
            recursive(i,remainder-candidates[i])
            path.pop()

            recursive(i+1,remainder)
        recursive(0,target)
        return ans
