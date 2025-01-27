class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L=sorted(nums)
        L1=sorted(nums,reverse=True)
        if nums==L or nums==L1:
            return True
        else:
            return False
