class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(0,len(nums)-1,2):
            for j in range(nums[i]):
                a.append(nums[i+1])
        return a
