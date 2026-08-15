class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=0
        for i in nums:
            xor=xor^i
        if(xor!=0):
            return len(nums)
        for i in nums:
            if(i!=0):
                return len(nums)-1
        return 0

            