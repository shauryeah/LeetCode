class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if(nums[mid]==target):
                return True
            elif(nums[mid]==nums[left]==nums[right]):
                left+=1
                right-=1
            elif(nums[left]<=nums[mid]):
                if(target>=nums[left] and target < nums[mid]):
                    right=mid
                else:
                    left=mid+1
            else:
                if(target>nums[mid] and target<=nums[right]):
                    left=mid+1
                else:
                    right=mid
        return False