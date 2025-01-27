class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        nums.sort(reverse=True)
        for i in nums:
            if -i not in nums:
                count+=1
                continue
            else:
                return i
        if count==len(nums):
            return -1

        