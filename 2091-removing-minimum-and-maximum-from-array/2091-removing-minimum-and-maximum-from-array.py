class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minind = nums.index(min(nums))
        maxind = nums.index(max(nums))
        left = min(minind, maxind)
        right = max(minind, maxind)
        option1 = right + 1
        option2 = n - left
        option3 = left + 1 + n - right
        return min(option1, option2, option3)